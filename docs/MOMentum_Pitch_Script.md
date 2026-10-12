# MOMentum — Pitch Script for Karan Sir
### Presenter: Swagata Banerjee | Duration: ~8 minutes
### Live Demo: https://momentum.loca.lt

---

## OPENING (30 sec)

Good afternoon, Sir.

In our meeting on 5th November, you outlined a clear requirement — a tool that goes beyond just meeting minutes. You wanted automated MOMs, task tracking, reminders to assignees and management, deadline alerts, and something the whole Micro Turners team can use.

I've built exactly that. It's called MOMentum.

---

## THE PROBLEM (45 sec)

Right now, every meeting at Micro Turners ends with decisions and action items. But where do those action items go? Into someone's notes. Or someone's WhatsApp chat. Or someone's memory.

A week later, the same items come up in the next meeting. "Who was supposed to do that?" Nobody remembers. Deadlines pass silently. There's no system to capture what comes out of a meeting and track it to completion.

MOMentum is that system.

---

## HOW IT WORKS (1 min)

The process is simple — four steps, each one click:

**Step 1** — After a meeting, upload the audio recording, or paste the transcript directly.

**Step 2** — The system uses AI to transcribe the audio into text.

**Step 3** — AI generates a formal Minutes of Meeting — with agenda, discussion summary, action items, and key decisions. Professional, consistent, every time.

**Step 4** — From that MOM, the system automatically extracts every action item — who it's assigned to, the deadline, and the priority. Tasks are created instantly.

One meeting goes in. Structured, trackable tasks come out. No manual work.

---

## YOUR 7 REQUIREMENTS — ALL DONE (1.5 min)

Sir, let me map this directly to the seven requirements you gave me:

**One — Automated MOM generation.** Done. Audio goes in, structured MOM comes out in seconds.

**Two — Task assignment tracking.** Done. Every task is tagged with an assignee, deadline, and priority. Each person can filter to see only their tasks.

**Three — Auto-reminders to assignees.** Done. Three days before a deadline, the assignee gets a reminder — "Your task is due on this date."

**Four — Auto-reminders to management.** Done. You receive a summary showing every team member's task status — how many pending, in progress, completed, and overdue. You don't have to open the tool. It comes to you.

**Five — Timeline and deadline alerts.** Done. The dashboard shows upcoming deadlines in real time. Overdue tasks are flagged automatically.

**Six — Communication channel integration.** Done. Reminders go out via email and Telegram. Each member chooses their preferred channel. WhatsApp can be added when we have the Business API.

**Seven — Usable by everyone.** Done. Every team member gets their own login. Members see their tasks. Management sees everything.

All seven. Done.

---

## LIVE DEMO (2 min)

*[Open https://momentum.loca.lt]*

Let me show you.

**Dashboard** — This is the first thing you see. Total meetings, total tasks, pending, completed, overdue — all at a glance. The progress ring shows overall completion. Below that, upcoming deadlines for the week, and team workload — each member's task breakdown. This is the management view you asked for.

**Meetings** — Here you can see all meetings. Click one — you see the full pipeline. Upload audio, transcribe, generate MOM, extract tasks. One click each. The generated MOM follows a standard format every time.

**Tasks** — Two views. A list with search and filters — by status, by member. Or a Kanban board — Pending, In Progress, Completed, Overdue. Status updates are inline, one click. When someone completes a task, they get a small celebration. Makes people want to close their tasks.

**Team** — All members, their roles, contact info, notification preferences.

**Notifications** — In settings, each member chooses how they want reminders — email, Telegram, or both. There's a test button to verify it works. And a manual "Send Reminders" button if you ever want an instant update.

---

## WHY CUSTOM, NOT MIRO OR ZOOM (1 min)

You asked me to evaluate Miro and other tools. I did.

Zoom AI transcribes meetings, but doesn't generate structured MOMs, doesn't extract tasks, doesn't send reminders.

Miro is a workflow tool, but doesn't do transcription, doesn't generate MOMs, doesn't send notifications.

No off-the-shelf tool covers all seven of your requirements. MOMentum does. And because it's custom-built for Micro Turners, we can adapt it — change reminder frequency, add new roles, integrate with whatever tools the team uses next.

---

## WHAT IT COSTS (30 sec)

The AI costs are minimal:
- Generating one MOM costs about 1–2 rupees
- Transcribing one hour of audio costs about 50 paise per minute
- Email reminders are free
- Telegram reminders are free
- Hosting — a basic server is 400–800 rupees per month

For a team of 5–15 people, we're looking at under 1000 rupees per month total.

---

## WHAT'S NEXT (30 sec)

The tool is ready today. Here's what I suggest:

**This week** — Deploy MOMentum on a proper server. Set up email and Telegram for the team. Onboard everyone.

**Next month** — WhatsApp integration once we have the Business API. Google Calendar sync so meetings auto-create.

**Long term** — Meeting analytics — which meetings produce results, which are wasted time. And a mobile app for recording on the go.

---

## CLOSING (30 sec)

Sir, every requirement you outlined is built and working. MOMentum turns every meeting into tracked, visible, accountable work.

No more "who was supposed to do that?" — the system knows, and it follows up automatically.

I'd love to hear your thoughts, and if you're happy with what you see, we can start onboarding the team this week.

Thank you.

---

## Q&A CHEAT SHEET

| Question | Answer |
|----------|--------|
| Can it work on phone? | Yes — the web UI is responsive, works on mobile browsers today |
| What about WhatsApp? | Architecture supports it. Needs WhatsApp Business API approval. Can add via Twilio |
| Is it secure? | Passwords are encrypted (bcrypt), sessions use JWT tokens, data stays on our server |
| Can others create meetings? | Yes — any logged-in user can create meetings, upload audio, generate MOMs |
| What if the AI makes a mistake? | The MOM is editable. Tasks can be manually adjusted. AI does 90% of the work, humans verify |
| Can we track across multiple meetings? | Yes — all tasks are in one dashboard regardless of which meeting they came from |
| How long to transcribe a meeting? | About 30 seconds for a 1-hour recording |
| Can we use it without AI keys? | Yes — meetings, tasks, team, dashboard all work without AI. Only transcription and MOM generation need API keys |
