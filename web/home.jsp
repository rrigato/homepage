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
                         
                         <li><a href="#midnight" data-toggle="tooltip" 
                                title="Click here to see ratings for the midnight slot of Adult Swim">
                                 Midnight Ratings</a></li>
                                 
                         <li><a href="#monthly" data-toggle="tooltip" 
                                title="Click here to see average monthly ratings for Toonami">
                                 Historical Monthly Ratings</a></li>
                                 
                         <li><a href="#household" data-toggle="tooltip" 
                                title="Click here to see average household ratings by year">
                                 Household Ratings</a></li>
                                 
                         <li><a href="#about" data-toggle="tooltip" 
                                title="Click here to learn more about this site">
                                 About</a></li>
                     </ul>-
                </div>       


        </div>
        
        <!--<div id ="startpage" ></div>-->
        
                <!-- Each Div represents a new page -->


                <div id="page1">
                  <a id="midnight" class="smooth"></a>
                    Portfolio page content goes here.
                    <div id="scatterContainer">

                    <script>
                        /*
                         * Reads the csv from include/data/samJack.csv
                         */
                        Plotly.d3.csv('include/data/midnight-slot/midnightBleach.csv', function(err, rows){
                          Plotly.d3.csv('include/data/midnight-slot/midnightDbzf.csv', function(err2, rows2){  
                              Plotly.d3.csv('include/data/midnight-slot/midnightDbz.csv', function(err3, rows3){ 
                                  Plotly.d3.csv('include/data/midnight-slot/midnightOpm.csv', function(err4, rows4){ 
                              
                            //function that returns each individual value 
                            //from a row
                        function unpack(rows, key) {
                                return rows.map(function(row)
                                { return row[key]; });
                            }
                        
                        //Traces data by mapping columns to x, y,z axis
                        var bleach = {
                                x:unpack(rows, 'Year'), y: unpack(rows, 'Total'), 
                                z: unpack(rows, 'ATotal'),
                                mode: 'markers',
                                marker: {
                                       size: 6,
                                       //Gives the color pink/purple
                                       color: 'rgb(0, 3, 232)'
                                        },
                                        
                                //Gives the name for the legend
                                name : 'Bleach',                                        
                                type: 'scatter3d'
                        };
                        
                        
                        //Traces data by mapping columns to x, y,z axis
                        var dbz_final = {
                                x:unpack(rows2, 'Year'), y: unpack(rows2, 'Total'), 
                                z: unpack(rows2, 'ATotal'),
                                mode: 'markers',
                                marker: {
                                       size: 6,

                                       color: 'rgb(248, 134, 232)'
                                        },
                                //Gives the name for the legend
                                name : 'DBZ Kai Final Chapters',
                                type: 'scatter3d'
                        };   
                        
                        
                       //Traces data by mapping columns to x, y,z axis
                        var dbz = {
                                x:unpack(rows3, 'Year'), y: unpack(rows3, 'Total'), 
                                z: unpack(rows3, 'ATotal'),
                                mode: 'markers',
                                marker: {
                                       size: 6,
                                       //Gives the color Red
                                       color: 'rgb(204, 51, 0)'
                                        },
 
                                        
                                //Gives the name for the legend
                                name : 'DBZ Kai',                                        
                                type: 'scatter3d'
                        };                   
                        
                        
                        //Traces data by mapping columns to x, y,z axis
                        var opm = {
                                x:unpack(rows4, 'Year'), y: unpack(rows4, 'Total'), 
                                z: unpack(rows4, 'ATotal'),
                                mode: 'markers',
                                marker: {
                                       size: 6,
                                       //Gives the color black
                                       color: 'rgb(0, 0, 0)'
                                        },

                                        
                                //Gives the name for the legend
                                name : 'One Punch Man',                                        
                                type: 'scatter3d'
                        };                          

                        
                        //concatenates all the individual points together so they can 
                        //appear on the same plot
                        var data = [bleach, dbz_final, dbz, opm];
                        
                        
                        //layout of the graph
                        var layout = {
                           autoscale:true,
                           height:700,
                          //title at the top of the page
                          title:'Midnight slot viewership',
                          
                          //A scene object must be used to encapsulate
                          //each axis title, not sure why this is...
                          scene :{
                                xaxis:{
                                    title:'Year',
                                    //Makes sure the ticks are every year
                                    autotick:false,
                                    dtick:1
                                    
                                    
                                },
                            
                                   yaxis:{
                                    title:'Total Viewers in thousands'
                                },                         
                            
                                 zaxis:{
                                    title:'Adults 18-49 in thousands'
                                }
                          },
                           //pixel margin around the graph
                            margin: {

                                l: 100,
                                r: 100,
                                b: 100,
                                t: 50
                          },
                          
                          legend:{
                              font:{
                                  size:18
                              }
                          }
                      };
                            console.log(layout);
                      
                        //populates the new plot with the string literal the
                        //id of the div you want this plot in
                        Plotly.newPlot('scatterContainer', data, layout);
                        
                                    });  //end fourth csv
                               });  //end third csv                            
                                
                            });  //end second csv
                        });  //end first csv                        
                        
                        
                        
                    </script>                        
                    </div>
                </div>

                <div id="page2">
                  <a id="monthly" class="smooth"></a>
                    Contact page content goes here.

                    <div id="monthly-ratings">
                        
                     <script>
                        Plotly.d3.csv('include/data/monthly-ratings/year2012.csv', function(err, rows){
                           Plotly.d3.csv('include/data/monthly-ratings/year2013.csv', function(err2013, rows2013){  
                              Plotly.d3.csv('include/data/monthly-ratings/year2014.csv', function(err2014, rows2014){
                                Plotly.d3.csv('include/data/monthly-ratings/year2015.csv', function(err2015, rows2015){
                                    Plotly.d3.csv('include/data/monthly-ratings/year2016.csv', function(err2016, rows2016){
                                         Plotly.d3.csv('include/data/monthly-ratings/year2017.csv', function(err2017, rows2017){
                            //function that returns each individual value 
                            //from a row
                                function unpack(rows, key) {
                                    return rows.map(function(row) 
                                    { return row[key]; });
                                }

                            //This variable corresponds to the include/data/year2012.csv
                            //file which gives the average monthly ratings for 2012
                            var year2012 = {
                                 //unpacks the csv into the x, y, and z axis
                              x: unpack(rows, 'Year'),
                              y: unpack(rows, 'Month'),
                              z: unpack(rows, 'Total'),
                              mode: 'lines',
                              //Sets the color/width of the lines
                              line: {
                                //gives color blue
                                color: '#1f77b4',
                                width: 4
                              },
                              //Gives the name for the legend
                              name:'2012',
                              type: 'scatter3d'
                            };

                            //This variable corresponds to the include/data/year2013.csv
                            //file which gives the average monthly ratings for 2013
                            var year2013 = {
                              //unpacks the csv into the x, y, and z axis
                              x: unpack(rows2013, 'Year'),
                              y: unpack(rows2013, 'Month'),
                              z: unpack(rows2013, 'Total'),
                              mode: 'lines',
                              //Sets the color/width of the lines
                              line: {
                                //gives the color red
                                color: '#ff0000',
                                width: 4
                              },
                              //Gives the name for the legend
                              name:'2013',
                              type: 'scatter3d'
                            };

                            //This variable corresponds to the include/data/year2014.csv
                            //file which gives the average monthly ratings for 2014
                            var year2014 = {
                              //unpacks the csv into the x, y, and z axis
                              x: unpack(rows2014, 'Year'),
                              y: unpack(rows2014, 'Month'),
                              z: unpack(rows2014, 'Total'),
                              mode: 'lines',
                              //Sets the color/width of the lines
                              line: {
                                //gives the color green
                                color: '#006400',
                                width: 4
                              },
                              //Gives the name for the legend
                              name:'2014',                              
                              type: 'scatter3d'
                            };
                            
                            
                            //This variable corresponds to the include/data/year2015.csv
                            //file which gives the average monthly ratings for 2015
                            var year2015 = {
                              //unpacks the csv into the x, y, and z axis
                              x: unpack(rows2015, 'Year'),
                              y: unpack(rows2015, 'Month'),
                              z: unpack(rows2015, 'Total'),
                              mode: 'lines',
                              //Sets the color/width of the lines
                              line: {
                                //gives the color gold
                                color: '#FFD700',
                                width: 4
                              },
                              //Gives the name for the legend
                              name:'2015',                              
                              type: 'scatter3d'
                            };                            



                            
                            //This variable corresponds to the include/data/year2016.csv
                            //file which gives the average monthly ratings for 2016
                            var year2016 = {
                              //unpacks the csv into the x, y, and z axis
                              x: unpack(rows2016, 'Year'),
                              y: unpack(rows2016, 'Month'),
                              z: unpack(rows2016, 'Total'),
                              mode: 'lines',
                              //Sets the color/width of the lines
                              line: {
                                //gives the color light purple
                                color: '#FF69B4',
                                width: 4
                              },
                              //Gives the name for the legend
                              name:'2016',                              
                              type: 'scatter3d'
                            };         
                            
                            
                            
                            //This variable corresponds to the include/data/year2017.csv
                            //file which gives the average monthly ratings for 2017
                            var year2017 = {
                              //unpacks the csv into the x, y, and z axis
                              x: unpack(rows2017, 'Year'),
                              y: unpack(rows2017, 'Month'),
                              z: unpack(rows2017, 'Total'),
                              mode: 'lines',
                              //Sets the color/width of the lines
                              line: {
                                //gives the color gray
                                color: '#808080',
                                width: 4
                              },
                              //Gives the name for the legend
                              name:'2017',                              
                              type: 'scatter3d'
                            };                                  

                            //combines individual lines into one 3d graph
                            var data = [year2012, year2013, year2014, year2015, year2016, year2017];
                            var layout = {
                              title: 'Average monthly ratings by year',
                              autosize: true,
                              height: 700,
                                //A scene object must be used to encapsulate
                                //each axis title, not sure why this is...                            
                                 scene :{
                                      xaxis:{
                                          title:'Year',
                                          //how far between tick marks on graph axis
                                          dtick : 1
                                      },

                                         yaxis:{
                                          title:'Month',
                                          //how far between tick marks on graph axis
                                          dtick :1
                                      },                         

                                       zaxis:{
                                          title:'Viewers in Thousands'
                                      }
                                },                              
                              margin: {
                                l: 50,
                                r: 50,
                                b: 50,
                                t: 50
                              },
                          
                             legend:{
                                 font:{
                                      size:18
                                }
                            }
                            };
                            
                            Plotly.newPlot('monthly-ratings', data, layout); 
                            
                                        });//End of 2016 csv
                                    });//End of 2016 csv
                                });//End of 2015 csv
                            });//End of 2014 csv
                          });//End of 2013 csv
                         });//End of 2012 csv

                        </script>

                    </div>
                </div>
                
                 <div id="page3">
                  <a id="household" class="smooth"></a>
                    About page content goes here.
                    <div id="annual-ratings">
                    <script>
                        /*
                         * Reads the csv from include/data/samJack.csv
                         */                        
                    Plotly.d3.csv('include/data/annualRatings.csv', function(err, rows){
                              //function that returns each individual value 
                            //from a row
                                function unpack(rows, key) {
                                    return rows.map(function(row) 
                                    { return row[key]; });
                                }

                          var annualRatings = {
                            x: unpack(rows, 'Total'),
                            y: unpack(rows, 'ATotal'),
                            z: unpack(rows, 'Year'),
                            mode: 'lines',
                            marker: {

                              size: 12,
                              symbol: 'circle',
                              line: {
                                color: 'rgb(0,0,0)',
                                width: 1
                              }},
                            line: {
                              color: unpack(rows,'Household'),
                                colorscale:'Bluered',
                              width: 6
                            },
                            type: 'scatter3d'
                          };


                          var data = [annualRatings];
                          var layout = {
                              //title at the top of the page
                            title: 'Average Annual Ratings for Toonami Block',
                            autosize: true,
                            height:700,
                            
                          //A scene object must be used to encapsulate
                          //each axis title, not sure why this is...                            
                           scene :{
                                xaxis:{
                                    title:'Total Viewers in thousands'
                                },
                            
                                   yaxis:{
                                    title:'Age 18-49 Viewers in thousands'
                                },                         
                            
                                 zaxis:{
                                    title:'Year'
                                }
                          },

                            margin: {
                              l: 50,
                              r: 50,
                              b: 50,
                              t: 50
                            }
                          };
                        //populates the new plot with the string literal the
                        //id of the div you want this plot in
                          Plotly.newPlot('annual-ratings', data, layout); 
                          });
                   
                        
                        
                        
                    </script>
                    </div>
                </div>
                
                

                <div id="page4">
                  <a id="about" class="smooth"></a>
                  
                    <div class="me"/>
                        <img src="images/myPhoto.jpg"  style="width:225px;height:225px;">
                    </div>
                    <div class="words"/>
                        <h2>About this site</h2>
                            <div class ="explanation">
                                <p>
                                    My name is Ryan Rigato and as you can probably guess I 
                                    am definitely not a web developer. However, I have found that
                                    knowing the fundamentals of web development is
                                    very useful in the world of analytics. I built this site because
                                    I find 3-Dimensional graphing fascinating, I hope you feel the same!

                                </p>
                                <p>
                                    All graphes were built with the Plotly.js JavaScript framework.
                                    I would like to say thank you to the plotly team for open sourceing
                                    their graphing library. Additionally, this site would not of been 
                                    possible without the wonderful <a href = https://www.w3schools.com/ > W3 Turtorials</a>
                                    and the <a href = http://getbootstrap.com/> Bootstrap  Front End Framework</a>
                                    Finally, the smooth transitions between views was built with <a> jQuery </a>
                                        
                                   </p>



                            </div>

                        
                        <br>       
                        <br>   

                        <h3>Here is some information about me</h3>

                        <a href ="http://ryanrigato-1252.appspot.com/">Check out my other website featuring D3.js</a>
                       
                        <br>       
                        <br>                        
                        
                        <%--External link to GitHub--%>
                        <a href ="https://github.com/rrigato">Check out my GitHub account</a>

                        <br>       
                        <br>
                        <a href ="https://www.kaggle.com/ryanrigato">Take a look at my Kaggle Profile </a>

                        <br>       
                        <br>
                        <a href ="https://www.linkedin.com/in/ryan-rigato-a9248397">Connect with me on Linkedin </a>

                        <br>
                        <br>
                        <a href="https://github.com/rrigato/ratings">Source Code for this website</a>
                </div>

                </div>
    </body>
</html>