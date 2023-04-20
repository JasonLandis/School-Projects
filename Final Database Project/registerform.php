<!DOCTYPE html>
<html lang="en">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <link rel="stylesheet" href="css/style.css">
    <title>Register Form</title>
</head>

<body>
    <div class="container" style="width: 340px;">
        <header>Registration</header>

        <form method="post">            
            <div class="fields">
                <div class="input-field">
                    <label>Full Name</label>
                    <input type="text" name="full_name" placeholder="Enter your name" required>
                </div>

                <div class="input-field">
                    <label>Email</label>
                    <input type="text" name="email" placeholder="Enter your email" required>
                </div>

                <div class="input-field">
                    <label>Password</label>
                    <input name="password" id="password" type="password" placeholder="Enter your password" onChange="checkPassword()" required/>
                </div>

                <div class="input-field">
                    <label>Confirm Password</label>
                    <input type="password" name="confirm_password" id="confirm_password"
                        placeholder="Confirm your password" onChange="checkPassword()" required/>
                    <span id='message'></span>
                </div>

                <div class="input-field">
                    <label>Credits</label>
                    <Span class="credits">If you are a transfer student, enter any number of credits you have already recieved from another school</span>
                    <input type="number" name="total_credits" placeholder="Enter amount of credits recieved" required>
                </div>

                <div class="input-field">
                    <label>Balance</label>
                    <input type="number" name="balance" placeholder="Enter your account balance" required>
                </div>
            </div>
            <button name="submit" class="btnText">Submit</button>
        </form>
    </div>
    <script src="scripts/script.js"></script>
</body>

</html>

<?php

include "mysqlcon.php";

if (isset($_POST['submit'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];
    $full_name = $_POST['full_name'];
    $total_credits = $_POST['total_credits'];
    $balance = $_POST['balance'];

    $query = "insert into student (email, password, full_name, total_credits, balance) values ('$email', '$password', '$full_name', '$total_credits', '$balance')";

    mysqli_query($conn, $query) or die(mysqli_error($conn));

    header("Location: success.php");    
}
?>