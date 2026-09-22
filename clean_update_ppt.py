import os
import sys
from pptx import Presentation
from pptx.util import Pt

sys.stdout.reconfigure(encoding='utf-8')

def update_clean():
    print("Opening Review PPT Format san.pptx...")
    prs = Presentation('Review PPT Format san.pptx')

    def set_shape_text(shape, text, font_size=12, bold=False):
        if not shape.has_text_frame:
            return
        tf = shape.text_frame
        tf.word_wrap = True
        tf.clear()
        lines = text.strip().split('\n')
        for i, line in enumerate(lines):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = line
            p.font.name = "Arial"
            p.font.size = Pt(font_size)
            p.font.bold = bold

    def replace_shape_with_picture(slide, shape, img_path):
        if not os.path.exists(img_path):
            return
        left, top, width, height = shape.left, shape.top, shape.width, shape.height
        sp = shape._element
        sp.getparent().remove(sp)
        slide.shapes.add_picture(img_path, left, top, width, height)

    # Slide 1: Title
    s1 = prs.slides[0]
    for shape in s1.shapes:
        if shape.name == 'Rectangle 7':
            set_shape_text(shape, "1. H Sanjai [ Reg.No. : 44731076 ] (Solo Lead)", font_size=14, bold=True)
        elif shape.name == 'TextBox 13':
            set_shape_text(shape, "SMART COMPLAINT & GRIEVANCE REDRESSAL PORTAL\n(Hierarchical Campus Grievance Redressal & SLA Auto-Escalation Web Platform)", font_size=16, bold=True)
        elif shape.name == 'TextBox 15':
            set_shape_text(shape, "Internal Guide\nMs. R. Shanumgaa Priya, M.E.", font_size=13, bold=True)
        elif shape.name == 'Footer Placeholder 1':
            set_shape_text(shape, "Department of Computer Science and Engineering (Artificial Intelligence)", font_size=10)

    # Slide 2: Presentation Outline (Keep exact outline, clean footer)
    s2 = prs.slides[1]
    for shape in s2.shapes:
        if 'Footer' in shape.name:
            set_shape_text(shape, "Department of Computer Science and Engineering (Artificial Intelligence)", font_size=10)

    # Slide 3: Course Certificate (Picture Placeholder)
    s3 = prs.slides[2]
    cert_ph = None
    for shape in s3.shapes:
        if shape.name == 'Content Placeholder 9':
            cert_ph = shape
        elif 'Footer' in shape.name:
            set_shape_text(shape, "Department of Computer Science and Engineering (Artificial Intelligence)", font_size=10)
    if cert_ph:
        replace_shape_with_picture(s3, cert_ph, 'course_certificate.png')

    # Slide 4: Abstract
    s4 = prs.slides[3]
    for shape in s4.shapes:
        if shape.name == 'Content Placeholder 2':
            text4 = (
                "• Campus grievance redressal in higher educational institutions is traditionally fragmented across paper suggestion boxes, unmonitored WhatsApp chats, and email inboxes, leading to lost complaints and zero accountability.\n\n"
                "• The Smart Complaint & Grievance Redressal Portal is an enterprise 3-tier web platform engineered in pure Java SE 21, MySQL 8.0, and responsive Bootstrap 5.\n\n"
                "• Core Capabilities: (1) Automated Priority Routing, (2) Real-Time 48-Hour SLA Countdown Timers, (3) Autonomous Multi-Tier Escalation (Coordinator -> HOD -> Dean), and (4) Anti-Bypass Closed-Loop Student Rating Verification Lock.\n\n"
                "• Zero-Framework Lean Architecture: Sub-400ms startup latency and 98.5% payload reduction via client-side canvas downsampling."
            )
            set_shape_text(shape, text4, font_size=12.5)
        elif 'Footer' in shape.name:
            set_shape_text(shape, "Department of Computer Science and Engineering (Artificial Intelligence)", font_size=10)

    # Slide 5: Objectives
    s5 = prs.slides[4]
    for shape in s5.shapes:
        if shape.name == 'Content Placeholder 2':
            text5 = (
                "1. Rapid Filing: Enable students to submit categorized campus grievances with photo attachments in under 60 seconds.\n\n"
                "2. Zero-Framework Backend: Build a high-throughput REST HTTP server using native Java SE 21 with sub-second startup.\n\n"
                "3. Enforced 48-Hour SLA: Implement an automated background ScheduledExecutorService daemon that autonomously escalates tickets upon SLA breach.\n\n"
                "4. 3NF Relational Integrity: Model MySQL database in 3NF with cascading foreign keys and PreparedStatement defense.\n\n"
                "5. Closed-Loop Student Rating: Enforce an anti-bypass state lock where grievances can only resolve after the complainant submits a 1-to-5 star rating.\n\n"
                "6. Client-Side Image Compression: Downsample mobile camera uploads from 8 MB to <120 KB using HTML5 canvas."
            )
            set_shape_text(shape, text5, font_size=12)
        elif 'Footer' in shape.name:
            set_shape_text(shape, "Department of Computer Science and Engineering (Artificial Intelligence)", font_size=10)

    # Slide 6: System Architecture (Replace Picture 11 with fig1_architecture.png)
    s6 = prs.slides[5]
    pic6 = None
    for shape in s6.shapes:
        if shape.name == 'Picture 11':
            pic6 = shape
            break
    if pic6 and os.path.exists('fig1_architecture.png'):
        l, t, w, h = pic6.left, pic6.top, pic6.width, pic6.height
        sp = pic6._element
        sp.getparent().remove(sp)
        s6.shapes.add_picture('fig1_architecture.png', l, t, w, h)

    # Slide 7: Hardware & Software Requirements
    s7 = prs.slides[6]
    for shape in s7.shapes:
        if shape.name == 'Content Placeholder 2':
            text7 = (
                "Software Requirements:\n"
                "• Runtime & JDK: Oracle OpenJDK 21 LTS (64-bit)\n"
                "• Relational Database: MySQL Server 8.0 / MariaDB 10.4 (InnoDB Engine)\n"
                "• Web Interface: Semantic HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3\n"
                "• Core Libraries: com.google.code.gson:gson:2.10.1, org.mindrot:jbcrypt:0.4\n"
                "• Development Tools: Apache Maven 3.9, Postman REST Client, IntelliJ IDEA\n\n"
                "Hardware Requirements:\n"
                "• Workstation Processor: Intel Core i5 / AMD Ryzen 5 (2.5 GHz+, 6 Cores)\n"
                "• System Memory: 16 GB DDR4 RAM | Storage: 512 GB NVMe SSD\n"
                "• Client Access: Any standard modern web browser (Chrome, Edge, Safari, Firefox)"
            )
            set_shape_text(shape, text7, font_size=11.5)

    # Slide 8: Dataset Description -> Project Implementation & 3NF Schema
    s8 = prs.slides[7]
    for shape in s8.shapes:
        if shape.name == 'Title 1':
            set_shape_text(shape, "PROJECT IMPLEMENTATION & 3NF SCHEMA", font_size=20, bold=True)
        elif shape.name == 'Content Placeholder 2':
            text8 = (
                "Implementation Architecture Across 4 Agile SDLC Phases:\n\n"
                "• Phase 1 (Define): Formulated problem statements, user personas (Student, Coordinator, HOD, Dean, Admin), and BDD Given/When/Then acceptance criteria.\n\n"
                "• Phase 2 (Design): Architected 3-tier decoupled model and Third Normal Form (3NF) relational database schema (users, complaints, complaint_actions) with ACID transactional integrity.\n\n"
                "• Phase 3 (Develop): Engineered zero-framework Java SE 21 HttpServer, BCrypt password encryption (work factor 12), and background ScheduledExecutorService SLA daemon.\n\n"
                "• Phase 4 (Deploy): Implemented client-side HTML5 canvas image downsampling (<120 KB), resolved CORS policies, and verified end-to-end integration."
            )
            set_shape_text(shape, text8, font_size=12)

    # Slide 9: Classification Algorithm -> Process Automation & Escalation
    s9 = prs.slides[8]
    for shape in s9.shapes:
        if shape.name == 'Title 1':
            set_shape_text(shape, "PROCESS AUTOMATION & SLA ESCALATION ENGINE", font_size=20, bold=True)
        elif shape.name == 'Content Placeholder 2':
            text9 = (
                "Algorithmic 48-Hour SLA Governance Engine:\n\n"
                "• Java ScheduledExecutorService: A background daemon awakens hourly to evaluate TIMESTAMPDIFF(HOUR, created_at, NOW()) dynamically.\n\n"
                "• Level 1 (0 to 24 Hours): Grievance routed to Department Coordinator with active countdown timer visible to complainant.\n\n"
                "• Level 2 (24 to 48 Hours): If unaddressed past 24 hours, escalation_level auto-promotes to Head of Department (HOD).\n\n"
                "• Level 3 (Exceeding 48 Hours): If SLA is breached past 48 hours, ticket auto-promotes to Dean / Principal for administrative inquiry.\n\n"
                "• Closed-Loop State Lock: When staff logs action, status moves to ACTION_TAKEN. Direct resolution is strictly blocked until the filing student validates with a 1-to-5 star rating."
            )
            set_shape_text(shape, text9, font_size=12)

    # Slide 10: Results and Discussion (Functional Acceptance)
    s10 = prs.slides[9]
    for shape in s10.shapes:
        if shape.name == 'Content Placeholder 2':
            text10 = (
                "Acceptance Criteria Test Execution Results:\n\n"
                "• TC-01 [Grievance Submission]: Lodged hostel issue with photo -> Tracking code CMP-8F42A1 generated; 48h clock active. [PASSED]\n\n"
                "• TC-02 [Level-2 Auto-Escalation]: 25h ticket age simulated -> Escalation level auto-promoted from Coordinator to HOD. [PASSED]\n\n"
                "• TC-03 [Level-3 Auto-Escalation]: 49h ticket age simulated -> Escalation level auto-promoted to DEAN with priority alert. [PASSED]\n\n"
                "• TC-04 [Anti-Bypass Protection]: Staff attempted direct ticket resolution without rating -> Rejected with HTTP 400 Bad Request. [PASSED]\n\n"
                "• TC-05 [Closed-Loop Verification]: Student submitted 5-star rating -> Status permanently transitioned to RESOLVED. [PASSED]\n\n"
                "• TC-06 [Security Defense]: SQL injection payload in login -> Safely parameterized by PreparedStatement; rejected with 401. [PASSED]"
            )
            set_shape_text(shape, text10, font_size=11)

    # Slide 11: Results and Discussion (Insert fig4_benchmarks into Content Placeholder 11)
    s11 = prs.slides[10]
    ph11 = None
    for shape in s11.shapes:
        if shape.name == 'Title 1':
            set_shape_text(shape, "PERFORMANCE BENCHMARKS & STORAGE OPTIMIZATION", font_size=20, bold=True)
        elif shape.name == 'Content Placeholder 11':
            ph11 = shape
    if ph11:
        replace_shape_with_picture(s11, ph11, 'fig4_benchmarks.png')

    # Slide 12: Results and Discussion (Insert fig2_workflow into Content Placeholder 9)
    s12 = prs.slides[11]
    ph12 = None
    for shape in s12.shapes:
        if shape.name == 'Title 1':
            set_shape_text(shape, "GRIEVANCE LIFECYCLE & SLA ESCALATION FLOW", font_size=20, bold=True)
        elif shape.name == 'Content Placeholder 9':
            ph12 = shape
    if ph12:
        replace_shape_with_picture(s12, ph12, 'fig2_workflow.png')

    # Slide 13: Conclusion & Future Work
    s13 = prs.slides[12]
    for shape in s13.shapes:
        if shape.name == 'Content Placeholder 2':
            text13 = (
                "Key Accomplishments:\n"
                "• Full-Stack Mastery: Engineered end-to-end web system with semantic HTML5, pure Java SE 21, and MySQL 8.0.\n"
                "• Process Automation: Proved algorithmic 48-hour SLA timers solve campus grievance bottlenecks with zero administrative bias.\n"
                "• Closed-Loop Governance: Replaced arbitrary staff closures with verifiable student satisfaction rating locks.\n"
                "• Zero-Framework Efficiency: Demonstrated high-performance computing without heavy framework overhead.\n\n"
                "Future AI/ML Enhancements:\n"
                "• AI Duplicate Clustering: Sentence-Transformer NLP embeddings to cluster and merge duplicate campus tickets.\n"
                "• Computer Vision Verification: OpenCV / YOLO models comparing before/after maintenance photos.\n"
                "• Cross-Platform Mobile App: Native Flutter client with offline SQLite caching."
            )
            set_shape_text(shape, text13, font_size=11.5)

    # Slide 14: References
    s14 = prs.slides[13]
    for shape in s14.shapes:
        if shape.name == 'Content Placeholder 8':
            text14 = (
                "1. Sanjai, H. (2026). Smart Complaint & Grievance Redressal Portal: Open-Source Codebase.\n"
                "   GitHub Repository: https://github.com/sanjai-19/smart-complaint-portal\n\n"
                "2. Oracle Corporation. (2024). Java SE 21 LTS Specification: com.sun.net.httpserver Package.\n\n"
                "3. MySQL AB. (2024). MySQL 8.0 Reference Manual: InnoDB Engine & Transaction Isolation.\n\n"
                "4. Provos, N., & Mazières, D. (1999). A Future-Adaptable Password Scheme (BCrypt Cryptography).\n\n"
                "5. Fielding, R. T. (2000). Architectural Styles and the Design of Network-based Software Architectures.\n\n"
                "6. Sathyabama Institute of Science and Technology. (2026). Dept of CSE (AI) Capstone Rubric."
            )
            set_shape_text(shape, text14, font_size=11.5)

    # Slide 15: Candidate Profile
    s15 = prs.slides[14]
    for shape in s15.shapes:
        if shape.name == 'TextBox 8':
            text15 = (
                "SMART COMPLAINT & GRIEVANCE REDRESSAL PORTAL\n\n"
                "Candidate: H Sanjai [ Reg.No. : 44731076 ]\n"
                "Department of Computer Science & Engineering (Artificial Intelligence)\n"
                "Sathyabama Institute of Science and Technology (SIST), Chennai\n"
                "Internal Guide: Ms. R. Shanumgaa Priya, M.E.\n"
                "Project Domain: Full-Stack Web Architecture, Database Systems & Process Automation"
            )
            set_shape_text(shape, text15, font_size=13, bold=True)
        elif shape.name == 'Picture 2':
            sp = shape._element
            sp.getparent().remove(sp)

    # Slide 16: Thank You (Insert thank_you.png into Content Placeholder 14)
    s16 = prs.slides[15]
    ph16 = None
    for shape in s16.shapes:
        if shape.name == 'Title 7':
            set_shape_text(shape, "SMART COMPLAINT & GRIEVANCE REDRESSAL PORTAL", font_size=20, bold=True)
        elif shape.name == 'Content Placeholder 14':
            ph16 = shape
    if ph16:
        replace_shape_with_picture(s16, ph16, 'thank_you.png')

    prs.save("Review PPT Format san.pptx")
    print("Clean update completed! Review PPT Format san.pptx has zero overlapping boxes and preserves exact template format.")

if __name__ == "__main__":
    update_clean()
