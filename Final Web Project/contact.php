<?php 
$errors = array();
$success = array();
$con = mysqli_connect('localhost', 'testuser', 'mypassword','product');

if (isset($_POST['Submit'])){
	$full_name = $_POST['firstName'];
	$email = $_POST['Email'];
	$message = $_POST["Message"];

	if (empty($full_name)){
		array_push($errors, "Please Enter Full Name.");
	}
	if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)){
		array_push($errors, "Please Enter your Email.");
	}
		
	if (empty($message)){
		array_push($errors, "Please Enter your message.");
	}


		$sql = "INSERT INTO `enquiry` (`Id`, `FullName`, `Email`, `Message`)  VALUES ('0', '$full_name', '$email', '$message') ";
	
		$rs = mysqli_query($con, $sql);
	
		if($rs)
		{
			echo '<script>alert("Your Message Has been Sent!")</script>';
		}
}


?>