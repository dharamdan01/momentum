const API_BASE = "";
const activityLog = [];

// ===== SPLASH SCREEN =====

window.addEventListener("load", () => {
  setTimeout(() => {
    const splash = document.getElementById("splash");
    splash.style.opacity = "0";
    setTimeout(() => (splash.style.display = "none"), 500);
  }, 1200);
});

// ===== TOAST NOTIFICATIONS =====

function toast(message, type = "info", duration = 3500) {
  const container = document.getElementById("toast-container");
  const icons = { success: "&#10003;", error: "&#10007;", info: "&#8505;" };
  const element = document.createElement("div");
  element.className = `toast toast-${type}`;
  element.innerHTML = `
    <div class="toast-icon">${icons[type] || icons.info}</div>
    <span>${message}</span>
  `;
  container.appendChild(element);
  setTimeout(() => {
    element.classList.add("removing");
    setTimeout(() => element.remove(), 300);
  }, duration);
}

// ===== CONFETTI =====

function fireConfetti() {
  const canvas = document.getElementById("confetti-canvas");
  const ctx = canvas.getContext("2d");
  canvas.width = innerWidth;
  canvas.height = innerHeight;

  const colors = [
    "#6366f1", "#a855f7", "#10b981", "#f59e0b",
    "#ef4444", "#3b82f6", "#ec4899", "#14b8a6",
  ];

  const particles = [];
  for (let i = 0; i < 100; i++) {
    particles.push({
      x: canvas.width / 2 + Math.random() * 300 - 150,
      y: canvas.height * 0.35,
      velocityX: (Math.random() - 0.5) * 14,
      velocityY: Math.random() * -16 - 5,
      width: Math.random() * 8 + 4,
      height: Math.random() * 6 + 3,
      color: colors[Math.floor(Math.random() * colors.length)],
      rotation: Math.random() * 360,
      rotationSpeed: (Math.random() - 0.5) * 14,
      gravity: 0.28,
      opacity: 1,
    });
  }

  let frame = 0;

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    let alive = false;

    particles.forEach((particle) => {
      particle.velocityY += particle.gravity;
      particle.x += particle.velocityX;
      particle.y += particle.velocityY;
      particle.rotation += particle.rotationSpeed;
      particle.velocityX *= 0.99;

      if (frame > 50) particle.opacity -= 0.012;
      if (particle.opacity <= 0) return;

      alive = true;
      ctx.save();
      ctx.translate(particle.x, particle.y);
      ctx.rotate((particle.rotation * Math.PI) / 180);
      ctx.globalAlpha = Math.max(0, particle.opacity);
      ctx.fillStyle = particle.color;
      ctx.fillRect(
        -particle.width / 2,
        -particle.height / 2,
        particle.width,
        particle.height
      );
      ctx.restore();
    });

    frame++;
    if (alive && frame < 220) {
      requestAnimationFrame(animate);
    } else {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }

  animate();
}

// ===== ACTIVITY LOG =====

function logActivity(action, detail) {
  activityLog.unshift({ action, detail, time: new Date() });
  if (activityLog.length > 20) activityLog.pop();
  renderActivity();
}

function renderActivity() {
  const feed = document.getElementById("activity-feed");
  if (!feed) return;

  if (activityLog.length === 0) {
    feed.innerHTML = `
      <div style="color:var(--text-tertiary);font-size:13px;padding:20px;text-align:center;">
        No recent activity
      </div>
    `;
    return;
  }

  feed.innerHTML = activityLog
    .slice(0, 8)
    .map((entry, index) => {
      const ago = timeAgo(entry.time);
      return `
        <div class="activity-item fade-in-up" style="animation-delay:${0.04 * index}s">
          <div class="activity-dot"></div>
          <div class="activity-content">
            <div class="activity-text"><strong>${entry.action}</strong> ${entry.detail}</div>
            <div class="activity-time">${ago}</div>
          </div>
        </div>
      `;
    })
    .join("");
}

function timeAgo(date) {
  const seconds = Math.floor((new Date() - date) / 1000);
  if (seconds < 60) return "just now";
  if (seconds < 3600) return Math.floor(seconds / 60) + "m ago";
  if (seconds < 86400) return Math.floor(seconds / 3600) + "h ago";
  return Math.floor(seconds / 86400) + "d ago";
}

// ===== THEME =====

function initTheme() {
  const saved = localStorage.getItem("mt-theme");
  if (saved) {
    document.documentElement.setAttribute("data-theme", saved);
  } else {
    const prefersDark = matchMedia("(prefers-color-scheme:dark)").matches;
    document.documentElement.setAttribute("data-theme", prefersDark ? "dark" : "light");
  }
}

function toggleTheme() {
  const root = document.documentElement;
  const current = root.getAttribute("data-theme");
  const next = current === "dark" ? "light" : "dark";

  root.setAttribute("data-theme", next);
  localStorage.setItem("mt-theme", next);

  const button = document.getElementById("theme-toggle");
  button.style.transform = "scale(0.8) rotate(-180deg)";
  setTimeout(() => (button.style.transform = ""), 300);

  toast(`${next === "dark" ? "Dark" : "Light"} mode`, "info", 1500);
}

initTheme();
document.getElementById("theme-toggle").addEventListener("click", toggleTheme);

// ===== GREETING =====

(function setGreeting() {
  const hour = new Date().getHours();
  let greeting = "Good evening";
  if (hour < 12) greeting = "Good morning";
  else if (hour < 17) greeting = "Good afternoon";

  document.getElementById("greeting-heading").textContent = greeting;

  const dateStr = new Date().toLocaleDateString("en-IN", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  });
  document.getElementById("greeting-text").textContent = dateStr;
})();

// ===== AVATAR =====

const AVATAR_COLORS = [
  "#6366f1", "#a855f7", "#ec4899", "#f43f5e", "#f59e0b",
  "#10b981", "#3b82f6", "#8b5cf6", "#14b8a6", "#f97316",
];

function avatar(name, sizeClass = "") {
  const initials = name
    .split(" ")
    .map((word) => word[0])
    .join("")
    .slice(0, 2);

  let hash = 0;
  for (let i = 0; i < name.length; i++) {
    hash = name.charCodeAt(i) + ((hash << 5) - hash);
  }

  const color = AVATAR_COLORS[Math.abs(hash) % AVATAR_COLORS.length];
  return `<div class="avatar ${sizeClass}" style="background:${color}">${initials}</div>`;
}

// ===== NAVIGATION =====

let currentPage = "dashboard";

function navigateTo(page) {
  if (page === currentPage) return;

  document.querySelectorAll("nav button").forEach((btn) => btn.classList.remove("active"));
  document.querySelector(`nav button[data-page="${page}"]`)?.classList.add("active");

  const oldPage = document.getElementById(`page-${currentPage}`);
  const newPage = document.getElementById(`page-${page}`);

  oldPage.style.opacity = "0";
  oldPage.style.transform = "translateY(8px)";

  setTimeout(() => {
    oldPage.classList.remove("active");
    oldPage.style.opacity = "";
    oldPage.style.transform = "";
    newPage.classList.add("active");
    currentPage = page;

    if (page === "dashboard") loadDashboard();
    else if (page === "meetings") loadMeetings();
    else if (page === "tasks") loadTasks();
    else if (page === "team") loadTeam();
  }, 180);
}

document.querySelectorAll("nav button").forEach((btn) => {
  btn.addEventListener("click", () => navigateTo(btn.dataset.page));
});

// ===== COMMAND PALETTE =====

const COMMANDS = [
  { name: "Go to Dashboard", icon: "&#9638;", action: () => navigateTo("dashboard") },
  { name: "Go to Meetings", icon: "&#128197;", action: () => navigateTo("meetings") },
  { name: "Go to Tasks", icon: "&#9745;", action: () => navigateTo("tasks") },
  { name: "Go to Team", icon: "&#128101;", action: () => navigateTo("team") },
  { name: "New Meeting", icon: "&#10010;", action: () => openModal("meeting-modal") },
  { name: "New Task", icon: "&#10010;", action: () => openModal("task-modal") },
  { name: "Add Team Member", icon: "&#10010;", action: () => openModal("member-modal") },
  { name: "Toggle Theme", icon: "&#127763;", action: () => toggleTheme() },
  { name: "Keyboard Shortcuts", icon: "&#9000;", action: () => openModal("shortcuts-modal") },
];

let commandIndex = 0;

function openCmdPalette() {
  const overlay = document.getElementById("cmd-overlay");
  overlay.classList.add("active");

  const input = document.getElementById("cmd-input");
  input.value = "";
  input.focus();

  commandIndex = 0;
  renderCmdResults("");
}

function closeCmdPalette() {
  document.getElementById("cmd-overlay").classList.remove("active");
}

function renderCmdResults(query) {
  const filtered = query
    ? COMMANDS.filter((cmd) => cmd.name.toLowerCase().includes(query.toLowerCase()))
    : COMMANDS;

  commandIndex = Math.min(commandIndex, Math.max(filtered.length - 1, 0));

  const resultsContainer = document.getElementById("cmd-results");
  if (filtered.length === 0) {
    resultsContainer.innerHTML =
      '<div style="padding:20px;text-align:center;color:var(--text-tertiary);">No results</div>';
    return;
  }

  resultsContainer.innerHTML = filtered
    .map((cmd, index) => {
      const globalIndex = COMMANDS.indexOf(cmd);
      const isActive = index === commandIndex ? "active" : "";
      return `
        <div class="cmd-result-item ${isActive}"
             onmouseenter="commandIndex=${index};renderCmdResults(document.getElementById('cmd-input').value)"
             onclick="executeCommand(${globalIndex})">
          <span class="cmd-result-icon">${cmd.icon}</span>${cmd.name}
        </div>
      `;
    })
    .join("");
}

function executeCommand(index) {
  closeCmdPalette();
  COMMANDS[index].action();
}

document.getElementById("cmd-input").addEventListener("input", (event) => {
  commandIndex = 0;
  renderCmdResults(event.target.value);
});

document.getElementById("cmd-input").addEventListener("keydown", (event) => {
  const query = event.target.value;
  const filtered = query
    ? COMMANDS.filter((cmd) => cmd.name.toLowerCase().includes(query.toLowerCase()))
    : COMMANDS;

  if (event.key === "ArrowDown") {
    event.preventDefault();
    commandIndex = Math.min(commandIndex + 1, filtered.length - 1);
    renderCmdResults(query);
  } else if (event.key === "ArrowUp") {
    event.preventDefault();
    commandIndex = Math.max(commandIndex - 1, 0);
    renderCmdResults(query);
  } else if (event.key === "Enter" && filtered[commandIndex]) {
    executeCommand(COMMANDS.indexOf(filtered[commandIndex]));
  } else if (event.key === "Escape") {
    closeCmdPalette();
  }
});

document.getElementById("cmd-overlay").addEventListener("click", (event) => {
  if (event.target.id === "cmd-overlay") closeCmdPalette();
});

// ===== USER PROFILE DROPDOWN =====

document.getElementById("user-profile").addEventListener("click", (event) => {
  event.stopPropagation();
  document.getElementById("user-dropdown").classList.toggle("active");
});

document.addEventListener("click", () => {
  document.getElementById("user-dropdown").classList.remove("active");
});

// ===== KEYBOARD SHORTCUTS =====

document.addEventListener("keydown", (event) => {
  const tag = event.target.tagName;
  if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") {
    if (event.key === "Escape") event.target.blur();
    return;
  }

  if (document.querySelector(".cmd-overlay.active")) return;

  if (document.querySelector(".modal-overlay.active")) {
    if (event.key === "Escape") {
      document.querySelectorAll(".modal-overlay.active").forEach((modal) => closeModal(modal.id));
    }
    return;
  }

  if ((event.ctrlKey || event.metaKey) && event.key === "k") {
    event.preventDefault();
    openCmdPalette();
    return;
  }

  switch (event.key) {
    case "1": navigateTo("dashboard"); break;
    case "2": navigateTo("meetings"); break;
    case "3": navigateTo("tasks"); break;
    case "4": navigateTo("team"); break;
    case "t":
    case "T": toggleTheme(); break;
    case "m":
    case "M": openModal("meeting-modal"); break;
    case "n":
    case "N": openModal("task-modal"); break;
    case "?": openModal("shortcuts-modal"); break;
  }
});

// ===== MODALS =====

function openModal(id) {
  document.getElementById(id).classList.add("active");
  document.body.style.overflow = "hidden";
  if (id === "task-modal") populateMemberDropdowns();
}

function closeModal(id) {
  const overlay = document.getElementById(id);
  const modal = overlay.querySelector(".modal");

  modal.style.transform = "scale(0.95) translateY(10px)";
  modal.style.opacity = "0";
  overlay.style.opacity = "0";

  setTimeout(() => {
    overlay.classList.remove("active");
    overlay.style.opacity = "";
    modal.style.transform = "";
    modal.style.opacity = "";
    document.body.style.overflow = "";
  }, 200);
}

document.querySelectorAll(".modal-overlay").forEach((overlay) => {
  overlay.addEventListener("click", (event) => {
    if (event.target === overlay) closeModal(overlay.id);
  });
});

// ===== HELPERS =====

function formatDate(dateStr) {
  if (!dateStr) return "—";
  return new Date(dateStr).toLocaleDateString("en-IN", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

function formatDateTime(dateStr) {
  if (!dateStr) return "—";
  return new Date(dateStr).toLocaleDateString("en-IN", {
    day: "numeric",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function badge(text, variant) {
  const cls = variant || text;
  return `<span class="badge badge-${cls}">${text.replace(/_/g, " ")}</span>`;
}

function daysUntil(dateStr) {
  if (!dateStr) return null;
  return Math.ceil((new Date(dateStr) - new Date()) / 864e5);
}

function deadlineLabel(dateStr) {
  const days = daysUntil(dateStr);
  if (days === null) return "—";

  const formatted = formatDate(dateStr);
  if (days < 0) {
    return `${formatted} <span style="color:var(--danger-text);font-weight:700;">${Math.abs(days)}d overdue</span>`;
  }
  if (days === 0) {
    return `${formatted} <span style="color:var(--danger-text);font-weight:700;">Today!</span>`;
  }
  if (days <= 3) {
    return `${formatted} <span style="color:var(--warning-text);font-weight:700;">${days}d left</span>`;
  }
  return `${formatted} <span style="color:var(--text-tertiary);">${days}d</span>`;
}

async function api(path, options = {}) {
  const response = await fetch(API_BASE + path, {
    headers: { "Content-Type": "application/json", ...options.headers },
    ...options,
  });
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || "Request failed");
  }
  return response.json();
}

function animateValue(element, start, end, duration) {
  if (end === start) {
    element.textContent = end;
    return;
  }
  const startTime = performance.now();

  function tick(now) {
    const progress = Math.min((now - startTime) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    element.textContent = Math.round(start + (end - start) * eased);
    if (progress < 1) requestAnimationFrame(tick);
  }

  requestAnimationFrame(tick);
}

function showSkeleton(container, count, className) {
  container.innerHTML = Array.from(
    { length: count },
    () => `<div class="skeleton ${className}"></div>`
  ).join("");
}

function setLoading(buttonId, isLoading) {
  const button = document.getElementById(buttonId);
  if (!button) return;

  if (isLoading) {
    button.classList.add("loading");
    button.dataset.orig = button.innerHTML;
    button.innerHTML = '<span class="spinner"></span> Working...';
  } else {
    button.classList.remove("loading");
    if (button.dataset.orig) button.innerHTML = button.dataset.orig;
  }
}

// ===== PROGRESS RING =====

function ringSVG(percent) {
  const radius = 54;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (percent / 100) * circumference;

  return `
    <svg width="140" height="140" viewBox="0 0 120 120">
      <circle cx="60" cy="60" r="${radius}" fill="none"
              stroke="var(--bg-inset)" stroke-width="10" />
      <circle cx="60" cy="60" r="${radius}" fill="none"
              stroke="url(#pgrad)" stroke-width="10" stroke-linecap="round"
              stroke-dasharray="${circumference}" stroke-dashoffset="${offset}"
              transform="rotate(-90 60 60)"
              style="transition:stroke-dashoffset 1.2s cubic-bezier(0.4,0,0.2,1)" />
      <defs>
        <linearGradient id="pgrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:var(--accent)" />
          <stop offset="100%" style="stop-color:#a855f7" />
        </linearGradient>
      </defs>
    </svg>
  `;
}

// ===== TASK VIEW (LIST / KANBAN) =====

let currentView = "list";

function setTaskView(view) {
  currentView = view;

  document.getElementById("view-list").classList.toggle("active", view === "list");
  document.getElementById("view-board").classList.toggle("active", view === "board");
  document.getElementById("tasks-list-view").style.display = view === "list" ? "" : "none";
  document.getElementById("tasks-board-view").style.display = view === "board" ? "" : "none";

  loadTasks();
}

function renderKanban(tasks) {
  const groups = { pending: [], in_progress: [], completed: [], overdue: [] };

  tasks.forEach((task) => {
    if (groups[task.status]) {
      groups[task.status].push(task);
    } else {
      groups.pending.push(task);
    }
  });

  ["pending", "in_progress", "completed", "overdue"].forEach((status) => {
    const column = document.getElementById(`kanban-${status}`);
    const countBadge = document.getElementById(`kanban-${status}-count`);
    countBadge.textContent = groups[status].length;

    if (groups[status].length === 0) {
      column.innerHTML =
        '<div style="padding:24px;text-align:center;color:var(--text-tertiary);font-size:12px;">No tasks</div>';
      return;
    }

    column.innerHTML = groups[status]
      .map((task, index) => {
        const assigneeHtml = task.assignee
          ? avatar(task.assignee.name, "avatar-sm") + `<span>${task.assignee.name}</span>`
          : '<span style="color:var(--text-tertiary)">Unassigned</span>';

        const deadlineHtml = task.deadline
          ? `<div style="font-size:11px;color:var(--text-tertiary);">${formatDate(task.deadline)}</div>`
          : "";

        return `
          <div class="kanban-card fade-in-up" style="animation-delay:${0.04 * index}s">
            <div class="kanban-card-priority">${badge(task.priority)}</div>
            <div class="kanban-card-title">${task.title}</div>
            <div class="kanban-card-meta">
              <div style="display:flex;align-items:center;gap:6px;">${assigneeHtml}</div>
              ${deadlineHtml}
            </div>
            <div class="kanban-card-actions">
              <select class="status-select" onchange="updateTaskStatus(${task.id},this.value)" style="flex:1;">
                <option value="pending" ${task.status === "pending" ? "selected" : ""}>Pending</option>
                <option value="in_progress" ${task.status === "in_progress" ? "selected" : ""}>In Progress</option>
                <option value="completed" ${task.status === "completed" ? "selected" : ""}>Completed</option>
              </select>
              <button class="btn btn-danger btn-sm" onclick="deleteTask(${task.id})">&#128465;</button>
            </div>
          </div>
        `;
      })
      .join("");
  });
}

// ===== NOTIFICATIONS =====

function updateNotifDot(alerts) {
  const dot = document.getElementById("notif-dot");
  const hasAlerts = alerts.overdue.length > 0 || alerts.upcoming_deadlines.length > 0;
  dot.style.display = hasAlerts ? "" : "none";
}

// ===== DASHBOARD =====

async function loadDashboard() {
  const statsGrid = document.getElementById("stats-grid");
  showSkeleton(statsGrid, 5, "skeleton-stat");

  try {
    const [stats, alerts, summary] = await Promise.all([
      api("/api/dashboard/stats"),
      api("/api/dashboard/alerts"),
      api("/api/dashboard/member-summary"),
    ]);

    const totalTasks = stats.total_tasks || 1;
    const completionPct = Math.round((stats.completed_tasks / totalTasks) * 100);
    updateNotifDot(alerts);

    // Stat cards
    statsGrid.innerHTML = `
      <div class="stat-card accent">
        <div class="stat-icon">&#128197;</div>
        <div class="label">Meetings</div>
        <div class="value" data-count="${stats.total_meetings}">0</div>
      </div>
      <div class="stat-card neutral">
        <div class="stat-icon">&#128203;</div>
        <div class="label">Total Tasks</div>
        <div class="value" data-count="${stats.total_tasks}">0</div>
      </div>
      <div class="stat-card warning">
        <div class="stat-icon">&#9203;</div>
        <div class="label">Pending</div>
        <div class="value" data-count="${stats.pending_tasks + stats.in_progress_tasks}">0</div>
      </div>
      <div class="stat-card success">
        <div class="stat-icon">&#10003;</div>
        <div class="label">Completed</div>
        <div class="value" data-count="${stats.completed_tasks}">0</div>
      </div>
      <div class="stat-card danger">
        <div class="stat-icon">&#9888;</div>
        <div class="label">Overdue</div>
        <div class="value" data-count="${stats.overdue_tasks}">0</div>
      </div>
    `;
    statsGrid.classList.add("stagger-fast");

    setTimeout(() => {
      statsGrid.querySelectorAll(".value[data-count]").forEach((el) => {
        animateValue(el, 0, parseInt(el.dataset.count), 900);
      });
    }, 300);

    // Progress overview
    document.getElementById("progress-overview").innerHTML = `
      <div class="progress-ring-wrapper">
        ${ringSVG(completionPct)}
        <div class="progress-ring-label">
          <span class="pct">${completionPct}%</span>
          <span class="pct-sub">Complete</span>
        </div>
      </div>
      <div class="progress-bars">
        <div class="progress-bar-item">
          <span class="bar-label">Pending</span>
          <div class="bar-track">
            <div class="bar-fill fill-accent" style="--fill:${(stats.pending_tasks / totalTasks) * 100}%;width:var(--fill);"></div>
          </div>
          <span class="bar-count">${stats.pending_tasks}</span>
        </div>
        <div class="progress-bar-item">
          <span class="bar-label">In Progress</span>
          <div class="bar-track">
            <div class="bar-fill fill-warning" style="--fill:${(stats.in_progress_tasks / totalTasks) * 100}%;width:var(--fill);"></div>
          </div>
          <span class="bar-count">${stats.in_progress_tasks}</span>
        </div>
        <div class="progress-bar-item">
          <span class="bar-label">Completed</span>
          <div class="bar-track">
            <div class="bar-fill fill-success" style="--fill:${(stats.completed_tasks / totalTasks) * 100}%;width:var(--fill);"></div>
          </div>
          <span class="bar-count">${stats.completed_tasks}</span>
        </div>
        <div class="progress-bar-item">
          <span class="bar-label">Overdue</span>
          <div class="bar-track">
            <div class="bar-fill fill-danger" style="--fill:${(stats.overdue_tasks / totalTasks) * 100}%;width:var(--fill);"></div>
          </div>
          <span class="bar-count">${stats.overdue_tasks}</span>
        </div>
      </div>
    `;

    // Alert banners
    let alertsHtml = "";
    if (alerts.overdue.length > 0) {
      alertsHtml += `
        <div class="alert-banner alert-danger">
          <div class="alert-icon">&#9888;</div>
          <span><strong>${alerts.overdue.length} task(s)</strong> past deadline and need attention.</span>
        </div>
      `;
    }
    if (alerts.upcoming_deadlines.length > 0) {
      alertsHtml += `
        <div class="alert-banner alert-warning" style="animation-delay:0.1s">
          <div class="alert-icon">&#9200;</div>
          <span><strong>${alerts.upcoming_deadlines.length} deadline(s)</strong> approaching in 3 days.</span>
        </div>
      `;
    }
    document.getElementById("alerts-container").innerHTML = alertsHtml;

    // Upcoming deadlines table
    const deadlinesBody = document.getElementById("upcoming-deadlines");
    const noDeadlines = document.getElementById("no-deadlines");
    document.getElementById("deadline-count").textContent = stats.upcoming_deadlines.length;

    if (stats.upcoming_deadlines.length === 0) {
      deadlinesBody.innerHTML = "";
      noDeadlines.style.display = "block";
    } else {
      noDeadlines.style.display = "none";
      deadlinesBody.innerHTML = stats.upcoming_deadlines
        .map((task, index) => {
          const assigneeHtml = task.assignee
            ? avatar(task.assignee.name, "avatar-sm") + task.assignee.name
            : '<span style="color:var(--text-tertiary)">Unassigned</span>';

          return `
            <tr class="fade-in-up" style="animation-delay:${0.05 * index}s">
              <td><strong>${task.title}</strong></td>
              <td>
                <div style="display:flex;align-items:center;gap:8px;">${assigneeHtml}</div>
              </td>
              <td>${deadlineLabel(task.deadline)}</td>
              <td>${badge(task.priority)}</td>
              <td>${badge(task.status)}</td>
            </tr>
          `;
        })
        .join("");
    }

    renderActivity();

    // Team workload
    const memberContainer = document.getElementById("member-summary");
    if (summary.length === 0) {
      memberContainer.innerHTML =
        '<div class="empty-state" style="padding:30px;"><h3>No team members</h3></div>';
    } else {
      memberContainer.innerHTML = summary
        .map(
          (member) => `
          <div class="member-card">
            <div class="member-card-top">
              ${avatar(member.name)}
              <div>
                <h3>${member.name}</h3>
                <div class="role">${member.total} tasks</div>
              </div>
            </div>
            <div class="task-counts">
              <span class="count-item">${badge("pending")} ${member.pending}</span>
              <span class="count-item">${badge("in_progress")} ${member.in_progress}</span>
              <span class="count-item">${badge("completed")} ${member.completed}</span>
              ${member.overdue > 0 ? `<span class="count-item">${badge("overdue")} ${member.overdue}</span>` : ""}
            </div>
          </div>
        `
        )
        .join("");
      memberContainer.classList.add("stagger");
    }
  } catch (error) {
    console.error(error);
  }
}

// ===== MEETINGS =====

async function loadMeetings() {
  const container = document.getElementById("meetings-list");
  const emptyState = document.getElementById("no-meetings");
  showSkeleton(container, 3, "skeleton-row");

  try {
    const meetings = await api("/api/meetings/");
    if (meetings.length === 0) {
      container.innerHTML = "";
      emptyState.style.display = "block";
      return;
    }

    emptyState.style.display = "none";
    container.innerHTML = meetings
      .map((meeting, index) => {
        let statusBadge;
        if (meeting.mom_text) {
          statusBadge = '<span class="badge badge-completed">MOM Ready</span>';
        } else if (meeting.transcript) {
          statusBadge = '<span class="badge badge-in_progress">Transcribed</span>';
        } else {
          statusBadge = '<span class="badge badge-pending">New</span>';
        }

        const taskCount = meeting.tasks.length;
        const taskLabel = `${taskCount} task${taskCount !== 1 ? "s" : ""}`;

        return `
          <div class="meeting-item fade-in-up" style="animation-delay:${0.06 * index}s"
               onclick="openMeetingDetail(${meeting.id})">
            <div class="meeting-item-inner">
              <div class="meeting-info">
                <strong>${meeting.title}</strong>
                <div class="meeting-meta">
                  <span>&#128197; ${formatDateTime(meeting.date)}</span>
                  <span>&#128101; ${meeting.participants || "—"}</span>
                </div>
              </div>
              <div class="meeting-badges">
                ${statusBadge}
                <span class="task-count">${taskLabel}</span>
              </div>
            </div>
          </div>
        `;
      })
      .join("");
  } catch (error) {
    console.error(error);
  }
}

async function createMeeting() {
  const title = document.getElementById("meeting-title").value.trim();
  const date = document.getElementById("meeting-date").value;
  const participants = document.getElementById("meeting-participants").value.trim();

  if (!title || !date) return toast("Title and date are required", "error");

  setLoading("btn-create-meeting", true);

  try {
    await api("/api/meetings/", {
      method: "POST",
      body: JSON.stringify({ title, date, participants }),
    });

    closeModal("meeting-modal");
    document.getElementById("meeting-title").value = "";
    document.getElementById("meeting-date").value = "";
    document.getElementById("meeting-participants").value = "";

    toast("Meeting created", "success");
    logActivity("Created meeting", title);
    loadMeetings();
  } catch (error) {
    toast(error.message, "error");
  }

  setLoading("btn-create-meeting", false);
}

async function openMeetingDetail(meetingId) {
  try {
    const meeting = await api(`/api/meetings/${meetingId}`);
    document.getElementById("detail-meeting-title").textContent = meeting.title;

    const hasAudio = meeting.audio_file || meeting.transcript;
    const hasTranscript = !!meeting.transcript;
    const hasMom = !!meeting.mom_text;
    const hasTasks = meeting.tasks.length > 0;

    let html = `
      <div class="fade-in" style="color:var(--text-secondary);margin-bottom:24px;display:flex;gap:16px;font-size:13px;">
        <span>&#128197; ${formatDateTime(meeting.date)}</span>
        <span>&#128101; ${meeting.participants || "—"}</span>
      </div>

      <div class="pipeline stagger-fast">
        <div class="pipeline-step ${hasAudio ? "done" : "active"}">
          <div class="step-num">1</div>
          <div class="step-label">Audio/Transcript</div>
        </div>
        <div class="pipeline-step ${hasTranscript ? "done" : meeting.audio_file ? "active" : ""}">
          <div class="step-num">2</div>
          <div class="step-label">Transcribe</div>
        </div>
        <div class="pipeline-step ${hasMom ? "done" : hasTranscript ? "active" : ""}">
          <div class="step-num">3</div>
          <div class="step-label">Generate MOM</div>
        </div>
        <div class="pipeline-step ${hasTasks ? "done" : hasMom ? "active" : ""}">
          <div class="step-num">4</div>
          <div class="step-label">Extract Tasks</div>
        </div>
      </div>

      <div class="form-group fade-in" style="animation-delay:0.15s">
        <label>Upload Recording</label>
        <input type="file" accept="audio/*,video/*" id="audio-upload-${meetingId}"
               style="padding:10px;background:var(--bg-inset);border:1.5px solid var(--border);border-radius:8px;width:100%;color:var(--text-primary);cursor:pointer;"
               onchange="uploadAudio(${meetingId},this)">
      </div>

      <div class="form-group fade-in" style="animation-delay:0.2s">
        <label>Or Paste Transcript</label>
        <textarea id="paste-transcript-${meetingId}" placeholder="Paste transcript here...">${meeting.transcript || ""}</textarea>
        <button class="btn btn-ghost btn-sm" style="margin-top:8px;" onclick="saveTranscript(${meetingId})">
          Save Transcript
        </button>
      </div>

      <div class="fade-in" style="display:flex;gap:10px;margin:24px 0;animation-delay:0.25s;">
    `;

    if (meeting.audio_file && !hasTranscript) {
      html += `<button class="btn btn-primary" onclick="transcribeMeeting(${meetingId})">&#127908; Transcribe</button>`;
    }
    if (hasTranscript) {
      html += `<button class="btn btn-primary" onclick="generateMOM(${meetingId})">&#128196; Generate MOM</button>`;
    }
    if (hasMom) {
      html += `<button class="btn btn-success" onclick="extractTasks(${meetingId})">&#9745; Extract Tasks</button>`;
    }

    html += "</div>";

    if (hasMom) {
      html += `
        <div class="section-title fade-in" style="animation-delay:0.3s">&#128196; Minutes of Meeting</div>
        <div class="mom-content fade-in" style="animation-delay:0.35s">${meeting.mom_text}</div>
      `;
    }

    if (hasTasks) {
      html += `
        <div class="section-title fade-in" style="animation-delay:0.35s">
          &#9745; Action Items (${meeting.tasks.length})
        </div>
        <div class="table-wrapper fade-in" style="animation-delay:0.4s">
          <table>
            <thead>
              <tr><th>Task</th><th>Assignee</th><th>Deadline</th><th>Priority</th><th>Status</th></tr>
            </thead>
            <tbody>
              ${meeting.tasks
                .map(
                  (task, index) => `
                  <tr class="fade-in-up" style="animation-delay:${0.4 + 0.04 * index}s">
                    <td><strong>${task.title}</strong></td>
                    <td>${task.assignee ? task.assignee.name : "—"}</td>
                    <td>${formatDate(task.deadline)}</td>
                    <td>${badge(task.priority)}</td>
                    <td>${badge(task.status)}</td>
                  </tr>
                `
                )
                .join("")}
            </tbody>
          </table>
        </div>
      `;
    }

    document.getElementById("meeting-detail-body").innerHTML = html;
    openModal("meeting-detail-modal");
  } catch (error) {
    toast(error.message, "error");
  }
}

async function uploadAudio(meetingId, input) {
  const file = input.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);

  try {
    await fetch(`/api/meetings/${meetingId}/upload-audio`, {
      method: "POST",
      body: formData,
    });
    toast("Audio uploaded", "success");
    openMeetingDetail(meetingId);
  } catch (error) {
    toast("Upload failed", "error");
  }
}

async function saveTranscript(meetingId) {
  const text = document.getElementById(`paste-transcript-${meetingId}`).value.trim();
  if (!text) return toast("Paste a transcript first", "error");

  const formData = new FormData();
  formData.append("transcript", text);

  try {
    await fetch(`/api/meetings/${meetingId}/paste-transcript`, {
      method: "POST",
      body: formData,
    });
    toast("Transcript saved", "success");
    logActivity("Saved transcript", "for meeting");
    openMeetingDetail(meetingId);
  } catch (error) {
    toast("Error", "error");
  }
}

async function transcribeMeeting(meetingId) {
  try {
    await api(`/api/meetings/${meetingId}/transcribe`, { method: "POST" });
    toast("Transcription complete", "success");
    logActivity("Transcribed", "meeting audio");
    openMeetingDetail(meetingId);
  } catch (error) {
    toast("Failed", "error");
  }
}

async function generateMOM(meetingId) {
  try {
    await api(`/api/meetings/${meetingId}/generate-mom`, { method: "POST" });
    toast("MOM generated", "success");
    logActivity("Generated MOM", "from transcript");
    openMeetingDetail(meetingId);
  } catch (error) {
    toast("Failed", "error");
  }
}

async function extractTasks(meetingId) {
  try {
    const result = await api(`/api/meetings/${meetingId}/extract-tasks`, { method: "POST" });
    toast(`${result.tasks_created} tasks extracted!`, "success");
    logActivity("Extracted tasks", `${result.tasks_created} from MOM`);
    fireConfetti();
    openMeetingDetail(meetingId);
  } catch (error) {
    toast("Failed", "error");
  }
}

// ===== TASKS =====

async function loadTasks() {
  const tableBody = document.getElementById("tasks-table");
  const emptyState = document.getElementById("no-tasks");

  try {
    const statusFilter = document.getElementById("filter-status").value;
    const memberFilter = document.getElementById("filter-member").value;
    const searchQuery = (document.getElementById("task-search")?.value.trim() || "").toLowerCase();

    let url = "/api/tasks/?";
    if (statusFilter) url += `status=${statusFilter}&`;
    if (memberFilter) url += `assigned_to=${memberFilter}&`;

    let tasks = await api(url);

    if (searchQuery) {
      tasks = tasks.filter(
        (task) =>
          task.title.toLowerCase().includes(searchQuery) ||
          (task.description || "").toLowerCase().includes(searchQuery)
      );
    }

    if (currentView === "board") {
      renderKanban(tasks);
      return;
    }

    if (tasks.length === 0) {
      tableBody.innerHTML = "";
      emptyState.style.display = "block";
      return;
    }

    emptyState.style.display = "none";
    tableBody.innerHTML = tasks
      .map((task, index) => {
        const assigneeHtml = task.assignee
          ? avatar(task.assignee.name, "avatar-sm") + task.assignee.name
          : '<span style="color:var(--text-tertiary)">Unassigned</span>';

        const descriptionHtml = task.description
          ? `<div style="font-size:12px;color:var(--text-tertiary);margin-top:3px;">${task.description}</div>`
          : "";

        return `
          <tr class="fade-in-up" style="animation-delay:${0.03 * index}s">
            <td><strong>${task.title}</strong>${descriptionHtml}</td>
            <td>
              <div style="display:flex;align-items:center;gap:8px;">${assigneeHtml}</div>
            </td>
            <td>${deadlineLabel(task.deadline)}</td>
            <td>${badge(task.priority)}</td>
            <td>
              <select class="status-select" onchange="updateTaskStatus(${task.id},this.value)">
                <option value="pending" ${task.status === "pending" ? "selected" : ""}>Pending</option>
                <option value="in_progress" ${task.status === "in_progress" ? "selected" : ""}>In Progress</option>
                <option value="completed" ${task.status === "completed" ? "selected" : ""}>Completed</option>
              </select>
            </td>
            <td>
              <button class="btn btn-danger btn-sm" onclick="deleteTask(${task.id})">&#128465;</button>
            </td>
          </tr>
        `;
      })
      .join("");
  } catch (error) {
    console.error(error);
  }
}

async function createTask() {
  const title = document.getElementById("task-title").value.trim();
  if (!title) return toast("Title required", "error");

  const assigneeValue = document.getElementById("task-assignee").value;
  const data = {
    title,
    description: document.getElementById("task-description").value.trim() || null,
    assigned_to: assigneeValue ? parseInt(assigneeValue) : null,
    deadline: document.getElementById("task-deadline").value || null,
    priority: document.getElementById("task-priority").value,
    status: document.getElementById("task-status").value,
  };

  setLoading("btn-create-task", true);

  try {
    await api("/api/tasks/", {
      method: "POST",
      body: JSON.stringify(data),
    });

    closeModal("task-modal");
    document.getElementById("task-title").value = "";
    document.getElementById("task-description").value = "";
    document.getElementById("task-deadline").value = "";

    toast("Task created", "success");
    logActivity("Created task", title);
    loadTasks();
    loadDashboard();
  } catch (error) {
    toast(error.message, "error");
  }

  setLoading("btn-create-task", false);
}

async function updateTaskStatus(taskId, status) {
  try {
    await api(`/api/tasks/${taskId}`, {
      method: "PATCH",
      body: JSON.stringify({ status }),
    });

    if (status === "completed") {
      toast("Task completed!", "success");
      logActivity("Completed task", "");
      fireConfetti();
    } else {
      toast("Updated", "info", 1500);
      logActivity("Updated task", `to ${status.replace("_", " ")}`);
    }

    loadTasks();
    loadDashboard();
  } catch (error) {
    toast(error.message, "error");
  }
}

async function deleteTask(taskId) {
  if (!confirm("Delete this task?")) return;

  try {
    await api(`/api/tasks/${taskId}`, { method: "DELETE" });
    toast("Task deleted", "info", 1500);
    logActivity("Deleted task", "");
    loadTasks();
    loadDashboard();
  } catch (error) {
    toast("Error", "error");
  }
}

// ===== TEAM =====

async function loadTeam() {
  const container = document.getElementById("team-list");
  const emptyState = document.getElementById("no-team");

  try {
    const members = await api("/api/members/");
    if (members.length === 0) {
      container.innerHTML = "";
      emptyState.style.display = "block";
      return;
    }

    emptyState.style.display = "none";
    container.innerHTML = members
      .map(
        (member) => `
        <div class="member-card">
          <div style="display:flex;justify-content:space-between;align-items:start;">
            <div class="member-card-top">
              ${avatar(member.name, "avatar-lg")}
              <div>
                <h3>${member.name}</h3>
                <div class="role">${member.role}</div>
              </div>
            </div>
            <button class="btn btn-danger btn-sm" onclick="deleteMember(${member.id})">&#128465;</button>
          </div>
          <div class="contact-info">
            ${member.email ? `<div>&#9993; ${member.email}</div>` : ""}
            ${member.phone ? `<div>&#9742; ${member.phone}</div>` : ""}
            ${!member.email && !member.phone ? '<div style="color:var(--text-tertiary)">No contact info</div>' : ""}
          </div>
        </div>
      `
      )
      .join("");
    container.classList.add("stagger");
  } catch (error) {
    console.error(error);
  }
}

async function createMember() {
  const name = document.getElementById("member-name").value.trim();
  if (!name) return toast("Name required", "error");

  const data = {
    name,
    email: document.getElementById("member-email").value.trim() || null,
    phone: document.getElementById("member-phone").value.trim() || null,
    role: document.getElementById("member-role").value,
  };

  setLoading("btn-create-member", true);

  try {
    await api("/api/members/", {
      method: "POST",
      body: JSON.stringify(data),
    });

    closeModal("member-modal");
    document.getElementById("member-name").value = "";
    document.getElementById("member-email").value = "";
    document.getElementById("member-phone").value = "";

    toast(`${name} added`, "success");
    logActivity("Added member", name);
    loadTeam();
    populateMemberDropdowns();
  } catch (error) {
    toast(error.message, "error");
  }

  setLoading("btn-create-member", false);
}

async function deleteMember(memberId) {
  if (!confirm("Remove member?")) return;

  try {
    await api(`/api/members/${memberId}`, { method: "DELETE" });
    toast("Removed", "info", 1500);
    logActivity("Removed member", "");
    loadTeam();
    populateMemberDropdowns();
  } catch (error) {
    toast("Error", "error");
  }
}

// ===== MEMBER DROPDOWNS =====

async function populateMemberDropdowns() {
  try {
    const members = await api("/api/members/");
    const dropdownIds = ["task-assignee", "filter-member"];

    dropdownIds.forEach((id) => {
      const select = document.getElementById(id);
      if (!select) return;

      const currentValue = select.value;
      const defaultLabel = id === "filter-member" ? "All Members" : "Unassigned";

      select.innerHTML =
        `<option value="">${defaultLabel}</option>` +
        members.map((member) => `<option value="${member.id}">${member.name}</option>`).join("");

      select.value = currentValue;
    });
  } catch (error) {
    // Silently fail — dropdowns will just be empty
  }
}

// ===== BUTTON GLOW EFFECT =====

document.addEventListener("mousemove", (event) => {
  const button = event.target.closest(".btn");
  if (button) {
    const rect = button.getBoundingClientRect();
    const xPercent = ((event.clientX - rect.left) / rect.width) * 100;
    const yPercent = ((event.clientY - rect.top) / rect.height) * 100;
    button.style.setProperty("--x", xPercent + "%");
    button.style.setProperty("--y", yPercent + "%");
  }
});

// ===== INIT =====

logActivity("Session started", "Welcome to MOMentum");
loadDashboard();
populateMemberDropdowns();
