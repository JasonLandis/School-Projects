import java.sql.*;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static Scanner input = new Scanner(System.in);
    public static mySQLConnector database;

    public static void main(String[] args) throws SQLException {
        // initializes connection
        database = new mySQLConnector();
        options();
    }

    private static void options() throws SQLException {
        while (true) {
            System.out.print(
                    "List of options\n"
                            + "----------------\n"
                            + "1: Add a customer\n"
                            + "2: Add an order\n"
                            + "3: Remove an order\n"
                            + "4: Ship an order\n"
                            + "5: Print pending orders\n"
                            + "6: Restock parts\n"
                            + "7: Change Address\n" // My additional feature
                            + "8: Exit\n"
                            + "----------------\n"
                            + "Select your choice: ");
            try {
                int choice = input.nextInt();
                input.nextLine();
                switch (choice) {
                    case 1:
                        addACustomer();
                        break;
                    case 2:
                        addAnOrder();
                        break;
                    case 3:
                        removeAnOrder();
                        break;
                    case 4:
                        shipAnOrder();
                        break;
                    case 5:
                        printPendingOrders();
                        break;
                    case 6:
                        restockParts();
                        break;
                    case 7:
                        changeAddress();
                        break;
                    case 8:
                        exit();
                        return;
                    default:
                        System.out.println("Please select an option\n\n");
                        break;
                }

            } catch (InputMismatchException error) {
                System.out.println("Please enter a number\n");
                input.nextLine();
            }
        }
    }

    private static void addACustomer() throws SQLException {
        // asks each value for customer
        System.out.print("Enter Customer's Name: ");
        String ContactName = input.nextLine();

        System.out.print("Enter Customer's Company's Name: ");
        String CompanyName = input.nextLine();

        System.out.print("Enter Customer's Title: ");
        String ContactTitle = input.nextLine();

        System.out.print("Enter Customer's Address: ");
        String Address = input.nextLine();

        System.out.print("Enter Customer's City: ");
        String City = input.nextLine();

        System.out.print("Enter Customer's Region: ");
        String Region = input.nextLine();

        System.out.print("Enter Customer's Zipcode: ");
        String PostalCode = input.nextLine();

        System.out.print("Enter Customer's Country: ");
        String Country = input.nextLine();

        System.out.print("Enter Customer's Phone: ");
        String Phone = input.nextLine();

        System.out.print("Enter Customer's Fax: ");
        String Fax = input.nextLine();

        // Creates unique CustomerID key Adds all values to database
        String CustomerID = "";
        try {
            CustomerID = CompanyName.substring(0, 5).toUpperCase();
            database.executeUpdate("INSERT INTO Customers VALUES ('" + CustomerID + "','" + CompanyName + "','"
                    + ContactName + "','" + ContactTitle + "','" + Address + "','" + City + "','" + Region + "','"
                    + PostalCode + "','" + Country + "','" + Phone + "','" + Fax + "')");
        } catch (Exception error) {
            CustomerID = CompanyName.substring(1, 6).toUpperCase();
            database.executeUpdate("INSERT INTO Customers VALUES ('" + CustomerID + "','" + CompanyName + "','"
                    + ContactName + "','" + ContactTitle + "','" + Address + "','" + City + "','" + Region + "','"
                    + PostalCode + "','" + Country + "','" + Phone + "','" + Fax + "')");
        }

        System.out.print("Customer Successfully Added\n\n");
    }

    private static void addAnOrder() throws SQLException {
        // Finds product to be ordered and checks if it is in the database
        ResultSet Products;
        System.out.print("Enter Product ID: ");
        int ProductID = input.nextInt();
        Products = database.executeQuery("SELECT * FROM Products WHERE ProductID = " + ProductID + ";");
        boolean isEmpty = Products.next();
        if (isEmpty == false) {
            System.out.println("The product number entered does not match any products on record\n\n");
            return;
        }

        // Checks if the product is discontinued
        char Discontinued = Products.getString("Discontinued").charAt(0);
        if (Discontinued == 'y') {
            System.out.println("This product has been discontinued\n\n");
            return;
        }

        // Asks for quantity of product to order
        System.out.print("Enter Quantity of Product: ");
        int Quantity = input.nextInt();
        input.nextLine();
        int available = Products.getInt("UnitsInStock");
        if (available < Quantity) {
            System.out.print("There are only " + available + " products remaining\n\n");
            return;
        }

        // Asks for CustomerID
        ResultSet Customers;
        System.out.print("Enter Customer's ID: ");
        String CustomerID = input.nextLine();
        Customers = database.executeQuery("SELECT * FROM Customers WHERE CustomerID = '" + CustomerID + "';");
        isEmpty = Customers.next();
        if (isEmpty == false) {
            System.out.print("The customer number entered does not match any customers on record\n\n");
            return;
        }

        // Asks for EmployeeID
        ResultSet Employees;
        System.out.print("Enter Employee's ID: ");
        int EmployeeID = input.nextInt();
        Employees = database.executeQuery("SELECT * FROM Employees WHERE EmployeeID = '" + EmployeeID + "';");
        isEmpty = Employees.next();
        if (isEmpty == false) {
            System.out.print("The employee number entered does not match any employees on record\n\n");
            return;
        }

        // Finds max order and adds 1 to create a new OrderID
        ResultSet Orders;
        Orders = database.executeQuery("SELECT MAX(OrderID) FROM Orders;");
        Orders.next();
        int OrderID = Orders.getInt(1) + 1;

        // Finds max ID and adds 1 to create a new ID
        ResultSet Order_details;
        Order_details = database.executeQuery("SELECT MAX(ID) FROM Order_details;");
        Order_details.next();
        int ID = Order_details.getInt(1) + 1;

        // Gets the current date and time
        java.util.Date currentTime = new java.util.Date();
        java.text.SimpleDateFormat sdf = new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String Date = sdf.format(currentTime);

        // Updates the Units on order value
        database.executeUpdate(
                "UPDATE Products SET UnitsOnOrder = " + Quantity + " WHERE ProductID = " + ProductID + ";");

        // Decreases the amount in stock
        database.executeUpdate("UPDATE Products SET UnitsInStock = " + (available - Quantity) + " WHERE ProductID = "
                + ProductID + ";");

        // Updates Orders table
        database.executeUpdate(
                "INSERT INTO Orders (OrderID, CustomerID, EmployeeID, OrderDate, ShipVia) VALUES (" + OrderID
                        + ",'" + CustomerID + "'," + EmployeeID + ",'" + Date + "'," + 3 + ");");

        // Updates Order_details table
        database.executeUpdate("INSERT INTO Order_details (ID, OrderID, ProductID) VALUES (" + ID + "," + OrderID + ","
                + ProductID + ");");

        Products.close();
        Customers.close();
        Employees.close();
        Order_details.close();
        Orders.close();
        System.out.print("The order has been placed\n\n");

    }

    private static void removeAnOrder() throws SQLException {
        // Finds order to be removed and checks if it is in the database
        ResultSet Orders;
        System.out.print("Enter Order ID to Remove: ");
        int OrderID = input.nextInt();
        Orders = database.executeQuery("SELECT * FROM Orders WHERE OrderID = " + OrderID + ";");
        boolean isEmpty = Orders.next();
        if (isEmpty == false) {
            System.out.println("The order number entered does not match any orders on record\n\n");
            return;
        }

        // Gets the quantity ordered and the ProductID of order from Order_details table
        ResultSet Order_details;
        Order_details = database.executeQuery("SELECT * From Order_details WHERE OrderID = " + OrderID + ";");
        Order_details.next();
        int Quantity = Order_details.getInt("Quantity");
        int ProductID = Order_details.getInt("ProductID");

        // Gets the UnitsOnOrder value from Product table with the same ProductID
        ResultSet Products;
        Products = database.executeQuery("SELECT * FROM Products WHERE ProductID = " + ProductID + ";");
        Products.next();
        int UnitsOnOrder = Products.getInt("UnitsOnOrder");

        // Removes the UnitsOnOrder by the quantity of the order
        database.executeUpdate(
                "UPDATE Products SET UnitsOnOrder = " + (UnitsOnOrder + Quantity) + " WHERE ProductID = " + ProductID
                        + ";");

        // Removes order from both Orders and Order_details
        database.executeUpdate("DELETE FROM Order_details WHERE OrderID = " + OrderID + ";");
        database.executeUpdate("DELETE FROM Orders WHERE OrderID = " + OrderID + ";");

        Orders.close();
        Order_details.close();
        Products.close();
        System.out.println("Order " + OrderID + " has been removed\n\n");
    }

    private static void shipAnOrder() throws SQLException {
        // Finds order to be shipped and checks if it is in the database
        ResultSet Orders;
        System.out.print("Enter Order ID to ship: ");
        int OrderID = input.nextInt();
        Orders = database
                .executeQuery("SELECT * FROM Orders WHERE OrderID = " + OrderID + " AND ShippedDate IS NULL;");
        boolean isEmpty = Orders.next();
        if (isEmpty == false) {
            System.out.println(
                    "The order number entered does not match any orders on record that have not already been shipped\n\n");
            return;
        }

        // Gets current date and time
        java.util.Date currentTime = new java.util.Date();
        java.text.SimpleDateFormat sdf = new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String Date = sdf.format(currentTime);

        // Updates the ShippedDate value of selected order
        database.executeUpdate("UPDATE Orders SET ShippedDate = '" + Date + "' WHERE OrderID = " + OrderID + ";");

        Orders.close();
        System.out.print("Order " + OrderID + " has been shipped\n\n");
    }

    private static void printPendingOrders() throws SQLException {
        // Selects values from Order table to be printed where ShippedDate is NULL
        ResultSet Orders;
        Orders = database.executeQuery(
                "SELECT OrderID, CustomerID, OrderDate, ShippedDate FROM Orders WHERE ShippedDate IS NULL;");
        System.out
                .printf("-------------------------------------------------\n"
                        + "| %7s | %10s | %-10s | %-10s\n"
                        + "-------------------------------------------------\n",
                        "OrderID", "CustomerID", "OrderDate", "ShippedDate");

        // Follows through each row and prints selected values
        while (Orders.next()) {
            System.out.printf("| %7d | %10s | %-10s | %-10d\n", Orders.getInt("OrderID"),
                    Orders.getString("CustomerID"), Orders.getDate("OrderDate"), Orders.getDate("ShippedDate"));
            System.out
                    .printf("-------------------------------------------------\n");
        }

        Orders.close();
        System.out.println("End of List\n\n");
    }

    private static void restockParts() throws SQLException {
        // Finds Products to be restocked and checks if it is in the database
        ResultSet Products;
        System.out.print("Enter Product ID to Restock: ");
        int ProductID = input.nextInt();
        Products = database.executeQuery("SELECT * FROM Products WHERE ProductID = " + ProductID + ";");
        boolean isEmpty = Products.next();
        if (isEmpty == false) {
            System.out.println("The product number entered does not match any products on record\n\n");
            return;
        }

        // Gets the current UnitsInStock
        int UnitsInStock = Products.getInt("UnitsInStock");

        // Asks for amount to be added
        System.out.print("Enter Quantity of Parts: ");
        int Quantity = input.nextInt();

        // Adds amount to database
        database.executeUpdate("UPDATE Products SET UnitsInStock = " + (UnitsInStock + Quantity) + " WHERE ProductID = "
                + ProductID + ";");

        Products.close();
        System.out.println("Product number " + ProductID + " now has " + (UnitsInStock + Quantity) + " in stock\n\n");
    }

    private static void changeAddress() throws SQLException {
        // Asks to change address of customer or employee
        System.out.print("Would you like to change the address of a Customer or Employee? ");
        String answer = input.nextLine();
        if (answer.toLowerCase().equals("customer")) {
            System.out.print("Enter a Customer ID: ");
            String CustomerID = input.nextLine();

            // Checks if customer is in the database
            ResultSet CustomerTable;
            CustomerTable = database.executeQuery("SELECT * FROM Customers WHERE CustomerID = '" + CustomerID + "';");
            boolean isEmpty = CustomerTable.next();
            if (isEmpty == false) {
                System.out.print("The customer you entered does not match any customers on record\n\n");
                return;
            }

            System.out.print("Enter a New Address: ");
            String Address = input.nextLine();

            // Updates with new address
            database.executeUpdate(
                    "UPDATE Customers SET Address = '" + Address + "' WHERE CustomerID = '" + CustomerID + "';");

            // Does the same above but with employee
        } else if (answer.toLowerCase().equals("employee")) {
            System.out.print("Enter a Employee ID: ");
            int EmployeeID = input.nextInt();

            ResultSet EmployeeTable;
            EmployeeTable = database.executeQuery("SELECT * FROM Employees WHERE EmployeeID = " + EmployeeID + ";");
            boolean isEmpty2 = EmployeeTable.next();
            if (isEmpty2 == false) {
                System.out.print("The employee you entered does not match any employees on record\n\n");
                return;
            }

            System.out.print("Enter a New Address: ");
            String Address = input.nextLine();
            input.nextLine();

            database.executeUpdate("UPDATE Employees SET Address = '" + Address + "' WHERE EmployeeID = "
                    + EmployeeID + ";");
        } else {
            System.out.print("Please enter 'Customer' or 'Employee'\n\n");
            return;
        }

        System.out.println("Address Changed\n\n");
    }

    private static void exit() throws SQLException {
        // Exits
        System.out.print("Exiting\n\n");
        database.conn.close();
    }
}