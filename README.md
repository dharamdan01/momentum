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

### **[Live Demo](https://momentum.loca.lt)**

<br>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Claude](https://img.shields.io/badge/Claude_AI-D97757?style=flat-square&logo=anthropic&logoColor=white)](https://anthropic.com)
[![Whisper](https://img.shields.io/badge/Whisper-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![License](https://img.shields.io/badge/MIT-green?style=flat-square&label=License)](LICENSE)

<br>

[Live Demo](https://momentum.loca.lt) · [Getting Started](#-getting-started) · [Features](#-features) · [How It Works](#-how-it-works) · [API Reference](#-api-reference) · [Pitch Deck](MOMentum_Pitch.pptx)

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

### Notifications & Reminders
- **Email** reminders via SMTP (Gmail, Outlook, etc.)
- **Telegram** bot notifications
- Auto-reminders for upcoming deadlines (3-day window)
- Overdue alerts sent to assignees
- Management summary notifications with full team status
- Per-member notification preferences (email / telegram / all)
- Background scheduler runs every 6 hours
- Manual trigger for instant reminders

</td>
<td width="50%">

### Auth & Multi-User
- JWT-based authentication (login / register)
- Role-based access (management / member / FDE / consultant)
- Management dashboard with team-wide visibility
- Personal notification preferences per user
- Secure password hashing (bcrypt)

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
Auth        →  JWT (python-jose) + bcrypt
Notifications → SMTP email + Telegram Bot API
Scheduler   →  APScheduler (async, background)
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
JWT_SECRET=any-random-string-here

# Email reminders (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password

# Telegram reminders (optional — create a bot via @BotFather)
TELEGRAM_BOT_TOKEN=your-bot-token
```

> **No keys? No problem.** Meetings, tasks, team, and dashboard all work fully offline. AI features need API keys, and notification channels are opt-in.

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
│   ├── main.py                # FastAPI entry, migrations, scheduler startup
│   ├── database.py            # SQLAlchemy engine + session
│   ├── models.py              # Member, Meeting, Task (with auth + notif fields)
│   ├── schemas.py             # Pydantic models (incl. auth, notification prefs)
│   │
│   ├── routers/
│   │   ├── auth.py            # Login, register, JWT token management
│   │   ├── dashboard.py       # Stats, alerts, workload summary
│   │   ├── meetings.py        # Meeting CRUD + AI pipeline
│   │   ├── members.py         # Team CRUD
│   │   ├── notifications.py   # Notification prefs, test, manual triggers
│   │   └── tasks.py           # Task CRUD with filters
│   │
│   ├── services/
│   │   ├── auth.py            # JWT + bcrypt password hashing
│   │   ├── mom_generator.py   # Whisper + Claude integration
│   │   ├── notifications.py   # Email (SMTP) + Telegram bot sending
│   │   ├── reminder.py        # Overdue detection + deadline alerts
│   │   └── scheduler.py       # APScheduler — auto-reminders every 6h
│   │
│   └── static/
│       ├── index.html         # SPA shell (with login screen)
│       ├── style.css          # Dual-theme, glassmorphism, animations
│       └── app.js             # Client-side logic (auth-aware)
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
| `PATCH` | `/api/members/{id}` | Update member |
| `DELETE` | `/api/members/{id}` | Remove member |

</details>

<details>
<summary><strong>Auth</strong> — Login & registration</summary>

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/register` | Register a new user |
| `POST` | `/api/auth/login` | Login, get JWT token |
| `GET` | `/api/auth/me` | Get current user info |

</details>

<details>
<summary><strong>Notifications</strong> — Reminders & preferences</summary>

| Method | Endpoint | Description |
|--------|----------|-------------|
| `PATCH` | `/api/notifications/preferences` | Update notification prefs |
| `POST` | `/api/notifications/test` | Send test notification |
| `POST` | `/api/notifications/send-summary` | Trigger management summary |
| `POST` | `/api/notifications/send-reminders` | Trigger full reminder cycle |
| `GET` | `/api/notifications/status` | Check configured channels |

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

## The Pitch

<br>

<div align="center">

### **$37 billion** is wasted every year on unproductive meetings.

*— Atlassian Workplace Research*

</div>

<br>

The average employee sits through **62 meetings a month**. Most end with verbal agreements that no one writes down. Action items get buried in Slack threads, scribbled on sticky notes, or — worst case — forgotten entirely. A week later, the same items resurface in the next meeting. The cycle repeats.

**MOMentum exists to kill that cycle.**

<br>

### What it does

| Before MOMentum | After MOMentum |
|:---|:---|
| Someone furiously scribbles notes | AI generates structured minutes in seconds |
| "Can you share the MOM?" — 3 days later | MOM is ready before the meeting room is empty |
| Action items live in someone's head | Tasks auto-created with owners, deadlines, priorities |
| "Wait, who was supposed to do that?" | Dashboard shows exactly who owns what |
| Overdue tasks discovered in the next meeting | Real-time alerts before deadlines hit |

<br>

### Why it matters

**For teams of 5–50 people**, meetings are the operating system of the company. Decisions happen there. Priorities shift there. Work gets assigned there. But there's no system to capture that output and track it to completion.

MOMentum is that system.

- **1 click** to transcribe a meeting
- **1 click** to generate structured minutes
- **1 click** to extract every action item
- **0 clicks** to track deadlines — it does that automatically

<br>

### The market

| Segment | Problem MOMentum solves |
|---------|------------------------|
| **Consulting firms** | Client meeting follow-ups slip through cracks |
| **Startups** | Fast-moving teams lose track of who's doing what |
| **Agencies** | Multiple client projects, dozens of weekly syncs |
| **Engineering teams** | Sprint planning decisions vanish after standup |
| **Leadership** | No visibility into whether meeting outcomes become reality |

<br>

### How it's different

| Tool | What it does | What it misses |
|------|-------------|----------------|
| Otter.ai | Transcribes meetings | No task extraction, no tracking |
| Notion | Organizes notes | Manual entry, no AI pipeline |
| Asana / Linear | Tracks tasks | Tasks must be created manually |
| **MOMentum** | **End-to-end: Record → Transcribe → MOM → Tasks → Track** | **Nothing. That's the point.** |

<br>

### The vision

Today, MOMentum handles the full meeting-to-task pipeline with auto-reminders, multi-user auth, and notifications via email + Telegram. Tomorrow:

- **Integrations** — Slack, Google Calendar, Zoom, Microsoft Teams, WhatsApp
- **Meeting analytics** — which meetings produce the most action? Which produce the most waste?
- **Cross-meeting intelligence** — "This task was discussed in 3 meetings and still isn't done"
- **Voice-first mobile app** — record on the go, tasks appear on your dashboard

The goal isn't to replace meetings. It's to make sure every meeting **actually leads somewhere**.

<br>

---

<br>

## License

MIT 

<br>

---

<div align="center">
<br>

Built by **Swagata Banerjee** — FDE at Micro Turners

*Stop losing action items. Start building MOMentum.*

<br>
</div>
