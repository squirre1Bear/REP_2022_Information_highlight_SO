#!/usr/bin/env python
# coding: utf-8
# After getting the results for per tags, this code combines all the results and generates the mean median and maximum for the whole dataset.


import pandas as pd
import glob
import os
import numpy


# setting the path for joining multiple files
files = os.path.join("/home/shahla/ProjectWorkHTML/Posts_csv_files/Delete", "*.csv")

# list of merged files returned
files = glob.glob(files)

# print("Resultant CSV after joining all CSV files at a particular location...");

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
# print(df)




df = df.drop_duplicates() # drop all the duplicate values




print(df.count()) # provides the count of the values

# Generate the mean, median and maximum of the highlighted word percentage and number of cases. To find out which data had the highest values, idmax() prints out the answer id.



mean_of_html = df['Number_of_cases'].mean()
median_of_html = df['Number_of_cases'].median()
maximum_of_html = df['Number_of_cases'].max()
print('Mean ' + str(mean_of_html) + "\n Median " + str(median_of_html) + "\n Maximum " + str(maximum_of_html))




df['Highlighted_text_percentage'] = numpy.where(df['Highlighted_text_length'] < 1, 0, df['Highlighted_text_length']/df['Answers_lengths']*100)
df['Highlighted_word_percentage'] = numpy.where(df['Highlighted_text_words'] < 1, 0, df['Highlighted_text_words']/df['Answers_words']*100)





mean_of_h_word = df['Highlighted_word_percentage'].mean()
median_of_h_word = df['Highlighted_word_percentage'].median()
maximum_of_h_word = df['Highlighted_word_percentage'].max()

if maximum_of_h_word > 100: # this could happen if the word division includes empty spaces as words.
    maximum_of_h_word = 100

print('Mean ' + str(mean_of_h_word) + "\n Median " + str(median_of_h_word) + "\n Maximum " + str(maximum_of_h_word))




# save the maximum values in a file
df[df['Highlighted_word_percentage']==df['Highlighted_word_percentage'].max()].to_csv('/home/shahla/ProjectWorkHTML/showMax_itPost.csv')




df.to_csv('/home/shahla/ProjectWorkHTML/All_3M_per_Posts_delete_body_2.csv') # save the file





