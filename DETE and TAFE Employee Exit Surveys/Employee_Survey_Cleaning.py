# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:15:08 2021

@author: Austin Cleveland
"""


# Import Libraries.
import pandas as pd
import numpy as np


# Import csv files from both datasets.
dete_survey = pd.read_csv(r"C:\Users\Dell User\Documents\Python Related Projects\DETE and TAFE Employee Exit Surveys\dete-exit-survey-january-2014.csv", encoding = 'utf-8', na_values = 'Not Stated')
tafe_survey = pd.read_csv(r"C:\Users\Dell User\Documents\Python Related Projects\DETE and TAFE Employee Exit Surveys\tafe-exit-survey-december-2013.csv", encoding = 'latin-1')


# Remove additional columns from both datasets.
dete_survey = dete_survey.drop(dete_survey.columns[28:49], axis = 1)
tafe_survey = tafe_survey.drop(tafe_survey.columns[17:66], axis = 1)


# Update the column names in both datasets.
rename_tafe_col = {'Record ID': 'id', 'CESSATION YEAR': 'cease_date', 'Reason for ceasing employment': 'separationtype', 'Gender. \xa0\xa0\xa0\xa0What is your Gender?': 'gender', 'CurrentAge. \xa0\xa0\xa0\xa0Current Age': 'age', 'Employment Type. \xa0\xa0\xa0\xa0Employment Type': 'employment_status', 'Classification. \xa0\xa0\xa0\xa0Classification': 'position', 'LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service', 'LengthofServiceCurrent. Length of Service at current workplace (in years)': 'role_service'}
tafe_survey = tafe_survey.rename(columns = rename_tafe_col, errors = 'raise')
tafe_survey.columns = tafe_survey.columns.str.lower()
dete_survey.columns = dete_survey.columns.str.lower().str.strip().str.replace(' ', '_')


# Select only the data for survey respondents who have a resignation 'separation type' (DETE).
dete_resignation = dete_survey.copy()
def resignation_qualification(element):
    if element == 'Resignation-Other reasons' or element == 'Resignation-Other employer' or element ==  'Resignation-Move overseas/interstate':
        return True
    else:
        return False

true_resignation = dete_resignation['separationtype'].apply(resignation_qualification)
dete_resignation['separationtype'] = dete_resignation.loc[true_resignation == True, 'separationtype'].drop(columns = 'separationtype')
dete_resignation = dete_resignation.drop(dete_resignation[dete_resignation['separationtype'].isnull()].index)
print(dete_resignation['separationtype'].unique())


# Select only the data for survey respondents who have a resignation 'separation type' (TAFE).
tafe_resignation = tafe_survey.copy()
tafe_resignation = tafe_resignation.drop(tafe_resignation[tafe_resignation['separationtype'] != 'Resignation'].index)
print(tafe_resignation['separationtype'].unique())





# My special code that tells me what the spacing inside the data looks like
#print(tafe_survey.columns.str.split("   ")[4])

















#TAFE:
# Separate tafe records into Topics and Questions
# Prepare to remove all of the Contributing Factors, Induction Info and Main Factor Columns (too many null values)
# Adjust Column headers
# Adjust work area columns to either corporate or teaching
# Remove 'TAFE' from the 'Institute' columns
# Address Id columns, reassign values
# Convert 'Agree' to A, 'Disagree' to D ... and so on
# Compute average ages in dete dataset
# Remove additional text from 'Classification' column
# Define one standard for 'Length of Service Overall'
# Determine the Columns with same data but different names


#DETE:
# Remove the last 5 rows (consider deleting 'Business Unit' and 'Classification')
# Address remaining null values in each dataset for concerning columns
# Define 'A', 'N', 'SA', 'M', 'D
# Compute average ages in dete dataset
# Determine the Columns with same data but different names

dete_survey