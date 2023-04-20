My code is written entirely in JAVA


I used XAMMP to run the database on my localhost server. 
The user can easily change the values to connect to the database in the mySQLConector.java file.


The 'mysql-connector-java-8.0.30.jar' in the project allows me to connect to the northwind database through the java.sql.DriverManager package.
The settings.JSON file in the .vscode folder specifies that this .jar file is added to the JAVA Project Library.


I use Visual Studio Code to edit and run my code.
My program will notify the user if the connection to the database was successful or not. 


EXTRA FEATURE:
An extra feature I added was the option to change an address. This options asks the user to specify if they want to change the address of an employee or a customer. My program then asks the user for a new address and a customer or employee ID number. If the ID is found in either the Customers table or the Employees table. The address will be updated.