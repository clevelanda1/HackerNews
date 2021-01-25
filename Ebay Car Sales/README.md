# Data Scrubbing and Observation Report - Ebay Car Sales

In this folder the data will be used to find inconsistencies, remove errors and support a clean dataset for further analysis. A gradual process implemented to achieve a high level of accuracy.  


## Table of Contents
 * [Project Background](#project-background)
 * [Column Description](#column-description)
 * [FAQs](#faqs)
 * [Requirements](#requirements)
 * [Requirements/Installation](#installation)
 * [Acknowledgments](#acknoledgments) 
 
 ## Project Background

The data provided for this project has been scraped from eBay Kleinanzeigen, a classfields section of the German eBay website. The content of this data consist of over 370,00 used cars and is presented in german. The sample data will consist of only 50,000 listings. In this project the intended goal is to clean the data made available and analyze the used car listings.
  
## Column Description

 Read carefully for the best understanding of the different columns being explored in this assignment.

   * dateCrawled - When this ad was first crawled. All field-values are taken from this date
   * name - Name of the car
   * seller - Whether the seller is private or a dealer
   * offerType - The type of listing
   * price - The price on the ad to sell the car
   * abtest - Whther the listing is included in an A/B test
   * vehicleType - The vehicle type
   * yearOfRegistration - The year in which the car was first registered
   * gearbox - The transmission type
   * powerPS - The power of the car in PS
   * model - The car model name
   * kilometer - How many kilometers the car has driven
   * monthOfRegistration - The month in which the car was first registered
   * fuelType - What type of fuel the car uses
   * brand - The brand of the car
   * notRepairDamage - If the car has a damage which is not yet repaired
   * dateCreated - The date on which the eBay listing was created
   * nrOfPictures - The number of pictures in the ad
   * postalCode - The postal code for the location of the vehicle
   * lastSeenOnline - When the crawler saw this ad last online
   
## FAQs

What is the definition of a [crawler](https://whatis.techtarget.com/definition/crawler)?  What is [A/B testing](https://en.wikipedia.org/wiki/A/B_testing)?  What does PS stand for in relation to Power? `Power Supply`

## Requirements/Installation

#### Download Python verion 3.8.3:
Follow the link and [Download](https://www.python.org/downloads) Python and the suite of libraries that enable scientific computing.
#### Download Anacondas:
Choose one of the two Anaconda distributions [Miniconda](http://conda.pydata.org/miniconda.html) or [Anaconda](https://www.continuum.io/downloads).
#### Run Jupyter Notebook:
Access the Jupyter Notebook package within the Anaconda distribution for this assignment.
#### Download: [Dataset](https://data.world/data-society/used-cars-data)
#### Imported Libraries:
Pandas, Datetime.

## Acknowledgments
The web sraping required for this data can be contributed from the Kaggle notebook by user [Orgesleka](https://www.kaggle.com/orgesleka).
