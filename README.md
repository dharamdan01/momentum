<div align="center">

<br>

<img src="https://img.shields.io/badge/%E2%9A%A1-MOMentum-7C6CF6?style=for-the-badge&labelColor=09090F" alt="MOMentum" height="40">

<br><br>

# MOMentum

**Turn meetings into momentum.**

Record. Transcribe. Generate MOMs. Extract tasks. Track everything.<br>
AI-powered meeting intelligence — so nothing falls through the cracks.

<br>

[![Live Demo](https://img.shields.io/badge/Live_Demo-momentum.loca.lt-7C6CF6?style=for-the-badge&logo=vercel&logoColor=white)](https://momentum.loca.lt)
&nbsp;&nbsp;
[![Pitch Deck](https://img.shields.io/badge/Pitch_Deck-Download_PPT-A855F7?style=for-the-badge&logo=microsoftpowerpoint&logoColor=white)](docs/MOMentum_Pitch.pptx)

<br>

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Claude AI](https://img.shields.io/badge/Claude_AI-D97757?style=flat-square&logo=anthropic&logoColor=white)](https://anthropic.com)
[![Whisper](https://img.shields.io/badge/Whisper-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![JWT Auth](https://img.shields.io/badge/JWT-Auth-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)](#auth--multi-user)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](#tech-stack)
[![Docker Ready](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)](#deployment)
[![MIT License](https://img.shields.io/badge/License-MIT-10B981?style=flat-square)](#license)

<br>

[Features](#features) · [Architecture](#system-architecture) · [Quick Start](#quick-start) · [API Reference](#api-reference) · [User Manual](#user-manual)

<br>

</div>

---

<br>

> **$37 billion** is wasted every year on unproductive meetings. — *Atlassian Workplace Research*
>
> The average employee sits through **62 meetings a month**. Most end with verbal agreements that no one writes down.

<br>

## The Problem

Every meeting ends with action items. Most of them die in chat threads, sticky notes, or someone's memory. A week later, the same items resurface in the next meeting — and the cycle repeats.

**There's no system to capture meeting output and track it to completion.**

MOMentum is that system.

<br>

## How It Works

```
╭──────────────────────────────────────────────────────────────────────────╮
│                                                                          │
│    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐      │
│    │  UPLOAD   │     │TRANSCRIBE│     │ GENERATE │     │ EXTRACT  │      │
│    │  Audio /  │────▶│   with   │────▶│ MOM with │────▶│  Tasks   │      │
│    │  Text     │     │ Whisper  │     │  Claude  │     │  (auto)  │      │
│    └──────────┘     └──────────┘     └──────────┘     └──────────┘      │
│                                                                          │
│    "Hey let's        Full text        # Meeting MOM    ☑ Fix API         │
│     discuss the      transcript       ## Decisions       → Karan         │
│     API bug..."      with speakers    ## Action Items    → Oct 18        │
│                                       ## Next Steps      → High          │
│                                                                          │
│                                              ┌───────────────────┐       │
│                                              │   📊 Dashboard     │       │
│                                              │   📋 Kanban Board  │       │
│                                              │   🔔 Auto-Alerts   │       │
│                                              └───────────────────┘       │
╰──────────────────────────────────────────────────────────────────────────╯
```

**One meeting goes in. Structured, trackable tasks come out. Zero manual work.**

<br>

## Before vs After

| Before MOMentum | After MOMentum |
|:---|:---|
| Someone furiously scribbles notes | AI generates structured minutes in **seconds** |
| "Can you share the MOM?" — 3 days later | MOM ready before the meeting room is empty |
| Action items live in someone's head | Tasks auto-created with owners, deadlines, priorities |
| "Wait, who was supposed to do that?" | Dashboard shows exactly who owns what |
| Overdue tasks discovered in the next meeting | Real-time alerts **before** deadlines hit |
| No visibility for management | Auto-summary of team status every 6 hours |

<br>

## Features

<table>
<tr>
<td width="50%" valign="top">

### 🤖 AI Meeting Pipeline
- **Upload audio** or paste transcripts
- Auto-transcription via **OpenAI Whisper**
- Structured MOM generation via **Claude**
- One-click task extraction with assignees, deadlines & priorities

</td>
<td width="50%" valign="top">

### 📋 Task Management
- `Pending` → `In Progress` → `Completed` workflow
- Auto-detects **overdue** tasks
- **List view** with search, status & member filters
- **Kanban board** with drag-friendly column grouping

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔔 Notifications & Reminders
- **Email** reminders via SMTP (Gmail, Outlook, etc.)
- **Telegram** bot notifications
- Auto-reminders for deadlines (3-day window)
- Overdue alerts to assignees
- Management summary — full team status
- Per-member notification preferences
- Background scheduler runs every **6 hours**
- Manual trigger for instant reminders

</td>
<td width="50%" valign="top">

### 🔐 Auth & Multi-User
- JWT-based authentication (login / register)
- Role-based access (`management` / `member` / `FDE` / `consultant`)
- Management dashboard with team-wide visibility
- Personal notification preferences per user
- Secure password hashing (**bcrypt**)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📊 Dashboard & Analytics
- Real-time stats with animated counters
- SVG progress ring for completion overview
- Deadline alerts (3-day & 7-day windows)
- Per-member workload breakdown
- Live activity feed

</td>
<td width="50%" valign="top">

### 🎨 Premium UI
- **Dark / Light mode** (respects system preference)
- Glassmorphism + animated gradient borders
- **Command palette** — `Ctrl+K` to do anything
- Keyboard-first navigation
- Confetti on task completion 🎉

</td>
</tr>
</table>

<br>

## Tech Stack

| Layer | Technology |
|:------|:-----------|
| **Frontend** | Vanilla HTML / CSS / JS — no framework, no build step |
| **Backend** | Python · FastAPI · SQLAlchemy ORM |
| **Database** | SQLite (zero-config, single-file) |
| **AI — MOM** | Anthropic Claude API |
| **AI — Audio** | OpenAI Whisper API |
| **Auth** | JWT (`python-jose`) + `bcrypt` |
| **Notifications** | SMTP email + Telegram Bot API |
| **Scheduler** | APScheduler (async, background) |
| **Deployment** | Docker + Nginx + systemd |

<br>

## System Architecture

> Deep-dive into how every component connects. For the non-technical walkthrough, see **[User Manual](#user-manual)** below.

<br>

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                     CLIENTS                                         │
│                                                                                     │
│          Browser (SPA)              Mobile Browser             API Consumer          │
│              │                           │                          │                │
└──────────────┼───────────────────────────┼──────────────────────────┼────────────────┘
               │ HTTPS                     │ HTTPS                    │ HTTPS
               ▼                           ▼                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              REVERSE PROXY (Nginx)                                  │
│                                                                                     │
│    SSL termination · Static file caching · Gzip · Rate limiting · Proxy pass        │
│                                         :443 → :8000                                │
└─────────────────────────────────────────┬───────────────────────────────────────────┘
                                          │
                                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          APPLICATION SERVER (Uvicorn + FastAPI)                      │
│                                                                                     │
│  ┌─────────────────┐   ┌──────────────────┐   ┌──────────────────────────────────┐  │
│  │   AUTH LAYER     │   │   ROUTER LAYER    │   │        SERVICE LAYER             │  │
│  │                  │   │                   │   │                                  │  │
│  │  JWT Decode ─────┼──▶│  /api/auth/*      │   │  mom_generator.py                │  │
│  │  bcrypt verify   │   │  /api/meetings/*  │──▶│    ├─ transcribe_audio()         │  │
│  │  Role gates:     │   │  /api/tasks/*     │   │    ├─ generate_mom()             │  │
│  │   require_auth   │   │  /api/members/*   │   │    └─ extract_tasks()            │  │
│  │   require_mgmt   │   │  /api/dashboard/* │   │                                  │  │
│  │                  │   │  /api/notifs/*     │   │  notifications.py                │  │
│  └─────────────────┘   └──────────────────┘   │    ├─ send_email()  [SMTP]        │  │
│                                                │    ├─ send_telegram() [Bot API]   │  │
│                                                │    └─ notify_member()             │  │
│                                                │                                  │  │
│                                                │  scheduler.py                     │  │
│                                                │    └─ APScheduler (6h interval)   │  │
│                                                │       └─ run_reminder_cycle()     │  │
│                                                │                                  │  │
│                                                │  reminder.py                      │  │
│                                                │    ├─ check_overdue_tasks()       │  │
│                                                │    ├─ get_upcoming_deadlines()    │  │
│                                                │    └─ get_member_tasks_summary()  │  │
│                                                └──────────────────────────────────┘  │
│                                                                                     │
│  ┌──────────────────────────────────────┐   ┌────────────────────────────────────┐  │
│  │        ORM LAYER (SQLAlchemy)         │   │       STATIC FILE SERVER           │  │
│  │                                       │   │                                    │  │
│  │  Member ←──┐                          │   │  /static/index.html  (SPA shell)   │  │
│  │  Meeting ──┼── relationships          │   │  /static/app.js     (client logic) │  │
│  │  Task ←────┘  (FK: assigned_to,       │   │  /static/style.css  (themes)       │  │
│  │               meeting_id)             │   │                                    │  │
│  └───────────────────┬───────────────────┘   └────────────────────────────────────┘  │
│                      │                                                               │
└──────────────────────┼───────────────────────────────────────────────────────────────┘
                       │ SQLAlchemy Engine
                       ▼
              ┌─────────────────┐
              │   SQLite (data.db)   │
              │                 │
              │  members        │
              │  meetings       │
              │  tasks          │
              └─────────────────┘
```

<br>

### Request Flow — Generating a MOM

```
   User clicks                                                              External
  "Generate MOM"                                                             APIs
       │                                                                      │
       ▼                                                                      │
  ┌─────────┐    POST /api/meetings/{id}/generate-mom    ┌──────────┐        │
  │ Browser  │ ──────────────────────────────────────────▶│  FastAPI  │        │
  │ (app.js) │    Authorization: Bearer <JWT>             │  Router   │        │
  └─────────┘                                             └────┬─────┘        │
                                                               │              │
                                          ┌────────────────────┘              │
                                          ▼                                   │
                                   ┌─────────────┐                            │
                                   │  Auth Layer  │                            │
                                   │  decode JWT  │                            │
                                   │  load Member │                            │
                                   └──────┬──────┘                            │
                                          │ ✅ Authenticated                   │
                                          ▼                                   │
                                   ┌──────────────┐                           │
                                   │  meetings.py  │                           │
                                   │  router       │                           │
                                   └──────┬───────┘                           │
                                          │                                   │
                              ┌───────────┴───────────┐                       │
                              ▼                       ▼                       │
                    ┌──────────────┐        ┌──────────────────┐              │
                    │  SQLAlchemy   │        │  mom_generator.py │              │
                    │  load meeting │        │                   │              │
                    │  + transcript │        │  generate_mom()  ─┼─────────────┤
                    └──────────────┘        │                   │   Anthropic  │
                                            │              ◀────┼── Claude API │
                                            │  extract_tasks() ─┼─────────────┤
                                            │              ◀────┼── Claude API │
                                            └────────┬─────────┘              │
                                                     │                        │
                                                     ▼                        │
                                              ┌─────────────┐                 │
                                              │  SQLAlchemy   │                │
                                              │  save MOM text│                │
                                              │  create Tasks │                │
                                              └──────┬──────┘                 │
                                                     │                        │
                                                     ▼                        │
                                              ┌─────────────┐                 │
                                              │   JSON 200   │                 │
                                              │  { mom, tasks}│                │
                                              └─────────────┘                 │
```

<br>

### Request Flow — Audio Transcription

```
                                          ┌──────────────────────────┐
   User uploads                           │                          │
   audio file                             │     OpenAI Whisper API   │
       │                                  │     (whisper-1 model)    │
       ▼                                  │                          │
  ┌─────────┐   multipart/form-data       └────────────▲─────────────┘
  │ Browser  │ ────────────────────┐                    │
  └─────────┘                      │                    │ Audio bytes
                                   ▼                    │
                            ┌─────────────┐      ┌──────┴──────┐
                            │   FastAPI    │─────▶│ mom_generator│
                            │   Router    │      │ .transcribe  │
                            └─────────────┘      │ _audio()     │
                                                  └──────┬──────┘
                                                         │
                                                         ▼
                                                  ┌─────────────┐
                                                  │  Save to DB  │
                                                  │  meeting     │
                                                  │  .transcript │
                                                  └─────────────┘
```

<br>

### Notification & Scheduler Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      BACKGROUND SCHEDULER (APScheduler)                     │
│                                                                             │
│    AsyncIOScheduler                                                         │
│    ├─ Trigger: IntervalTrigger(hours=6)                                     │
│    ├─ First run: 1 minute after app startup                                 │
│    └─ Job: run_reminder_cycle()                                             │
│                                                                             │
│    ┌─────────────── run_reminder_cycle() ──────────────────────────┐        │
│    │                                                                │        │
│    │   1. check_overdue_tasks(db)                                   │        │
│    │      ├─ Query: deadline < now AND status ≠ completed           │        │
│    │      ├─ Update status → OVERDUE                                │        │
│    │      └─ For each → notify_overdue(assignee, task)              │        │
│    │                                                                │        │
│    │   2. get_upcoming_deadlines(db, days=3)                        │        │
│    │      ├─ Query: now ≤ deadline ≤ now+3d AND status ≠ completed  │        │
│    │      ├─ Filter: reminder_sent = 0                              │        │
│    │      ├─ For each → notify_task_reminder(assignee, task)        │        │
│    │      └─ Mark reminder_sent = 1                                 │        │
│    │                                                                │        │
│    │   3. Management summary                                        │        │
│    │      ├─ Query all members with role = "management"             │        │
│    │      ├─ get_member_tasks_summary(db)                           │        │
│    │      └─ For each manager → notify_management_summary()         │        │
│    │                                                                │        │
│    └────────────────────────────────────────────────────────────────┘        │
│                                                                             │
└───────┬─────────────────────────────────┬───────────────────────────────────┘
        │                                 │
        ▼                                 ▼
┌───────────────┐                 ┌───────────────┐
│  SMTP Server   │                 │  Telegram API  │
│                │                 │                │
│  Gmail         │                 │  Bot sends     │
│  Outlook       │                 │  via HTTP POST │
│  Any SMTP      │                 │  to chat_id    │
│                │                 │                │
│  Assignee gets │                 │  Assignee gets │
│  HTML email    │                 │  formatted msg │
└───────────────┘                 └───────────────┘

    ┌──────────────────────────────────────────────┐
    │          MEMBER NOTIFICATION ROUTING          │
    │                                               │
    │  notification_pref = "email"    → SMTP only   │
    │  notification_pref = "telegram" → TG only     │
    │  notification_pref = "all"      → both        │
    │                                               │
    │  notify_member() checks pref and routes       │
    └──────────────────────────────────────────────┘
```

<br>

### Authentication & Authorization

```
┌──────────────────────────────────────────────────────────────────┐
│                       AUTH FLOW                                   │
│                                                                   │
│   REGISTER                           LOGIN                        │
│   ────────                           ─────                        │
│   POST /api/auth/register            POST /api/auth/login         │
│   { name, email, password }          { email, password }          │
│          │                                  │                     │
│          ▼                                  ▼                     │
│   ┌──────────────┐                   ┌──────────────┐            │
│   │ bcrypt.hashpw │                   │ bcrypt.checkpw│            │
│   │ (salt rounds) │                   │ (verify)      │            │
│   └──────┬───────┘                   └──────┬───────┘            │
│          │                                  │                     │
│          ▼                                  │ ✅ Match            │
│   ┌──────────────┐                          ▼                     │
│   │ Store member  │                   ┌──────────────┐            │
│   │ + hash in DB  │                   │ jwt.encode()  │            │
│   └──────────────┘                   │ {sub, role,   │            │
│                                       │  exp: +72h}   │            │
│                                       └──────┬───────┘            │
│                                              │                     │
│                                              ▼                     │
│                                       ┌──────────────┐            │
│                                       │ Return JWT    │            │
│                                       │ to client     │            │
│                                       └──────────────┘            │
│                                                                   │
│   PROTECTED ROUTE ACCESS                                          │
│   ──────────────────────                                          │
│   Authorization: Bearer <token>                                   │
│          │                                                        │
│          ▼                                                        │
│   ┌──────────────┐     ┌──────────┐     ┌──────────────────┐     │
│   │ jwt.decode()  │────▶│ Load     │────▶│ require_auth()    │     │
│   │ verify sig    │     │ Member   │     │ require_mgmt()    │     │
│   │ check expiry  │     │ from DB  │     │ (role gate)       │     │
│   └──────────────┘     └──────────┘     └──────────────────┘     │
│                                                                   │
│   ROLE HIERARCHY                                                  │
│   ──────────────                                                  │
│   management ──▶ Full access: all endpoints + team summaries      │
│   member     ──▶ Standard access: own tasks, meetings, CRUD       │
│   FDE        ──▶ Standard access: same as member                  │
│   consultant ──▶ Standard access: same as member                  │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

<br>

### Database Schema (ERD)

```
┌────────────────────────────┐       ┌────────────────────────────────┐
│         MEMBERS             │       │           MEETINGS              │
├────────────────────────────┤       ├────────────────────────────────┤
│ id           INTEGER PK     │       │ id             INTEGER PK       │
│ name         VARCHAR(100)   │       │ title          VARCHAR(300)     │
│ email        VARCHAR(200)   │       │ date           DATETIME         │
│ phone        VARCHAR(20)    │       │ participants   TEXT              │
│ role         VARCHAR(50)    │       │ transcript     TEXT              │
│ password_hash VARCHAR(200)  │       │ mom_text       TEXT              │
│ telegram_chat_id VARCHAR(100│)      │ audio_file     VARCHAR(500)     │
│ notification_pref VARCHAR(20│)      │ created_at     DATETIME         │
│ created_at   DATETIME       │       └───────────────┬────────────────┘
└──────────────┬─────────────┘                        │
               │                                      │
               │ 1                                    │ 1
               │                                      │
               │ ╲╱ *                                  │ ╲╱ *
               │                                      │
┌──────────────┴──────────────────────────────────────┴────────────────┐
│                              TASKS                                    │
├─────────────────────────────────────────────────────────────────────┤
│ id              INTEGER PK                                           │
│ title           VARCHAR(500)                                         │
│ description     TEXT                                                  │
│ status          ENUM(pending, in_progress, completed, overdue)       │
│ priority        ENUM(high, medium, low)                              │
│ deadline        DATETIME                                             │
│ assigned_to     INTEGER FK → members.id                              │
│ meeting_id      INTEGER FK → meetings.id                             │
│ reminder_sent   INTEGER (0/1 flag)                                   │
│ created_at      DATETIME                                             │
│ updated_at      DATETIME (auto on update)                            │
└─────────────────────────────────────────────────────────────────────┘
```

<br>

### Deployment Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                        PRODUCTION (VPS / EC2)                        │
│                                                                      │
│   ┌──────────┐      ┌───────────────┐      ┌──────────────────────┐ │
│   │  Nginx    │      │   Gunicorn     │      │    SQLite            │ │
│   │  :443     │─────▶│   + Uvicorn    │─────▶│    data.db           │ │
│   │  SSL/TLS  │      │   workers      │      │    (persistent vol)  │ │
│   └──────────┘      └───────┬───────┘      └──────────────────────┘ │
│                              │                                       │
│                              │ on startup                            │
│                              ▼                                       │
│                       ┌─────────────┐                                │
│                       │ APScheduler  │──── every 6h ──── reminders   │
│                       └─────────────┘                                │
│                                                                      │
│   systemd: momentum.service                                          │
│   Auto-restart on failure · Logs to journalctl                       │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                        DOCKER DEPLOYMENT                             │
│                                                                      │
│   docker-compose.yml                                                 │
│   ┌──────────────────────────────────────────────────┐               │
│   │  momentum (python:3.12-slim)                      │               │
│   │  ├─ gunicorn + uvicorn workers                    │               │
│   │  ├─ /app/data.db  → volume mount                  │               │
│   │  ├─ /app/uploads/ → volume mount                  │               │
│   │  ├─ healthcheck: curl http://localhost:8000/       │               │
│   │  └─ env_file: .env                                │               │
│   └──────────────────────────────────────────────────┘               │
└──────────────────────────────────────────────────────────────────────┘
```

<br>

### Security Model

| Layer | Implementation |
|:------|:---------------|
| **Password storage** | bcrypt with random salt — never plaintext |
| **Session tokens** | JWT (HS256) with 72-hour expiry, server-side secret |
| **Transport** | HTTPS via Nginx SSL termination (Let's Encrypt) |
| **Auth enforcement** | FastAPI `Depends()` — every protected route requires valid JWT |
| **Role gating** | `require_management` dependency rejects non-management roles |
| **Input validation** | Pydantic schemas validate all request bodies at the boundary |
| **SQL injection** | SQLAlchemy ORM parameterizes all queries |
| **Data isolation** | SQLite file lives on server, not exposed to network |
| **Secrets management** | All credentials in `.env`, never committed (`.gitignore`) |

<br>

## Quick Start

### 1. Clone & install

```bash
git clone https://github.com/gitswagata1/momentum.git
cd momentum

python -m venv venv
source venv/bin/activate          # macOS / Linux
venv\Scripts\activate             # Windows

pip install -r requirements.txt
```

### 2. Configure

```bash
cp .env.example .env
```

Edit `.env` with your keys:

```env
# Required for AI features (optional — app works without them)
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...

# Auth
JWT_SECRET=any-random-string-here

# Email reminders (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=you@gmail.com
SMTP_PASS=your-app-password

# Telegram reminders (optional — create via @BotFather)
TELEGRAM_BOT_TOKEN=your-bot-token
```

> **No keys?** Meetings, tasks, team, and dashboard work fully offline. AI features need API keys. Notifications are opt-in.

### 3. Run

```bash
uvicorn app.main:app --reload
```

Open **http://127.0.0.1:8000** — done.

<br>

## Deployment

<details>
<summary><strong>🐳 Docker (recommended)</strong></summary>

```bash
docker compose up -d
```

That's it. App runs on port 8000 with persistent SQLite volume.

</details>

<details>
<summary><strong>☁️ Render (one-click)</strong></summary>

1. Fork this repo
2. Connect to [render.com](https://render.com)
3. The `render.yaml` blueprint auto-configures everything
4. Add your API keys in the Render dashboard

</details>

<details>
<summary><strong>🖥️ Ubuntu VPS / EC2 / Lightsail</strong></summary>

```bash
# One-command setup
curl -sSL https://raw.githubusercontent.com/gitswagata1/momentum/main/deploy/setup.sh | bash
```

Sets up Python, venv, Nginx reverse proxy, systemd service, and SSL.

</details>

<br>

## Project Structure

```
momentum/
│
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI entry · lifespan · router registration
│   ├── config.py                # Centralized settings (all env vars in one place)
│   ├── database.py              # SQLAlchemy engine + session factory
│   ├── migrations.py            # SQLite ALTER TABLE migrations
│   │
│   ├── models/                  # SQLAlchemy ORM models (one per domain entity)
│   │   ├── __init__.py          # Re-exports: Member, Meeting, Task, TaskStatus, TaskPriority
│   │   ├── member.py            # Member model (auth fields, notification prefs)
│   │   ├── meeting.py           # Meeting model (transcript, MOM, audio)
│   │   └── task.py              # Task model + status/priority enums
│   │
│   ├── schemas/                 # Pydantic request/response models (one per domain)
│   │   ├── __init__.py          # Re-exports all schemas
│   │   ├── auth.py              # LoginRequest · RegisterRequest · LoginResponse
│   │   ├── member.py            # MemberCreate · MemberOut
│   │   ├── meeting.py           # MeetingCreate · MeetingOut
│   │   ├── task.py              # TaskCreate · TaskUpdate · TaskOut
│   │   ├── dashboard.py         # DashboardStats
│   │   └── notification.py      # NotificationPrefUpdate
│   │
│   ├── routers/                 # API route handlers
│   │   ├── __init__.py
│   │   ├── auth.py              # Login · register · JWT management
│   │   ├── dashboard.py         # Stats · alerts · workload summary
│   │   ├── meetings.py          # Meeting CRUD + AI pipeline
│   │   ├── members.py           # Team CRUD
│   │   ├── notifications.py     # Prefs · test · manual triggers
│   │   └── tasks.py             # Task CRUD with filters
│   │
│   ├── services/                # Business logic layer
│   │   ├── __init__.py
│   │   ├── auth.py              # JWT creation/validation + bcrypt hashing
│   │   ├── mom_generator.py     # Whisper transcription + Claude MOM/task extraction
│   │   ├── notifications.py     # Email (SMTP) + Telegram bot dispatch
│   │   ├── reminder.py          # Overdue detection + deadline scanning
│   │   └── scheduler.py         # APScheduler — background reminder cycle
│   │
│   ├── static/                  # Frontend (vanilla SPA — no build step)
│   │   ├── index.html           # Shell: login screen + dashboard layout
│   │   ├── app.js               # Client-side logic (auth-aware, API calls)
│   │   └── style.css            # Dual-theme · glassmorphism · animations
│   │
│   └── uploads/                 # Audio file storage (gitignored, .gitkeep)
│       └── .gitkeep
│
├── deploy/                      # Production deployment configs
│   ├── setup.sh                 # One-command Ubuntu server setup
│   ├── update.sh                # Pull latest + restart service
│   ├── nginx.conf               # Reverse proxy config
│   └── momentum.service         # systemd unit file
│
├── docs/                        # Presentation & pitch materials
│   ├── MOMentum_Pitch.pptx      # 10-slide dark-themed PowerPoint
│   ├── MOMentum_Pitch_Script.md # 8-minute spoken script + Q&A cheat sheet
│   └── PRESENTATION.md          # Slide-by-slide outline
│
├── Dockerfile                   # Python 3.12-slim + gunicorn
├── docker-compose.yml           # One-command Docker deployment
├── render.yaml                  # Render one-click deploy blueprint
├── requirements.txt             # Python dependencies
├── .env.example                 # Template for environment variables
├── .gitignore
├── LICENSE                      # MIT
└── README.md
```

<br>

## Keyboard Shortcuts

| Key | Action |
|:---:|:-------|
| `Ctrl+K` | Command palette |
| `T` | Toggle dark / light mode |
| `1` `2` `3` `4` | Dashboard · Meetings · Tasks · Team |
| `M` | New meeting |
| `N` | New task |
| `?` | Show all shortcuts |
| `Esc` | Close anything open |

<br>

## API Reference

<details>
<summary><strong>Auth</strong> — Login & registration</summary>

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/register` | Register new user |
| `POST` | `/api/auth/login` | Login → JWT token |
| `GET` | `/api/auth/me` | Current user info |

</details>

<details>
<summary><strong>Meetings</strong> — CRUD + AI pipeline</summary>

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/meetings/` | List all meetings |
| `POST` | `/api/meetings/` | Create meeting |
| `GET` | `/api/meetings/{id}` | Meeting details + tasks |
| `POST` | `/api/meetings/{id}/upload-audio` | Upload audio file |
| `POST` | `/api/meetings/{id}/paste-transcript` | Paste transcript |
| `POST` | `/api/meetings/{id}/transcribe` | Whisper transcription |
| `POST` | `/api/meetings/{id}/generate-mom` | Claude MOM generation |
| `POST` | `/api/meetings/{id}/extract-tasks` | Claude task extraction |

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

## Why Custom — Not Miro, Not Zoom

| Capability | Zoom AI | Miro | Notion | Asana | **MOMentum** |
|:-----------|:-------:|:----:|:------:|:-----:|:------------:|
| Transcription | ✅ | ❌ | ❌ | ❌ | ✅ |
| Structured MOM | ❌ | ❌ | ❌ | ❌ | ✅ |
| Auto task extraction | ❌ | ❌ | ❌ | ❌ | ✅ |
| Task tracking | ❌ | Partial | Manual | ✅ | ✅ |
| Auto-reminders | ❌ | ❌ | ❌ | ❌ | ✅ |
| Management summary | ❌ | ❌ | ❌ | ❌ | ✅ |
| Email + Telegram alerts | ❌ | ❌ | ❌ | ❌ | ✅ |
| Custom-built for your team | ❌ | ❌ | ❌ | ❌ | ✅ |

**No off-the-shelf tool covers all 7 requirements. MOMentum does.**

<br>

## What It Costs

| Component | Cost | Via |
|:----------|:-----|:----|
| MOM Generation | ~₹1–2 per MOM | Claude AI |
| Audio Transcription | ~₹0.50/min | Whisper AI |
| Email Reminders | Free | SMTP |
| Telegram Reminders | Free | Bot API |
| Server Hosting | ₹400–800/mo | Basic VPS |

> **Total: Under ₹1,000/month** for a team of 5–15 people.

<br>

## Roadmap

| Phase | Timeline | What's Coming |
|:------|:---------|:--------------|
| **Now** | This week | Deploy for Micro Turners · Set up email & Telegram · Onboard team |
| **Next** | Next month | WhatsApp integration · Google Calendar sync · Custom reminder schedules |
| **Future** | Q1 2027 | Meeting analytics · Cross-meeting intelligence · Mobile app |

<br>

## Target Market

| Segment | Problem Solved |
|:--------|:---------------|
| **Consulting firms** | Client meeting follow-ups slip through cracks |
| **Startups** | Fast-moving teams lose track of who's doing what |
| **Agencies** | Multiple client projects, dozens of weekly syncs |
| **Engineering teams** | Sprint planning decisions vanish after standup |
| **Leadership** | No visibility into whether meetings become outcomes |

<br>

## User Manual

> **For everyone on the team.** No technical knowledge needed. This guide covers everything you need to use MOMentum day-to-day.

<br>

### Getting Started — Your First Login

<table>
<tr>
<td width="60">

**1**

</td>
<td>

**Open MOMentum** — Go to the link shared by your team lead (e.g. `https://momentum.loca.lt`).

</td>
</tr>
<tr>
<td>

**2**

</td>
<td>

**Register** — Click "Register", enter your name, email, and a password. Your email should match what's already in the system.

</td>
</tr>
<tr>
<td>

**3**

</td>
<td>

**Login** — Use your email and password. You'll stay logged in for 3 days.

</td>
</tr>
</table>

<br>

### The Dashboard — Your Home Screen

When you log in, you'll see the **Dashboard**. Here's what each part means:

| What You See | What It Means |
|:-------------|:--------------|
| **Total Meetings** | How many meetings have been recorded in the system |
| **Total Tasks** | All tasks across all meetings |
| **Pending / In Progress / Completed** | How many tasks are in each stage |
| **Overdue** (red) | Tasks that missed their deadline — these need attention |
| **Progress Ring** | A visual showing what % of tasks are done |
| **Upcoming Deadlines** | Tasks due in the next 7 days — plan your week here |
| **Team Workload** | How many tasks each person has (management view) |

<br>

### Recording a Meeting — Step by Step

<table>
<tr>
<td width="60">

**1**

</td>
<td>

**Create a meeting** — Go to the Meetings tab, click **"New Meeting"**. Give it a title (e.g. "Weekly Sync — Oct 14"), set the date, and list who was there.

</td>
</tr>
<tr>
<td>

**2**

</td>
<td>

**Add the recording** — You have two options:
- **Upload audio** — Click "Upload Audio" and select your recording file (MP3, WAV, M4A, etc.)
- **Paste text** — If someone already typed up notes, click "Paste Transcript" and paste them in

</td>
</tr>
<tr>
<td>

**3**

</td>
<td>

**Transcribe** (if you uploaded audio) — Click **"Transcribe"**. The AI converts your audio to text in about 30 seconds per hour of recording.

</td>
</tr>
<tr>
<td>

**4**

</td>
<td>

**Generate MOM** — Click **"Generate MOM"**. The AI reads the transcript and creates a professional Minutes of Meeting with agenda, discussion summary, action items, and key decisions. Takes about 10 seconds.

</td>
</tr>
<tr>
<td>

**5**

</td>
<td>

**Extract Tasks** — Click **"Extract Tasks"**. The AI pulls out every action item and creates tasks with the right person's name, deadline, and priority already filled in.

</td>
</tr>
</table>

> **That's it.** Five clicks, and your meeting is fully documented with tracked tasks.

<br>

### Managing Your Tasks

Go to the **Tasks** tab. You'll see two views:

**List View** — A searchable table of all tasks. Use the filters at the top:
- **Status** — Show only Pending, In Progress, Completed, or Overdue
- **Assigned To** — Show only your tasks, or a specific team member's
- **Search** — Type to find any task by name

**Kanban Board** — Visual columns: `Pending` → `In Progress` → `Completed` → `Overdue`. Great for seeing the big picture at a glance.

**Updating a task:**
| What to do | How |
|:-----------|:----|
| Start working on it | Change status to **"In Progress"** |
| Finish it | Change status to **"Completed"** (you'll get a confetti celebration!) |
| See who it's for | Check the **Assigned To** field |
| Check the deadline | The **Deadline** column shows the date — red means overdue |

<br>

### Notifications — Never Miss a Deadline

MOMentum sends you reminders automatically. Here's what you'll receive:

| When | What You Get |
|:-----|:-------------|
| **3 days before a deadline** | A friendly reminder: "Your task is due on [date]" |
| **After a deadline passes** | An urgent alert: "OVERDUE: [task name]" |
| **Every 6 hours** (management) | A summary of the whole team's task status |

**Setting up your notifications:**

1. Click your **name** in the top-right corner
2. Click **"Notification Settings"**
3. Choose how you want reminders:
   - **Email** — Reminders go to your registered email
   - **Telegram** — Reminders go to your Telegram (enter your Chat ID)
   - **Both** — Get reminders on both channels
4. Click **"Send Test"** to make sure it works

**Setting up Telegram:**
1. Search for the team's MOMentum bot on Telegram
2. Send `/start` to the bot
3. The bot replies with your **Chat ID** (a number)
4. Paste that Chat ID in MOMentum's notification settings

<br>

### Managing Your Team (Management Only)

If you're logged in as **management**, you have extra powers:

| Feature | Where to Find It |
|:--------|:-----------------|
| **See everyone's tasks** | Dashboard → Team Workload section |
| **Get team summary** | Automatic email/Telegram every 6 hours |
| **Send instant reminders** | Click **"Send Reminders"** button in the header |
| **Add team members** | Team tab → "Add Member" |
| **View all meetings** | Meetings tab — all meetings from all users |

<br>

### Keyboard Shortcuts (Power Users)

These work anywhere in the app:

| Press | What Happens |
|:-----:|:-------------|
| `Ctrl+K` | Opens the **Command Palette** — type to do anything |
| `T` | Switch between **dark mode** and **light mode** |
| `1` | Jump to Dashboard |
| `2` | Jump to Meetings |
| `3` | Jump to Tasks |
| `4` | Jump to Team |
| `M` | Create a new meeting |
| `N` | Create a new task |
| `?` | Show all shortcuts |

<br>

### FAQ — Common Questions

<details>
<summary><strong>Can I use MOMentum on my phone?</strong></summary>

Yes. Open the same link in your phone's browser. The app is fully responsive and works on any screen size.

</details>

<details>
<summary><strong>What if the AI makes a mistake in the MOM?</strong></summary>

The MOM is editable. You can review it and make changes. Tasks can also be manually adjusted — change the assignee, deadline, or priority anytime.

</details>

<details>
<summary><strong>Can I create tasks without a meeting?</strong></summary>

Yes. Go to the Tasks tab and click "New Task". You can create standalone tasks that aren't linked to any meeting.

</details>

<details>
<summary><strong>I'm not getting email notifications</strong></summary>

1. Check your notification settings (click your name → Notification Settings)
2. Make sure your email is correct in the system
3. Click "Send Test" to verify
4. Check your spam/junk folder

</details>

<details>
<summary><strong>Can multiple people create meetings?</strong></summary>

Yes. Any logged-in user can create meetings, upload audio, generate MOMs, and extract tasks. It's not limited to management.

</details>

<details>
<summary><strong>How do I change my password?</strong></summary>

Currently, contact your admin to reset it. A self-service password reset feature is on the roadmap.

</details>

<details>
<summary><strong>What audio formats are supported?</strong></summary>

MP3, WAV, M4A, WEBM, MP4, OGG, and FLAC. Most phone and laptop recordings work out of the box.

</details>

<details>
<summary><strong>Is my data safe?</strong></summary>

Yes. Passwords are encrypted, sessions use secure tokens, and all data stays on your company's server. Nothing is shared with third parties. The AI APIs only receive the meeting transcript text — no personal data.

</details>

<br>

---

<br>

<div align="center">

### The Vision

The goal isn't to replace meetings.<br>
It's to make sure every meeting **actually leads somewhere**.

<br>

---

<br>

**MIT License**

Built by **[Swagata Banerjee](https://github.com/gitswagata1)** — FDE at Micro Turners

*Stop losing action items. Start building MOMentum.*

<br>
</div>
