package util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DatabaseConnection {

    private static final String BASE_URL = "jdbc:mysql://localhost:3306/";
    private static final String DB_NAME = "complaint_system_db";
    private static final String URL = BASE_URL + DB_NAME + "?createDatabaseIfNotExist=true&useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC";
    private static final String USER = "root";
    private static final String PASSWORD = "";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    /**
     * Automatically initializes database tables, missing columns, and default demo accounts.
     */
    public static void initDatabase() {
        try {
            // 1. Ensure database exists
            try (Connection conn = DriverManager.getConnection(BASE_URL, USER, PASSWORD);
                 Statement stmt = conn.createStatement()) {
                stmt.executeUpdate("CREATE DATABASE IF NOT EXISTS " + DB_NAME);
            }

            // 2. Connect to database and create/migrate tables
            try (Connection conn = getConnection();
                 Statement stmt = conn.createStatement()) {

                // Create users table if not exists
                stmt.executeUpdate(
                        "CREATE TABLE IF NOT EXISTS users (" +
                                "id INT AUTO_INCREMENT PRIMARY KEY, " +
                                "name VARCHAR(100) NOT NULL, " +
                                "email VARCHAR(150) NOT NULL UNIQUE, " +
                                "password VARCHAR(255) NOT NULL, " +
                                "role VARCHAR(30) NOT NULL DEFAULT 'STUDENT', " +
                                "department VARCHAR(100) DEFAULT 'General'" +
                                ")"
                );

                // Add missing columns to users table safely
                addColumnIfNotExists(conn, "users", "department", "VARCHAR(100) DEFAULT 'General'");

                // Create complaints table if not exists
                stmt.executeUpdate(
                        "CREATE TABLE IF NOT EXISTS complaints (" +
                                "id INT AUTO_INCREMENT PRIMARY KEY, " +
                                "reference_id VARCHAR(50), " +
                                "user_id INT NOT NULL, " +
                                "title VARCHAR(200) NOT NULL, " +
                                "description TEXT NOT NULL, " +
                                "category VARCHAR(100) DEFAULT 'Hostel', " +
                                "department VARCHAR(100) DEFAULT 'Hostel', " +
                                "priority VARCHAR(20) DEFAULT 'MEDIUM', " +
                                "status VARCHAR(50) DEFAULT 'Pending', " +
                                "attachment_path VARCHAR(255), " +
                                "assigned_coordinator VARCHAR(100), " +
                                "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, " +
                                "sla_deadline TIMESTAMP NULL, " +
                                "resolution TEXT, " +
                                "rating INT NULL, " +
                                "feedback TEXT, " +
                                "escalation_level INT DEFAULT 0, " +
                                "escalated_to VARCHAR(100)" +
                                ")"
                );

                // Add missing columns to complaints table safely
                addColumnIfNotExists(conn, "complaints", "reference_id", "VARCHAR(50)");
                addColumnIfNotExists(conn, "complaints", "category", "VARCHAR(100) DEFAULT 'Hostel'");
                addColumnIfNotExists(conn, "complaints", "priority", "VARCHAR(20) DEFAULT 'MEDIUM'");
                addColumnIfNotExists(conn, "complaints", "attachment_path", "LONGTEXT");
                addColumnIfNotExists(conn, "complaints", "assigned_coordinator", "VARCHAR(100)");
                addColumnIfNotExists(conn, "complaints", "created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP");
                addColumnIfNotExists(conn, "complaints", "sla_deadline", "TIMESTAMP NULL");
                addColumnIfNotExists(conn, "complaints", "rating", "INT NULL");
                addColumnIfNotExists(conn, "complaints", "feedback", "TEXT");
                addColumnIfNotExists(conn, "complaints", "escalation_level", "INT DEFAULT 0");
                addColumnIfNotExists(conn, "complaints", "escalated_to", "VARCHAR(100)");

                // Ensure attachment_path is LONGTEXT for Base64 attachments
                try {
                    stmt.executeUpdate("ALTER TABLE complaints MODIFY COLUMN attachment_path LONGTEXT");
                } catch (Exception ignored) {}

                // Seed initial student and officer accounts if users table is empty
                seedDemoAccounts(conn);
                System.out.println("✅ Database schema initialized and verified successfully.");
            }

        } catch (Exception e) {
            System.err.println("⚠️ Database initialization note: " + e.getMessage());
        }
    }

    private static void addColumnIfNotExists(Connection conn, String table, String column, String definition) {
        try (Statement stmt = conn.createStatement()) {
            stmt.executeUpdate("ALTER TABLE " + table + " ADD COLUMN " + column + " " + definition);
        } catch (SQLException e) {
            // Column already exists or error ignored
        }
    }

    private static void seedDemoAccounts(Connection conn) {
        try {
            seedUserIfMissing(conn, "Rahul Sharma (Student)", "student@campus.edu", "password123", "STUDENT", "Hostel");
            seedUserIfMissing(conn, "Prof. Alok (Hostel Coordinator)", "hostel@campus.edu", "password123", "COORDINATOR", "Hostel");
            seedUserIfMissing(conn, "Dr. Meena (Academics Coordinator)", "academics@campus.edu", "password123", "COORDINATOR", "Academics");
            seedUserIfMissing(conn, "Er. Rajesh (Infra Coordinator)", "infra@campus.edu", "password123", "COORDINATOR", "Infrastructure");
            seedUserIfMissing(conn, "Dr. K. Raman (HOD)", "hod@campus.edu", "password123", "HOD", "All");
            seedUserIfMissing(conn, "Dr. V. Sen (Dean of Student Affairs)", "dean@campus.edu", "password123", "DEAN", "All");
            seedUserIfMissing(conn, "Portal Administrator", "admin@campus.edu", "password123", "ADMIN", "All");
        } catch (Exception e) {
            System.err.println("Note on demo seeding: " + e.getMessage());
        }
    }

    private static void seedUserIfMissing(Connection conn, String name, String email, String plainPassword, String role, String dept) throws SQLException {
        String checkSql = "SELECT COUNT(*) FROM users WHERE LOWER(email) = LOWER(?)";
        try (PreparedStatement checkStmt = conn.prepareStatement(checkSql)) {
            checkStmt.setString(1, email);
            try (ResultSet rs = checkStmt.executeQuery()) {
                if (rs.next() && rs.getInt(1) == 0) {
                    String insertSql = "INSERT INTO users (name, email, password, role, department) VALUES (?, ?, ?, ?, ?)";
                    try (PreparedStatement ps = conn.prepareStatement(insertSql)) {
                        String hashed = PasswordUtil.hashPassword(plainPassword);
                        ps.setString(1, name);
                        ps.setString(2, email);
                        ps.setString(3, hashed);
                        ps.setString(4, role);
                        ps.setString(5, dept);
                        ps.executeUpdate();
                    }
                }
            }
        }
    }
}