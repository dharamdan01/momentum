<p align="center">
  <img src="https://img.shields.io/badge/MOM-entum-6366f1?style=for-the-badge&labelColor=0a0d14" alt="MOMentum" />
</p>

<h1 align="center">MOMentum</h1>

<p align="center">
  <strong>Turn meetings into momentum.</strong><br>
  AI-powered meeting intelligence — record, transcribe, generate MOMs, extract tasks, and track everything from one dashboard.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Claude_AI-Anthropic-D97757?logo=anthropic&logoColor=white" alt="Claude AI" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License" />
</p>

---

## What is MOMentum?

Most meetings end with vague action items that get lost in chat threads. **MOMentum** fixes that.

It takes your meeting recordings or transcripts, uses AI to generate structured Minutes of Meeting, automatically extracts tasks with assignees and deadlines, and gives you a real-time dashboard to track everything — so nothing falls through the cracks.

**The pipeline:**

```
  Record / Paste  →  Transcribe (Whisper)  →  Generate MOM (Claude)  →  Extract Tasks (Claude)
       ↓                                                                        ↓
   Meeting saved                                                    Tasks auto-created with
                                                                  assignees, deadlines & priority
```

---

## Features

### AI Meeting Pipeline
- Upload audio recordings or paste transcripts manually
- **Auto-transcription** via OpenAI Whisper
- **MOM generation** via Claude — structured with agenda, decisions, and action items
- **Task extraction** via Claude — pulls out tasks with assignees, deadlines, and priorities

### Task Management
- Statuses: `Pending` → `In Progress` → `Completed` (auto-detects `Overdue`)
- Priority levels: `High`, `Medium`, `Low`
- **List view** with search and filters (status, member, keyword)
- **Kanban board** view with column grouping

### Team & Dashboard
- Team members with roles (Management, Member, FDE, Consultant)
- Real-time stats with animated counters and SVG progress ring
- Deadline alerts (3-day and 7-day windows)
- Per-member workload breakdown
- Activity feed

### Premium UI
- **Dark / Light mode** with system preference detection
- Glassmorphism design with animated gradient borders
- **Command palette** (`Ctrl+K`) with fuzzy search
- Keyboard shortcuts for every major action
- Splash screen, toast notifications, confetti on task completion
- Fully responsive (desktop → tablet → mobile)

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, FastAPI, SQLAlchemy ORM |
| **Database** | SQLite (zero-config, file-based) |
| **Frontend** | Vanilla HTML, CSS, JavaScript — no framework, no build step |
| **AI — MOMs** | Anthropic Claude API |
| **AI — Transcription** | OpenAI Whisper API |

---

## Quick Start

```bash
# Clone
git clone https://github.com/your-username/momentum.git
cd momentum

# Setup
python -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows
pip install -r requirements.txt

# (Optional) Add API keys for AI features
cp .env.example .env
# Edit .env with your ANTHROPIC_API_KEY and OPENAI_API_KEY

# Run
uvicorn app.main:app --reload
```

Open **http://127.0.0.1:8000** and you're in.

> **Works without API keys** — meetings, tasks, team, and dashboard all work fully offline. AI features (transcription, MOM generation, task extraction) require the respective API keys.

---

## Project Structure

```
momentum/
├── app/
│   ├── main.py              # FastAPI entry point, mounts static, serves SPA
│   ├── database.py           # SQLAlchemy engine + session factory
│   ├── models.py             # Member, Meeting, Task models
│   ├── schemas.py            # Pydantic request/response schemas
│   ├── routers/
│   │   ├── dashboard.py      # Stats, alerts, member workload summary
│   │   ├── meetings.py       # Meeting CRUD + AI pipeline endpoints
│   │   ├── members.py        # Team member CRUD
│   │   └── tasks.py          # Task CRUD with status/priority/member filters
│   ├── services/
│   │   ├── mom_generator.py  # Whisper transcription + Claude MOM & task extraction
│   │   └── reminder.py       # Overdue detection + upcoming deadline alerts
│   └── static/
│       ├── index.html        # Single-page application shell
│       ├── style.css         # Dual-theme styles, glassmorphism, animations
│       └── app.js            # All client-side logic
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+K` | Command palette |
| `T` | Toggle dark / light mode |
| `1` `2` `3` `4` | Dashboard / Meetings / Tasks / Team |
| `M` | New meeting |
| `N` | New task |
| `?` | Show all shortcuts |
| `Esc` | Close modal or palette |

---

## API Reference

### Meetings
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/meetings/` | List all meetings |
| `POST` | `/api/meetings/` | Create a meeting |
| `GET` | `/api/meetings/{id}` | Get meeting details + tasks |
| `POST` | `/api/meetings/{id}/upload-audio` | Upload audio recording |
| `POST` | `/api/meetings/{id}/paste-transcript` | Save pasted transcript |
| `POST` | `/api/meetings/{id}/transcribe` | Transcribe audio via Whisper |
| `POST` | `/api/meetings/{id}/generate-mom` | Generate MOM via Claude |
| `POST` | `/api/meetings/{id}/extract-tasks` | Extract tasks from MOM via Claude |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks/?status=&assigned_to=&priority=` | List with filters |
| `POST` | `/api/tasks/` | Create a task |
| `PATCH` | `/api/tasks/{id}` | Update task fields |
| `DELETE` | `/api/tasks/{id}` | Delete a task |

### Members
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/members/` | List all members |
| `POST` | `/api/members/` | Add a member |
| `DELETE` | `/api/members/{id}` | Remove a member |

### Dashboard
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/dashboard/stats` | Stats + upcoming deadlines |
| `GET` | `/api/dashboard/alerts` | Overdue + 3-day warnings |
| `GET` | `/api/dashboard/member-summary` | Per-member task breakdown |

---

## License

MIT

---

<p align="center">
  Built by <strong>Swagata Banerjee</strong> — FDE at Micro Turners
</p>
