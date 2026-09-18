package dao;

import model.User;
import util.DatabaseConnection;
import util.PasswordUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class UserDAO {

    public boolean registerUser(User user) {
        String sql = "INSERT INTO users (name, email, password, role, department) VALUES (?, ?, ?, ?, ?)";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql, java.sql.Statement.RETURN_GENERATED_KEYS)) {

            String hashedPassword = PasswordUtil.hashPassword(user.getPassword());

            statement.setString(1, user.getName());
            statement.setString(2, user.getEmail().trim().toLowerCase());
            statement.setString(3, hashedPassword);
            statement.setString(4, user.getRole() != null ? user.getRole().toUpperCase() : "STUDENT");
            statement.setString(5, user.getDepartment() != null ? user.getDepartment() : "General");

            int rowsInserted = statement.executeUpdate();
            if (rowsInserted > 0) {
                var keys = statement.getGeneratedKeys();
                if (keys.next()) {
                    user.setId(keys.getInt(1));
                }
                return true;
            }
            return false;

        } catch (SQLException e) {
            System.err.println("Registration failed: " + e.getMessage());
            return false;
        }
    }

    public User loginUser(String email, String password) {
        String sql = "SELECT * FROM users WHERE LOWER(email) = LOWER(?)";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setString(1, email.trim());
            ResultSet resultSet = statement.executeQuery();

            if (resultSet.next()) {
                String storedPassword = resultSet.getString("password");

                if (PasswordUtil.checkPassword(password, storedPassword)) {
                    String dept = "General";
                    try {
                        dept = resultSet.getString("department");
                    } catch (SQLException ignored) {}

                    return new User(
                            resultSet.getInt("id"),
                            resultSet.getString("name"),
                            resultSet.getString("email"),
                            storedPassword,
                            resultSet.getString("role"),
                            dept
                    );
                }
            }

        } catch (SQLException e) {
            System.err.println("Login failed: " + e.getMessage());
        }

        return null;
    }

    public User getUserById(int userId) {
        String sql = "SELECT * FROM users WHERE id = ?";
        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setInt(1, userId);
            ResultSet rs = statement.executeQuery();
            if (rs.next()) {
                String dept = "General";
                try {
                    dept = rs.getString("department");
                } catch (SQLException ignored) {}

                return new User(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("email"),
                        rs.getString("password"),
                        rs.getString("role"),
                        dept
                );
            }
        } catch (SQLException e) {
            System.err.println("Error getting user by id: " + e.getMessage());
        }
        return null;
    }

    public List<User> getAllUsers() {
        List<User> list = new ArrayList<>();
        String sql = "SELECT id, name, email, role, department FROM users ORDER BY id DESC";

        try (Connection connection = DatabaseConnection.getConnection();
             PreparedStatement statement = connection.prepareStatement(sql);
             ResultSet rs = statement.executeQuery()) {

            while (rs.next()) {
                String dept = "General";
                try {
                    dept = rs.getString("department");
                } catch (SQLException ignored) {}

                list.add(new User(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("email"),
                        "",
                        rs.getString("role"),
                        dept
                ));
            }

        } catch (SQLException e) {
            System.err.println("Error retrieving users: " + e.getMessage());
        }
        return list;
    }
}