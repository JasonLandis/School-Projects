<?php

require_once('config.php'); 

function product() {
	try {
		$pdo = new PDO(DBCONNSTRING,DBUSER,DBPASS);
		$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$sql = "select * from Item";
		$result = $pdo->query($sql);
		while ($row = $result->fetch()) {
			echo '<div class="col-md-4 mb-5">';
			echo '<div class="product-card h-100">';
			echo '<div class="card-body">';
			echo '<h2 class="card-title"><strong>' . $row['ItemName'] . '</strong></h2>';
			echo '<img class="img-fluid rounded mb-4 mb-lg-0" src="' . $row['ItemPic'] . '" alt="' . $row['ItemName'] . '" />';
			echo '<p class="card-text">' . $row['Description'] . '</p>';
			echo '<div class="price-button">';
			echo '<h4><strong> $' . $row['Price'] . '</strong></h4>';
			echo '<a href="' . $row['ItemLink'] . '" class="btn btn-primary">Add to Cart</a>';
			echo '</div>';
			echo '</div>';
			echo '</div>';
			echo '</div>';

		}
	 }
	 catch (PDOException $e) {
		die( $e->getMessage() );
	 }
}

?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
         <title>Catalog</title>
        <link href="css/styles.css" rel="stylesheet" />
        <link href = "css/custom-styles.css" rel="stylesheet" />
		<style type="text/css">
			.shadow{
				transition: box-shadow .3s;
			}
			.shadow:hover{
				box-shadow: 0 0 11px rgba(33,33,33,.2);
			}
		</style>
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
                    </ul>
                </div>
            </div>
        </nav>		
			<div class="card text-white bg-secondary my-5 py-4 text-center">
				<div class="card-body"><h1 class="text-white m-0"><strong>Everything you need to home develop a film</strong></h1></div>
				</div>
				<div class="container px-4 px-lg-5">
				<div class="row gx-5 gx-lg-5">
					<?php product(); ?>
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