Movie Trailer Website Project: Best of Bogart
==================
#####Udacity FS Web Developer Nanodegree - Project 1#####
---

Contents
--------

1. [How to Run / Test](#chapter-1)  
2. [Python Libraries Used](#chapter-2)    

How to Run / Test <a id="chapter-1"></a>
-----------------
Follow these steps to run the Movie Trailer website project:    

1. Download and unzip the "Movies" folder.
2. Open and run the *openmovies.py*.

The application will call the Open Movies Database web API and collect information on some of my favorite Humphrey Bogart movies, then display it in a web browser. 

I have also included an HTML file (movies/freshj_tomatoes.html) that can be opened directly in a browser for demo purposes. This HTML is the output of the Python application.

Here's a screenshot of what to expect: 

![Best of Bogart Screenshot](https://github.com/vincemaling/Full-Stack-Web-Dev-P1/blob/master/movies/screenshot_best_of_bogie.png) 

Python Libraries Used <a id="chapter-2"></a>
-----------------
In addition to the project-required resources (fresh_tomatoes and media), I used the following Python libraries to add special functionality to my website:  

<dl><dt>(1) [Requests](http://docs.python-requests.org/en/latest/ "Request: HTTP For Humans")</dt>
<dd>This Python loibrary allows users to issue simple HTTP requests to leverage popular web APIs. In my case, I used the library to make calls to [Open Movie Database](http://www.omdbapi.com/ "OMDb"), which provides information (such as plot summaries, casts, etc.) on movies<dd>  

<dt>(2) json</dt>
<dd>I also imported Python's built-in json library to manipulate the JSON returned by OMDb (see above)</dd>  
