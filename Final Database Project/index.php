<!DOCTYPE html>
<html lang="en">
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
		<link rel="icon" href="art/favicon.ico">
		<link rel="stylesheet" href="css/style.css">		
		<title>Western Michigan University</title>	 
	</head>
	<body>
		<header>
			<div class="topnav">
				<ul>
					<img src="art/wmu-logo.svg" style: width="15%" align="right" vertic>
					<a href="#">Home</a>					
					<a href="courses.php">Courses</a>
					<a href="faculty.php">Faculty</a>
				</ul>					
			</div>
		</header>		
		<div class="container">
			<form method="post">
				<header>Welcome to Western Michigan University!</header>            	
				<p>We offer a special program where students can graduate with minimal credits required!</p>
				<p><strong>The credits system is as follows</strong></p>
				<ul>
					<li>If you have 5 or less credits you are considered a Freshman</li>
					<li>If you have between 6 and 10 credits you are considered a Sophomore</li>
					<li>If you have between 11 and 15 credits you are considered a Junior</li>
					<li>If you have between 16 and 20 credits you are considered a Senior</li>
					<li>If you have over 20 credits you are able to graduate!</li>
				</ul>
				<p><strong>Getting Started</strong></p>
				<p>Your first step will be to register as a student</p>
				<p>Once registered, you can login to your account and register for a course</p>
				<p>Once you achieve over 20 credits on your account, you can graduate!</p>			
				<button name="register" class="btnText">Register</button>
				<button name="login" class="btnText">Log in</button>
			</post>
		</div>		
	</body>
</html>

<?php

if (isset($_POST['register'])) {
	header("location: registerform.php");
}

if (isset($_POST['login'])) {
	header("location: loginform.php");
}