<!DOCTYPE html>
<html>
	<head>	
		<!-- Refresh page every 60 seconds to update plot -->
		<meta http-equiv="refresh" content="60">
		
		<title> Temperature Logger </title>
		
		<!-- Instead of having CSS, it is embedded here for header and image -->
		<style>
			img {
				/* I found these specs to be the best for the image I have saved */
				width: 1400px;
				height: 600px;
			}

			.image-container {
				/* This centers the image to the best of its ability */
				display: block;
				text-align: center;
				margin: 0 auto;
			}

			.header {
				/* The h1 tag has these specs */
				padding: 0px;
				text-align: center;
				background: white;
				font-size:20px;
				font:verdana;
			}
		</style>
		
		<!-- The header tag for the 'title' of the web page-->
		<div class="header">
			<h1> Isaac Violette's Temperature Logger </h1>
		</div>

	</head>

<body>
	<!-- Upload picture with specific style -->
	<div class="image-container">
		<img src="temp_plot.png">
	</div>
	
</body>

</html>
