<%-- 
    Document   : home
    Created on : Aug 26, 2017, 3:43:47 PM
    Author     : ryan
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <title>3-D Graphing</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <!--Importing javascript and css dependencies for bootstrap-->
        <link rel="stylesheet" href="include/styles/bootstrap.min.css" type="text/css"/>
        <script src="include/js/bootstrap.min.js"></script>
        
           <!-- Including jquery libraries -->
       <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
        <script src="include/js/jquery.smooth-scroll.min.js"></script>
     
        <!--header.css = navbar css
            home.css = css for the actual homepage
        -->
        <link rel="stylesheet" href="include/styles/header.css" type="text/css"/>      
        
        <link rel="stylesheet" href="include/styles/home.css" type="text/css"/>  
        
        <!--Library for plotly.js-->
        <script src="include/js/plotly-latest.min.js"></script>
    </head>
        <!--Function that allows for a smooth scroll between navbar elements
            
            credit on this function goes to this stack overflow post:
        https://stackoverflow.com/questions/19833657/simple-html5-way-to-vertically-split-a-website-page-in-vertical-slides-with-navi
        -->
        <script>
                $(function() {
             $('a[href*=#]:not([href=#])').click(function() {
               if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
                 var target = $(this.hash);
                 target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                 if (target.length) {
                   $('html,body').animate({
                     scrollTop: target.offset().top
                   }, 1000);
                   return false;
                 }
               }
             });
           });
        </script>
    <body>
        
        
        <div class="container-fluid" id ="home">
                <!-- 
                    Creates a vertical scrolling webpage
                    Typically you have the navbar href attribute point to another webpage
                    Here I am using the # css class attribute

                -->
                                <!-- Header for the webpage that brings you back
                                to the top-->
                        <div class="navbar-header">
                            <a href="#page1" class="navbar-brand" 
                               data-toggle="tooltip" title="Click to go back to the top">Ryan Rigato</a>
                        </div>
                <!-- Gives the actual navbar elements, basically a link to 
                each portion of the webpage-->
                <div id="nav">
                     <ul class="nav navbar-nav">
                         
                         <li><a href="#portfolio" data-toggle="tooltip" 
                                title="Click here to learn more about this website">
                                 Portfolio</a></li>
                                 
                         <li><a href="#contact" data-toggle="tooltip" 
                                title="Click here to learn more about this website">
                                 Contact</a></li>
                                 
                         <li><a href="#about" data-toggle="tooltip" 
                                title="Click here to learn more about this website">
                                 About</a></li>
                     </ul>-
                </div>       


        </div>
        
        <!--<div id ="startpage" ></div>-->
        
                <!-- Each Div represents a new page -->


                <div id="page1">
                  <a id="portfolio" class="smooth"></a>
                    Portfolio page content goes here.
                    <div id="myDiv">
                        <script>
                            Plotly.d3.csv('include/data/test.csv', function(err, rows){
function unpack(rows, key) {
	return rows.map(function(row)
	{ return row[key]; });}

var trace1 = {
	x:unpack(rows, 'x1'), y: unpack(rows, 'y1'), z: unpack(rows, 'z1'),
	mode: 'markers',
	marker: {
		size: 12,
		line: {
		color: 'rgba(217, 217, 217, 0.14)',
		width: 0.5},
		opacity: 0.8},
	type: 'scatter3d'
};

var trace2 = {
	x:unpack(rows, 'x2'), y: unpack(rows, 'y2'), z: unpack(rows, 'z2'),
	mode: 'markers',
	marker: {
		color: 'rgb(127, 127, 127)',
		size: 12,
		symbol: 'circle',
		line: {
		color: 'rgb(204, 204, 204)',
		width: 1},
		opacity: 0.8},
	type: 'scatter3d'};

var data = [trace1, trace2];
var layout = {margin: {
	l: 0,
	r: 0,
	b: 0,
	t: 0
  }};
Plotly.newPlot('myDiv', data, layout);
});
                        </script>
                    </div>
                </div>

                <div id="page2">
                  <a id="contact" class="smooth"></a>
                    Contact page content goes here.
                </div>
                
                 <div id="page3">
                  <a id="about" class="smooth"></a>
                    About page content goes here.
                </div>
    </body>
</html>