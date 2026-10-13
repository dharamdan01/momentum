import asyncio
import wave
from types import SimpleNamespace
from unittest.mock import Mock
import pytest
from app.services import mom_generator

@pytest.fixture
def mock_openai(monkeypatch):
    client = Mock()
    constructor = Mock(return_value=client)
    monkeypatch.setattr(mom_generator, "OpenAI", constructor)
    return client, constructor
@pytest.fixture
def audio_file(tmp_path):
    path = tmp_path / "sample.wav"
    with wave.open(str(path), "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(16000)
        audio.writeframes(b"\x00\x00" * 1600)
    return path
# this func test successful transcription
def test_transcription_success_func(audio_file, mock_openai):
    client, constructor = mock_openai
    client.audio.transcriptions.create.return_value = SimpleNamespace(
        text="Hello World"
    )
    result = asyncio.run(
        mom_generator.transcribe_audio(str(audio_file))
    )
    assert result == "Hello World"
    constructor.assert_called_once_with(
        api_key=mom_generator.OPENAI_API_KEY
    )




# this func test correct whisper model and binary audio
def test_transcription_uses_whisper(audio_file, mock_openai):
    client, _ = mock_openai
    received = {}
    def fake_transcription(*, model, file):
        received["model"] = model
        received["mode"] = file.mode
        received["content"] = file.read()
        return SimpleNamespace(text="Transcribed")
    client.audio.transcriptions.create.side_effect = fake_transcription
    asyncio.run(mom_generator.transcribe_audio(str(audio_file)))
    assert received["model"] == "whisper-1"
    assert received["mode"] == "rb"
    assert received["content"] == audio_file.read_bytes()
    client.audio.transcriptions.create.assert_called_once()



# this func test empty audio
def test_empty_audio_file(tmp_path, mock_openai):
    client, _ = mock_openai
    path = tmp_path / "empty.wav"
    path.write_bytes(b"")
    def fake_transcription(*, model, file):
        assert file.read() == b""
        return SimpleNamespace(text="")
    client.audio.transcriptions.create.side_effect = fake_transcription
    result = asyncio.run(
        mom_generator.transcribe_audio(str(path))
    )
    assert result == ""
    client.audio.transcriptions.create.assert_called_once()




# this func test very short audio clip
def test_short_audio_file(tmp_path, mock_openai):
    client, _ = mock_openai
    path = tmp_path / "short.wav"
    with wave.open(str(path), "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(16000)
        audio.writeframes(b"\x00\x00" * 160)
    received = {}
    def fake_transcription(*, model, file):
        received["content"] = file.read()
        return SimpleNamespace(text="Hi")
    client.audio.transcriptions.create.side_effect = fake_transcription
    result = asyncio.run(
        mom_generator.transcribe_audio(str(path))
    )
    assert result == "Hi"
    assert received["content"] == path.read_bytes()
    client.audio.transcriptions.create.assert_called_once()





# this func test unsupported audio format rejected by API
def test_unsupported_format_file(tmp_path, mock_openai):
    client, _ = mock_openai
    path = tmp_path / "invalid.txt"
    path.write_text("Not an audio file")
    client.audio.transcriptions.create.side_effect = ValueError(
        "Unsupported audio format"
    )
    with pytest.raises(ValueError, match="Unsupported audio format"):
        asyncio.run(mom_generator.transcribe_audio(str(path)))

    client.audio.transcriptions.create.assert_called_once()





# this function test external API failure
def test_api_failure(audio_file, mock_openai):
    client, _ = mock_openai
    client.audio.transcriptions.create.side_effect = RuntimeError(
        "Transcription service unavailable"
    )
    with pytest.raises(
        RuntimeError,
        match="Transcription service unavailable"
    ):
        asyncio.run(
            mom_generator.transcribe_audio(str(audio_file))
        )
    client.audio.transcriptions.create.assert_called_once()




# this function test missing audio file
def test_missing_audio_file(tmp_path, mock_openai):
    client, _ = mock_openai
    missing_path = tmp_path / "missing.wav"
    with pytest.raises(FileNotFoundError):
        asyncio.run(
            mom_generator.transcribe_audio(str(missing_path))
        )
    client.audio.transcriptions.create.assert_not_called()