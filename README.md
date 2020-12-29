# Hacker News - Ranking System - Comment Driven Results

In this repository the data will be used to support and determine characteristics of a model that may further assist the community. The idea states that through the findings referenced in the project, anyone who uses this flatform can receive some valuable information that can affect the value in which they receive from others. 

## Table of Contents
 * [Project Background](#project-background)
 * [FAQs](#faqs)
 * [Column Description](#column-description)
 * [Requirements](#requirements)
 * [Requirements/Installation](#installation)
 * [Acknoledgments](#acknoledgments) 
 
 ## Project Background

The Hacker News website is a servicable platform where users interact with each other, typically through sourcing information or in the form of posing a formal question. A single posts non discriminant to the type of post will be ranked accordingly. 

> The basic algorithm divides points by a power of the time since a story was submitted. Comments in threads are ranked the same way. Other factors affecting rank include user flags, anti-abuse software, software which demotes overheated discussions, account or site weighting, and moderator action. 

Given the system Hacker News uses to support its community, our analysis will be based off the part of the algorithm dealing with the comments. 

## FAQs

Without further information being provided about the Hacker News website or how it functions in terms of how users interact with one another. Check out the [frequently asked questions](https://news.ycombinator.com/newsfaq.html) page for more details.
  
## Column Description

 Read carefully for the best understanding of the different columns being explored in this assignment.

   * id: The unique identifier from Hacker News for the post
   * title: The title of the post
   * url: The URL that the posts links to, if the post has a URL
   * num_points: The number of points the post acquired, calculated as the total number of upvotes minus the total number of downvotes
   * num_comments: The number of comments that wer made on the post
   * author: The username of the person who submitted the post
   * crated_at: The date and time at which the post was submitted

## Requirements/Installation

*Download Python verion 3.8.3*: 
Follow the link and [download](https://www.python.org/downloads) Python and the suite of libraries that enable scientific computing.
*Download Anacondas*: 
Choose one of the two Anaconda distributions [Miniconda](http://conda.pydata.org/miniconda.html) or [Anaconda](https://www.continuum.io/downloads).
*Run Jupyter Notebook*: 
Access the Jupyter Notebook package within the Anaconda distribution for this assignment.
*Download Dataset*: [Hacker News Dataset](https://www.kaggle.com/hacker-news/hacker-news-posts).
*Imported Libraries*: Reader, Pandas, Datetime, Matplotlib.

## Acknowledgments

The web sraping required for this data can be contributed from the Kaggle notebook [Hacker News Post](https://www.kaggle.com/hacker-news/hacker-news-posts).

