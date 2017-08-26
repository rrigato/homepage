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
        <script src="https://github.com/kswedberg/jquery-smooth-scroll/blob/master/jquery.smooth-scroll.min.js"></script>
     
        <!--header.css = navbar css
            home.css = css for the actual homepage
        -->
        <link rel="stylesheet" href="include/styles/header.css" type="text/css"/>      
        
        <link rel="stylesheet" href="include/styles/home.css" type="text/css"/>     
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
                            <a href="#home" class="navbar-brand" 
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
                     </ul>
                </div>       


                <!-- Each Div represents a new page -->


                <div id="page1">
                  <a id="portfolio" class="smooth"></a>
                    Portfolio page content goes here.
                </div>

                <div id="page2">
                  <a id="contact" class="smooth"></a>
                    Contact page content goes here.
                </div>
                
                 <div id="page3">
                  <a id="about" class="smooth"></a>
                    About page content goes here.
                </div>
        </div>
    </body>
</html>