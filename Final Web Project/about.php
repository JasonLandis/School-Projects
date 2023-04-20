<?php include('contact.php') ?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
         <title>About</title>
        <link href="css/styles.css" rel="stylesheet" />
        <link href = "css/custom-styles.css" rel="stylesheet" />
    </head>
    <style>
        

    </style>
    <body style="background-image: url('images/background.jpg')">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container px-5">
                <a class="navbar-brand" href="#!">Filmology</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item">
				<a class="nav-link" aria-current="page" href="index.php">Home</a>
			  </li>
			  <li class="nav-item">
				<a class="nav-link" href="c41.php">C-41 Processing</a>
			  </li>
			  <li class="nav-item">
				<a class="nav-link" href="b&w.php">Black & White Processing</a>
			  </li>
			  <li class="nav-item">
				<a class="nav-link" href="catalog.php">Equipment</a>
			  </li>
			  <li class="nav-item">
				<a class="nav-link" href="about.php">About</a>
			  </li>
                    </ul>
                </div>
            </div>
        </nav>			
			<div class="card text-white bg-secondary my-5 py-4 text-center">
				<div class="card-body"><h1 class="text-white m-0"><strong>About Us</strong></h1></div>
			</div>
            <div class="container px-4 px-lg-5">
			<div class="row gx-5 gx-lg-5">
                <div class="col-md-4 mb-5">
                    <div class="custom-card">
                        <div class="card-body">
                            <h2 class="card-title"><strong>Zack Scarpelli</strong></h2>
                            <p class="card-text">Hi! I'm Zack and I have been taking photos on film for almost a year now, and have been using a digital camera for almost 2. The process of home developing film is captivating to me; the ability to transform a piece of plastic coated in silver into a photograph is fascinating. When I saw there was an option to do a tutorial website, I knew I wanted to do a tutorial on film developing. I wrote most of the HTML and website content, took all of the images, and did the Javascript and jQuery elements of the project.</p>
                        </div>                        
                    </div>
                </div>
                <div class="col-md-4 mb-5">
                    <div class="custom-card">
                        <div class="card-body">
                            <h2 class="card-title"><strong>Praveen Kumar</strong></h2>
                            <p class="card-text">Hey, I'm Praveen, Our projects is based on how to develop films at home. In this project I have majorly contributed to building the databases and the working with PHP. I have also worked on some of the styling for the cards.</p>
                        </div>                        
                    </div>
                </div>
                <div class="col-md-4 mb-5">
                    <div class="custom-card">
                        <div class="card-body">
                            <h2 class="card-title"><strong>Jason Landis</strong></h2>
                            <p class="card-text">Hi, I'm Jason. Many people, myself included, do not know much about developing a film let alone doing it yourself at home. This website goes through the basics and provides helpful information for anyone who is interested in the process. I have learned, not only about the process of film development, but the process of making a website. I feel I am much better now at using CSS to express my creativity and to more importantly, captivate the viewer to keep them interested.</p>
                        </div>                        
                    </div>
                </div>
            </div>
            </div>                       
                                             
            <div class="contact">  
                                           
                <form name="frmContact" method="post" action="contact.php">
                <h1><strong>Contact us!</strong></h1>
                <br>
                <?php include('errors.php'); ?>  
                <p class="field1">
                <label for="Name"><b>Name</b></label>
                <input type="text" placeholder="Enter your name" name="firstName" id="txtName" required>
                </p>
                <p class="field2">
                <label for="email"><b>Email</b></label>
                <input type="text" placeholder="Enter Email" name="Email" id="txtEmail" required>
                </p>
                <p class="field3">
                <label for="message"><b>Message</b></label>
                <textarea name="Message" placeholder="Enter message" id="txtMessage"></textarea>
                </p>
                <p>
                <input type="submit" name="Submit" id="Submit" value="Submit">
                </p>
            </div>
            </div>
            </div>                        
			<footer class="py-5 bg-dark">
				<div class="col-lg-12"><h2 class="m-0 text-center text-white"><strong>Film Developing - The Basics</strong></h2>
				<p class="m-0 text-center text-white">&copy; 2021 Copyright: film-developing.com</p></div>        
			</footer>
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
		<script src="js/scripts.js"></script>		
	</body>
</html>
