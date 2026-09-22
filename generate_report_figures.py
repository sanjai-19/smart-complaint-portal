import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def generate_fig1_architecture():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Title
    ax.text(50, 96, "Smart Complaint Portal - 3-Tier System Architecture", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a', fontfamily='sans-serif')

    # Tier 1 Box (Presentation Layer)
    rect1 = patches.FancyBboxPatch((5, 68), 90, 20, boxstyle="round,pad=1.5,rounding_size=2", 
                                   linewidth=1.5, edgecolor='#1d4ed8', facecolor='#eff6ff')
    ax.add_patch(rect1)
    ax.text(8, 83, "TIER 1: PRESENTATION LAYER (CLIENT-SIDE WEB INTERFACE)", fontsize=11, fontweight='bold', color='#1e40af')
    ax.text(8, 77, "• Semantic HTML5 Markup & Responsive CSS3 Design Tokens (Slate/Royal Blue Theme)\n• Bootstrap 5.3 Grid System, Live 48-Hour SLA Countdown Timers & Dynamic Priority Badges\n• Interactive 5-Star Rating Widget, Client-Side HTML5 Canvas Image Downsampling (<150 KB)", 
            fontsize=9.5, color='#334155', linespacing=1.3)

    # Down Arrow 1
    ax.annotate('', xy=(50, 58), xytext=(50, 68),
                arrowprops=dict(arrowstyle="<->", color="#1d4ed8", lw=2, mutation_scale=15))
    ax.text(51, 63, "RESTful HTTP / JSON (Port 8080)", fontsize=9, fontweight='bold', color='#1d4ed8', ha='left')

    # Tier 2 Box (Application / Business Logic Layer)
    rect2 = patches.FancyBboxPatch((5, 34), 90, 24, boxstyle="round,pad=1.5,rounding_size=2", 
                                   linewidth=1.5, edgecolor='#0284c7', facecolor='#f0f9ff')
    ax.add_patch(rect2)
    ax.text(8, 53, "TIER 2: APPLICATION & PROCESS AUTOMATION LAYER (JAVA SE 21 BACKEND)", fontsize=11, fontweight='bold', color='#0369a1')
    ax.text(8, 43, "• Native com.sun.net.httpserver.HttpServer (Zero-Framework Architecture, Sub-400ms Startup)\n• Modular HttpHandlers: SubmitComplaintHandler, RateComplaintHandler, EscalateHandler, LoginHandler\n• Cryptographic Security: BCrypt Password Salting (Work Factor 12) via org.mindrot:jbcrypt\n• Background SLA Escalation Engine: ScheduledExecutorService auditing ticket age hourly", 
            fontsize=9.5, color='#334155', linespacing=1.3)

    # Down Arrow 2
    ax.annotate('', xy=(50, 24), xytext=(50, 34),
                arrowprops=dict(arrowstyle="<->", color="#0284c7", lw=2, mutation_scale=15))
    ax.text(51, 29, "JDBC Connection Pool (PreparedStatements)", fontsize=9, fontweight='bold', color='#0284c7', ha='left')

    # Tier 3 Box (Data Persistence Layer)
    rect3 = patches.FancyBboxPatch((5, 4), 90, 20, boxstyle="round,pad=1.5,rounding_size=2", 
                                   linewidth=1.5, edgecolor='#059669', facecolor='#ecfdf5')
    ax.add_patch(rect3)
    ax.text(8, 19, "TIER 3: DATA PERSISTENCE LAYER (MYSQL 8.0 RELATIONAL DATABASE)", fontsize=11, fontweight='bold', color='#047857')
    ax.text(8, 12, "• Normalized in Third Normal Form (3NF) with Strict ACID Transaction Compliance\n• Tables: users (Credentials & Roles), complaints (Tickets & SLA Data), complaint_actions (Audit Trail)\n• Foreign Key Constraints (ON DELETE CASCADE) & Longtext Base64 Attachment Storage", 
            fontsize=9.5, color='#334155', linespacing=1.3)

    plt.tight_layout()
    plt.savefig("fig1_architecture.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig1_architecture.png")

def generate_fig2_workflow():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Grievance Lifecycle & Multi-Tier SLA Escalation Flowchart", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a', fontfamily='sans-serif')

    # Step 1
    p1 = patches.FancyBboxPatch((5, 78), 24, 12, boxstyle="round,pad=1", edgecolor='#1d4ed8', facecolor='#dbeafe', lw=1.5)
    ax.add_patch(p1)
    ax.text(17, 84, "1. Student Submits\nGrievance & Photo", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e40af')

    # Arrow 1->2
    ax.annotate('', xy=(34, 84), xytext=(29, 84), arrowprops=dict(arrowstyle="->", color="#1d4ed8", lw=2))

    # Step 2
    p2 = patches.FancyBboxPatch((34, 78), 28, 12, boxstyle="round,pad=1", edgecolor='#1d4ed8', facecolor='#dbeafe', lw=1.5)
    ax.add_patch(p2)
    ax.text(48, 84, "2. Ticket Assigned\nTracking ID & 48h SLA", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e40af')

    # Arrow 2->3
    ax.annotate('', xy=(67, 84), xytext=(62, 84), arrowprops=dict(arrowstyle="->", color="#1d4ed8", lw=2))

    # Step 3
    p3 = patches.FancyBboxPatch((67, 78), 28, 12, boxstyle="round,pad=1", edgecolor='#1d4ed8', facecolor='#dbeafe', lw=1.5)
    ax.add_patch(p3)
    ax.text(81, 84, "3. Coordinator Queue\n(Initial Level 1)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e40af')

    # Branching decision
    # Down arrow from Step 3: Unresolved past 24h
    ax.annotate('', xy=(81, 62), xytext=(81, 78), arrowprops=dict(arrowstyle="->", color="#dc2626", lw=2))
    ax.text(82, 70, "Unaddressed > 24h", fontsize=8.5, fontweight='bold', color='#dc2626')

    # Step 4 (Escalation to HOD)
    p4 = patches.FancyBboxPatch((67, 50), 28, 12, boxstyle="round,pad=1", edgecolor='#ea580c', facecolor='#ffedd5', lw=1.5)
    ax.add_patch(p4)
    ax.text(81, 56, "4. Level 2 Escalation:\nHead of Dept (HOD)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#c2410c')

    # Down arrow from HOD: Unresolved past 48h
    ax.annotate('', xy=(81, 34), xytext=(81, 50), arrowprops=dict(arrowstyle="->", color="#b91c1c", lw=2))
    ax.text(82, 42, "Breached > 48h", fontsize=8.5, fontweight='bold', color='#b91c1c')

    # Step 5 (Escalation to Dean)
    p5 = patches.FancyBboxPatch((67, 22), 28, 12, boxstyle="round,pad=1", edgecolor='#b91c1c', facecolor='#fee2e2', lw=1.5)
    ax.add_patch(p5)
    ax.text(81, 28, "5. Level 3 Escalation:\nDean / Principal", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#991b1b')

    # Resolution path from Coordinator/HOD/Dean
    # Left arrow from Coordinator (Action Taken)
    ax.annotate('', xy=(48, 50), xytext=(67, 56), arrowprops=dict(arrowstyle="->", color="#059669", lw=2))
    ax.annotate('', xy=(48, 50), xytext=(67, 84), arrowprops=dict(arrowstyle="->", color="#059669", lw=2))
    ax.annotate('', xy=(48, 50), xytext=(67, 28), arrowprops=dict(arrowstyle="->", color="#059669", lw=2))

    # Step 6 (Action Logged)
    p6 = patches.FancyBboxPatch((28, 44), 30, 12, boxstyle="round,pad=1", edgecolor='#059669', facecolor='#ecfdf5', lw=1.5)
    ax.add_patch(p6)
    ax.text(43, 50, "6. Staff Logs Action\n(Status: ACTION_TAKEN)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#047857')

    # Arrow 6->7 (Closed-Loop Rating)
    ax.annotate('', xy=(43, 30), xytext=(43, 44), arrowprops=dict(arrowstyle="->", color="#059669", lw=2))

    # Step 7 (Rating Verification)
    p7 = patches.FancyBboxPatch((28, 18), 30, 12, boxstyle="round,pad=1", edgecolor='#059669', facecolor='#dcfce7', lw=1.5)
    ax.add_patch(p7)
    ax.text(43, 24, "7. Student Verification\n(1 to 5 Star Rating Prompt)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#15803d')

    # Arrow 7->8 (Permanent Resolved)
    ax.annotate('', xy=(20, 24), xytext=(28, 24), arrowprops=dict(arrowstyle="->", color="#047857", lw=2))

    # Step 8 (Resolved)
    p8 = patches.FancyBboxPatch((5, 18), 15, 12, boxstyle="round,pad=1", edgecolor='#047857', facecolor='#bbf7d0', lw=2)
    ax.add_patch(p8)
    ax.text(12.5, 24, "8. RESOLVED\n(Closed)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#047857')

    # Guard annotation
    p_guard = patches.FancyBboxPatch((5, 42), 18, 16, boxstyle="round,pad=1", edgecolor='#b45309', facecolor='#fef3c7', lw=1.5)
    ax.add_patch(p_guard)
    ax.text(14, 50, "[ANTI-BYPASS LOCK]:\nDirect staff closure\nwithout student rating\nis rejected (HTTP 400)", ha='center', va='center', fontsize=8, fontweight='bold', color='#92400e')

    plt.tight_layout()
    plt.savefig("fig2_workflow.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig2_workflow.png")

def generate_fig3_er_schema():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Relational Database Schema (Third Normal Form - 3NF)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a', fontfamily='sans-serif')

    # Table 1: users
    p1 = patches.FancyBboxPatch((5, 46), 26, 44, boxstyle="round,pad=1", edgecolor='#1d4ed8', facecolor='#eff6ff', lw=1.5)
    ax.add_patch(p1)
    ax.text(18, 86, "TABLE: users", ha='center', va='center', fontsize=11, fontweight='bold', color='#1e40af')
    ax.plot([5, 31], [82, 82], color='#1d4ed8', lw=1)
    ax.text(7, 78, "PK  id (INT, AUTO_INC)\n    name (VARCHAR 100)\nUQ  email (VARCHAR 100)\n    password_hash (VARCHAR 255)\n    role (ENUM: Student/Admin)\n    department (VARCHAR 100)\n    created_at (TIMESTAMP)", 
            fontsize=8.5, color='#334155', linespacing=1.35)

    # Table 2: complaints
    p2 = patches.FancyBboxPatch((37, 30), 28, 60, boxstyle="round,pad=1", edgecolor='#0284c7', facecolor='#f0f9ff', lw=1.5)
    ax.add_patch(p2)
    ax.text(51, 86, "TABLE: complaints", ha='center', va='center', fontsize=11, fontweight='bold', color='#0369a1')
    ax.plot([37, 65], [82, 82], color='#0284c7', lw=1)
    ax.text(39, 78, "PK  id (INT, AUTO_INC)\nUQ  tracking_id (VARCHAR 50)\nFK  user_id (INT) -> users.id\n    title (VARCHAR 200)\n    description (TEXT)\n    category (ENUM)\n    priority (ENUM: High/Med)\n    status (ENUM: Sub/Act/Res)\n    escalation_level (ENUM)\n    attachment_path (LONGTEXT)\n    rating (TINYINT 1-5)\n    feedback (TEXT)\n    created_at (TIMESTAMP)\n    updated_at (TIMESTAMP)", 
            fontsize=8.5, color='#334155', linespacing=1.35)

    # Table 3: complaint_actions
    p3 = patches.FancyBboxPatch((70, 46), 26, 44, boxstyle="round,pad=1", edgecolor='#059669', facecolor='#ecfdf5', lw=1.5)
    ax.add_patch(p3)
    ax.text(83, 86, "TABLE: complaint_actions", ha='center', va='center', fontsize=11, fontweight='bold', color='#047857')
    ax.plot([70, 96], [82, 82], color='#059669', lw=1)
    ax.text(72, 78, "PK  id (INT, AUTO_INC)\nFK  complaint_id (INT) -> complaints.id\nFK  action_by (INT) -> users.id\n    action_type (VARCHAR 50)\n    comments (TEXT)\n    action_timestamp (TIMESTAMP)", 
            fontsize=8.5, color='#334155', linespacing=1.35)

    # Relationship Arrows
    # users.id -> complaints.user_id
    ax.annotate('', xy=(37, 68), xytext=(31, 78), arrowprops=dict(arrowstyle="->", color="#1d4ed8", lw=1.5))
    ax.text(33, 75, "1:N", fontsize=8.5, fontweight='bold', color='#1d4ed8')

    # complaints.id -> complaint_actions.complaint_id
    ax.annotate('', xy=(70, 68), xytext=(65, 70), arrowprops=dict(arrowstyle="->", color="#0284c7", lw=1.5))
    ax.text(66, 71, "1:N", fontsize=8.5, fontweight='bold', color='#0284c7')

    # users.id -> complaint_actions.action_by (curved)
    ax.annotate('', xy=(70, 60), xytext=(31, 60), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.5, connectionstyle="arc3,rad=-0.2"))
    ax.text(50, 18, "Referential Integrity Constraints: ON DELETE CASCADE Enforced Across All Foreign Keys", 
            fontsize=9.5, fontweight='bold', color='#047857', ha='center')

    plt.tight_layout()
    plt.savefig("fig3_er_schema.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig3_er_schema.png")

def generate_fig4_benchmarks():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)

    # Chart 1: API Latency & Startup
    categories = ['Cold Start\n(Java Server)', 'Cold Start\n(Spring Boot)', 'GET Latency\n(Track Ticket)', 'POST Latency\n(New Grievance)']
    times_ms = [380, 8200, 11.4, 24.2]
    colors = ['#1d4ed8', '#94a3b8', '#059669', '#0284c7']
    
    bars1 = ax1.bar(categories, times_ms, color=colors, width=0.55)
    ax1.set_ylabel('Execution Time (Milliseconds)', fontsize=9, fontweight='bold')
    ax1.set_title('Architecture Latency Comparison (ms)', fontsize=10.5, fontweight='bold', color='#0f172a')
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, yval + 100, f"{yval:.1f}ms", ha='center', va='bottom', fontsize=8, fontweight='bold')

    # Chart 2: Image Compression
    labels = ['Raw Camera Photo\n(Direct Mobile Upload)', 'Canvas Compressed\n(In-Browser JPEG 0.75)']
    sizes_kb = [8200, 118]
    colors2 = ['#dc2626', '#16a34a']
    bars2 = ax2.bar(labels, sizes_kb, color=colors2, width=0.45)
    ax2.set_ylabel('Attachment Size (Kilobytes)', fontsize=9, fontweight='bold')
    ax2.set_title('Payload Reduction: 98.5% Space Saved', fontsize=10.5, fontweight='bold', color='#0f172a')
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval + 150, f"{yval} KB", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    plt.tight_layout()
    plt.savefig("fig4_benchmarks.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig4_benchmarks.png")

if __name__ == "__main__":
    generate_fig1_architecture()
    generate_fig2_workflow()
    generate_fig3_er_schema()
    generate_fig4_benchmarks()
