<!DOCTYPE html>
<html lang="en">

<?php
include "mysqlcon.php";
?>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
    <link rel="stylesheet" href="css/style.css">
    <title>Account Created</title>
</head>

<?php
    $select = "select studentid, full_name, total_credits, year from student where studentid = (select max(studentid) from student)";
    $result = mysqli_query($conn, $select);
    $student = mysqli_fetch_array($result);
?> 

<body>
    <div class="container">
        <header>Account Created!</header>
        <form action="index.php" method="post">             
        <p>Thank you for signing up <strong><?php echo $student['full_name'] . "!";?></strong></p> 
        <br>
        <p>Your student ID is <strong><?php echo $student['studentid'];?></strong></p>         
        <br>        
        <p><strong>Be sure to remember this as you will need it when you login to your account!</strong></p>
        <br>
        <p>You will start as a<strong> 
        <?php
            $id = $student['studentid'];
            if ($student['total_credits'] <= 5) {
                echo "Freshman";
                $sql = "update student set year='FR' where studentid = $id;";
                mysqli_query($conn, $sql);
            }
            else if ($student['total_credits'] <= 10) {
                echo "Sophomore";
                $student['year'] = 'SO';
                $sql = "update student set year='SO' where studentid = $id;";
                mysqli_query($conn, $sql);
            }
            else if ($student['total_credits'] <= 15) {
                echo "Junior";
                $student['year'] = 'JR';
                $sql = "update student set year='JR' where studentid = $id;";
                mysqli_query($conn, $sql);
            }
            else if ($student['total_credits'] <= 20) {
                echo "Senior";
                $student['year'] = 'SR';
                $sql = "update student set year='SR' where studentid = $id;";
                mysqli_query($conn, $sql);
            } 
            else {
                echo "Senior";
                $student['year'] = 'SR';
                $sql = "update student set year='SR' where studentid = $id;";
                mysqli_query($conn, $sql);                
            }
        ?></strong> since you have <strong><?php echo $student['total_credits']; ?></strong> credits</p>
        <br>
        <?php 
            if ($student['total_credits'] > 20) {
                echo "You can graduate because you have over 20 credits!";
            }         
        ?>
        <br>
        <br>
        <img src="art/favicon.png" style: width="100%" align="center" vertic>                                           
        <button name="home" class="btnText">Home</button>            
        </form>       
    </div>
</body>

</html>