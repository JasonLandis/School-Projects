<!DOCTYPE html>
<html lang="en">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <link rel="stylesheet" href="css/style.css">
    <title>Login Form</title>
</head>

<body>
    <div class="container" style="width: 340px;margin-top: 250px;">
        <header>Log in</header>
        <form action="accountpage.php" method="post" style="min-height: 250px;">                                
            <div class="fields">
                <div class="input-field">
                    <label>Student ID</label>
                    <input type="number" name="studentid" placeholder="Enter your student ID" required>
                </div>
                <div class="input-field">
                    <label>Password</label>
                    <input type="text" name="password" placeholder="Enter your password" required>
                </div>                        
            </div>
            <button name="login">Log in</button>
        </form>
    </div>    
</body>

</html>