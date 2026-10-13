import anthropic
from openai import OpenAI

from ..config import ANTHROPIC_API_KEY, OPENAI_API_KEY


async def transcribe_audio(audio_path: str) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)
    with open(audio_path, "rb") as f:
        result = client.audio.transcriptions.create(model="whisper-1", file=f)
    return result.text
async def generate_mom(transcript: str, meeting_title: str, participants: str) -> str:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    prompt = f"""You are a professional meeting minutes writer.
Given the following meeting transcript, generate a formal Minutes of Meeting (MOM) document.
Meeting Title: {meeting_title}
Participants: {participants}
Transcript:
{transcript}
Generate the MOM with these sections:
1. Meeting Details (title, date, participants)
2. Agenda Items
3. Discussion Summary (key points discussed)
4. Action Items (in a table with: #, Action Item, Assigned To, Deadline)
5. Key Decisions
Keep it professional and concise. Use bullet points for clarity."""
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


async def extract_tasks(mom_text: str) -> list[dict]:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = f"""Extract all action items/tasks from this Minutes of Meeting.

MOM:
{mom_text}

Return ONLY a JSON array. Each item must have:
- "title": the action item description
- "assigned_to": person's name (or "Unassigned")
- "deadline": deadline if mentioned (ISO format YYYY-MM-DD), or null
- "priority": "high", "medium", or "low" based on urgency

Example: [{{"title": "Follow up with vendor", "assigned_to": "Swagata", "deadline": "2026-10-15", "priority": "high"}}]

Return ONLY the JSON array, no other text."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    import json

    text = message.content[0].text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)
