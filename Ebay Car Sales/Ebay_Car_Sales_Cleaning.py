# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import pandas library
import pandas as pd

# Open file and import dataset as an dataframe
autos = pd.read_csv('autos.csv', encoding = "Latin-1")

# Rename the autos dataframe columns
autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'abtest', 'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model', 'odometer_km', 'registration_month', 'fuel_type', 'brand', 'unrepaired_damage', 'ad_created', 'n_of_pictures', 'postal_code', 'last_seen']

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
autos.loc[:,'gearbox'] = autos.loc[:,'gearbox'].astype(str)

# Remove all unwanted records from the defined columns
autos = autos[autos['seller'] != 'gewerblich']
autos = autos[autos['offer_type'] != 'Gesuch']

# Format defined column by date and times
autos['date_crawled'] = autos['date_crawled'].str[:10]
autos['ad_created'] = autos['ad_created'].str[:10]
last_seen_copy = autos['last_seen'].copy()
autos['last_seen'] = autos['last_seen'].str[:10]
autos['last_seen_hour'] = last_seen_copy.str[12:]

# Formatted apprpriate columns 
pd.options.display.float_format = '{:,.2f}'.format

# Replace all German words with their English translation
autos["seller"] = autos["seller"].replace("privat", "Private")
autos["offer_type"] = autos["offer_type"].replace("Angebot", "Offer")
autos["gearbox"] = autos["gearbox"].replace("manuell", "Manual").replace("automatik", "Automatic")
autos["fuel_type"] = autos["fuel_type"].replace("benzin", "Gasoline").replace("diesel", "Diesel")
autos["unrepaired_damage"] = autos["unrepaired_damage"].replace("ja", "Yes").replace("nan", "Nan").replace("nein", "No")
autos["vehicle_type"] = autos["vehicle_type"].replace("kleinwagen", "Mini").replace("coupe", "Coupe").replace("suv", "SUV").replace("limousine", "Limousine").replace("cabrio", "Convertible").replace("bus", "Bus").replace("kombi", "Combination").replace("andere", "Other")
autos["abtest"] = autos["abtest"].replace("test", "Test").replace("control", "Control") 
autos["model"] = autos["model"].replace("2_reihe", "2 Series").replace("Andere", "Other").replace("3_reihe", "3 Series").replace("A_klasse", "A Class").replace("3er", "3s").replace("5er", "5s").replace("E_klasse", "E Class").replace("Kadett", "Cadet").replace("1er", "1s").replace("B_klasse", "B Class").replace("C_klasse", "C Class").replace("Xc_reihe", "Xc Series").replace("7er", "7s").replace("Z_reihe", "Z Series").replace("M_klasse", "M Class").replace("I_reihe", "I Series").replace("6_reihe", "6 Series").replace("5_reihe", "5 Series").replace("Rx_reihe", "Rx Series").replace("6er", "6s").replace("X_reihe", "X Series").replace("S_klasse", "S Class").replace("4_reihe", "4 Series").replace("1_reihe", "1 Series").replace("Ptcruiser", "Pt Cruiser").replace("Mx_reihe", "Mx Series").replace("Mx_reihe", "M Series").replace("Cr_reihe", "Cr Series").replace("C_reihe", "C Series").replace("V Classe", "V Class").replace("X_type", "X Type").replace("S_type", "S type").replace("X_trail", "X Trail").replace("Cx_reihe", "Cx Series").replace("Range_rover_evoque", "Range Rover Evoque").replace("G_klasse", "G Class").replace("Serie_2", "Serie 2").replace("B_max", "B Max").replace("Serie_3", "Serie 3").replace("Serie_1", "Serie 1")
autos["brand"] = autos["brand"].replace("Mercedes_benz", "Mercedes Benz").replace("Sonstige_autos", "Sonstige").replace("Alfa_romeo", "Alfa Romeo").replace("Land_rover", "Land Rover")

# Capitalize all Words
autos["model"] = autos["model"].str.capitalize()
autos["brand"] = autos["brand"].str.capitalize()

# Remove all rows where the registration year is not in range
autos = autos.drop(autos[(autos["registration_year"] > 2016) | (autos["registration_year"] < 1900)].index)

#autos_clean_data = autos.to_csv('autos_clean.csv', index = True)