<?php
include "mysqlcon.php";

$sql = "select full_name, profession, email from staff;";

$res = mysqli_query($conn, $sql);

?>

<!DOCTYPE html>
<html lang="en">
	<head>
        <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
		<link rel="icon" href="art/favicon.ico">
		<link rel="stylesheet" href="css/style.css">		
		<title>Faculty</title>
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
        <div class="container" style="width: 855px;">
            <header>Faculty</header>
            <form style="min-height: 200px;">
            <table style="width: 850px;">
                <tr>
                    <th style="width: 850px;">Name</th>
                    <th style="width: 850px;">Profession</th>
                    <th style="width: 850px;">Contact</th>
                </tr>
<?php
foreach ($res as $res) {
    $full_name = $res['full_name'];
    $profession = $res['profession'];
    $email = $res['email'];
?>                
                <tr>
                    <td style="width: 850px;"><?php echo $full_name;?>
                    <td style="width: 850px;"><?php echo $profession;?>               
                    <td style="width: 850px;"><?php echo $email;?>                    
                </tr>

<?php
}
?>
            </table>
            </form>
        </div>
    </body>
</html>
