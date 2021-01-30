# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:15:08 2021

@author: Austin Cleveland
"""

# Import Libraries.
import pandas as pd
import numpy as np


# Import csv files from both datasets.
tafe_survey = pd.read_csv(r"C:\Users\Dell User\Documents\Python Related Projects\DETE and TAFE Employee Exit Surveys\tafe-exit-survey-december-2013.csv", encoding = 'latin-1')
dete_survey = pd.read_csv(r"C:\Users\Dell User\Documents\Python Related Projects\DETE and TAFE Employee Exit Surveys\dete-exit-survey-january-2014.csv", encoding = 'utf-8', na_values = 'Not Stated')


# Remove additional columns from both datasets.
tafe_survey = tafe_survey.drop(tafe_survey.columns[17:66], axis = 1)
dete_survey = dete_survey.drop(dete_survey.columns[28:49], axis = 1)


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


# Select only the data for survey respondents who have a resignation 'separation type' (TAFE).
tafe_resignation = tafe_survey.copy()
tafe_resignation = tafe_resignation.drop(tafe_resignation[tafe_resignation['separationtype'] != 'Resignation'].index)


# Amend any single formatted dates from both datasets.
tafe_resignation['cease_date'] = tafe_resignation['cease_date'].astype(str).str.split('.').str[0]
dete_resignation['dete_start_date'] = dete_resignation['dete_start_date'].astype(str).str.split('.').str[0]
dete_resignation['cease_date'] = dete_resignation['cease_date'].astype(str).str.split("/").str[-1]


# Amend any null values from both datasets.                              
tafe_resignation = tafe_resignation.drop(tafe_resignation[tafe_resignation['institute_service'] == 'nan'].index)
dete_resignation = dete_resignation.drop(dete_resignation[dete_resignation['cease_date'] == 'nan'].index)
dete_resignation = dete_resignation.drop(dete_resignation[dete_resignation['dete_start_date'] == 'nan'].index)
                                         

# Create an identical column 'institute service' for the (DETE) dataset.
dete_resignation['institute_service'] = dete_resignation['cease_date'].astype(int) - dete_resignation['dete_start_date'].astype(int)


# Convert values in corresponding dissatisfaction columns to true, false or a null value. 
tafe_resignation.at[tafe_resignation['contributing factors. dissatisfaction'] == '-', 'contributing factors. dissatisfaction'] = 'False'
tafe_resignation.at[tafe_resignation['contributing factors. dissatisfaction'] == 'Contributing Factors. Dissatisfaction ', 'contributing factors. dissatisfaction' ] = 'True'
tafe_resignation.at[tafe_resignation['contributing factors. dissatisfaction'].isnull(), 'contributing factors. dissatisfaction' ] = np.nan

tafe_resignation.at[tafe_resignation['contributing factors. job dissatisfaction'] == '-', 'contributing factors. job dissatisfaction'] = 'False'
tafe_resignation.at[tafe_resignation['contributing factors. job dissatisfaction'] == 'Job Dissatisfaction', 'contributing factors. job dissatisfaction' ] = 'True'
tafe_resignation.at[tafe_resignation['contributing factors. job dissatisfaction'].isnull(), 'contributing factors. job dissatisfaction' ] = np.nan


# Mark employee as dissatisfied based on factors from the following columns.
tafe_resignation_up = tafe_resignation.copy()
tafe_resignation_up['dissatisfied'] = tafe_resignation_up[['contributing factors. dissatisfaction', 'contributing factors. job dissatisfaction']].any(axis = 1, skipna=False)

dete_resignation_up = dete_resignation.copy()
dete_resignation_up['dissatisfied'] = dete_resignation_up[['job_dissatisfaction', 'dissatisfaction_with_the_department', 'physical_work_environment', 'lack_of_recognition', 'lack_of_job_security', 'work_location', 'employment_conditions', 'work_life_balance', 'workload']].any(axis = 1, skipna = False)


# Add a column to the two dataframes to distinguish the data between the two
tafe_resignation_up['source'] = 'TAFE'
dete_resignation_up['source'] = 'DETE'


# Combine the two datasets and remove any columns with more than 500 null values.
combined_resignation = pd.concat([tafe_resignation_up, dete_resignation_up], axis = 0, ignore_index = True).dropna(thresh = 500, axis = 1)


# Extract the differnt data types in the 'institute_service' column and establish a single format of reference.
def i_service_map(element):
    element = int(element)
    if element == 00:
        return np.nan
    elif element < 3:
        return 'New: 0-2 years'
    elif element <= 6 and element >=3:
        return 'Experienced: 3-6 years'
    elif element <= 10 and element >=7: 
        return 'Established: 7-10 years'
    elif element >= 11:
        return 'Veteran: 11+ years'

def extract_value(index):
    years = r"[1-1000](\d)"
    index = str(index)
    if "than" in index:
        index = index.split(" ")[2]
    return index

combined_resignation['time_in_service'] = combined_resignation['institute_service'].apply(extract_value).astype(str).str.split('-').str[-1].replace('nan', "00")
combined_resignation['time_in_service'] = combined_resignation['time_in_service'].apply(i_service_map)                                             


# Reassign a new 'id' number for each number to the same format.
combined_resignation['id'] = combined_resignation['id'].index + 1


# Fill in the null values for the particular column
combined_resignation[combined_resignation['cease_date'] == 'nan'] = '2012'


# Reassign the ages in the 'age' column to to the same format and remove null values.
combined_resignation['age'] = combined_resignation['age'].replace('21 \x96 25', '21-25').replace('31 \x96 35', '31-35').replace('26 \x96 30', '26-30').replace('41 \x96 45', '41-45').replace('56 or older', '56-60').replace('46 \x96 50', '46-50').replace('36 \x96 40', '36-40').replace('2012', 'nan')
combined_resignation = combined_resignation.drop(combined_resignation[combined_resignation['age'] == 'nan'].index)


# Format the boolean values to match one another.
combined_resignation[combined_resignation['dissatisfied'] == True] = 'True'
combined_resignation[combined_resignation['dissatisfied'] == False] = 'False'


# Replace missing values with the boolean value, 'False' (Most Frequent)
combined_resignation['dissatisfied'] = combined_resignation['dissatisfied'].replace(np.nan, 'False')


# Remove any additional records with outstanding null values in each column.
combined_resignation = combined_resignation.dropna(axis = 0)


# Remove any additional records that are inherently incorrect.
error_rows_t = combined_resignation[combined_resignation['id'] == 'True'].index
error_rows_f = combined_resignation[combined_resignation['id'] == 'False'].index
combined_resignation.drop(error_rows_t, inplace = True)
combined_resignation.drop(error_rows_f, inplace = True)


# Export dataframe to a csv file.
tafe_dete_survey = combined_resignation.to_csv('Tafe_Dete_Clean.csv', index = True)


