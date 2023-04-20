import java.sql.*;

public class mySQLConnector {
    // Values to connect to database
    private final String userName = "root";
    private final String password = "";
    private final String serverName = "localhost";
    private final int portNumber = 3306;
    private final String dbName = "northwind";

    Connection conn = null;

    public mySQLConnector() {
        // Attempts connection
        try {
            conn = this.getConnection();
            System.out.println("The connection was successful...\n");
        } catch (SQLException error) {
            System.out.println("ERROR: The connection was unsuccessful...\n");
            error.printStackTrace();
            return;
        }
    }

    private Connection getConnection() throws SQLException {
        // Connects using the jdbc driver in the project
        Connection conn = null;
        conn = DriverManager.getConnection(
                "jdbc:mysql://" + this.serverName + ":" + this.portNumber + "/" + this.dbName, userName, password);
        return conn;
    }

    public boolean executeUpdate(String command) throws SQLException {
        // Function to update the database using SQL
        Statement stmt = null;
        try {
            stmt = conn.createStatement();
            stmt.executeUpdate(command);
            return true;
        } finally {
            if (stmt != null) {
                stmt.close();
            }
        }
    }

    public ResultSet executeQuery(String command) throws SQLException {
        // Function to create a query from a database using SQL
        Statement stmt = null;
        stmt = conn.createStatement();
        return stmt.executeQuery(command);
    }
}