// ==========================================
// APP STATE & ACTIVE USER
// ==========================================
let currentUser = {
    id: 1,
    name: "Rahul Sharma (Student)",
    email: "student@campus.edu",
    role: "STUDENT",
    department: "Hostel"
};

let allComplaintsCache = [];
let currentTrackingRef = null;
let currentRatingComplaintId = null;
let currentActionComplaintId = null;
let selectedStarRating = 5;
let slaTickerInterval = null;
let base64Attachment = null;

// ==========================================
// INITIALIZATION
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
    // Try to restore user from localStorage if saved
    const savedUser = localStorage.getItem("smart_portal_user");
    if (savedUser) {
        try {
            currentUser = JSON.parse(savedUser);
        } catch (e) {}
    }
    updateUserDisplay();
    loadDashboard();
    startSlaTicker();
});

function updateUserDisplay() {
    document.getElementById("currentUserDisplay").textContent = currentUser.name;
    const badge = document.getElementById("currentRoleBadge");
    badge.textContent = currentUser.role;

    if (currentUser.role === "STUDENT") {
        badge.className = "badge bg-warning text-dark";
        document.getElementById("nav-submit-li").classList.remove("d-none");
        document.getElementById("nav-staff-li").classList.add("d-none");
        document.getElementById("dashboardTitle").innerHTML = '<i class="fa-solid fa-list-check me-2 text-primary"></i> My Submitted Grievances';
    } else {
        badge.className = "badge bg-info text-white";
        document.getElementById("nav-submit-li").classList.add("d-none");
        document.getElementById("nav-staff-li").classList.remove("d-none");
        document.getElementById("dashboardTitle").innerHTML = '<i class="fa-solid fa-list-check me-2 text-primary"></i> Officer Department Queue';
    }
}

// ==========================================
// QUICK DEMO SWITCHER
// ==========================================
async function quickSwitch(email) {
    showAlert("Switching user to " + email + "...", "info");
    try {
        const res = await fetch("/api/auth/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email: email, password: "password123" })
        });
        const data = await res.json();
        if (data.success && data.user) {
            currentUser = data.user;
            localStorage.setItem("smart_portal_user", JSON.stringify(currentUser));
            updateUserDisplay();
            showAlert(`Switched to: ${currentUser.name} (${currentUser.role})`, "success");
            loadDashboard();
        } else {
            showAlert("Login failed: " + data.message, "danger");
        }
    } catch (e) {
        showAlert("Server offline or error: " + e.message, "danger");
    }
}

function logout() {
    localStorage.removeItem("smart_portal_user");
    quickSwitch("student@campus.edu");
}

// ==========================================
// NAVIGATION / SECTION TOGGLE
// ==========================================
function showSection(sectionId) {
    document.querySelectorAll(".content-section").forEach(s => s.classList.add("d-none"));
    document.querySelectorAll(".nav-link").forEach(l => l.classList.remove("active"));

    const targetSection = document.getElementById("section-" + sectionId);
    if (targetSection) {
        targetSection.classList.remove("d-none");
    }

    const navLink = document.getElementById("nav-" + sectionId);
    if (navLink) {
        navLink.classList.add("active");
    }

    if (sectionId === "dashboard") {
        loadDashboard();
    } else if (sectionId === "staff") {
        loadStaffQueue();
    }
}

// ==========================================
// LIVE AUTOMATED PRIORITY CALCULATOR (AC 1)
// ==========================================
function calculateLivePriority() {
    const cat = document.getElementById("formCategory").value;
    const title = document.getElementById("formTitle").value.toLowerCase();
    const desc = document.getElementById("formDescription").value.toLowerCase();
    const combined = title + " " + desc;

    const badge = document.getElementById("livePriorityBadge");
    const reason = document.getElementById("priorityReason");

    const highTriggers = ["leak", "fire", "shock", "water", "electric", "power", "danger", "ragging", "medical", "emergency", "ceiling", "exam", "hall ticket", "admit card"];
    const isHigh = highTriggers.some(t => combined.includes(t));

    if (isHigh) {
        badge.className = "badge bg-danger fs-6 px-3 py-2";
        badge.textContent = "HIGH (Urgent)";
        reason.textContent = "Detected urgent campus hazard / safety keyword: High Priority applied.";
        return "HIGH";
    }

    const medTriggers = ["wifi", "internet", "fan", "clean", "mess", "food", "library", "timetable", "attendance", "ac", "door", "bench"];
    const isMed = medTriggers.some(t => combined.includes(t)) || cat === "Hostel" || cat === "Infrastructure";

    if (isMed) {
        badge.className = "badge bg-warning text-dark fs-6 px-3 py-2";
        badge.textContent = "MEDIUM";
        reason.textContent = "Standard grievance routing: Medium Priority applied.";
        return "MEDIUM";
    }

    badge.className = "badge bg-info text-dark fs-6 px-3 py-2";
    badge.textContent = "LOW";
    reason.textContent = "General request / inquiry: Low Priority applied.";
    return "LOW";
}

// ==========================================
// ATTACHMENT PREVIEW (AC 1)
// ==========================================
function previewAttachment(input) {
    const file = input.files[0];
    const previewContainer = document.getElementById("attachmentPreview");
    const previewImg = document.getElementById("previewImg");
    const previewDoc = document.getElementById("previewDoc");
    const nameSpan = document.getElementById("attachmentName");

    if (!file) {
        previewContainer.classList.add("d-none");
        base64Attachment = null;
        return;
    }

    nameSpan.textContent = file.name;
    previewContainer.classList.remove("d-none");

    const reader = new FileReader();
    reader.onload = function(e) {
        if (file.type.startsWith("image/")) {
            const img = new Image();
            img.onload = function() {
                const maxDim = 1200;
                let width = img.width;
                let height = img.height;
                if (width > maxDim || height > maxDim) {
                    if (width > height) {
                        height = Math.round((height * maxDim) / width);
                        width = maxDim;
                    } else {
                        width = Math.round((width * maxDim) / height);
                        height = maxDim;
                    }
                }
                const canvas = document.createElement("canvas");
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0, width, height);
                base64Attachment = canvas.toDataURL("image/jpeg", 0.75);
                previewImg.src = base64Attachment;
                previewImg.classList.remove("d-none");
                previewDoc.classList.add("d-none");
            };
            img.src = e.target.result;
        } else {
            base64Attachment = e.target.result;
            previewImg.classList.add("d-none");
            previewDoc.classList.remove("d-none");
        }
    };
    reader.readAsDataURL(file);
}

// ==========================================
// SUBMIT COMPLAINT (AC 1 & AC 2)
// ==========================================
async function handleComplaintSubmit(e) {
    e.preventDefault();
    const submitBtn = document.getElementById("submitBtn");
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin me-1"></i> Submitting...';

    const priority = calculateLivePriority();
    const payload = {
        userId: currentUser.id,
        userName: currentUser.name,
        category: document.getElementById("formCategory").value,
        title: document.getElementById("formTitle").value.trim(),
        description: document.getElementById("formDescription").value.trim(),
        priority: priority,
        attachmentPath: base64Attachment || ""
    };

    try {
        const res = await fetch("/api/complaints/submit", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
            showAlert(`🎉 Grievance submitted successfully! Reference ID: <strong>${data.referenceId}</strong> with 48h SLA timer started.`, "success");
            document.getElementById("complaintForm").reset();
            document.getElementById("attachmentPreview").classList.add("d-none");
            base64Attachment = null;
            
            // Navigate to tracking for this ticket
            showSection("track");
            document.getElementById("trackSearchInput").value = data.referenceId;
            handleTrackSearch();
        } else {
            showAlert("Submission failed: " + data.message, "danger");
        }
    } catch (err) {
        showAlert("Error submitting grievance: " + err.message, "danger");
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<i class="fa-solid fa-paper-plane me-1"></i> Submit & Start 48h SLA';
    }
}

// ==========================================
// LOAD DASHBOARD / METRICS
// ==========================================
async function loadDashboard() {
    try {
        const endpoint = (currentUser.role === "STUDENT")
            ? `/api/complaints/my?userId=${currentUser.id}`
            : `/api/complaints/all`;

        const res = await fetch(endpoint);
        const complaints = await res.json();
        allComplaintsCache = complaints;

        // Update metric stats
        updateMetricStats(complaints);

        // Render table
        renderComplaintsTable(complaints);
    } catch (e) {
        console.error("Dashboard load error", e);
    }
}

function updateMetricStats(complaints) {
    document.getElementById("statTotal").textContent = complaints.length;
    const active = complaints.filter(c => c.status !== "Resolved").length;
    const escalated = complaints.filter(c => c.status && c.status.toLowerCase().includes("escalated")).length;
    const resolved = complaints.filter(c => c.status === "Resolved").length;

    document.getElementById("statActive").textContent = active;
    document.getElementById("statEscalated").textContent = escalated;
    document.getElementById("statResolved").textContent = resolved;
}

// ==========================================
// RENDER COMPLAINTS TABLE (STUDENT)
// ==========================================
function renderComplaintsTable(complaints) {
    const tbody = document.getElementById("myComplaintsTbody");
    if (!complaints || complaints.length === 0) {
        tbody.innerHTML = `<tr><td colspan="8" class="text-center py-4 text-muted">No grievances found. Click <strong>New Grievance</strong> to submit one.</td></tr>`;
        return;
    }

    tbody.innerHTML = complaints.map(c => {
        const slaInfo = calculateSlaRemaining(c.slaDeadline, c.status);
        const isActionTaken = (c.status === "Action Taken");

        return `
            <tr>
                <td class="fw-bold text-primary font-monospace">${c.referenceId || ("CMP-" + c.id)}</td>
                <td><span class="badge bg-light text-dark border">${c.category || c.department}</span></td>
                <td>
                    <div class="fw-semibold text-dark">${escapeHtml(c.title)}</div>
                    <small class="text-muted d-inline-block text-truncate" style="max-width: 250px;">${escapeHtml(c.description)}</small>
                </td>
                <td><span class="badge badge-priority-${c.priority || 'MEDIUM'}">${c.priority || 'MEDIUM'}</span></td>
                <td><small class="text-muted">${c.assignedCoordinator || 'Coordinator'}</small></td>
                <td>${formatStatusBadge(c.status)}</td>
                <td><span class="sla-badge ${slaInfo.cssClass}"><i class="fa-regular fa-clock me-1"></i>${slaInfo.text}</span></td>
                <td class="text-end">
                    <button class="btn btn-outline-primary btn-sm me-1" onclick="viewComplaintTrack('${c.referenceId || c.id}')" title="Track Ticket & SLA"><i class="fa-solid fa-magnifying-glass"></i></button>
                    ${isActionTaken ? `<button class="btn btn-warning btn-sm fw-bold" onclick="openRatingModalFor('${c.id}')" title="Action Taken! Please rate to resolve"><i class="fa-solid fa-star me-1"></i> Rate & Close</button>` : ''}
                </td>
            </tr>
        `;
    }).join("");
}

// ==========================================
// TRACK COMPLAINT SEARCH (AC 2 & AC 3)
// ==========================================
async function handleTrackSearch() {
    const ref = document.getElementById("trackSearchInput").value.trim();
    if (!ref) {
        showAlert("Please enter a complaint reference ID (e.g. CMP-000001)", "warning");
        return;
    }
    viewComplaintTrack(ref);
}

async function viewComplaintTrack(ref) {
    showSection("track");
    document.getElementById("trackSearchInput").value = ref;

    try {
        const res = await fetch(`/api/complaints/track?referenceId=${encodeURIComponent(ref)}`);
        const c = await res.json();

        if (!c || c.error) {
            showAlert("Complaint not found with ID: " + ref, "danger");
            document.getElementById("trackResultContainer").classList.add("d-none");
            return;
        }

        currentTrackingRef = c;
        document.getElementById("trackResultContainer").classList.remove("d-none");

        document.getElementById("trackRefId").textContent = c.referenceId || ("CMP-" + c.id);
        document.getElementById("trackCategory").textContent = c.category || c.department;

        const priorityBadge = document.getElementById("trackPriority");
        priorityBadge.className = `badge badge-priority-${c.priority || 'MEDIUM'}`;
        priorityBadge.textContent = c.priority || 'MEDIUM';

        document.getElementById("trackStatusBadge").innerHTML = formatStatusBadge(c.status);
        document.getElementById("trackTitle").textContent = c.title;
        document.getElementById("trackDescription").textContent = c.description;
        document.getElementById("trackCreated").textContent = c.createdAt || "N/A";
        document.getElementById("trackDeadline").textContent = c.slaDeadline || "48 Hours";
        document.getElementById("trackOfficer").textContent = c.assignedCoordinator || "Department Coordinator";
        document.getElementById("trackEscalatedTo").textContent = c.escalatedTo || (c.status.includes("Escalated") ? "HOD / Dean" : "None");

        // Attachment
        const attachRow = document.getElementById("trackAttachmentRow");
        const attachLink = document.getElementById("trackAttachmentLink");
        if (c.attachmentPath && c.attachmentPath.length > 5) {
            attachRow.classList.remove("d-none");
            attachLink.href = c.attachmentPath;
        } else {
            attachRow.classList.add("d-none");
        }

        // Resolution remarks
        const resBox = document.getElementById("resolutionBox");
        if (c.resolutionRemarks && c.resolutionRemarks.trim().length > 0) {
            resBox.classList.remove("d-none");
            document.getElementById("trackResolutionText").textContent = c.resolutionRemarks;
        } else {
            resBox.classList.add("d-none");
        }

        // Student feedback card (AC 4)
        const feedbackCard = document.getElementById("studentFeedbackCard");
        const completedCard = document.getElementById("completedFeedbackCard");

        if (c.status === "Action Taken" && currentUser.role === "STUDENT") {
            feedbackCard.classList.remove("d-none");
            completedCard.classList.add("d-none");
            currentRatingComplaintId = c.id;
        } else if (c.status === "Resolved" && c.rating) {
            feedbackCard.classList.add("d-none");
            completedCard.classList.remove("d-none");
            document.getElementById("displayStars").textContent = "⭐".repeat(c.rating);
            document.getElementById("displayFeedbackComment").textContent = c.feedback ? `"${c.feedback}"` : "";
        } else {
            feedbackCard.classList.add("d-none");
            completedCard.classList.add("d-none");
        }

        updateTrackSlaBar(c);

    } catch (e) {
        showAlert("Error loading complaint: " + e.message, "danger");
    }
}

function updateTrackSlaBar(c) {
    const slaInfo = calculateSlaRemaining(c.slaDeadline, c.status);
    document.getElementById("trackCountdownTimer").textContent = slaInfo.text;

    const pBar = document.getElementById("trackProgressBar");
    const breachAlert = document.getElementById("slaBreachAlert");

    if (c.status === "Resolved") {
        pBar.style.width = "100%";
        pBar.className = "progress-bar bg-success";
        breachAlert.classList.add("d-none");
    } else if (slaInfo.isBreached) {
        pBar.style.width = "100%";
        pBar.className = "progress-bar bg-danger progress-bar-striped progress-bar-animated";
        breachAlert.classList.remove("d-none");
    } else {
        breachAlert.classList.add("d-none");
        const percent = Math.max(5, Math.min(100, (slaInfo.remainingMs / (48 * 3600 * 1000)) * 100));
        pBar.style.width = percent + "%";
        if (percent < 25) {
            pBar.className = "progress-bar bg-danger progress-bar-striped progress-bar-animated";
        } else if (percent < 50) {
            pBar.className = "progress-bar bg-warning progress-bar-striped";
        } else {
            pBar.className = "progress-bar bg-success";
        }
    }
}

// ==========================================
// STAFF & OFFICER QUEUE (COORDINATOR / HOD / DEAN)
// ==========================================
async function loadStaffQueue() {
    try {
        const res = await fetch("/api/complaints/all");
        const complaints = await res.json();
        allComplaintsCache = complaints;
        renderStaffTable(complaints);
    } catch (e) {
        console.error("Staff queue error", e);
    }
}

function filterStaffTable(cat, btn) {
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active", "btn-primary"));
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.add("btn-outline-secondary"));
    btn.classList.add("active", "btn-primary");
    btn.classList.remove("btn-outline-secondary");

    if (cat === "ALL") {
        renderStaffTable(allComplaintsCache);
    } else if (cat === "ESCALATED") {
        const filtered = allComplaintsCache.filter(c => c.status && c.status.toLowerCase().includes("escalated"));
        renderStaffTable(filtered);
    } else {
        const filtered = allComplaintsCache.filter(c => (c.category === cat || c.department === cat));
        renderStaffTable(filtered);
    }
}

function renderStaffTable(complaints) {
    const tbody = document.getElementById("staffQueueTbody");
    if (!complaints || complaints.length === 0) {
        tbody.innerHTML = `<tr><td colspan="9" class="text-center py-4 text-muted">No grievances in queue.</td></tr>`;
        return;
    }

    tbody.innerHTML = complaints.map(c => {
        const slaInfo = calculateSlaRemaining(c.slaDeadline, c.status);
        const canTakeAction = (c.status !== "Resolved");

        return `
            <tr>
                <td class="fw-bold font-monospace text-primary">${c.referenceId || ("CMP-" + c.id)}</td>
                <td><small class="fw-semibold">${c.userName || 'Student'}</small></td>
                <td><span class="badge bg-light text-dark border">${c.category || c.department}</span></td>
                <td>
                    <div class="fw-semibold text-dark">${escapeHtml(c.title)}</div>
                    <small class="text-muted d-inline-block text-truncate" style="max-width: 200px;">${escapeHtml(c.description)}</small>
                </td>
                <td><span class="badge badge-priority-${c.priority || 'MEDIUM'}">${c.priority || 'MEDIUM'}</span></td>
                <td><span class="sla-badge ${slaInfo.cssClass}">${slaInfo.text}</span></td>
                <td>${formatStatusBadge(c.status)}</td>
                <td><small class="text-danger fw-semibold">${c.escalatedTo ? ('Escalated to: ' + c.escalatedTo) : 'None'}</small></td>
                <td class="text-end">
                    <button class="btn btn-outline-primary btn-sm me-1" onclick="viewComplaintTrack('${c.referenceId || c.id}')" title="Track Details"><i class="fa-solid fa-eye"></i></button>
                    ${canTakeAction ? `
                        <button class="btn btn-success btn-sm me-1" onclick="openActionModal('${c.id}')" title="Take Action / Resolve"><i class="fa-solid fa-check"></i> Action</button>
                        <button class="btn btn-outline-danger btn-sm" onclick="quickEscalate('${c.id}')" title="Manual Escalate to HOD/Dean"><i class="fa-solid fa-arrow-up"></i></button>
                    ` : '<span class="badge bg-success small">Closed</span>'}
                </td>
            </tr>
        `;
    }).join("");
}

// ==========================================
// MODAL ACTIONS: ACTION TAKEN & ESCALATION
// ==========================================
function openActionModal(id) {
    currentActionComplaintId = id;
    document.getElementById("actionRemarks").value = "";
    const modal = new bootstrap.Modal(document.getElementById("actionModal"));
    modal.show();
}

async function submitActionTaken() {
    const remarks = document.getElementById("actionRemarks").value.trim();
    if (!remarks) {
        showAlert("Please enter action remarks detailing work done.", "warning");
        return;
    }

    try {
        const res = await fetch("/api/complaints/action", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ complaintId: currentActionComplaintId, remarks: remarks })
        });
        const data = await res.json();
        if (data.success) {
            bootstrap.Modal.getInstance(document.getElementById("actionModal")).hide();
            showAlert("Action recorded! Status changed to 'Action Taken' (awaiting student satisfaction rating).", "success");
            loadDashboard();
            loadStaffQueue();
        } else {
            showAlert("Failed: " + data.message, "danger");
        }
    } catch (e) {
        showAlert("Error: " + e.message, "danger");
    }
}

async function quickEscalate(id) {
    if (!confirm("Are you sure you want to escalate this complaint to the Head of Department / Dean?")) return;
    try {
        const res = await fetch("/api/complaints/escalate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ complaintId: id, targetRole: "HOD" })
        });
        const data = await res.json();
        if (data.success) {
            showAlert("Ticket escalated to HOD / Dean successfully!", "warning");
            loadStaffQueue();
            loadDashboard();
        }
    } catch (e) {
        showAlert("Escalation error: " + e.message, "danger");
    }
}

async function triggerAutoEscalationCheck() {
    showAlert("Running 48-hour SLA Auto-Escalator check...", "info");
    try {
        const res = await fetch("/api/complaints/check-escalations", { method: "POST" });
        const data = await res.json();
        showAlert(`SLA Auto-Escalator Check Complete: ${data.escalatedCount} breached tickets escalated to HOD/Dean.`, "success");
        loadStaffQueue();
        loadDashboard();
    } catch (e) {
        showAlert("Error running auto-escalator: " + e.message, "danger");
    }
}

// ==========================================
// MODAL: 5-STAR SATISFACTION RATING (AC 4)
// ==========================================
function openRatingModalFor(id) {
    currentRatingComplaintId = id;
    openRatingModal();
}

function openRatingModal() {
    setStarRating(5);
    document.getElementById("feedbackComment").value = "";
    const modal = new bootstrap.Modal(document.getElementById("ratingModal"));
    modal.show();
}

function setStarRating(stars) {
    selectedStarRating = stars;
    const starBtns = document.querySelectorAll(".star-rating .star-btn");
    starBtns.forEach(btn => {
        const val = parseInt(btn.getAttribute("data-val"));
        if (val <= stars) {
            btn.className = "fa-solid fa-star star-btn text-warning";
        } else {
            btn.className = "fa-regular fa-star star-btn text-secondary";
        }
    });

    const labels = ["", "Poor (1 Star)", "Fair (2 Stars)", "Good (3 Stars)", "Very Good (4 Stars)", "Excellent (5 Stars)"];
    document.getElementById("ratingLabel").textContent = labels[stars] || `${stars} Stars`;
}

async function submitSatisfactionRating() {
    if (!currentRatingComplaintId) return;
    const comment = document.getElementById("feedbackComment").value.trim();

    try {
        const res = await fetch("/api/complaints/rate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                complaintId: currentRatingComplaintId,
                rating: selectedStarRating,
                feedback: comment
            })
        });
        const data = await res.json();

        if (data.success) {
            bootstrap.Modal.getInstance(document.getElementById("ratingModal")).hide();
            showAlert(`🌟 Satisfaction rating submitted! Ticket status transitioned to RESOLVED.`, "success");
            loadDashboard();
            if (currentTrackingRef) {
                viewComplaintTrack(currentTrackingRef.referenceId || currentTrackingRef.id);
            }
        } else {
            showAlert("Rating submission failed: " + data.message, "danger");
        }
    } catch (e) {
        showAlert("Error submitting rating: " + e.message, "danger");
    }
}

// ==========================================
// SLA COUNTDOWN LOGIC (AC 2 & AC 3)
// ==========================================
function calculateSlaRemaining(deadlineStr, status) {
    if (status === "Resolved") {
        return { text: "Completed", cssClass: "sla-green", isBreached: false, remainingMs: 0 };
    }

    if (!deadlineStr) {
        return { text: "48h 00m", cssClass: "sla-green", isBreached: false, remainingMs: 48 * 3600 * 1000 };
    }

    // Parse deadline string "yyyy-MM-dd HH:mm:ss"
    const deadline = new Date(deadlineStr.replace(" ", "T")).getTime();
    const now = new Date().getTime();
    const diff = deadline - now;

    if (diff <= 0) {
        return { text: "BREACHED (Escalated)", cssClass: "sla-red", isBreached: true, remainingMs: 0 };
    }

    const hours = Math.floor(diff / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    const formatted = `${hours}h ${minutes}m ${seconds}s`;

    if (hours < 12) {
        return { text: formatted, cssClass: "sla-red", isBreached: false, remainingMs: diff };
    } else if (hours < 24) {
        return { text: formatted, cssClass: "sla-yellow", isBreached: false, remainingMs: diff };
    }
    return { text: formatted, cssClass: "sla-green", isBreached: false, remainingMs: diff };
}

function startSlaTicker() {
    if (slaTickerInterval) clearInterval(slaTickerInterval);
    slaTickerInterval = setInterval(() => {
        // Update live tracker if visible
        if (currentTrackingRef && !document.getElementById("section-track").classList.contains("d-none")) {
            updateTrackSlaBar(currentTrackingRef);
        }
    }, 1000);
}

// ==========================================
// HELPERS
// ==========================================
function formatStatusBadge(status) {
    const s = status || "Submitted";
    let css = "bg-secondary";
    if (s === "In Progress") css = "bg-primary";
    if (s === "Action Taken") css = "bg-warning text-dark";
    if (s === "Resolved") css = "bg-success";
    if (s.includes("Escalated")) css = "bg-danger";

    return `<span class="badge ${css}">${s}</span>`;
}

function showAlert(message, type = "info") {
    const placeholder = document.getElementById("alertPlaceholder");
    placeholder.innerHTML = `
        <div class="alert alert-${type} alert-dismissible fade show shadow-sm" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;
    setTimeout(() => {
        const alert = placeholder.querySelector(".alert");
        if (alert) alert.remove();
    }, 6000);
}

function escapeHtml(text) {
    if (!text) return "";
    return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}
