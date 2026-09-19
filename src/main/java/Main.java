import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;
import dao.ComplaintDAO;
import dao.UserDAO;
import model.Complaint;
import model.User;
import util.DatabaseConnection;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class Main {

    private static final int PORT = 8080;
    private static final Gson gson = new Gson();
    private static final UserDAO userDAO = new UserDAO();
    private static final ComplaintDAO complaintDAO = new ComplaintDAO();

    public static void main(String[] args) throws IOException {

        // ==========================================
        // 1. INITIALIZE DATABASE & DEMO SEED
        // ==========================================
        System.out.println("Initializing MySQL database & checking schema...");
        DatabaseConnection.initDatabase();

        // ==========================================
        // 2. START HTTP WEB SERVER (PORT 8080)
        // ==========================================
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);
        server.setExecutor(Executors.newFixedThreadPool(10));

        // Static Files Handler (HTML, CSS, JS)
        server.createContext("/", new StaticFileHandler());

        // Auth API Handlers
        server.createContext("/api/auth/login", new LoginHandler());
        server.createContext("/api/auth/register", new RegisterHandler());

        // Complaint API Handlers
        server.createContext("/api/complaints/submit", new SubmitComplaintHandler());
        server.createContext("/api/complaints/my", new MyComplaintsHandler());
        server.createContext("/api/complaints/all", new AllComplaintsHandler());
        server.createContext("/api/complaints/track", new TrackComplaintHandler());
        server.createContext("/api/complaints/action", new ActionTakenHandler());
        server.createContext("/api/complaints/rate", new RateComplaintHandler());
        server.createContext("/api/complaints/escalate", new EscalateHandler());
        server.createContext("/api/complaints/check-escalations", new CheckEscalationHandler());

        server.start();

        // ==========================================
        // 3. BACKGROUND 48-HOUR SLA AUTO-ESCALATOR (AC 3)
        // ==========================================
        ScheduledExecutorService scheduler = Executors.newSingleThreadScheduledExecutor();
        scheduler.scheduleAtFixedRate(() -> {
            try {
                int escalated = complaintDAO.checkAndEscalateBreachedTickets();
                if (escalated > 0) {
                    System.out.println("🚨 [SLA Auto-Escalator] Breached SLA detected: " + escalated + " ticket(s) automatically escalated to HOD / Dean!");
                }
            } catch (Exception e) {
                System.err.println("Error in SLA scheduler: " + e.getMessage());
            }
        }, 10, 60, TimeUnit.SECONDS);

        // ==========================================
        // 4. DISPLAY CONSOLE BANNER
        // ==========================================
        System.out.println("\n================================================================================");
        System.out.println("    🎓 SMART COMPLAINT RESOLUTION PORTAL (STUDENT EDITION) READY!");
        System.out.println("================================================================================");
        System.out.println("  🌐 Open in Browser: http://localhost:" + PORT);
        System.out.println("  📊 Viva Presentation: http://localhost:" + PORT + "/presentation/presentation.html");
        System.out.println("  ⏱️  Background SLA Auto-Escalation Engine: ACTIVE (Checking every 60s)");
        System.out.println("  ⭐ Acceptance Criteria 1 to 4: Fully Supported & Visualized");
        System.out.println("================================================================================\n");
    }

    // ==========================================
    // STATIC FILE HANDLER
    // ==========================================
    static class StaticFileHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String path = exchange.getRequestURI().getPath();
            if (path.equals("/") || path.isBlank()) {
                path = "/index.html";
            }

            // Find file in src/main/resources/web or presentation or root
            File file = new File("src/main/resources/web" + path);
            if (!file.exists() && path.startsWith("/presentation/")) {
                file = new File("." + path);
            }
            if (!file.exists()) {
                // Try classpath resource
                try (InputStream is = getClass().getResourceAsStream("/web" + path)) {
                    if (is != null) {
                        byte[] bytes = is.readAllBytes();
                        String contentType = getContentType(path);
                        exchange.getResponseHeaders().set("Content-Type", contentType);
                        exchange.sendResponseHeaders(200, bytes.length);
                        try (OutputStream os = exchange.getResponseBody()) {
                            os.write(bytes);
                        }
                        return;
                    }
                }
            }

            if (file.exists() && !file.isDirectory()) {
                byte[] bytes = new FileInputStream(file).readAllBytes();
                String contentType = getContentType(path);
                exchange.getResponseHeaders().set("Content-Type", contentType);
                exchange.sendResponseHeaders(200, bytes.length);
                try (OutputStream os = exchange.getResponseBody()) {
                    os.write(bytes);
                }
            } else {
                String notFound = "404 Not Found: " + path;
                exchange.sendResponseHeaders(404, notFound.length());
                try (OutputStream os = exchange.getResponseBody()) {
                    os.write(notFound.getBytes());
                }
            }
        }

        private String getContentType(String path) {
            if (path.endsWith(".html")) return "text/html; charset=UTF-8";
            if (path.endsWith(".css")) return "text/css; charset=UTF-8";
            if (path.endsWith(".js")) return "application/javascript; charset=UTF-8";
            if (path.endsWith(".png")) return "image/png";
            if (path.endsWith(".jpg") || path.endsWith(".jpeg")) return "image/jpeg";
            if (path.endsWith(".pdf")) return "application/pdf";
            return "text/plain; charset=UTF-8";
        }
    }

    // ==========================================
    // AUTH HANDLERS
    // ==========================================
    static class LoginHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if ("OPTIONS".equalsIgnoreCase(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            JsonObject json = JsonParser.parseString(body).getAsJsonObject();
            String email = json.get("email").getAsString();
            String password = json.get("password").getAsString();

            User user = userDAO.loginUser(email, password);
            Map<String, Object> resp = new HashMap<>();

            if (user != null) {
                resp.put("success", true);
                resp.put("user", user);
            } else {
                resp.put("success", false);
                resp.put("message", "Invalid email or password.");
            }

            sendJsonResponse(exchange, 200, resp);
        }
    }

    static class RegisterHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if ("OPTIONS".equalsIgnoreCase(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            JsonObject json = JsonParser.parseString(body).getAsJsonObject();

            String name = json.get("name").getAsString();
            String email = json.get("email").getAsString();
            String password = json.get("password").getAsString();
            String role = json.has("role") ? json.get("role").getAsString() : "STUDENT";
            String department = json.has("department") ? json.get("department").getAsString() : "General";

            User user = new User(0, name, email, password, role, department);
            boolean created = userDAO.registerUser(user);

            Map<String, Object> resp = new HashMap<>();
            resp.put("success", created);
            if (created) {
                resp.put("user", user);
            } else {
                resp.put("message", "Registration failed. Email may already be in use.");
            }

            sendJsonResponse(exchange, 200, resp);
        }
    }

    // ==========================================
    // COMPLAINT HANDLERS
    // ==========================================
    static class SubmitComplaintHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if ("OPTIONS".equalsIgnoreCase(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            JsonObject json = JsonParser.parseString(body).getAsJsonObject();

            Complaint c = new Complaint();
            c.setUserId(json.get("userId").getAsInt());
            c.setTitle(json.get("title").getAsString());
            c.setDescription(json.get("description").getAsString());
            c.setCategory(json.get("category").getAsString());
            c.setDepartment(c.getCategory());

            if (json.has("priority") && !json.get("priority").isJsonNull()) {
                c.setPriority(json.get("priority").getAsString());
            }

            if (json.has("attachmentPath") && !json.get("attachmentPath").isJsonNull()) {
                c.setAttachmentPath(json.get("attachmentPath").getAsString());
            }

            int id = complaintDAO.submitComplaint(c);
            Map<String, Object> resp = new HashMap<>();

            if (id > 0) {
                resp.put("success", true);
                resp.put("complaintId", id);
                resp.put("referenceId", c.getReferenceId());
                resp.put("priority", c.getPriority());
                resp.put("assignedCoordinator", c.getAssignedCoordinator());
            } else {
                resp.put("success", false);
                resp.put("message", "Unable to submit complaint to database.");
            }

            sendJsonResponse(exchange, 200, resp);
        }
    }

    static class MyComplaintsHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            String query = exchange.getRequestURI().getQuery();
            int userId = 1;
            if (query != null && query.contains("userId=")) {
                try {
                    userId = Integer.parseInt(query.split("userId=")[1].split("&")[0]);
                } catch (Exception ignored) {}
            }

            List<Complaint> list = complaintDAO.getComplaintsByUser(userId);
            sendJsonResponse(exchange, 200, list);
        }
    }

    static class AllComplaintsHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            List<Complaint> list = complaintDAO.getAllComplaints();
            sendJsonResponse(exchange, 200, list);
        }
    }

    static class TrackComplaintHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            String query = exchange.getRequestURI().getQuery();
            String ref = "";
            if (query != null && query.contains("referenceId=")) {
                ref = query.split("referenceId=")[1].split("&")[0];
            }

            Complaint c = complaintDAO.trackComplaint(ref);
            if (c != null) {
                sendJsonResponse(exchange, 200, c);
            } else {
                Map<String, Object> err = new HashMap<>();
                err.put("error", "Complaint not found");
                sendJsonResponse(exchange, 404, err);
            }
        }
    }

    static class ActionTakenHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if ("OPTIONS".equalsIgnoreCase(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            JsonObject json = JsonParser.parseString(body).getAsJsonObject();

            int id = json.get("complaintId").getAsInt();
            String remarks = json.get("remarks").getAsString();

            boolean ok = complaintDAO.recordActionTaken(id, remarks);
            Map<String, Object> resp = new HashMap<>();
            resp.put("success", ok);
            sendJsonResponse(exchange, 200, resp);
        }
    }

    static class RateComplaintHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if ("OPTIONS".equalsIgnoreCase(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            JsonObject json = JsonParser.parseString(body).getAsJsonObject();

            int id = json.get("complaintId").getAsInt();
            int rating = json.get("rating").getAsInt();
            String feedback = json.has("feedback") && !json.get("feedback").isJsonNull() ? json.get("feedback").getAsString() : "";

            boolean ok = complaintDAO.submitStudentFeedback(id, rating, feedback);
            Map<String, Object> resp = new HashMap<>();
            resp.put("success", ok);
            if (!ok) {
                resp.put("message", "Rating must be between 1 and 5 stars.");
            }
            sendJsonResponse(exchange, 200, resp);
        }
    }

    static class EscalateHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            if ("OPTIONS".equalsIgnoreCase(exchange.getRequestMethod())) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            JsonObject json = JsonParser.parseString(body).getAsJsonObject();

            int id = json.get("complaintId").getAsInt();
            String target = json.has("targetRole") ? json.get("targetRole").getAsString() : "HOD";

            boolean ok = complaintDAO.manualEscalate(id, target);
            Map<String, Object> resp = new HashMap<>();
            resp.put("success", ok);
            sendJsonResponse(exchange, 200, resp);
        }
    }

    static class CheckEscalationHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            addCorsHeaders(exchange);
            int count = complaintDAO.checkAndEscalateBreachedTickets();
            Map<String, Object> resp = new HashMap<>();
            resp.put("success", true);
            resp.put("escalatedCount", count);
            sendJsonResponse(exchange, 200, resp);
        }
    }

    // ==========================================
    // UTILITY METHODS
    // ==========================================
    private static void addCorsHeaders(HttpExchange exchange) {
        exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
        exchange.getResponseHeaders().set("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
        exchange.getResponseHeaders().set("Access-Control-Allow-Headers", "Content-Type, Authorization");
    }

    private static void sendJsonResponse(HttpExchange exchange, int status, Object data) throws IOException {
        String json = gson.toJson(data);
        byte[] bytes = json.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");
        exchange.sendResponseHeaders(status, bytes.length);
        try (OutputStream os = exchange.getResponseBody()) {
            os.write(bytes);
        }
    }
}