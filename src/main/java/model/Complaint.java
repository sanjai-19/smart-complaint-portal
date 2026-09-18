package model;

public class Complaint {

    private int id;
    private String referenceId;
    private int userId;
    private String userName;
    private String title;
    private String description;
    private String category;            // Hostel, Infrastructure, Academics
    private String department;
    private String priority;            // HIGH, MEDIUM, LOW (automated)
    private String status;              // Pending, In Progress, Action Taken, Resolved, Escalated to HOD, Escalated to Dean
    private String attachmentPath;      // Photo or Document filename/base64
    private String assignedCoordinator; // Assigned department officer
    private String createdAt;
    private String slaDeadline;         // 48 hours from creation
    private String resolutionRemarks;   // Remarks entered by staff
    private Integer rating;             // 1 to 5 stars (submitted by student)
    private String feedback;            // Feedback comments by student
    private int escalationLevel;        // 0: Coordinator, 1: HOD, 2: Dean
    private String escalatedTo;

    public Complaint() {
    }

    public Complaint(int id, int userId, String title, String description,
                     String department, String status) {
        this.id = id;
        this.userId = userId;
        this.title = title;
        this.description = description;
        this.department = department;
        this.category = department;
        this.status = status;
        this.priority = "MEDIUM";
        this.escalationLevel = 0;
    }

    // Full constructor
    public Complaint(int id, String referenceId, int userId, String userName,
                     String title, String description, String category,
                     String department, String priority, String status,
                     String attachmentPath, String assignedCoordinator,
                     String createdAt, String slaDeadline, String resolutionRemarks,
                     Integer rating, String feedback, int escalationLevel, String escalatedTo) {
        this.id = id;
        this.referenceId = referenceId;
        this.userId = userId;
        this.userName = userName;
        this.title = title;
        this.description = description;
        this.category = category;
        this.department = department;
        this.priority = priority;
        this.status = status;
        this.attachmentPath = attachmentPath;
        this.assignedCoordinator = assignedCoordinator;
        this.createdAt = createdAt;
        this.slaDeadline = slaDeadline;
        this.resolutionRemarks = resolutionRemarks;
        this.rating = rating;
        this.feedback = feedback;
        this.escalationLevel = escalationLevel;
        this.escalatedTo = escalatedTo;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getReferenceId() {
        return referenceId;
    }

    public void setReferenceId(String referenceId) {
        this.referenceId = referenceId;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getAttachmentPath() {
        return attachmentPath;
    }

    public void setAttachmentPath(String attachmentPath) {
        this.attachmentPath = attachmentPath;
    }

    public String getAssignedCoordinator() {
        return assignedCoordinator;
    }

    public void setAssignedCoordinator(String assignedCoordinator) {
        this.assignedCoordinator = assignedCoordinator;
    }

    public String getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
    }

    public String getSlaDeadline() {
        return slaDeadline;
    }

    public void setSlaDeadline(String slaDeadline) {
        this.slaDeadline = slaDeadline;
    }

    public String getResolutionRemarks() {
        return resolutionRemarks;
    }

    public void setResolutionRemarks(String resolutionRemarks) {
        this.resolutionRemarks = resolutionRemarks;
    }

    public Integer getRating() {
        return rating;
    }

    public void setRating(Integer rating) {
        this.rating = rating;
    }

    public String getFeedback() {
        return feedback;
    }

    public void setFeedback(String feedback) {
        this.feedback = feedback;
    }

    public int getEscalationLevel() {
        return escalationLevel;
    }

    public void setEscalationLevel(int escalationLevel) {
        this.escalationLevel = escalationLevel;
    }

    public String getEscalatedTo() {
        return escalatedTo;
    }

    public void setEscalatedTo(String escalatedTo) {
        this.escalatedTo = escalatedTo;
    }
}