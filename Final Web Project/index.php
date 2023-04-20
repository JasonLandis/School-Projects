<?php 
  session_start(); 

  if (!isset($_SESSION['username'])) {
  	$_SESSION['msg'] = "You must log in first";
  }
  if (isset($_GET['logout'])) {
  	session_destroy();
  	unset($_SESSION['username']);
  	header("location: index.php");
  }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
         <title>Film Developing - The Basics</title>
        <link href="css/styles.css" rel="stylesheet" />
        <link href = "css/custom-styles.css" rel="stylesheet" />
    </head>
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
              <li class="nav-item">
              <?php  if (!isset($_SESSION['username'])) : ?>
    	        <a class="loginButton" href="Login.php">Login</a>
              <?php endif ?>

              <?php  if (isset($_SESSION['username'])) : ?>
    	        <a href="index.php?logout='1'" class="loginButton">Logout</a>
              <?php endif ?>
			  </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="content">
  	<!-- notification message -->
  	<?php if (isset($_SESSION['success'])) : ?>
      <div class="error success" >
      	<h3>
          <?php 
          	echo $_SESSION['success']; 
          	unset($_SESSION['success']);
          ?>
      	</h3>
      </div>
  	<?php endif ?>

      <?php  if (isset($_SESSION['username'])) : ?>
    	<p>Welcome <strong><?php echo $_SESSION['username']; ?></strong></p>
      <?php endif ?>

</div>
        <div class="container px-4 px-lg-5">
			<div class="row gx-4 gx-lg-5 align-items-center my-5">
                <div class="col-lg-5">
                    <h1 class="font-weight-light"><strong>Developing Film at Home</strong></h1>
                    <p>
                        <strong>If you like to take pictures on film, you know how much of a hassle it is to get your film developed. You have to mail the film to a lab and wait days or even weeks, and you pay a fortune to boot! What if I told you there was a much easier, more fulfilling, and much cheaper way to develop film? That's right, you can just do it yourself! This site contains comprehensive guides for home-developing both black and white and color negative film, and a catalog of items that you will need! For beginners, I recommend starting at the page for <a href="b&w.html">Black & White Developing</strong></a>.
                    </p> 
                </div>                          
                <div class="col-lg-7">
					<div id = "slideshow">
					<div>
						<img class="img-fluid rounded mb-4 mb-lg-0" id = "img5"  class = "img5 testimage" src="images/house.jpg" alt="house"/>
					</div>
					<div>
					<img class="img-fluid rounded mb-4 mb-lg-0" id = "img4"  class = "img4 testimage" src="images/road.jpg" alt="road"/>
					</div>
					<div>
					<img class="img-fluid rounded mb-4 mb-lg-0" id = "img3"  class = "img3 testimage" src="images/rabbit.jpg" alt="rabbit"/>
					</div>
					<div>
					<img class="img-fluid rounded mb-4 mb-lg-0" id = "img2"  class = "img2 testimage" src="images/peter.jpg" alt="peter"/>
					</div>
					<div>
					<img class="img-fluid rounded mb-4 mb-lg-0" id = "img1"  class = "img1 testimage" src="images/mitch.jpg" alt="mitch"/>
					</div>
					<div>
						<img class="img-fluid rounded mb-4 mb-lg-0" id = "img6" class = "img6 testimage" src="images/blackcanyon.jpg" alt="blackcanyon"/>
					</div>
					</div>
                    <span><strong>Cycle through to see some pictures taken on home developed film!
				<input id="imagecarousel" type = "submit" value = "Next Image" /></strong></span>
				</div>  
            </div>
            </div>
            <div class="card text-white bg-secondary my-5 py-4 text-center">
                <div class="card-body"><h1 class="text-white m-0"><strong>The Advantages of Home Developing</strong></h1></div>
            </div>            
            <div class="container px-4 px-lg-5">	           
            <div class="row gx-5 gx-lg-5">
                <div class="col-md-4 mb-5">
                    <div class="card h-100">
                        <div class="card-body">
                            <h2 class="card-title"><strong>Turnaround</strong></h2>
                            <p class="card-text">Home developing allows you to see your images much sooner than sending your film to a lab. If you don't home develop, you must mail your film away and wait until the lab processes it and mails it back. This process can take weeks, and some people can't wait that long to see their images. You could process your film immediately after finishing your photos!</p>
                        </div>                        
                    </div>
                </div>
                <div class="col-md-4 mb-5">
                    <div class="card h-100">
                        <div class="card-body">
                            <h2 class="card-title"><strong>Creative Control</strong></h2>
                            <p class="card-text">If your picture is overexposed or underexposed in camera, you can fix that in home developing! You can adjust the developing time to brighten or darken an image and add a few other effects. This will be expanded upon in the guides.</p>
                        </div>                        
                    </div>
                </div>
                <div class="col-md-4 mb-5">
                    <div class="card h-100">
                        <div class="card-body">
                            <h2 class="card-title"><strong>It's Really Cheap...</strong></h2>
                            <p class="card-text">Home developing cuts down on costs significantly. On average, you can pay as low as only $2 per roll to develop, compared to around $10 per roll or sometimes even more when sent to a lab. Once you put a small initial investment into developing equipment, the difference in expense is significant.</p>
                        </div>                        
                    </div>
                </div>
            </div>
        </div>
    </div>
    </body>
    <footer class="py-5 bg-dark">
        <div class="col-lg-12"><h2 class="m-0 text-center text-white"><strong>Film Developing - The Basics</strong></h2>
        <p class="m-0 text-center text-white">&copy; 2021 Copyright: film-developing.com</p></div>        
    </footer>        
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="js/indexscript.js"></script>   
</html>
