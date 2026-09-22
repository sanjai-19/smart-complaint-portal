import matplotlib.pyplot as plt
import matplotlib.patches as patches

def make_cert():
    fig, ax = plt.subplots(figsize=(8, 5.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Border
    rect = patches.FancyBboxPatch((3, 3), 94, 94, boxstyle="round,pad=1.5,rounding_size=2", 
                                   linewidth=3, edgecolor='#1d4ed8', facecolor='#f8fafc')
    ax.add_patch(rect)
    inner = patches.FancyBboxPatch((6, 6), 88, 88, boxstyle="round,pad=1.5,rounding_size=1", 
                                   linewidth=1, edgecolor='#94a3b8', facecolor='#ffffff')
    ax.add_patch(inner)

    ax.text(50, 84, "SATHYABAMA INSTITUTE OF SCIENCE AND TECHNOLOGY", ha='center', va='center', fontsize=11, fontweight='bold', color='#0f172a')
    ax.text(50, 78, "DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING (ARTIFICIAL INTELLIGENCE)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1d4ed8')
    
    ax.text(50, 68, "CERTIFICATE OF COURSE COMPLETION", ha='center', va='center', fontsize=13, fontweight='bold', color='#1e40af')
    ax.text(50, 62, "PROFESSIONAL TRAINING / CAPSTONE SPECIALIZATION", ha='center', va='center', fontsize=9, color='#64748b')

    ax.text(50, 50, "This is to certify that", ha='center', va='center', fontsize=9.5, style='italic', color='#334155')
    ax.text(50, 42, "H SANJAI  (Register No: 44731076)", ha='center', va='center', fontsize=12, fontweight='bold', color='#0f172a')

    ax.text(50, 32, "has successfully completed the Professional Training Capstone Project entitled:\n\"SMART COMPLAINT & GRIEVANCE REDRESSAL PORTAL\"\nSpecialization: Full-Stack Web Architecture, Database Systems & Process Automation", 
            ha='center', va='center', fontsize=8.5, color='#334155', linespacing=1.35)

    ax.text(25, 14, "Ms. R. Shanumgaa Priya\nInternal Guide / Mentor", ha='center', va='center', fontsize=8, fontweight='bold', color='#0f172a')
    ax.text(75, 14, "Dr. P. Ajitha, M.E., Ph.D.\nHead of the Department", ha='center', va='center', fontsize=8, fontweight='bold', color='#0f172a')

    plt.tight_layout()
    plt.savefig("course_certificate.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated course_certificate.png")

def make_thank_you():
    fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    rect = patches.FancyBboxPatch((5, 5), 90, 90, boxstyle="round,pad=1.5,rounding_size=2", 
                                   linewidth=2, edgecolor='#1d4ed8', facecolor='#f8fafc')
    ax.add_patch(rect)

    ax.text(50, 75, "THANK YOU!", ha='center', va='center', fontsize=22, fontweight='bold', color='#1d4ed8')
    ax.text(50, 60, "SMART COMPLAINT & GRIEVANCE REDRESSAL PORTAL", ha='center', va='center', fontsize=12, fontweight='bold', color='#0f172a')
    ax.text(50, 48, "Candidate: H Sanjai [ Reg.No. : 44731076 ]\nDepartment of Computer Science and Engineering (Artificial Intelligence)\nSathyabama Institute of Science and Technology (SIST)", 
            ha='center', va='center', fontsize=10, color='#334155', linespacing=1.4)
    ax.text(50, 25, "🎤 Open for Viva Defense Questions & Evaluator Feedback", ha='center', va='center', fontsize=11, fontweight='bold', color='#15803d')

    plt.tight_layout()
    plt.savefig("thank_you.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated thank_you.png")

if __name__ == "__main__":
    make_cert()
    make_thank_you()
