<?php
include "mysqlcon.php";

$sql = "select courseid, subject, location, day, start_time, end_time, start_date, end_date, credits, price from course, room where course.roomid = room.roomid";

$res = mysqli_query($conn, $sql);

?>

<!DOCTYPE html>
<html lang="en">
	<head>
        <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
		<link rel="icon" href="art/favicon.ico">
		<link rel="stylesheet" href="css/style.css">
		<title>Courses</title>	 
	</head>
		<header>
			<div class="topnav">
				<ul>
					<img src="art/wmu-logo.svg" style: width="15%" align="right" vertic>
					<a href="index.php">Home</a>					
					<a href="courses.php">Courses</a>
					<a href="faculty.php">Faculty</a>
				</ul>					
			</div>
		</header>
    </head>
    <body>
        <div class="container" style="width: 1505px">
            <header>Courses Available</header>
            <form style="min-height: 300px;">
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
            </form>
        </div>
    </body>
</html>
