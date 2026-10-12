# MOMentum — Presentation Script & Slide Outline
**Audience:** Karan Sir (Management, Micro Turners)
**Duration:** ~10–12 minutes
**Presenter:** Swagata Banerjee

---

## SLIDE 1 — Title

**Visual:** MOMentum logo, tagline "Turn meetings into momentum.", Micro Turners branding.

**Script:**

> Good afternoon, Sir. In our last meeting on 5th November, you outlined a clear need — a tool that goes beyond just meeting minutes. You wanted automated MOMs, task tracking with reminders, deadline alerts, and something the entire team can use.
>
> I've built that tool. It's called **MOMentum** — and I'd like to walk you through it today.

---

## SLIDE 2 — The Problem We Discussed

**Visual:** Three pain points as icons/cards:
1. Action items die in chat threads
2. No one remembers who was assigned what
3. Deadlines pass with no follow-up

**Script:**

> Every meeting at Micro Turners ends with decisions and action items. But right now, those live in someone's notes — or worse, someone's memory. A week later, the same items come up again. There's no system to capture meeting output and track it to completion.
>
> That's exactly what you told me needed to change. And that's what MOMentum does.

---

## SLIDE 3 — What MOMentum Does (Pipeline)

**Visual:** 4-step pipeline diagram:
```
Upload Audio → Transcribe (Whisper AI) → Generate MOM (Claude AI) → Extract Tasks (auto)
```

**Script:**

> Here's how it works. After a meeting, you either upload the recording or paste a transcript. The system uses OpenAI Whisper to transcribe the audio, then Claude AI generates a structured Minutes of Meeting — with agenda, discussion summary, action items, and key decisions.
>
> From that MOM, it automatically extracts every action item, assigns it to the right person, sets deadlines and priorities. One meeting goes in — structured tasks come out. No manual work.

---

## SLIDE 4 — Your 7 Requirements (Checklist)

**Visual:** Table with each requirement and a green checkmark:

| # | Requirement | Status |
|---|-------------|--------|
| 1 | Automated MOM Generation | Done |
| 2 | Task Assignment Tracking | Done |
| 3 | Auto-Reminders to Assignees | Done |
| 4 | Auto-Reminders to Management | Done |
| 5 | Timeline & Deadline Alerts | Done |
| 6 | Communication Channel Integration | Done |
| 7 | Usable by Everyone | Done |

**Script:**

> Let me map this directly to the seven requirements you gave me.
>
> **One** — Automated MOM generation. Done. Audio goes in, structured MOM comes out.
>
> **Two** — Task assignment tracking. Done. Every task extracted from a MOM is tagged with an assignee, deadline, and priority. Each person can filter to see only their tasks.
>
> **Three** — Auto-reminders to assignees. Done. The system automatically sends reminders when deadlines are approaching — 3 days before — via email or Telegram.
>
> **Four** — Auto-reminders to management. Done. You get a summary notification showing every team member's task status — how many pending, in progress, completed, and overdue.
>
> **Five** — Timeline and deadline alerts. Done. The dashboard shows upcoming deadlines, and overdue tasks are flagged in real-time. Alerts are sent automatically.
>
> **Six** — Communication channel integration. Done. We support email via SMTP and Telegram bots. Each member chooses their preferred channel. WhatsApp integration can be added when we get the Business API.
>
> **Seven** — Usable by everyone. Done. The tool has a login system. Every team member gets their own account, sees their own tasks, and receives their own reminders. Management sees everything.

---

## SLIDE 5 — Live Demo: Dashboard

**Visual:** Screenshot of the MOMentum dashboard (dark mode) showing stats, progress ring, upcoming deadlines, team workload.

**Script:**

> This is the dashboard. At a glance, you can see total meetings, total tasks, how many are pending, completed, or overdue. The progress ring shows overall completion percentage.
>
> Below that, upcoming deadlines for the next week. And at the bottom, team workload — each member's task breakdown. This is the management view you asked for — who's doing what, and what's falling behind.

---

## SLIDE 6 — Live Demo: Meetings & MOM Pipeline

**Visual:** Screenshot of the meeting detail modal showing the 4-step pipeline (Audio → Transcribe → MOM → Tasks) with a generated MOM.

**Script:**

> Here's a meeting in the system. You can see the four-step pipeline. Upload the recording, transcribe it, generate the MOM, extract tasks. Each step is one click.
>
> The generated MOM follows a standard format — meeting details, agenda, discussion summary, action items table, key decisions. It's professional and consistent every time.

---

## SLIDE 7 — Live Demo: Task Management

**Visual:** Split screen — list view with filters on left, Kanban board on right.

**Script:**

> Tasks can be viewed two ways. A list view with search, status filters, and member filters — so anyone can quickly find what's assigned to them. Or a Kanban board that groups tasks by status — Pending, In Progress, Completed, Overdue.
>
> Status updates are inline — one dropdown change and it's done. When a task is completed, you get a little celebration. Small thing, but it makes people want to close tasks.

---

## SLIDE 8 — Notifications & Reminders

**Visual:** Diagram showing:
- Scheduler (every 6 hours) → checks deadlines
- Sends to Assignees: "Your task is due in 2 days"
- Sends to Management: "Team status summary"
- Channels: Email / Telegram

**Script:**

> The reminder system runs automatically in the background, every 6 hours. It checks for two things:
>
> First — tasks with deadlines in the next 3 days. It sends a reminder to the assignee: "Your task is due on this date."
>
> Second — overdue tasks. It alerts the assignee that the task is past deadline.
>
> And for you, Sir — it sends a management summary. A table showing every team member's task counts: pending, in progress, completed, overdue. You don't have to open the tool to know what's happening. It comes to you.
>
> Each member chooses their channel — email, Telegram, or both. And if you ever need an immediate update, there's a "Send Reminders" button on the dashboard that triggers it manually.

---

## SLIDE 9 — Multi-User & Security

**Visual:** Login screen screenshot + role diagram (Management → sees all, Member → sees own tasks)

**Script:**

> Every team member registers with a name and password. The system uses industry-standard encryption for passwords and JWT tokens for sessions.
>
> Roles matter. Management sees the full dashboard — all tasks, all members, all deadlines. Members see their own tasks and can update their status. This means the whole team uses one tool, but everyone gets a relevant view.

---

## SLIDE 10 — Why Custom vs. Off-the-Shelf

**Visual:** Comparison table:

| | Zoom AI | Miro | MOMentum |
|---|---------|------|----------|
| Transcription | Yes | No | Yes |
| Structured MOM | No | No | Yes |
| Auto task extraction | No | No | Yes |
| Task tracking | No | Partial | Yes |
| Auto-reminders | No | No | Yes |
| Management summary | No | No | Yes |
| Telegram/Email alerts | No | No | Yes |
| Customizable for MT | No | No | Yes |

**Script:**

> You asked me to evaluate Miro and other tools. I did. Here's the comparison.
>
> Zoom AI transcribes meetings, but it doesn't generate structured MOMs, extract tasks, or send reminders. Miro is a workflow tool, but it doesn't do transcription, automated MOM generation, or proactive notifications.
>
> No off-the-shelf tool covers all seven of your requirements. MOMentum does. And because it's custom-built, we can adapt it to exactly how Micro Turners works — add WhatsApp when we need it, change reminder frequency, add new roles, integrate with whatever tools the team uses next.

---

## SLIDE 11 — Tech Stack (Brief)

**Visual:** Clean icon row:
- Python + FastAPI (backend)
- Claude AI (MOM generation)
- Whisper AI (transcription)
- SQLite (database)
- Vanilla JS (frontend, no heavy frameworks)

**Script:**

> A quick note on the tech. The backend is Python with FastAPI — fast, modern, easy to maintain. AI is powered by Claude for MOM generation and OpenAI Whisper for transcription. Database is SQLite — zero configuration, single file, no server needed.
>
> The frontend is plain HTML, CSS, and JavaScript — no heavy framework, no build step, runs anywhere. The whole thing can be deployed on a single server or even a laptop.

---

## SLIDE 12 — What's Next

**Visual:** Roadmap with 3 phases:
- **Now:** Deploy for Micro Turners team, onboard members
- **Next:** WhatsApp integration, Google Calendar sync
- **Future:** Meeting analytics, cross-meeting intelligence, mobile app

**Script:**

> The tool is ready to use today. Here's what I suggest as next steps:
>
> **Immediate** — Deploy MOMentum for the Micro Turners team. Set up email and Telegram notifications. Onboard team members.
>
> **Short-term** — Add WhatsApp integration once we have the Business API. Sync with Google Calendar so meetings are auto-created.
>
> **Long-term** — Meeting analytics: which meetings produce the most action items? Which produce the most waste? Cross-meeting intelligence: "This task was discussed in 3 meetings and still isn't done." And a mobile app for recording meetings on the go.

---

## SLIDE 13 — Closing

**Visual:** MOMentum logo + tagline: *"Stop losing action items. Start building MOMentum."*

**Script:**

> Sir, every requirement you outlined — automated MOMs, task tracking, reminders to assignees, reminders to you, deadline alerts, communication integration, and company-wide access — is built and working.
>
> MOMentum turns every meeting into tracked, visible, accountable work. No more "who was supposed to do that?" — the system knows, and it follows up automatically.
>
> I'd like to demo it live for you now, and then discuss deployment. Thank you.

---

## Presenter Notes

**Before the presentation:**
- Have MOMentum running locally at localhost:8000
- Pre-load a sample meeting with a generated MOM and extracted tasks
- Add 2-3 team members with tasks in different statuses
- Have both dark and light mode ready to toggle

**During Q&A, be ready for:**
- "What does it cost?" → Claude API ~$0.01-0.03 per MOM, Whisper ~$0.006/min audio. Email is free (Gmail SMTP). Telegram is free. Hosting: a basic server is ~$5-10/month.
- "Can it work on phone?" → The web UI is responsive, works on mobile browsers today. A native app is on the roadmap.
- "What about WhatsApp?" → Requires WhatsApp Business API approval. Can integrate via Twilio once approved. Architecture supports it — just another notification channel.
- "How secure is it?" → Passwords are bcrypt-hashed, sessions use JWT tokens, data stays on our server (not third-party). Can add HTTPS with a simple certificate.
- "Can others add meetings too?" → Yes. Any logged-in user can create meetings, upload audio, and generate MOMs. Tasks are visible to everyone; management sees the full picture.
