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
                    <div id="scatterContainer">

                    <script>
                        /*
                         * Reads the csv from include/data/samJack.csv
                         */
                        Plotly.d3.csv('include/data/midnightBleach.csv', function(err, rows){
                          Plotly.d3.csv('include/data/midnightDbzf.csv', function(err2, rows2){  
                              Plotly.d3.csv('include/data/midnightDbz.csv', function(err3, rows3){ 
                                  Plotly.d3.csv('include/data/midnightOpm.csv', function(err4, rows4){ 
                              
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
                  <a id="contact" class="smooth"></a>
                    Contact page content goes here.
                    <div id="myDiv2">
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

                          var trace1 = {
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


                          var data = [trace1];
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
                          Plotly.newPlot('myDiv2', data, layout); 
                          });
                   
                        
                        
                        
                    </script>
                    </div>
                </div>
                
                 <div id="page3">
                  <a id="about" class="smooth"></a>
                    About page content goes here.
                    <div id="myDiv">
                        
                        <script>
                            Plotly.d3.csv(
                               'https://raw.githubusercontent.com/plotly/datasets/master/_3d-line-plot.csv', 
                            //function that returns each individual value 
                            //from a row
                                function unpack(rows, key) {
                                    return rows.map(function(row) 
                                    { return row[key]; });
                                }


                            var trace1 = {
                              x: unpack(rows, 'x1'),
                              y: unpack(rows, 'y1'),
                              z: unpack(rows, 'z1'),
                              mode: 'lines',
//                              marker: {
//                                color: '#1f77b4',
//                                size: 12,
//                                symbol: 'circle',
//                                line: {
//                                  color: 'rgb(0,0,0)',
//                                  width: 0
//                                }},
                              line: {
                                color: '#1f77b4',
                                width: 4
                              },
                              type: 'scatter3d'
                            };

                            var trace2 = {
                              x: unpack(rows, 'x2'),
                              y: unpack(rows, 'y2'),
                              z: unpack(rows, 'z2'),
                              mode: 'lines',
                              marker: {
                                color: '#9467bd',
                                size: 12,
                                symbol: 'circle',
                                line: {
                                  color: 'rgb(0,0,0)',
                                  width: 0
                                }},
                              line: {
                                color: 'rgb(44, 160, 44)',
                                width: 1
                              },
                              type: 'scatter3d'
                            };

//                            var trace3 = {
//                              x: unpack(rows, 'x3'),
//                              y: unpack(rows, 'y3'),
//                              z: unpack(rows, 'z3'),
//                              mode: 'lines',
//                              marker: {
//                                color: '#bcbd22',
//                                size: 12,
//                                symbol: 'circle',
//                                line: {
//                                  color: 'rgb(0,0,0)',
//                                  width: 0
//                                }},
//                              line: {
//                                color: '#bcbd22',
//                                width: 1
//                              },
//                              type: 'scatter3d'
//                            };

                            var data = [trace1, trace2, trace3];
                            var layout = {
                              title: '3D Line Plot',
                              autosize: false,
                              width: 500,
                              height: 500,
                              margin: {
                                l: 0,
                                r: 0,
                                b: 0,
                                t: 65
                              }
                            };
                            Plotly.newPlot('myDiv', data, layout); 
                            });

                        </script>

                    </div>
                </div>
    </body>
</html>