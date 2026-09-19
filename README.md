# 🏛️ Smart Complaint & Grievance Redressal Portal

![Smart Complaint Portal Banner](linkedin_cover.jpg)

> **Campus and civic hierarchical grievance redressal portal with automated priority routing, 48-hour resolution SLA countdown timers, auto-escalation to HOD/Dean, and mandatory student satisfaction ratings.**

---

## 📌 Problem Statement

Campus and civic grievance redressal processes are fragmented across paper complaint boxes and unmonitored emails, resulting in untracked complaint escalations, delayed resolutions, and zero accountability for administrative officers.

## 💡 Solution Overview

A hierarchical grievance redressal web portal featuring:
* **Automated Priority Routing:** Real-time priority calculation (`HIGH`, `MEDIUM`, `LOW`) based on grievance categories and hazard keywords.
* **48-Hour Resolution SLA Countdown:** Auto-assignment to department coordinators with an active, visual 48-hour SLA countdown timer bar.
* **Hierarchical Auto-Escalation Engine:** Background scheduled worker automatically escalates unresolved tickets past SLA deadline to **HOD (Level 1)** and **Dean (Level 2)**.
* **Mandatory Student Feedback Prior to Closure:** Staff records action taken, but the ticket **cannot** transition to `RESOLVED` status until the student submits a **1 to 5 Star Satisfaction Rating & Feedback**.

---

## 🛠️ Tech Stack

* **Frontend:** Semantic HTML5, Bootstrap 5.3, FontAwesome 6, Vanilla JavaScript (AJAX / Fetch API)
* **Backend:** Standard Java SE 21 (Built-in lightweight `HttpServer` with REST API endpoints)
* **Database:** MySQL 8.0 / JDBC (`mysql-connector-j`)
* **Security & Utilities:** `jBCrypt` (Password hashing), `Gson` (JSON serialization)

---

## 🚀 Key Features & Acceptance Criteria

| Acceptance Criteria | Implementation Details |
| :--- | :--- |
| **1. Categorized Grievances & Attachments** | Submissions across **Hostel**, **Infrastructure**, and **Academics** with photo/document upload preview. Automated priority classification (`HIGH` for leaks, fire, power hazards; `MEDIUM` for mess, wifi; `LOW` for general queries). |
| **2. Auto-Assignment & 48-Hour SLA** | Tickets automatically assigned to respective Department Coordinators. Generates unique reference IDs (e.g. `CMP-000001`) and initiates a live 48-hour resolution SLA countdown bar. |
| **3. Automated SLA Escalation** | Background Java timer checks for breached tickets every 60 seconds and auto-escalates unresolved tickets: **Coordinator $\rightarrow$ HOD $\rightarrow$ Dean**. |
| **4. Student Satisfaction Rating Before Closure** | Staff marks resolution as `Action Taken`. The student verifies the work and submits a **1 to 5 star rating + comments** to finalize status to `RESOLVED`. |

---

## 👥 Built-in Demo Accounts

The application automatically seeds test accounts on first launch:

| Role | Email | Password | Scope |
| :--- | :--- | :--- | :--- |
| **Student** | `student@campus.edu` | `password123` | Submit, track, and rate grievances |
| **Hostel Coordinator** | `hostel@campus.edu` | `password123` | Manage Hostel grievances & submit action |
| **Academics Coordinator** | `academics@campus.edu` | `password123` | Manage Academic grievances |
| **Infrastructure Coordinator** | `infra@campus.edu` | `password123` | Manage Infrastructure grievances |
| **Head of Department (HOD)** | `hod@campus.edu` | `password123` | Review Level 1 Escalations |
| **Dean of Student Affairs** | `dean@campus.edu` | `password123` | Review Level 2 Final Escalations |
| **Administrator** | `admin@campus.edu` | `password123` | System oversight & full queue access |

*(Quick switch between roles is available anytime from the top-right navbar dropdown.)*

---

## ⚙️ Setup & Running Locally

### Prerequisites
1. **Java Development Kit (JDK 21+)**
2. **MySQL Server (e.g. via XAMPP or standalone MySQL)** running on `localhost:3306`

### Steps to Run
1. Start your local MySQL server. The application will automatically create the database `complaint_system_db` and tables if they don't exist.
2. Compile and run the application:
   ```bash
   # From the project root:
   javac -d target/classes -cp "target/classes;lib/*" src/main/java/model/*.java src/main/java/util/*.java src/main/java/dao/*.java src/main/java/Main.java
   java -cp "target/classes;lib/*" Main
   ```
   *(Or simply right-click `Main.java` and click **Run** in IntelliJ IDEA).*
3. Open your browser at:
   ```
   http://localhost:8080
   ```

---

## 📂 Project Structure

```
Smart Complaint Portal/
├── src/
│   └── main/
│       ├── java/
│       │   ├── dao/
│       │   │   ├── ComplaintDAO.java       # Database queries, SLA math & auto-escalation
│       │   │   └── UserDAO.java            # User authentication & role management
│       │   ├── model/
│       │   │   ├── Complaint.java          # Complaint entity model
│       │   │   └── User.java               # User entity model
│       │   ├── util/
│       │   │   ├── DatabaseConnection.java # MySQL connection & auto-migration
│       │   │   └── PasswordUtil.java       # BCrypt password hashing
│       │   └── Main.java                   # HTTP Server & background SLA scheduler
│       └── resources/
│           └── web/
│               ├── index.html              # Responsive Bootstrap 5 portal
│               ├── style.css               # Portal styles & SLA timer badges
│               └── app.js                  # Dynamic UI logic, AJAX & countdown tickers
├── pom.xml                                 # Maven dependencies (MySQL, BCrypt, Gson)
└── README.md
```
