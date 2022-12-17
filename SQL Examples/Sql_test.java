import java.sql.*;

public class Main {
  public static void main(String[] args) {
    try {
      // Load the MySQL driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      // Establish a connection to the database
      String url = "jdbc:mysql://localhost:3306/database_name";
      String username = "username";
      String password = "password";
      Connection conn = DriverManager.getConnection(url, username, password);

      // Execute a SQL query
      String query = "SELECT * FROM table_name";
      Statement stmt = conn.createStatement();
      ResultSet rs = stmt.executeQuery(query);

      // Iterate over the result set and print the rows
      while (rs.next()) {
        int id = rs.getInt("id");
        String name = rs.getString("name");
        System.out.println(id + " " + name);
      }

      // Close the resources
      rs.close();
      stmt.close();
      conn.close();
    } catch (ClassNotFoundException e) {
      System.out.println("Unable to load the MySQL driver.");
    } catch (SQLException e) {
      System.out.println("An error occurred while connecting to the database.");
    }
  }
}
