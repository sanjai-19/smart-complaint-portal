import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def update_review_ppt():
    print("Opening Review PPT Format san.pptx...")
    prs = Presentation("Review PPT Format san.pptx")

    # Helper to set text cleanly
    def set_shape_text(shape, text, font_size=None, bold=None, color=None):
        if not shape.has_text_frame:
            return
        tf = shape.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = text
        if font_size:
            r.font.size = Pt(font_size)
        if bold is not None:
            r.font.bold = bold
        if color:
            r.font.color.rgb = color

    # Helper to replace text in paragraphs preserving other formatting
    def replace_text_in_shape(shape, old_str, new_str):
        if not shape.has_text_frame:
            return
        for p in shape.text_frame.paragraphs:
            if old_str.lower() in p.text.lower():
                p.text = p.text.replace(old_str, new_str)

    # -------------------------------------------------------------
    # SLIDE 1: TITLE SLIDE
    # -------------------------------------------------------------
    s1 = prs.slides[0]
    for shape in s1.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                if "Pattan Abdul Kalam" in p.text or "Reg.No." in p.text:
                    p.text = "1. H Sanjai [ Reg.No. : 44731076 ] (Solo Lead)"
                elif "PROJECT TITLE" in p.text:
                    p.text = "SMART COMPLAINT & GRIEVANCE REDRESSAL PORTAL\n(Hierarchical Campus Grievance Redressal & SLA Auto-Escalation Web Platform)"
                    p.font.size = Pt(18)
                    p.font.bold = True
                elif "Dr. R. Sathya Bama" in p.text:
                    p.text = "Ms. R. Shanumgaa Priya, M.E."
                elif "Department of Computer Science" in p.text:
                    p.text = "Department of Computer Science and Engineering (Artificial Intelligence)"

    # -------------------------------------------------------------
    # SLIDE 2: PRESENTATION OUTLINE
    # -------------------------------------------------------------
    s2 = prs.slides[1]
    for shape in s2.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                if "Department of Computer Science" in p.text:
                    p.text = "Department of Computer Science and Engineering (Artificial Intelligence)"

    # -------------------------------------------------------------
    # SLIDE 3: COURSE CERTIFICATE
    # -------------------------------------------------------------
    s3 = prs.slides[2]
    # Add a clean summary text box for Course Certificate
    tx_box3 = s3.shapes.add_textbox(Inches(1.5), Inches(2.2), Inches(10.3), Inches(4.5))
    tf3 = tx_box3.text_frame
    tf3.word_wrap = True
    p3_1 = tf3.paragraphs[0]
    p3_1.text = "PROFESSIONAL TRAINING / CAPSTONE SPECIALIZATION"
    p3_1.font.bold = True
    p3_1.font.size = Pt(16)
    p3_1.font.color.rgb = RGBColor(29, 78, 216)

    p3_2 = tf3.add_paragraph()
    p3_2.text = (
        "• Domain: Full-Stack Web Architecture, Database Systems & Process Automation\n"
        "• Core Competencies Mastered: Native Java SE 21 HttpServer, MySQL 3NF Normalization, REST API Engineering, Cryptographic Security (BCrypt), and Real-Time SLA Scheduling\n"
        "• Candidate: H Sanjai (Register Number: 44731076)\n"
        "• Institution: Sathyabama Institute of Science and Technology (SIST)\n"
        "• Status: 100% Completed with Functional Prototype, Full Unit Tests, and Public GitHub Repository"
    )
    p3_2.font.size = Pt(14)
    p3_2.space_before = Pt(14)

    # -------------------------------------------------------------
    # SLIDE 4: ABSTRACT
    # -------------------------------------------------------------
    s4 = prs.slides[3]
    for shape in s4.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                if "Diabetes" in p.text or "Random Forest" in p.text:
                    p.text = ""
            if "Diabetes" in shape.text_frame.text or "insulin" in shape.text_frame.text or len(shape.text_frame.paragraphs) > 2:
                shape.text_frame.clear()
                p = shape.text_frame.paragraphs[0]
                p.text = (
                    "• In campus environments, grievance management is heavily fragmented across physical boxes, unmonitored WhatsApp messages, and email chains, leading to lost complaints and zero accountability.\n\n"
                    "• The Smart Complaint Portal is an enterprise 3-tier web platform engineered in pure Java SE 21, MySQL 8.0, and responsive Bootstrap 5.\n\n"
                    "• Features: (1) Automated Priority Routing, (2) Real-Time 48-Hour SLA Countdown Timers, (3) Autonomous Multi-Tier Escalation (Coordinator -> HOD -> Dean), and (4) Anti-Bypass Closed-Loop Student Rating Verification Lock.\n\n"
                    "• Zero-Framework Efficiency: Sub-400ms startup latency and 98.5% payload compression via client-side canvas downsampling."
                )
                p.font.size = Pt(13)

    # -------------------------------------------------------------
    # SLIDE 5: OBJECTIVES
    # -------------------------------------------------------------
    s5 = prs.slides[4]
    for shape in s5.shapes:
        if shape.has_text_frame and ("To develop a system" in shape.text_frame.text or "diagnostic dataset" in shape.text_frame.text):
            shape.text_frame.clear()
            p = shape.text_frame.paragraphs[0]
            p.text = (
                "1. Rapid Filing: Enable students to file categorized grievances with photos in under 60 seconds.\n\n"
                "2. Zero-Framework Backend: Engineer a lean Java SE 21 HttpServer on port 8080 with sub-second startup.\n\n"
                "3. 48-Hour SLA Guarantee: Enforce automated countdown timers with ScheduledExecutorService auto-escalation.\n\n"
                "4. 3NF Relational Integrity: Model MySQL database in 3NF with foreign keys and PreparedStatement security.\n\n"
                "5. Closed-Loop Student Rating: Prevent ticket resolution until complainant validates repairs (1-5 stars).\n\n"
                "6. Client-Side Image Compression: Reduce mobile camera photos from 8 MB to <120 KB via HTML5 canvas."
            )
            p.font.size = Pt(13)

    # -------------------------------------------------------------
    # SLIDE 6: SYSTEM ARCHITECTURE
    # -------------------------------------------------------------
    s6 = prs.slides[5]
    if os.path.exists("fig1_architecture.png"):
        s6.shapes.add_picture("fig1_architecture.png", Inches(1.8), Inches(1.8), width=Inches(9.5))

    # -------------------------------------------------------------
    # SLIDE 7: HARDWARE AND SOFTWARE REQUIREMENTS
    # -------------------------------------------------------------
    s7 = prs.slides[6]
    for shape in s7.shapes:
        if shape.has_text_frame and ("Jupyter Notebook" in shape.text_frame.text or "Pandas" in shape.text_frame.text):
            shape.text_frame.clear()
            p = shape.text_frame.paragraphs[0]
            p.text = (
                "SOFTWARE REQUIREMENTS:\n"
                "• Operating System: Windows 11 / Linux Ubuntu 22.04 LTS\n"
                "• Runtime & Language: Java SE Development Kit (JDK 21 LTS)\n"
                "• Database: MySQL Server 8.0 / MariaDB 10.4 (InnoDB Engine, ACID)\n"
                "• Web Stack: Semantic HTML5, CSS3, ES6+ JavaScript, Bootstrap 5.3.3\n"
                "• Libraries: com.google.code.gson (JSON), org.mindrot:jbcrypt (Security)\n"
                "• Tooling: Apache Maven 3.9, Postman REST Client, IntelliJ IDEA\n\n"
                "HARDWARE REQUIREMENTS:\n"
                "• Processor: Intel Core i5 / AMD Ryzen 5 (2.5 GHz+, 6 Cores)\n"
                "• Memory: 16 GB DDR4 RAM | Storage: 512 GB NVMe SSD\n"
                "• Network: Gigabit Ethernet / Wi-Fi | Client: Any modern mobile/PC browser"
            )
            p.font.size = Pt(11.5)

    # -------------------------------------------------------------
    # SLIDE 8: 3NF DATABASE SCHEMA (Renamed from DATASET DESCRIPTION)
    # -------------------------------------------------------------
    s8 = prs.slides[7]
    for shape in s8.shapes:
        if shape.has_text_frame:
            if "DATASET DESCRIPTION" in shape.text_frame.text:
                shape.text_frame.text = "RELATIONAL DATABASE SCHEMA (3NF)"
                shape.text_frame.paragraphs[0].font.size = Pt(20)
                shape.text_frame.paragraphs[0].font.bold = True
            elif "GetData" in shape.text_frame.text or "DataCleaning" in shape.text_frame.text:
                shape.text_frame.clear()
    if os.path.exists("fig3_er_schema.png"):
        s8.shapes.add_picture("fig3_er_schema.png", Inches(1.8), Inches(1.8), width=Inches(9.5))

    # -------------------------------------------------------------
    # SLIDE 9: PROCESS AUTOMATION & ESCALATION (Renamed from CLASSIFICATION ALGORITHM)
    # -------------------------------------------------------------
    s9 = prs.slides[8]
    for shape in s9.shapes:
        if shape.has_text_frame:
            if "CLASSIFICATION ALGORTIHM" in shape.text_frame.text or "CLASSIFICATION" in shape.text_frame.text:
                shape.text_frame.text = "PROCESS AUTOMATION & SLA ESCALATION ENGINE"
                shape.text_frame.paragraphs[0].font.size = Pt(20)
                shape.text_frame.paragraphs[0].font.bold = True
            elif "random forest" in shape.text_frame.text.lower() or "sklearn" in shape.text_frame.text.lower():
                shape.text_frame.clear()
    if os.path.exists("fig2_workflow.png"):
        s9.shapes.add_picture("fig2_workflow.png", Inches(1.8), Inches(1.8), width=Inches(9.5))

    # -------------------------------------------------------------
    # SLIDE 10: RESULTS AND DISCUSSION (Functional Verification)
    # -------------------------------------------------------------
    s10 = prs.slides[9]
    for shape in s10.shapes:
        if shape.has_text_frame and ("Confusion matrix" in shape.text_frame.text or "good score" in shape.text_frame.text):
            shape.text_frame.clear()
            p = shape.text_frame.paragraphs[0]
            p.text = (
                "ACCEPTANCE CRITERIA VERIFICATION MATRIX:\n\n"
                "• TC-01 [Grievance Submission]: Lodged hostel issue with photo -> Tracking code CMP-8F42A1 generated, 48h timer active. [PASSED]\n\n"
                "• TC-02 [Level-2 Auto-Escalation]: 25h elapsed age simulated -> Escalation level auto-promoted from Coordinator to HOD. [PASSED]\n\n"
                "• TC-03 [Level-3 Auto-Escalation]: 49h elapsed age simulated -> Escalation level auto-promoted to DEAN with priority alert. [PASSED]\n\n"
                "• TC-04 [Anti-Bypass Protection]: Staff attempted direct ticket resolution without rating -> Rejected with HTTP 400 Bad Request. [PASSED]\n\n"
                "• TC-05 [Closed-Loop Verification]: Student submitted 5-star rating -> Status permanently transitioned to RESOLVED. [PASSED]\n\n"
                "• TC-06 [Security]: SQL Injection payload in login email -> Safely parameterized by PreparedStatement; rejected with 401. [PASSED]"
            )
            p.font.size = Pt(11)

    # -------------------------------------------------------------
    # SLIDE 11: PERFORMANCE & BENCHMARKS (Insert fig4)
    # -------------------------------------------------------------
    s11 = prs.slides[10]
    for shape in s11.shapes:
        if shape.has_text_frame and "RESULTS AND DISCUSSION" in shape.text_frame.text:
            shape.text_frame.text = "PERFORMANCE BENCHMARKS & STORAGE OPTIMIZATION"
            shape.text_frame.paragraphs[0].font.size = Pt(20)
            shape.text_frame.paragraphs[0].font.bold = True
    if os.path.exists("fig4_benchmarks.png"):
        s11.shapes.add_picture("fig4_benchmarks.png", Inches(1.5), Inches(2.0), width=Inches(10.0))

    # -------------------------------------------------------------
    # SLIDE 12: ENGINEERING BUG LOG
    # -------------------------------------------------------------
    s12 = prs.slides[11]
    for shape in s12.shapes:
        if shape.has_text_frame and "RESULTS AND DISCUSSION" in shape.text_frame.text:
            shape.text_frame.text = "ENGINEERING CHALLENGES & PRODUCTION BUG FIXES"
            shape.text_frame.paragraphs[0].font.size = Pt(20)
            shape.text_frame.paragraphs[0].font.bold = True
    tx_box12 = s12.shapes.add_textbox(Inches(1.5), Inches(2.2), Inches(10.3), Inches(4.5))
    tf12 = tx_box12.text_frame
    tf12.word_wrap = True
    p12 = tf12.paragraphs[0]
    p12.text = (
        "1. Bug 1: Base64 Photo Attachment Truncation\n"
        "   • Issue: Saving mobile photos failed with 'Data truncation for column attachment_path'.\n"
        "   • Root Cause: Base64 string length exceeded standard VARCHAR(255) capacity.\n"
        "   • Resolution: Altered column to MySQL LONGTEXT and implemented in-browser HTML5 canvas downsampling to max 1200px (saving 98.5% space).\n\n"
        "2. Bug 2: Database Connection Refusal (HY000/2002)\n"
        "   • Issue: phpMyAdmin and Java backend failed to connect to MySQL daemon.\n"
        "   • Root Cause: Windows MariaDB daemon crashed during system restart.\n"
        "   • Resolution: Configured mysqld with explicit defaults-file console logging and persistent auto-start.\n\n"
        "3. Bug 3: Thread-Safety & Concurrent Updates\n"
        "   • Issue: Escalation daemon and staff actions caused race conditions on ticket status.\n"
        "   • Resolution: Encapsulated DAO queries in transactional PreparedStatements with atomic WHERE status = 'ACTION_TAKEN' locks."
    )
    p12.font.size = Pt(11.5)

    # -------------------------------------------------------------
    # SLIDE 13: CONCLUSION & FUTURE WORK
    # -------------------------------------------------------------
    s13 = prs.slides[12]
    for shape in s13.shapes:
        if shape.has_text_frame and ("Machine learning" in shape.text_frame.text or "research" in shape.text_frame.text):
            shape.text_frame.clear()
            p = shape.text_frame.paragraphs[0]
            p.text = (
                "KEY ACCOMPLISHMENTS:\n"
                "• Full-Stack Mastery: Engineered end-to-end web system with semantic HTML5, pure Java SE 21, and MySQL 8.0.\n"
                "• Process Automation: Proved algorithmic 48-hour SLA timers solve campus grievance bottlenecks with zero human bias.\n"
                "• Closed-Loop Governance: Replaced arbitrary staff closures with verifiable student satisfaction rating locks.\n"
                "• Zero-Framework Efficiency: Demonstrated high-performance computing without heavy framework overhead.\n\n"
                "FUTURE AI/ML ENHANCEMENTS:\n"
                "• AI Duplicate Clustering: Sentence-Transformer NLP embeddings to cluster and merge duplicate campus tickets.\n"
                "• Computer Vision Verification: OpenCV / YOLO models comparing before/after maintenance photos.\n"
                "• Cross-Platform Mobile App: Native Flutter client with offline SQLite caching."
            )
            p.font.size = Pt(12)

    # -------------------------------------------------------------
    # SLIDE 14: REFERENCES
    # -------------------------------------------------------------
    s14 = prs.slides[13]
    for shape in s14.shapes:
        if shape.has_text_frame and ("diabetes" in shape.text_frame.text.lower() or "scikit-learn" in shape.text_frame.text.lower()):
            shape.text_frame.clear()
            p = shape.text_frame.paragraphs[0]
            p.text = (
                "1. Sanjai, H. (2026). Smart Complaint & Grievance Redressal Portal: Open-Source Codebase.\n"
                "   GitHub Repository: https://github.com/sanjai-19/smart-complaint-portal\n\n"
                "2. Oracle Corporation. (2024). Java SE 21 LTS Specification: com.sun.net.httpserver Package.\n\n"
                "3. MySQL AB. (2024). MySQL 8.0 Reference Manual: InnoDB Engine & Transaction Isolation.\n\n"
                "4. Provos, N., & Mazières, D. (1999). A Future-Adaptable Password Scheme (BCrypt Cryptography).\n\n"
                "5. Fielding, R. T. (2000). Architectural Styles and the Design of Network-based Software Architectures.\n\n"
                "6. Sathyabama Institute of Science and Technology. (2026). Dept of CSE (AI) Capstone Rubric."
            )
            p.font.size = Pt(11.5)

    # -------------------------------------------------------------
    # SLIDE 15 & 16: SUMMARY & THANK YOU
    # -------------------------------------------------------------
    s15 = prs.slides[14]
    for shape in s15.shapes:
        if shape.has_text_frame and "EARLY-STAGE DIABETES" in shape.text_frame.text:
            shape.text_frame.text = "SMART COMPLAINT & GRIEVANCE REDRESSAL PORTAL"
            shape.text_frame.paragraphs[0].font.size = Pt(20)
            shape.text_frame.paragraphs[0].font.bold = True
    tx_box15 = s15.shapes.add_textbox(Inches(1.5), Inches(2.5), Inches(10.3), Inches(3.5))
    tf15 = tx_box15.text_frame
    p15 = tf15.paragraphs[0]
    p15.text = (
        "CANDIDATE PROFILE & PROJECT DETAILS:\n\n"
        "• Student Lead: H Sanjai (Register Number: 44731076)\n"
        "• Degree: Bachelor of Engineering in Computer Science and Engineering (Artificial Intelligence)\n"
        "• Batch & Year: 2024 – 2028 / 3rd Year\n"
        "• Institution: Sathyabama Institute of Science and Technology (SIST), Chennai\n"
        "• Internal Guide: Ms. R. Shanumgaa Priya, M.E.\n"
        "• Live Demonstration: Java SE 21 HTTP Server (Port 8080) & MySQL 8.0 (Port 3306)"
    )
    p15.font.size = Pt(13)

    s16 = prs.slides[15]
    for shape in s16.shapes:
        if shape.has_text_frame and "EARLY-STAGE DIABETES" in shape.text_frame.text:
            shape.text_frame.text = "THANK YOU & VIVA DEFENSE Q&A"
            shape.text_frame.paragraphs[0].font.size = Pt(24)
            shape.text_frame.paragraphs[0].font.bold = True
    tx_box16 = s16.shapes.add_textbox(Inches(2.5), Inches(3.2), Inches(8.5), Inches(2.5))
    tf16 = tx_box16.text_frame
    p16 = tf16.paragraphs[0]
    p16.text = (
        "Smart Complaint & Grievance Redressal Portal\n\n"
        "Presented by: H Sanjai (44731076)\n"
        "B.E. CSE (Artificial Intelligence) | SIST\n\n"
        "🎤 Open for Viva Defense Questions & Evaluator Feedback"
    )
    p16.font.size = Pt(16)
    p16.font.bold = True
    p16.alignment = 2 # Center

    # Try saving to original or UPDATED file
    try:
        prs.save("Review PPT Format san.pptx")
        print("Successfully updated Review PPT Format san.pptx with full project presentation content!")
    except PermissionError:
        output_name = "Review PPT Format san_UPDATED.pptx"
        prs.save(output_name)
        print(f"Original file is open in PowerPoint. Saved full updated presentation into: {output_name}")

if __name__ == "__main__":
    update_review_ppt()
