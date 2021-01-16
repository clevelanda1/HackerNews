# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import pandas library
import pandas as pd

# Open file and import dataset as an dataframe
autos = pd.read_csv('autos.csv', encoding = "Latin-1")

# Display information about the dataset
#autos.info()


# Rename the autos dataframe columns
autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'abtest', 'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model', 'odometer_km', 'registration_month', 'fuel_type', 'brand', 'unrepaired_damage', 'ad_created', 'n_of_pictures', 'postal_code', 'last_seen']

# Print snakecase version of autos dataframe columns
print(autos.columns)

# Convert column to a string and remove additional characters - Convert to an interger datatype
autos.loc[:,'price'] = autos.loc[:,'price'].astype(str).str.replace("$","").str.replace(",","")
autos.loc[:,'price'] = autos.loc[:,'price'].astype(int)

autos.loc[:,'odometer_km'] = autos.loc[:,'odometer_km'].astype(str).str.replace("km","").str.replace(",","")
autos.loc[:,'odometer_km'] = autos.loc[:,'odometer_km'].astype(int)

# Convert datatype to a string
autos.loc[:,'vehicle_type'] = autos.loc[:,'vehicle_type'].astype(str)
autos.loc[:,'model'] = autos.loc[:,'model'].astype(str)
autos.loc[:,'fuel_type'] = autos.loc[:,'fuel_type'].astype(str)
autos.loc[:,'unrepaired_damage'] = autos['unrepaired_damage'].astype(str)

# Import datetime lirbrary
import datetime as dt

# Seperate and format defined column
def seperate_date_time(column_choice):
    for i in column_choice:
 
        choice_date = i.split()
        choice_date = choice_date[0]
        choice_date = str(choice_date)
        choice_date = dt.datetime.strptime(choice_date, "%Y-%m-%d")
        column_choice.replace(i, choice_date)
        
# Call Function
seperate_date_time(autos.loc[:,"ad_created"])
seperate_date_time(autos.loc[:,"date_crawled"])

#Format defined column by date and time
for i in autos.loc[:,"last_seen"]:
    last_seen = i.split()
    
    last_seen_date = last_seen[0]
    last_seen_hour = last_seen[1]
    
    last_seen_date = str(last_seen_date)
    last_seen_hour = str(last_seen_hour)
    
    last_seen_date = dt.datetime.strptime(last_seen_date, "%Y-%m-%d")
    last_seen_hour = dt.datetime.strptime(last_seen_date, "%H:%M-%s")
    #autos.loc[:,"date_crawled"].replace(i, ad_crawled_hr)

# Display Results
print(autos.loc[:,["date_crawled", "ad_created", "last_seen"]])