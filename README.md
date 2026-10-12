# Micro Turners - Meeting & Task Manager

An AI-powered meeting management and task tracking web application built for **Micro Turners**. Record meetings, auto-generate Minutes of Meeting (MOM) using AI, extract action items, and track tasks across your team — all from a single dashboard.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Claude AI](https://img.shields.io/badge/Claude_AI-Anthropic-D97757?logo=anthropic&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Features

### Meeting Management
- Create and organize meetings with title, date, and participants
- Upload audio recordings or paste transcripts manually
- **AI Transcription** — transcribe meeting audio using OpenAI Whisper
- **AI MOM Generation** — generate structured Minutes of Meeting using Claude
- **AI Task Extraction** — automatically extract action items from MOMs with assignees, deadlines, and priorities

### Task Tracking
- Full CRUD for tasks with status (`Pending`, `In Progress`, `Completed`, `Overdue`)
- Priority levels: `High`, `Medium`, `Low`
- Assign tasks to team members with deadlines
- **List view** with search, status/member filters
- **Kanban board view** with drag-friendly columns
- Auto-detection of overdue tasks

### Team Management
- Add, view, and remove team members
- Roles: Management, Member, Consultant
- Per-member workload breakdown on dashboard

### Dashboard
- Real-time stats with animated counters
- Completion overview with SVG progress ring
- Upcoming deadline alerts (3-day and 7-day windows)
- Overdue task warnings
- Team workload distribution
- Recent activity feed

### UI/UX
- **Dark / Light mode** with system preference detection
- Glassmorphism design with animated gradient borders
- Command palette (`Ctrl+K`) with fuzzy search
- Keyboard shortcuts for all major actions
- Splash screen, toast notifications, confetti celebrations
- Fully responsive (desktop, tablet, mobile)

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, FastAPI, SQLAlchemy ORM |
| **Database** | SQLite |
| **Frontend** | Vanilla HTML, CSS, JavaScript (no framework) |
| **AI - MOM Generation** | Anthropic Claude API |
| **AI - Transcription** | OpenAI Whisper API |

---

## Project Structure

```
micro-turners-mom/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── database.py           # SQLAlchemy engine & session
│   ├── models.py             # DB models (Member, Meeting, Task)
│   ├── schemas.py            # Pydantic request/response schemas
│   ├── routers/
│   │   ├── dashboard.py      # Stats, alerts, member summary
│   │   ├── meetings.py       # Meeting CRUD + AI pipeline
│   │   ├── members.py        # Team member CRUD
│   │   └── tasks.py          # Task CRUD with filters
│   ├── services/
│   │   ├── mom_generator.py  # Whisper transcription + Claude MOM/task extraction
│   │   └── reminder.py       # Overdue detection + deadline alerts
│   └── static/
│       ├── index.html        # Single-page application
│       ├── style.css         # Themed styles with animations
│       └── app.js            # Client-side logic
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- (Optional) Anthropic API key — for MOM generation and task extraction
- (Optional) OpenAI API key — for audio transcription

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/micro-turners-mom.git
   cd micro-turners-mom
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your API keys:

   ```
   ANTHROPIC_API_KEY=your_key_here
   OPENAI_API_KEY=your_key_here
   ```

   > The app works without API keys — you just won't be able to use the AI transcription, MOM generation, and task extraction features. All other features (meetings, tasks, team, dashboard) work fully offline.

5. **Run the server**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Open in browser**

   ```
   http://127.0.0.1:8000
   ```

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+K` | Open command palette |
| `T` | Toggle dark/light mode |
| `1` / `2` / `3` / `4` | Navigate to Dashboard / Meetings / Tasks / Team |
| `M` | New meeting |
| `N` | New task |
| `?` | Show shortcuts |
| `Esc` | Close modal / palette |

---

## API Endpoints

### Members
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/members/` | List all members |
| `POST` | `/api/members/` | Create a member |
| `GET` | `/api/members/{id}` | Get member by ID |
| `DELETE` | `/api/members/{id}` | Delete a member |

### Meetings
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/meetings/` | List all meetings |
| `POST` | `/api/meetings/` | Create a meeting |
| `GET` | `/api/meetings/{id}` | Get meeting details |
| `POST` | `/api/meetings/{id}/upload-audio` | Upload audio recording |
| `POST` | `/api/meetings/{id}/paste-transcript` | Save pasted transcript |
| `POST` | `/api/meetings/{id}/transcribe` | Transcribe audio (Whisper) |
| `POST` | `/api/meetings/{id}/generate-mom` | Generate MOM (Claude) |
| `POST` | `/api/meetings/{id}/extract-tasks` | Extract tasks from MOM (Claude) |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks/` | List tasks (filterable by status, assignee, priority) |
| `POST` | `/api/tasks/` | Create a task |
| `GET` | `/api/tasks/{id}` | Get task by ID |
| `PATCH` | `/api/tasks/{id}` | Update task fields |
| `DELETE` | `/api/tasks/{id}` | Delete a task |

### Dashboard
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/dashboard/stats` | Aggregated stats + upcoming deadlines |
| `GET` | `/api/dashboard/alerts` | Overdue tasks + 3-day deadline warnings |
| `GET` | `/api/dashboard/member-summary` | Per-member task breakdown |

---

## AI Pipeline

The meeting-to-tasks pipeline works in 4 steps:

```
Upload Audio  →  Transcribe (Whisper)  →  Generate MOM (Claude)  →  Extract Tasks (Claude)
      or
Paste Transcript manually
```

1. **Upload** an audio/video recording or paste a transcript
2. **Transcribe** the audio using OpenAI Whisper (if audio was uploaded)
3. **Generate MOM** — Claude creates a structured document with agenda, discussion points, decisions, and action items
4. **Extract Tasks** — Claude parses the MOM and returns structured tasks with titles, assignees, deadlines, and priority levels, which are automatically saved to the database

---

## License

MIT

---

## Author

**Swagata Banerjee** — Consultant at Micro Turners
