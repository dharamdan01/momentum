<div align="center">

<br>

```
 ███╗   ███╗ ██████╗ ███╗   ███╗███████╗███╗   ██╗████████╗██╗   ██╗███╗   ███╗
 ████╗ ████║██╔═══██╗████╗ ████║██╔════╝████╗  ██║╚══██╔══╝██║   ██║████╗ ████║
 ██╔████╔██║██║   ██║██╔████╔██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
 ██║╚██╔╝██║██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
 ██║ ╚═╝ ██║╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 ╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
```

### Turn meetings into momentum.

AI-powered meeting intelligence that records, transcribes, generates MOMs,<br>extracts tasks, and tracks everything — so nothing falls through the cracks.

<br>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Claude](https://img.shields.io/badge/Claude_AI-D97757?style=flat-square&logo=anthropic&logoColor=white)](https://anthropic.com)
[![Whisper](https://img.shields.io/badge/Whisper-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![License](https://img.shields.io/badge/MIT-green?style=flat-square&label=License)](LICENSE)

<br>

[Getting Started](#-getting-started) · [Features](#-features) · [How It Works](#-how-it-works) · [API Reference](#-api-reference) · [Shortcuts](#-keyboard-shortcuts)

<br>

</div>

---

<br>

## The Problem

Every meeting ends with action items. Most of them die in chat threads, sticky notes, or someone's memory. A week later, the same items resurface in the next meeting — and the cycle repeats.

**MOMentum breaks that cycle.**

Record your meeting → get structured minutes in seconds → tasks auto-created with owners and deadlines → track everything from one dashboard. No more "who was supposed to do that?"

<br>

## How It Works

```
                                    MOMentum Pipeline
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                         │
  │   STEP 1            STEP 2             STEP 3             STEP 4        │
  │                                                                         │
  │   Upload Audio      Transcribe         Generate MOM       Extract       │
  │   ── or ──     ───► with Whisper  ───► with Claude   ───► Tasks    ───► │
  │   Paste Text        (auto)             (structured)       (auto)        │
  │                                                                         │
  │                                                                         │
  │   "Hey let's        Full text          # Meeting MOM      [x] Fix API  │
  │    discuss the      transcript         ## Decisions            → Karan  │
  │    API bug..."      with speaker       ## Action Items         → Oct 18 │
  │                     attribution        ## Next Steps           → High   │
  │                                                                         │
  └─────────────────────────────────────────────────────────────────────────┘
                                                                    │
                                              ┌─────────────────────┘
                                              ▼
                                    Dashboard · Kanban · Alerts
```

<br>

## Features

<table>
<tr>
<td width="50%">

### AI Meeting Pipeline
- Upload audio or paste transcripts
- Auto-transcription via **OpenAI Whisper**
- Structured MOM generation via **Claude**
- One-click task extraction with assignees, deadlines & priorities

</td>
<td width="50%">

### Task Management
- `Pending` → `In Progress` → `Completed` workflow
- Auto-detects **overdue** tasks
- **List view** with search, status & member filters
- **Kanban board** with column grouping

</td>
</tr>
<tr>
<td width="50%">

### Dashboard & Analytics
- Real-time stats with animated counters
- SVG progress ring for completion overview
- Deadline alerts (3-day & 7-day windows)
- Per-member workload breakdown
- Live activity feed

</td>
<td width="50%">

### Premium UI
- **Dark / Light mode** (respects system preference)
- Glassmorphism + animated gradient borders
- **Command palette** — `Ctrl+K` to do anything
- Keyboard-first navigation
- Confetti on task completion

</td>
</tr>
</table>

<br>

## Tech Stack

```
Frontend    →  Vanilla HTML / CSS / JS (no framework, no build step)
Backend     →  Python · FastAPI · SQLAlchemy ORM
Database    →  SQLite (zero-config, single file)
AI (MOM)    →  Anthropic Claude API
AI (Audio)  →  OpenAI Whisper API
```

<br>

## Getting Started

### 1. Clone & install

```bash
git clone https://github.com/gitswagata1/momentum.git
cd momentum

python -m venv venv
source venv/bin/activate          # macOS / Linux
venv\Scripts\activate             # Windows

pip install -r requirements.txt
```

### 2. Configure AI keys *(optional)*

```bash
cp .env.example .env
```

Add your keys in `.env`:

```env
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
```

> **No keys? No problem.** Meetings, tasks, team, and dashboard all work fully offline. AI features just need the keys.

### 3. Run

```bash
uvicorn app.main:app --reload
```

Open **http://127.0.0.1:8000** — that's it.

<br>

## Project Structure

```
momentum/
├── app/
│   ├── main.py                # FastAPI entry point, serves SPA
│   ├── database.py            # SQLAlchemy engine + session
│   ├── models.py              # Member, Meeting, Task
│   ├── schemas.py             # Pydantic request/response models
│   │
│   ├── routers/
│   │   ├── dashboard.py       # Stats, alerts, workload summary
│   │   ├── meetings.py        # Meeting CRUD + AI pipeline
│   │   ├── members.py         # Team CRUD
│   │   └── tasks.py           # Task CRUD with filters
│   │
│   ├── services/
│   │   ├── mom_generator.py   # Whisper + Claude integration
│   │   └── reminder.py        # Overdue detection + alerts
│   │
│   └── static/
│       ├── index.html         # SPA shell
│       ├── style.css          # Dual-theme, glassmorphism, animations
│       └── app.js             # All client-side logic
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

<br>

## Keyboard Shortcuts

| Key | Action |
|:---:|--------|
| `Ctrl+K` | Open command palette |
| `T` | Toggle dark / light mode |
| `1` `2` `3` `4` | Jump to Dashboard / Meetings / Tasks / Team |
| `M` | Create new meeting |
| `N` | Create new task |
| `?` | Show all shortcuts |
| `Esc` | Close anything open |

<br>

## API Reference

<details>
<summary><strong>Meetings</strong> — CRUD + AI pipeline</summary>

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/meetings/` | List all meetings |
| `POST` | `/api/meetings/` | Create meeting |
| `GET` | `/api/meetings/{id}` | Meeting details + tasks |
| `POST` | `/api/meetings/{id}/upload-audio` | Upload audio file |
| `POST` | `/api/meetings/{id}/paste-transcript` | Paste transcript text |
| `POST` | `/api/meetings/{id}/transcribe` | AI transcription (Whisper) |
| `POST` | `/api/meetings/{id}/generate-mom` | AI MOM generation (Claude) |
| `POST` | `/api/meetings/{id}/extract-tasks` | AI task extraction (Claude) |

</details>

<details>
<summary><strong>Tasks</strong> — CRUD with filters</summary>

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks/?status=&assigned_to=&priority=` | List with filters |
| `POST` | `/api/tasks/` | Create task |
| `PATCH` | `/api/tasks/{id}` | Update task |
| `DELETE` | `/api/tasks/{id}` | Delete task |

</details>

<details>
<summary><strong>Members</strong> — Team management</summary>

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/members/` | List all members |
| `POST` | `/api/members/` | Add member |
| `DELETE` | `/api/members/{id}` | Remove member |

</details>

<details>
<summary><strong>Dashboard</strong> — Analytics & alerts</summary>

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/dashboard/stats` | Stats + upcoming deadlines |
| `GET` | `/api/dashboard/alerts` | Overdue + 3-day warnings |
| `GET` | `/api/dashboard/member-summary` | Per-member task breakdown |

</details>

<br>

## License

MIT — do whatever you want with it.

<br>

---

<div align="center">
<br>

Built by **Swagata Banerjee** — FDE at Micro Turners

*Stop losing action items. Start building MOMentum.*

<br>
</div>
