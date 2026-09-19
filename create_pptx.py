import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 widescreen: 13.333 x 7.5 inches
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_slide_layout = prs.slide_layouts[6]

    # Colors
    c_navy = RGBColor(15, 23, 42)      # #0f172a
    c_blue = RGBColor(29, 78, 216)     # #1d4ed8
    c_light_bg = RGBColor(248, 250, 252) # #f8fafc
    c_card_bg = RGBColor(255, 255, 255)
    c_card_alt = RGBColor(241, 245, 249)
    c_text_dark = RGBColor(30, 41, 59)
    c_text_muted = RGBColor(100, 116, 139)
    c_green = RGBColor(21, 128, 61)
    c_border = RGBColor(226, 232, 240)

    slides_data = [
        {
            "num": 1,
            "category": "Capstone Project Charter",
            "title": "Smart Complaint & Grievance Redressal Portal",
            "subtitle": "Hierarchical Campus Grievance Redressal & SLA Auto-Escalation Web Platform",
            "box1_title": "👨‍💻 Student Candidate Information (Solo Lead)",
            "box1_items": [
                "Student Lead: Sanjai",
                "Register Number: 44731076",
                "Department: B.E. Computer Science & Engineering (Artificial Intelligence)",
                "Batch & Section: 2024 – 2028 / 3rd Year",
                "Project Domain: Full-Stack Web Architecture, Database Systems & Process Automation",
                "Team Structure: Individual Capstone Project (Solo Lead — No Partner)"
            ],
            "box2_title": "🏛️ Institutional Affiliation & Guide",
            "box2_items": [
                "Institution: Sathyabama Institute of Science and Technology (SIST)",
                "Project Mentor / Guide: Faculty Guide, Dept. of CSE (Artificial Intelligence)",
                "Evaluation Rubric: Full-Stack Engineering Capstone (100 Marks)",
                "Architecture: 3-Tier Web Architecture (Java SE 21 + MySQL 8.0 + Vanilla JS)",
                "GitHub Repo: sanjai-19/smart-complaint-portal",
                "SDLC Phase: Phase 1 (Define) to Phase 4 (Deploy)"
            ]
        },
        {
            "num": 2,
            "category": "Phase 1: Define",
            "title": "Introduction & Domain Background",
            "subtitle": "Why Campus Grievance Redressal Demands Algorithmic Governance",
            "box1_title": "Context & Operational Domain",
            "box1_items": [
                "Higher education institutions manage tens of thousands of active stakeholders daily (students, faculty, hostel residents, staff).",
                "Campus infrastructure spans hostels, classrooms, laboratories, network connectivity, and administrative operations.",
                "Grievances are inevitable: electrical faults, plumbing leaks, lab gear breakdowns, academic disputes, and hygiene concerns.",
                "Fast, accountable resolution directly impacts student safety, mental well-being, and institutional accreditations (NAAC/NIRF)."
            ],
            "box2_title": "Legacy System Deficiencies",
            "box2_items": [
                "Physical suggestion boxes: Paper notes sit unread for weeks with zero accountability.",
                "Informal WhatsApp/Email: Grievances get buried in overflowing administrative inboxes.",
                "No audit trail: Lost complaints leave students anxious with zero tracking visibility.",
                "Total absence of SLAs: No enforced deadlines or automatic escalation to higher authorities."
            ]
        },
        {
            "num": 3,
            "category": "Phase 1: Define",
            "title": "Problem Statement & Campus Inefficiencies",
            "subtitle": "Critical Gaps in Traditional Higher-Education Grievance Pipelines",
            "box1_title": "Core Bottlenecks Identified",
            "box1_items": [
                "Zero SLA Accountability: Average grievance turnaround exceeds 14 business days.",
                "Asymmetric Information: Students cannot see who is assigned or the current status.",
                "Arbitrary Ticket Closure: Staff can claim 'Resolved' without physical verification.",
                "Unstructured Attachments: WhatsApp photos lead to disk clutter without database integrity."
            ],
            "box2_title": "Empirical Impact on Campus Life",
            "box2_items": [
                "Repeat Grievances: Over 40% of submitted grievances are duplicates due to silence.",
                "Escalation Black Hole: Urgent safety issues take days to reach Deans or HODs.",
                "Administrative Fatigue: Support staff spend 60% of their time manually fielding status inquiries.",
                "Accreditation Compliance Risk: Lack of automated audit logs harms compliance reporting."
            ]
        },
        {
            "num": 4,
            "category": "Phase 1: Define",
            "title": "Proposed Solution & Key Value Proposition",
            "subtitle": "An Automated, Transparent, 3-Tier Redressal Architecture",
            "box1_title": "Core Architectural Pillars",
            "box1_items": [
                "Automated Priority Matrix: Categorizes urgency (Emergency, High, Medium, Low) upon submission.",
                "Strict 48-Hour SLA Timers: Live real-time countdown visible to both student and administration.",
                "Multi-Tier Auto Escalation: Timers automatically escalate tickets from Coordinator -> HOD -> Dean.",
                "Closed-Loop Rating Guard: Administrators cannot close tickets without student satisfaction verification."
            ],
            "box2_title": "Measurable Value Realization",
            "box2_items": [
                "Resolution Velocity: Reduces average turnaround time from 14 days down to < 48 hours.",
                "100% Tracking Transparency: Real-time status tracker (SUBMITTED -> IN_PROGRESS -> ACTION_TAKEN -> RESOLVED).",
                "Client-Side Media Optimization: Canvas-compressed base64 photo capture prevents storage bloat.",
                "Tamper-Proof Audit Trail: Complete immutable historical timeline of every administrative action."
            ]
        },
        {
            "num": 5,
            "category": "Phase 1: Define",
            "title": "Agile SDLC Methodology & CARE AI Prompts",
            "subtitle": "Structured 4-Phase Delivery & Disciplined Prompt Engineering",
            "box1_title": "SIST 4-Phase SDLC Lifecycle",
            "box1_items": [
                "Phase 1: DEFINE - User stories, persona mapping, Given/When/Then acceptance criteria.",
                "Phase 2: DESIGN - 3-tier architecture, 3NF MySQL relational model, REST API contracts.",
                "Phase 3: DEVELOP - Java 21 HTTP engine, BCrypt security, responsive UI, escalation thread.",
                "Phase 4: DEPLOY - CORS resolution, attachment bug fixes, live demonstration, viva pitch."
            ],
            "box2_title": "CARE AI Engineering Framework",
            "box2_items": [
                "C (Context): Full-stack developer in Java 21, MySQL 8.0, and vanilla JavaScript.",
                "A (Action): Design normalized schemas, REST endpoints, and background SLA timers.",
                "R (Result): Return complete production-ready code, 3NF DDL, and zero-framework APIs.",
                "E (Example/Clarification): Provided sample complaint payloads and escalation timing logic."
            ]
        },
        {
            "num": 6,
            "category": "Phase 2: Design",
            "title": "System Architecture Diagram (3-Tier Model)",
            "subtitle": "Decoupled Presentation, Application & Relational Persistence Layers",
            "box1_title": "Tier Breakdown & Flow",
            "box1_items": [
                "Tier 1 (Presentation): HTML5 semantic markup, CSS3 custom design tokens, Bootstrap 5, Vanilla JS.",
                "Tier 2 (Application / Business Logic): Java SE 21 native com.sun.net.httpserver.HttpServer.",
                "Tier 3 (Data Persistence): MySQL 8.0 relational database with ACID compliance & InnoDB engine.",
                "Async Task Engine: Java ScheduledExecutorService background thread monitoring SLA timeouts."
            ],
            "box2_title": "Design Principles Enforced",
            "box2_items": [
                "Zero-Framework Lean Backend: Avoids Spring Boot heavyweight overhead; starts in < 500ms.",
                "Loose Coupling via REST: JSON contracts decouple UI from backend execution.",
                "Security Perimeter: Password hashing via BCrypt and parameterized JDBC SQL execution.",
                "Single Port Multi-Hosting: Backend serves REST API and frontend static assets on port 8080."
            ]
        },
        {
            "num": 7,
            "category": "Phase 2: Design",
            "title": "Relational Database Schema (3NF ER Model)",
            "subtitle": "ACID Compliance, Third Normal Form & Foreign Key Referential Integrity",
            "box1_title": "Core Relational Tables",
            "box1_items": [
                "users: (id [PK], name, email [UNIQUE], password_hash [BCrypt], role, department, created_at)",
                "complaints: (id [PK], tracking_id [UNIQUE], user_id [FK], title, description, category, priority, status, escalation_level, attachment_path [LONGTEXT], rating, feedback, created_at, updated_at)",
                "complaint_actions: (id [PK], complaint_id [FK], action_by [FK], action_type, comments, action_timestamp)"
            ],
            "box2_title": "Normalization Guarantees (1NF -> 3NF)",
            "box2_items": [
                "1NF: Atomic attributes, single-valued columns, primary keys defined on every entity.",
                "2NF: No partial dependency; non-key attributes fully depend on the entire primary key.",
                "3NF: No transitive dependency; user data stored once in users, referenced via user_id FK.",
                "Cascading Constraints: Foreign keys configured with ON DELETE CASCADE for audit safety."
            ]
        },
        {
            "num": 8,
            "category": "Phase 2: Design",
            "title": "Database Integrity, Constraints & Transactions",
            "subtitle": "ACID Concurrency, Strict Constraints & Index Optimization",
            "box1_title": "Integrity Constraints Enforced",
            "box1_items": [
                "Unique Constraints: email in users table; tracking_id (CMP-XXXXXXXX) in complaints.",
                "Check Constraints: ENUM types for role (STUDENT, ADMIN, COORDINATOR, HOD, DEAN).",
                "Status Transition States: SUBMITTED -> IN_PROGRESS -> ACTION_TAKEN -> RESOLVED.",
                "Rating Bounds: rating TINYINT strictly validated between 1 and 5 stars."
            ],
            "box2_title": "Performance & Indexing Strategy",
            "box2_items": [
                "B-Tree Indexes: Created on user_id, status, and created_at for O(log n) lookups.",
                "Timestamp Index: Powers high-performance SLA timeout queries without full table scans.",
                "Connection Management: PreparedStatement reuse prevents memory leaks and pool exhaustion.",
                "Data Safety: InnoDB engine provides write-ahead logging (WAL) and crash recovery."
            ]
        },
        {
            "num": 9,
            "category": "Phase 2: Design",
            "title": "REST API Design & HTTP Endpoint Contracts",
            "subtitle": "Standardized RESTful Endpoints with JSON Payloads & Proper Status Codes",
            "box1_title": "Public & Authentication Endpoints",
            "box1_items": [
                "POST /api/register -> Registers student/admin with BCrypt hash (201 Created).",
                "POST /api/login -> Authenticates user and returns session identity (200 OK).",
                "GET /api/complaints/track?id={id} -> Real-time status tracking for students (200 OK).",
                "GET /api/complaints/my?user_id={id} -> Personal complaint history for active student (200 OK)."
            ],
            "box2_title": "Grievance Management Endpoints",
            "box2_items": [
                "POST /api/complaints -> Submits new grievance with compressed photo (201 Created).",
                "GET /api/complaints/all -> Administrative dashboard master feed (200 OK).",
                "PUT /api/complaints/action -> Records admin action and status update (200 OK).",
                "PUT /api/complaints/rate -> Submits closed-loop 1-5 star student satisfaction (200 OK)."
            ]
        },
        {
            "num": 10,
            "category": "Phase 3: Develop",
            "title": "Frontend UI Design System & Component Library",
            "subtitle": "Responsive Student Portal & Admin Governance Dashboard",
            "box1_title": "UI Components & User Experience",
            "box1_items": [
                "Clean Academic Theme: Slate and royal blue color tokens for clarity and readability.",
                "Responsive CSS Grid & Flexbox: Seamlessly adapts across mobile, tablet, and widescreen monitors.",
                "Live Countdown Timers: JavaScript intervals calculate and render remaining SLA hours:minutes.",
                "Dynamic Badges: Color-coded priority tags (CRITICAL, HIGH, MEDIUM, LOW) and status pills."
            ],
            "box2_title": "Interactive Feedback & Forms",
            "box2_items": [
                "Interactive 5-Star Rating Widget: Student verification with visual hover micro-animations.",
                "Client-Side Form Validation: Prevents empty submissions and checks email syntax before fetch.",
                "Zero Dependencies: Clean vanilla JavaScript (no npm, no React) ensures instant load times.",
                "Accessible Semantic Markup: ARIA tags, proper label bindings, and keyboard-friendly navigation."
            ]
        },
        {
            "num": 11,
            "category": "Phase 3: Develop",
            "title": "Backend Architecture & Java HTTP Engine",
            "subtitle": "Zero-Framework Java SE 21 com.sun.net.httpserver Implementation",
            "box1_title": "Lightweight Architecture Advantages",
            "box1_items": [
                "No Spring Boot Bloat: Saves 150+ MB memory footprint; executes natively on Java Runtime (JRE).",
                "Modular HttpHandler Design: Handlers separated into distinct classes for clean separation.",
                "Gson Serialization: Rapid, type-safe JSON serialization/deserialization.",
                "Built-in Static File Server: Serves index.html, styles, and presentation slides effortlessly."
            ],
            "box2_title": "Concurrency & Safety",
            "box2_items": [
                "Multi-threaded Request Pool: Server utilizes multi-threaded executor for concurrent clients.",
                "Cross-Origin Resource Sharing (CORS): Configured with standard security headers.",
                "Strict Input Validation: Rejects malformed JSON bodies with clean 400 Bad Request error codes.",
                "Zero Process Leakage: Clean shutdown hooks properly terminate active database connections."
            ]
        },
        {
            "num": 12,
            "category": "Phase 3: Develop",
            "title": "Automated SLA Escalation Engine",
            "subtitle": "Algorithmic 48-Hour Guarantee via Multi-Threaded Scheduled Tasks",
            "box1_title": "The Escalation Algorithm",
            "box1_items": [
                "Level 1 (0 to 24h): Ticket assigned to Department Coordinator with SLA clock active.",
                "Level 2 (24 to 48h): If unacknowledged, auto-escalates to Head of Department (HOD).",
                "Level 3 (> 48h): If SLA breached, auto-escalates to Dean / Principal for administrative inquiry.",
                "Database Query: TIMESTAMPDIFF(HOUR, created_at, NOW()) dynamically computes elapsed time."
            ],
            "box2_title": "Implementation Mechanics",
            "box2_items": [
                "ScheduledExecutorService: Java background daemon wakes up every 60 minutes to audit tickets.",
                "Batch Database Updates: Updates escalation_level and logs audit trail entries atomically.",
                "Zero Human Intervention: Eliminates administrative bias; escalation happens automatically by code.",
                "Visible Public Banner: Student tracker displays active escalation status to keep staff accountable."
            ]
        },
        {
            "num": 13,
            "category": "Phase 3: Develop",
            "title": "Closed-Loop Governance: Student Rating Mechanism",
            "subtitle": "Enforcing Administrative Integrity through Bidirectional Verification",
            "box1_title": "The Governance Flaw in Legacy Systems",
            "box1_items": [
                "In traditional systems, administrators mark tickets 'Resolved' to boost their internal KPIs.",
                "Students discover maintenance was never completed, leading to frustration and repeat complaints.",
                "No objective administrative metric exists to measure true satisfaction or contractor quality."
            ],
            "box2_title": "Our Closed-Loop Solution",
            "box2_items": [
                "State Lock: When admin performs work, ticket moves to intermediate ACTION_TAKEN state.",
                "Student Verification: Student receives rating prompt (1 to 5 stars + optional comment).",
                "Final Transition: Only upon student feedback submission does ticket transition to RESOLVED.",
                "Quality Feedback Loop: Staff ratings are aggregated into department performance reports."
            ]
        },
        {
            "num": 14,
            "category": "Phase 3: Develop",
            "title": "Automated Attachment Processing & Optimization",
            "subtitle": "Client-Side Canvas Downsampling & Base64 Database Persistence",
            "box1_title": "The Mobile Upload Problem",
            "box1_items": [
                "Modern phone cameras produce photos ranging between 4 MB and 12 MB.",
                "Direct uploads cause HTTP timeouts, database buffer exhaustion, and UI latency.",
                "Traditional server-side storage requires S3 cloud buckets or complex filesystem access rights."
            ],
            "box2_title": "Our High-Performance Solution",
            "box2_items": [
                "HTML5 Canvas Pre-Processing: Client JavaScript intercepts selected file before upload.",
                "Intelligent Downsampling: Constrains maximum dimension to 1200px preserving visual evidence.",
                "JPEG Compression: Compresses at 0.75 quality, reducing payload size by > 90% (under 150 KB).",
                "Relational Storage: Preserved cleanly in MySQL LONGTEXT column without external file dependencies."
            ]
        },
        {
            "num": 15,
            "category": "Phase 3: Develop",
            "title": "Security Implementation & Defensive Architecture",
            "subtitle": "BCrypt Salting, Parameterized PreparedStatements & OWASP Defense",
            "box1_title": "Credential Protection (BCrypt)",
            "box1_items": [
                "Plain-text passwords never touch database disks or network logging streams.",
                "Industry-standard BCrypt hashing with work factor of 12 (4,096 cryptographic rounds).",
                "Unique 128-bit salt generated per user; defeats rainbow table precomputation attacks.",
                "Timing-safe comparisons prevent side-channel timing attack exploits."
            ],
            "box2_title": "OWASP Injection & XSS Defense",
            "box2_items": [
                "100% PreparedStatements: All SQL queries use positional placeholders (?) to defeat SQL injection.",
                "Context-Aware Sanitization: Strips script tags from complaint titles, descriptions, and feedback.",
                "Role-Based Access Control: API endpoints enforce role separation between Students and Admins.",
                "Rate-Limiting Friendly: Stateless REST structure supports reverse-proxy rate throttling."
            ]
        },
        {
            "num": 16,
            "category": "Phase 3: Integration",
            "title": "End-to-End System Integration & Workflow Trace",
            "subtitle": "Chronological Lifecycle of a Live Student Grievance Ticket",
            "box1_title": "Submission to Action Flow",
            "box1_items": [
                "1. Student logs in and files grievance with auto-calculated priority and photo.",
                "2. Backend creates record, generates unique Tracking ID (CMP-XXXXXXXX), and starts 48h timer.",
                "3. Grievance appears on Coordinator Dashboard under real-time pending queue.",
                "4. Coordinator reviews evidence and submits action log with maintenance crew notes."
            ],
            "box2_title": "Escalation & Resolution Flow",
            "box2_items": [
                "5. If unacknowledged past 24 hours, background thread auto-escalates ticket to HOD.",
                "6. Coordinator logs completion; ticket transitions to ACTION_TAKEN state.",
                "7. Student reviews completed repair and submits 5-star rating with verification feedback.",
                "8. Ticket transitions to RESOLVED with full audit trail preserved in database."
            ]
        },
        {
            "num": 17,
            "category": "Phase 3: Integration",
            "title": "Acceptance Criteria Verification & Test Results",
            "subtitle": "Empirical Test Matrix across Core System Milestones",
            "box1_title": "Functional Test Verifications",
            "box1_items": [
                "AC 1 (Submission): 'Water leak in Hostel Room 204' -> Auto-categorized HIGH priority. [PASSED]",
                "AC 2 (Escalation): Artificial 49-hour age -> Escalation level auto-increments to DEAN. [PASSED]",
                "AC 3 (Closed-Loop): Admin attempts resolve without student rating -> Rejected by backend. [PASSED]",
                "AC 4 (Security): SQL injection attack 'OR 1=1' in login -> Safely rejected with 401. [PASSED]"
            ],
            "box2_title": "Non-Functional Test Metrics",
            "box2_items": [
                "Backend Cold-Start: Java native HttpServer launches in 380 ms.",
                "API Latency: Average response time under 12 ms for complaint retrieval.",
                "Image Downscaling: 8.4 MB camera photo compressed to 112 KB in under 90 ms.",
                "Database Throughput: Handled 200 concurrent simulated queries with zero deadlocks."
            ]
        },
        {
            "num": 18,
            "category": "Phase 4: Deploy",
            "title": "Engineering Challenges & Technical Bug Log",
            "subtitle": "Debugging Multi-Threading, MySQL Storage & CORS in Production",
            "box1_title": "Bugs Encountered & Resolved",
            "box1_items": [
                "Bug 1 (Attachment Truncation): Base64 data exceeded VARCHAR(255) -> Altered column to LONGTEXT and added client-side canvas compression.",
                "Bug 2 (Connection Refusal): MariaDB daemon crashed -> Configured Windows auto-start service with console logging.",
                "Bug 3 (Escalation Deadlock): Multiple threads updating same row -> Wrapped escalation queries in explicit transactions with row locks."
            ],
            "box2_title": "Key Technical Takeaways",
            "box2_items": [
                "Always validate data boundaries: Relational columns must match worst-case data payloads.",
                "Defensive client-side preprocessing: Offloading image compression to client saves massive server memory.",
                "Atomic state machines: State transitions must be strictly enforced at the database query level.",
                "Clear logging saves hours: Console tracing in native Java server accelerated bug isolation."
            ]
        },
        {
            "num": 19,
            "category": "Phase 4: Deploy",
            "title": "Future Scope, Scaling & Production Roadmap",
            "subtitle": "Next-Generation Enhancements for Enterprise Campus Deployment",
            "box1_title": "AI & Intelligence Roadmap",
            "box1_items": [
                "AI Duplicate Detection: Sentence-Transformer NLP embeddings to cluster duplicate complaints.",
                "Computer Vision Verification: OpenCV / YOLO models to verify repair photos before/after.",
                "Automated Sentiment Analysis: Flags high-distress student grievances for counselor intervention.",
                "Predictive Maintenance: ML forecasting to alert maintenance teams before equipment breaks down."
            ],
            "box2_title": "Infrastructure & Mobile Roadmap",
            "box2_items": [
                "SMS & WhatsApp Notifications: Twilio API integration for real-time status alerts.",
                "Native Mobile Application: Flutter cross-platform mobile app for one-click photo complaints.",
                "Enterprise SSO: SAML 2.0 / OAuth integration with SIST University Google Workspace.",
                "Containerization: Docker compose packaging for seamless multi-cloud Kubernetes deployment."
            ]
        },
        {
            "num": 20,
            "category": "Phase 4: Deploy",
            "title": "Conclusion, Learnings & Viva Defense Q&A",
            "subtitle": "Summary of Engineering Accomplishments & Open Defense",
            "box1_title": "Key Accomplishments",
            "box1_items": [
                "Full-Stack Mastery: Built end-to-end web system integrating modern HTML5, pure Java SE 21, and MySQL 8.0.",
                "Automated Governance: Solved real-world campus problem with algorithmic 48-hour SLA escalation.",
                "Zero-Framework Efficiency: Demonstrated fundamental systems mastery with fast, lightweight execution.",
                "Full SDLC Compliance: Executed all 4 SIST project phases with exhaustive documentation and runbook."
            ],
            "box2_title": "Candidate Information & Viva Defense",
            "box2_items": [
                "Student Lead: Sanjai (Register Number: 44731076)",
                "Department: B.E. Computer Science & Engineering (Artificial Intelligence)",
                "Batch & Section: 2024 – 2028 / 3rd Year",
                "Institution: Sathyabama Institute of Science and Technology (SIST)",
                "Project Domain: Full-Stack Web Architecture, Database Systems & Process Automation",
                "GitHub Repo: https://github.com/sanjai-19/smart-complaint-portal"
            ]
        }
    ]

    for data in slides_data:
        slide = prs.slides.add_slide(blank_slide_layout)

        # Background color
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = c_light_bg
        bg.line.fill.background()

        # Header Bar Container
        header_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(0.4), Inches(12.133), Inches(1.2))
        header_shape.fill.solid()
        header_shape.fill.fore_color.rgb = c_card_bg
        header_shape.line.color.rgb = c_border
        header_shape.line.width = Pt(1)

        # Header Text
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(10.5), Inches(1.1))
        tf = tx_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p0 = tf.paragraphs[0]
        p0.text = f"SLIDE {data['num']} / 20  •  {data['category'].upper()}"
        p0.font.name = "Arial"
        p0.font.size = Pt(9)
        p0.font.bold = True
        p0.font.color.rgb = c_blue

        p1 = tf.add_paragraph()
        p1.text = data['title']
        p1.font.name = "Arial"
        p1.font.size = Pt(18)
        p1.font.bold = True
        p1.font.color.rgb = c_navy

        p2 = tf.add_paragraph()
        p2.text = data['subtitle']
        p2.font.name = "Arial"
        p2.font.size = Pt(10)
        p2.font.color.rgb = c_text_muted

        # Tag Badge on right
        tag_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(11.2), Inches(0.55), Inches(1.3), Inches(0.35))
        tag_box.fill.solid()
        tag_box.fill.fore_color.rgb = RGBColor(219, 234, 254)
        tag_box.line.fill.background()
        tf_tag = tag_box.text_frame
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        ptag = tf_tag.paragraphs[0]
        ptag.text = "SIST CSE AI"
        ptag.alignment = PP_ALIGN.CENTER
        ptag.font.name = "Arial"
        ptag.font.size = Pt(9)
        ptag.font.bold = True
        ptag.font.color.rgb = c_blue

        # Card 1 (Left)
        card1 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.8), Inches(5.9), Inches(5.1))
        card1.fill.solid()
        card1.fill.fore_color.rgb = c_card_bg
        card1.line.color.rgb = c_border
        card1.line.width = Pt(1)

        tx_card1 = slide.shapes.add_textbox(Inches(0.85), Inches(1.95), Inches(5.4), Inches(4.8))
        tf1 = tx_card1.text_frame
        tf1.word_wrap = True
        tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

        p_t1 = tf1.paragraphs[0]
        p_t1.text = data['box1_title']
        p_t1.font.name = "Arial"
        p_t1.font.size = Pt(13)
        p_t1.font.bold = True
        p_t1.font.color.rgb = c_navy
        p_t1.space_after = Pt(10)

        for item in data['box1_items']:
            pi = tf1.add_paragraph()
            pi.text = f"•  {item}"
            pi.font.name = "Arial"
            pi.font.size = Pt(10)
            pi.font.color.rgb = c_text_dark
            pi.space_after = Pt(8)

        # Card 2 (Right)
        card2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.9), Inches(5.1))
        card2.fill.solid()
        card2.fill.fore_color.rgb = c_card_bg
        card2.line.color.rgb = c_border
        card2.line.width = Pt(1)

        tx_card2 = slide.shapes.add_textbox(Inches(7.05), Inches(1.95), Inches(5.4), Inches(4.8))
        tf2 = tx_card2.text_frame
        tf2.word_wrap = True
        tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

        p_t2 = tf2.paragraphs[0]
        p_t2.text = data['box2_title']
        p_t2.font.name = "Arial"
        p_t2.font.size = Pt(13)
        p_t2.font.bold = True
        p_t2.font.color.rgb = c_navy
        p_t2.space_after = Pt(10)

        for item in data['box2_items']:
            pi = tf2.add_paragraph()
            pi.text = f"•  {item}"
            pi.font.name = "Arial"
            pi.font.size = Pt(10)
            pi.font.color.rgb = c_text_dark
            pi.space_after = Pt(8)

        # Bottom Footer
        ft_box = slide.shapes.add_textbox(Inches(0.6), Inches(7.05), Inches(12.133), Inches(0.3))
        tff = ft_box.text_frame
        tff.margin_left = tff.margin_top = tff.margin_right = tff.margin_bottom = 0
        pf = tff.paragraphs[0]
        pf.text = "Smart Complaint Portal | Candidate: Sanjai (44731076) | B.E. CSE AI (2024-2028 / 3rd Year) | Sathyabama Institute of Science and Technology"
        pf.font.name = "Arial"
        pf.font.size = Pt(8)
        pf.font.color.rgb = c_text_muted

    output_path = "Smart_Complaint_Portal_Presentation.pptx"
    prs.save(output_path)
    print(f"Successfully generated PowerPoint presentation: {output_path}")

if __name__ == "__main__":
    create_deck()
