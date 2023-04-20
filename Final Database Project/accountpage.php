<?php
include "mysqlcon.php";
session_start();

if (isset($_POST['login'])) {
    $studentid = mysqli_real_escape_string($conn, $_POST['studentid']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);

    $account = "select * from student where studentid = '$studentid' AND password = '$password'";
    $_SESSION['studentid'] = $studentid;
    $result = mysqli_query($conn, $account);
    if (mysqli_num_rows($result) == 1) {
        $student = mysqli_fetch_array($result);
?>
        <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">		
                    <link rel="stylesheet" href="css/style.css">
                    <title>Account Page</title>
                </head>
                <body>
                    <div class="container" style="width: 350px;">
                        <form method="post">
                            <header>Welcome <?php echo $student['full_name'];?>!</header>
                            <br>
                            <p>What would you like to do?<p>                            
                            <button name="course" class="btnText">Register for a course</button>                            
                            <button name="balance" class="btnText">Update your balance</button>
                            <button name="grades" class="btnText">View your grades</button>
                            <button name="graduate" class="btnText">Graduate</button>
                            <button name="logout" class="btnText">Log out</button>
                        </form>
                    </div>
                </body>
            </html>
<?php
    } 
    else {
        $staffid = mysqli_real_escape_string($conn, $_POST['studentid']);
        $password = mysqli_real_escape_string($conn, $_POST['password']);

        $account = "select * from staff where staffid = '$staffid' AND password = '$password'";
        $_SESSION['staffid'] = $staffid;
        $result = mysqli_query($conn, $account);
        if (mysqli_num_rows($result) == 1) {            
            $staff = mysqli_fetch_array($result);
            ?>
            <!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">		
                        <link rel="stylesheet" href="css/style.css">
                        <title>Account Page</title>
                    </head>
                    <body>
                        <div class="container" style="width: 350px;">
                            <form method="post">
                                <header>Welcome <?php echo $staff['full_name'];?>!</header>
                                <br>
                                <p>What would you like to do?<p>                            
                                <button name="viewstudents" class="btnText">View Students</button>
                                <button name="logout" class="btnText">Log out</button>
                            </form>
                        </div>
                    </body>
                </html>
                <?php
        } 
        else {
            echo ("<script LANGUAGE='JavaScript'> window.alert('Invalid login, try again'); window.location.href='loginform.php'; </script>");
        }
    }
}

if (isset($_POST['viewstudents'])) {
    $sql = "select studentid, full_name, total_credits from student;";
    $res = mysqli_query($conn, $sql);
    ?>    
    <link rel="stylesheet" href="css/style.css">
    <div class="container" style="width: 350px;">
            <header>List of Students</header>
            <form method="post">
            <table style="width: 350px;">
                <tr>
                    <th style="width: 350px;">student ID</th>
                    <th style="width: 350px;">Name</th>
                    <th style="width: 350px;">Total credits</th>                    
                </tr>

                <?php
                    foreach ($res as $res) {
                    $studentid = $res['studentid'];
                    $full_name = $res['full_name'];
                    $total_credits = $res['total_credits'];    
                ?>                
                            <tr>
                                <td style="width: 350px;"><?php echo $studentid;?>
                                <td style="width: 350px;"><?php echo $full_name;?>               
                                <td style="width: 350px;"><?php echo $total_credits;?>                    
                            </tr>

                <?php
                }
                ?>
            </table>
                <button name="logout" class="btnText">Log out</button>
            </form>
        </div>
    <?php           
}

$studentid = $_SESSION['studentid'];
$account = "select * from student where studentid = '$studentid'";
$result = mysqli_query($conn, $account);
$student = mysqli_fetch_array($result);

if (isset($_POST['course'])) {    
    ?>
    <link rel="stylesheet" href="css/style.css">
    <div class="container" style="width: 350px;">
        <form method="post">
            <header><?php echo $student['full_name'] . "'s Course Registration";?></header>
            <br>
            <p>You can register for upcoming courses by entering the course ID below</p>
            <br>                      
                <div class="input-field">                    
                    <input type="number" name="courseid" placeholder="Enter course ID">
                    <button type="submit" name="register" class="btnText">Register</button>
                    <button type="submit" name="courselist" class="btnText">View list of all courses</button>
                    <button type="submit" name="coursereg" class="btnText">View list of registered courses</button>
                    <button type="submit" name="back" class="btnText">Back</button>
                </div>            
        </form>
    </div>
    <?php  
}

if (isset($_POST['register'])) {
    $courseid = $_POST['courseid'];
    $sql = "select * from course where courseid = '$courseid'";
    $query = mysqli_query($conn, $sql);

    if (mysqli_num_rows($query) == 1) {
        $course = mysqli_fetch_array($query);
        $balance = $student['balance'];        
        $price = $course['price'];
        
        if ($price > $balance) {                    
            ?>
            <link rel="stylesheet" href="css/style.css">
            <div class="container" style="width: 350px;">
                <form method="post">
                    <header><?php echo $student['full_name'] . "'s Course Registration";?></header>
                    <br>
                    <p>You can register for upcoming courses by entering the course ID below</p>
                    <br>
                    <?php echo "You do not have enough funds in your account" ?>
                    <br>
                    <br>                      
                        <div class="input-field">                    
                            <input type="number" name="courseid" placeholder="Enter course ID">
                            <button type="submit" name="register" class="btnText">Register</button>
                            <button type="submit" name="courselist" class="btnText">View list of courses</button>
                            <button type="submit" name="coursereg" class="btnText">View list of registered courses</button>
                            <button type="submit" name="back" class="btnText">Back</button>
                        </div>            
                </form>
            </div>
            <?php
        }
        else {
            $sql = "insert into grades (studentid, courseid, grade) values ('$studentid', '$courseid', 'O');";
            mysqli_query($conn, $sql);
            ?>
            <link rel="stylesheet" href="css/style.css">
            <div class="container" style="width: 350px;">
                <form method="post">
                    <header><?php echo $student['full_name'] . "'s Course Registration";?></header>
                    <br>
                    <p>You can register for upcoming courses by entering the course ID below</p>
                    <br>
                    <?php echo "Class registered successfully" ?>
                    <br>
                    <br>
                        <div class="input-field">                    
                            <input type="number" name="courseid" placeholder="Enter course ID">
                            <button type="submit" name="register" class="btnText">Register</button>
                            <button type="submit" name="courselist" class="btnText">View list of courses</button>
                            <button type="submit" name="coursereg" class="btnText">View list of registered courses</button>
                            <button type="submit" name="back" class="btnText">Back</button>
                        </div>            
                </form>
            </div>
            <?php        
        }              
    }    
    else {
        ?>
        <link rel="stylesheet" href="css/style.css">
        <div class="container" style="width: 350px;">
            <form method="post">
                <header><?php echo $student['full_name'] . "'s Course Registration";?></header>
                <br>
                <p>You can register for upcoming courses by entering the course ID below</p>
                <br>
                <?php echo "Course not found" ?>
                <br>
                <br>                      
                    <div class="input-field">                    
                        <input type="number" name="courseid" placeholder="Enter course ID">
                        <button type="submit" name="register" class="btnText">Register</button>
                        <button type="submit" name="courselist" class="btnText">View list of courses</button>
                        <button type="submit" name="coursereg" class="btnText">View list of registered courses</button>
                        <button type="submit" name="back" class="btnText">Back</button>
                    </div>            
            </form>
        </div>
        <?php        
    } 
    
}

if (isset($_POST['courselist'])) { 
    $sql = "select courseid, subject, location, day, start_time, end_time, start_date, end_date, credits, price from course, room where course.roomid = room.roomid";

    $res = mysqli_query($conn, $sql);   
    ?>
    <link rel="stylesheet" href="css/style.css">
    <div class="container" style="width: 1505px">
            <header>Courses Available</header>
            <form method="post">
            <table>
                <tr>
                    <th>course ID</th>
                    <th>Subject</th>
                    <th>Location</th>
                    <th>Day</th>
                    <th>Start Time</th>
                    <th>End Time</th>
                    <th>Start Date</th>
                    <th>End Date</th>
                    <th>Credits</th>
                    <th>Price</th>
                </tr>

<?php
foreach ($res as $res) {
    $courseid = $res['courseid'];
    $subject = $res['subject'];
    $location = $res['location'];
    $day = $res['day'];
    $start_time = $res['start_time'];
    $end_time = $res['end_time'];
    $start_date = $res['start_date'];
    $end_date = $res['end_date'];
    $credits = $res['credits'];
    $price = $res['price'];
?>                
                <tr>
                    <td><?php echo $courseid;?>
                    <td><?php echo $subject;?>               
                    <td><?php echo $location;?>
                    <td><?php echo $day;?>
                    <td><?php echo $start_time;?>
                    <td><?php echo $end_time;?>
                    <td><?php echo $start_date;?>
                    <td><?php echo $end_date;?>
                    <td><?php echo $credits;?>
                    <td>$<?php echo $price;?>
                </tr>

<?php
}
?>
            </table>
            <button type="submit" name="back" class="btnText">Back</button>
            </form>
        </div>
    <?php  
}

if (isset($_POST['coursereg'])) {
    $sql = "select subject, grade, credits from grades, course where grades.courseid = course.courseid AND studentid = '$studentid' AND grade = 'O'";
    $res = mysqli_query($conn, $sql);
    ?>    
    <link rel="stylesheet" href="css/style.css">
    <div class="container" style="width: 350px;">
            <header><?php echo $student['full_name'] . "'s Registered Courses";?></header>
            <form method="post">
            <table style="width: 350px;">
                <tr>
                    <th style="width: 350px;">Course</th>
                    <th style="width: 350px;">Grade</th>
                    <th style="width: 350px;">Credits</th>                    
                </tr>

                <?php
                    foreach ($res as $res) {
                    $subject = $res['subject'];
                    $grade = $res['grade'];
                    $credits = $res['credits'];    
                ?>                
                            <tr>
                                <td style="width: 350px;"><?php echo $subject;?>
                                <td style="width: 350px;"><?php echo $grade;?>               
                                <td style="width: 350px;"><?php echo $credits;?>                    
                            </tr>

                <?php
                }
                ?>
            </table>
                <button type="submit" name="back" class="btnText">Back</button>
            </form>
        </div>
    <?php           
}

if (isset($_POST['balance'])) {    
    ?>
    <link rel="stylesheet" href="css/style.css">
    <div class="container" style="width: 350px;">
        <form method="post">
            <header><?php echo $student['full_name'] . "'s Balance";?></header>
            <p>Your current balance is <?php echo $student['balance']; ?></p>
            <br>                      
            <div class="input-field">                    
                <input type="number" name="amount" placeholder="Enter amount to add">
                <button type="submit" name="submit_balance" class="btnText">Submit</button>                
                <button type="submit" name="back" class="btnText">Back</button>
            </div>
        </form>
    </div>
    <?php  
}

if (isset($_POST['submit_balance'])) {
    if (!empty($_POST['amount'])) {       
        $balance = $student['balance'];
        $addbalance = $_POST['amount'];
        $newbalance = $balance + $addbalance;  
        $sql = "update student set balance = '$newbalance' where studentid = '$studentid';";
        mysqli_query($conn, $sql);

        ?>
        <link rel="stylesheet" href="css/style.css">
        <div class="container" style="width: 350px;">
            <form method="post">
                <header><?php echo $student['full_name'] . "'s Balance";?></header>
                <p>Your current balance is <?php echo $newbalance; ?></p>
                <br>                      
                <div class="input-field">                    
                    <input type="number" name="amount" placeholder="Enter amount to add">
                    <button type="submit" name="submit_balance" class="btnText">Submit</button>                
                    <button type="submit" name="back" class="btnText">Back</button>
                </div>
            </form>
        </div>
        <?php
    }    
}

if (isset($_POST['grades'])) {
    $sql = "select subject, grade, credits from grades, course where grades.courseid = course.courseid AND studentid = '$studentid' AND grade <> 'O'";
    $res = mysqli_query($conn, $sql);
    ?>    
    <link rel="stylesheet" href="css/style.css">
    <div class="container" style="width: 350px;">
            <header><?php echo $student['full_name'] . "'s Grades";?></header>
            <form method="post">
            <table style="width: 350px;">
                <tr>
                    <th style="width: 350px;">Course</th>
                    <th style="width: 350px;">Grade</th>
                    <th style="width: 350px;">Credits Earned</th>                    
                </tr>

                <?php
                    foreach ($res as $res) {
                    $subject = $res['subject'];
                    $grade = $res['grade'];
                    $credits = $res['credits'];    
                ?>                
                            <tr>
                                <td style="width: 350px;"><?php echo $subject;?>
                                <td style="width: 350px;"><?php echo $grade;?>               
                                <td style="width: 350px;"><?php echo $credits;?>                    
                            </tr>

                <?php
                }
                ?>
            </table>
                <button type="submit" name="back" class="btnText">Back</button>
            </form>
        </div>
    <?php           
}

if (isset($_POST['graduate'])) {    
    ?>
    <link rel="stylesheet" href="css/style.css">
    <div class="container" style="width: 350px;">
        <form method="post">            
            <header>
            <?php
                if ($student['total_credits'] > 20) {
                    echo $student['full_name'] . ", you are able to graduate!";
                    ?><br><br><?php
                    echo "The graduation requirement is completion of over 20 credits. You have completed " . $student['total_credits'] . " credits.";
                } 
                else {
                    echo $student['full_name'] . ", you are not able to graduate just yet...";
                    ?><br><br><?php
                    echo "The graduation requirement is completion of over 20 credits. You have completed " . $student['total_credits'] . " credits.";
                } 
            ?>
            </header>
            <button type="submit" name="back" class="btnText">Back</button>
        </form>
    </div>
    <?php           
}

if (isset($_POST['back'])) { 
    ?>
    <link rel="stylesheet" href="css/style.css">  
    <div class="container" style="width: 350px;">
        <form method="post">
            <header>Welcome <?php echo $student['full_name'];?>!</header>
            <br>
            <p>What would you like to do?<p>                            
            <button name="course" class="btnText">Register for a course</button>                            
            <button name="balance" class="btnText">Update your balance</button>
            <button name="grades" class="btnText">View your grades</button>
            <button name="graduate" class="btnText">Graduate</button>
            <button name="logout" class="btnText">Log out</button>
        </form>
    </div>
    <?php       
}

if (isset($_POST['logout'])) {    
    header("Location: index.php");       
}
?>
