

var imagecounter = 1;
$("#imagecarousel").click(function(){

imagecounter = imagecounter + 1;
		if(imagecounter == 7)
			{
				imagecounter = 1;
			}
		if(imagecounter == 2)
			{
				$("#img1").hide();
				$("#img2").show();
				$("#img3").hide();
				$("#img4").hide();
				$("#img5").hide();
				$("#img6").hide();
			}
		if(imagecounter == 3)
			{
				$("#img1").hide();
				$("#img2").hide();
				$("#img3").show();
				$("#img4").hide();
				$("#img5").hide();
				$("#img6").hide();
			}
		if(imagecounter == 4)
			{
				$("#img1").hide();
				$("#img2").hide();
				$("#img3").hide();
				$("#img4").show();
				$("#img5").hide();
				$("#img6").hide();
			}
		if(imagecounter == 5)
			{
				$("#img1").hide();
				$("#img2").hide();
				$("#img3").hide();
				$("#img4").hide();
				$("#img5").show();
				$("#img6").hide();
			}
		if(imagecounter == 6)
			{
				$("#img1").hide();
				$("#img2").hide();
				$("#img3").hide();
				$("#img4").hide();
				$("#img5").hide();
				$("#img6").show();
			}
		if(imagecounter == 1)
			{
				$("#img1").show();
				$("#img2").hide();
				$("#img3").hide();
				$("#img4").hide();
				$("#img5").hide();
				$("#img6").hide();
			}
		
		






});