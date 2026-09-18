package dao;

import model.Complaint;
import util.DatabaseConnection;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class ComplaintDAO {

    private static final DateTimeFormatter DT_FORMATTER = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

    // ==========================================
    // AUTOMATED PRIORITY ROUTING
    // ==========================================
    public String calculatePriority(String category, String title, String description) {
        String combined = (title + " " + description).toLowerCase();

        // High priority triggers
        if (combined.contains("leak") || combined.contains("fire") || combined.contains("shock") ||
                combined.contains("water") || combined.contains("electric") || combined.contains("power") ||
                combined.contains("danger") || combined.contains("ragging") || combined.contains("medical") ||
                combined.contains("emergency") || combined.contains("ceiling") || combined.contains("exam") ||
                combined.contains("hall ticket") || combined.contains("admit card") || combined.contains("harassment")) {
            return "HIGH";
        }

        // Medium priority triggers
        if (combined.contains("wifi") || combined.contains("internet") || combined.contains("fan") ||
                combined.contains("clean") || combined.contains("mess") || combined.contains("food") ||
                combined.contains("library") || combined.contains("timetable") || combined.contains("attendance") ||
                combined.contains("ac") || combined.contains("door") || combined.contains("bench")) {
            return "MEDIUM";
        }

        // Category default
        if ("Hostel".equalsIgnoreCase(category) || "Infrastructure".equalsIgnoreCase(category)) {
            return "MEDIUM";
        }

        return "LOW";
    }

    // ==========================================
    // AUTO-ASSIGN COORDINATOR
    // ==========================================
    public String autoAssignCoordinator(String category) {
        if ("Hostel".equalsIgnoreCase(category)) {
            return "Prof. Alok (Hostel Coordinator)";
        } else if ("Academics".equalsIgnoreCase(category)) {
            return "Dr. Meena (Academics Coordinator)";
        } else if ("Infrastructure".equalsIgnoreCase(category)) {
            return "Er. Rajesh (Infra Coordinator)";
        }
        return "Department Coordinator";
    }

    // ==========================================
    // SUBMIT COMPLAINT (AC 1 & AC 2)
    // ==========================================
    public int submitComplaint(Complaint complaint) {
        // 1. Calculate Priority automatically if not specified
        if (complaint.getPriority() == null || complaint.getPriority().isBlank()) {
            complaint.setPriority(calculatePriority(complaint.getCategory(), complaint.getTitle(), complaint.getDescription()));
        }

        // 2. Auto-assign coordinator based on category
        if (complaint.getAssignedCoordinator() == null || complaint.getAssignedCoordinator().isBlank()) {
            complaint.setAssignedCoordinator(autoAssignCoordinator(complaint.getCategory()));
        }

        // 3. 48-Hour Resolution SLA Countdown
        LocalDateTime now = LocalDateTime.now();
        LocalDateTime deadline = now.plusHours(48);

        String sql = "INSERT INTO complaints " +
                "(user_id, title, description, category, department, priority, status, " +
                "attachment_path, assigned_coordinator, created_at, sla_deadline, escalation_level) " +
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

            statement.setInt(1, complaint.getUserId());
            statement.setString(2, complaint.getTitle());
            statement.setString(3, complaint.getDescription());
            statement.setString(4, complaint.getCategory() != null ? complaint.getCategory() : "Hostel");
            statement.setString(5, complaint.getDepartment() != null ? complaint.getDepartment() : complaint.getCategory());
            statement.setString(6, complaint.getPriority());
            statement.setString(7, "Submitted");
            statement.setString(8, complaint.getAttachmentPath());
            statement.setString(9, complaint.getAssignedCoordinator());
            statement.setTimestamp(10, Timestamp.valueOf(now));
            statement.setTimestamp(11, Timestamp.valueOf(deadline));

            int rowsInserted = statement.executeUpdate();
            if (rowsInserted > 0) {
                var generatedKeys = statement.getGeneratedKeys();
                if (generatedKeys.next()) {
                    int id = generatedKeys.getInt(1);
                    String referenceId = formatComplaintId(id);

                    // Update reference ID
                    updateReferenceId(id, referenceId);
                    complaint.setId(id);
                    complaint.setReferenceId(referenceId);
                    return id;
                }
            }

        } catch (SQLException e) {
            System.err.println("Complaint submission failed: " + e.getMessage());
        }

        return 0;
    }

    private void updateReferenceId(int id, String referenceId) {
        String sql = "UPDATE complaints SET reference_id = ? WHERE id = ?";
        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, referenceId);
            statement.setInt(2, id);
            statement.executeUpdate();
        } catch (SQLException ignored) {}
    }

    public String formatComplaintId(int complaintId) {
        return String.format("CMP-%06d", complaintId);
    }

    // ==========================================
    // GET COMPLAINTS BY USER (STUDENT)
    // ==========================================
    public List<Complaint> getComplaintsByUser(int userId) {
        List<Complaint> list = new ArrayList<>();
        String sql = "SELECT c.*, u.name as user_name FROM complaints c " +
                "JOIN users u ON c.user_id = u.id " +
                "WHERE c.user_id = ? ORDER BY c.id DESC";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setInt(1, userId);
            try (ResultSet rs = statement.executeQuery()) {
                while (rs.next()) {
                    list.add(mapResultSetToComplaint(rs));
                }
            }

        } catch (SQLException e) {
            System.err.println("Error fetching user complaints: " + e.getMessage());
        }
        return list;
    }

    // ==========================================
    // GET ALL COMPLAINTS (OFFICER / HOD / DEAN)
    // ==========================================
    public List<Complaint> getAllComplaints() {
        List<Complaint> list = new ArrayList<>();
        String sql = "SELECT c.*, u.name as user_name FROM complaints c " +
                "JOIN users u ON c.user_id = u.id " +
                "ORDER BY c.id DESC";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql);
             ResultSet rs = statement.executeQuery()) {

            while (rs.next()) {
                list.add(mapResultSetToComplaint(rs));
            }

        } catch (SQLException e) {
            System.err.println("Error fetching all complaints: " + e.getMessage());
        }
        return list;
    }

    // ==========================================
    // TRACK COMPLAINT BY REFERENCE ID
    // ==========================================
    public Complaint trackComplaint(String referenceId) {
        String cleanRef = referenceId.trim();
        int id = 0;
        try {
            id = Integer.parseInt(cleanRef.replace("CMP-", ""));
        } catch (NumberFormatException ignored) {}

        String sql = "SELECT c.*, u.name as user_name FROM complaints c " +
                "JOIN users u ON c.user_id = u.id " +
                "WHERE c.reference_id = ? OR c.id = ?";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setString(1, cleanRef);
            statement.setInt(2, id);

            try (ResultSet rs = statement.executeQuery()) {
                if (rs.next()) {
                    return mapResultSetToComplaint(rs);
                }
            }

        } catch (SQLException e) {
            System.err.println("Error tracking complaint: " + e.getMessage());
        }
        return null;
    }

    // ==========================================
    // STAFF ACTION TAKEN (PRE-CLOSURE)
    // ==========================================
    public boolean recordActionTaken(int complaintId, String remarks) {
        String sql = "UPDATE complaints SET status = 'Action Taken', resolution = ? WHERE id = ?";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setString(1, remarks);
            statement.setInt(2, complaintId);

            return statement.executeUpdate() > 0;

        } catch (SQLException e) {
            System.err.println("Error recording action: " + e.getMessage());
            return false;
        }
    }

    // ==========================================
    // STUDENT FEEDBACK & RATING (AC 4: MANDATORY FOR RESOLVED)
    // ==========================================
    public boolean submitStudentFeedback(int complaintId, int rating, String feedback) {
        if (rating < 1 || rating > 5) {
            return false;
        }

        // Only transitions to RESOLVED upon student rating
        String sql = "UPDATE complaints SET status = 'Resolved', rating = ?, feedback = ? WHERE id = ?";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setInt(1, rating);
            statement.setString(2, feedback);
            statement.setInt(3, complaintId);

            return statement.executeUpdate() > 0;

        } catch (SQLException e) {
            System.err.println("Error submitting feedback: " + e.getMessage());
            return false;
        }
    }

    // ==========================================
    // AUTO-ESCALATE BREACHED TICKETS (AC 3)
    // ==========================================
    public int checkAndEscalateBreachedTickets() {
        int escalatedCount = 0;
        String findBreachedSql = "SELECT id, escalation_level FROM complaints " +
                "WHERE status NOT IN ('Resolved') " +
                "AND sla_deadline IS NOT NULL " +
                "AND sla_deadline < NOW() " +
                "AND escalation_level < 2";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(findBreachedSql);
             ResultSet rs = statement.executeQuery()) {

            while (rs.next()) {
                int id = rs.getInt("id");
                int currentLevel = rs.getInt("escalation_level");

                int nextLevel = currentLevel + 1;
                String newStatus = (nextLevel == 1) ? "Escalated to HOD" : "Escalated to Dean";
                String officer = (nextLevel == 1) ? "Dr. K. Raman (HOD)" : "Dr. V. Sen (Dean)";

                String updateSql = "UPDATE complaints SET status = ?, escalation_level = ?, escalated_to = ? WHERE id = ?";
                try (PreparedStatement updateStmt = connection.prepareStatement(updateSql)) {
                    updateStmt.setString(1, newStatus);
                    updateStmt.setInt(2, nextLevel);
                    updateStmt.setString(3, officer);
                    updateStmt.setInt(4, id);
                    if (updateStmt.executeUpdate() > 0) {
                        escalatedCount++;
                    }
                }
            }

        } catch (SQLException e) {
            System.err.println("Error during auto-escalation check: " + e.getMessage());
        }

        return escalatedCount;
    }

    // ==========================================
    // MANUAL ESCALATION
    // ==========================================
    public boolean manualEscalate(int complaintId, String targetRole) {
        int nextLevel = "DEAN".equalsIgnoreCase(targetRole) ? 2 : 1;
        String newStatus = (nextLevel == 1) ? "Escalated to HOD" : "Escalated to Dean";
        String officer = (nextLevel == 1) ? "Dr. K. Raman (HOD)" : "Dr. V. Sen (Dean)";

        String sql = "UPDATE complaints SET status = ?, escalation_level = ?, escalated_to = ? WHERE id = ?";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setString(1, newStatus);
            statement.setInt(2, nextLevel);
            statement.setString(3, officer);
            statement.setInt(4, complaintId);

            return statement.executeUpdate() > 0;

        } catch (SQLException e) {
            System.err.println("Error manual escalating: " + e.getMessage());
            return false;
        }
    }

    // ==========================================
    // RESULT SET MAPPER HELPER
    // ==========================================
    private Complaint mapResultSetToComplaint(ResultSet rs) throws SQLException {
        int id = rs.getInt("id");
        String refId = rs.getString("reference_id");
        if (refId == null || refId.isBlank()) {
            refId = formatComplaintId(id);
        }

        String createdAt = "";
        Timestamp catTs = rs.getTimestamp("created_at");
        if (catTs != null) {
            createdAt = catTs.toLocalDateTime().format(DT_FORMATTER);
        }

        String slaDeadline = "";
        Timestamp slaTs = rs.getTimestamp("sla_deadline");
        if (slaTs != null) {
            slaDeadline = slaTs.toLocalDateTime().format(DT_FORMATTER);
        }

        Integer rating = rs.getInt("rating");
        if (rs.wasNull()) {
            rating = null;
        }

        String category = rs.getString("category");
        if (category == null || category.isBlank()) {
            category = rs.getString("department");
        }

        return new Complaint(
                id,
                refId,
                rs.getInt("user_id"),
                rs.getString("user_name"),
                rs.getString("title"),
                rs.getString("description"),
                category,
                rs.getString("department"),
                rs.getString("priority"),
                rs.getString("status"),
                rs.getString("attachment_path"),
                rs.getString("assigned_coordinator"),
                createdAt,
                slaDeadline,
                rs.getString("resolution"),
                rating,
                rs.getString("feedback"),
                rs.getInt("escalation_level"),
                rs.getString("escalated_to")
        );
    }
}