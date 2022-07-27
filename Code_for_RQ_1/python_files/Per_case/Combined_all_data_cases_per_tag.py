#!/usr/bin/env python
# coding: utf-8
# After getting the results for per tags, this code combines all the results and generates the mean median and maximum for the whole dataset.


import pandas as pd
import glob
import os

# setting the path for joining multiple files. 
files = os.path.join("/home/shahla/ProjectWorkHTML/Posts_csv_files/Delete/Tags", "*.csv")

# list of merged files returned
files = glob.glob(files)

# print("Resultant CSV after joining all CSV files at a particular location...");

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
# print(df)


df = df.drop_duplicates() # drop all the duplicate values

print(df.count()) # provides the count of the values

# Generate the mean, median and maximum of the highlighted text length and word count. To find out which data had the highest values, idmax() prints out the answer id.



mean_of_characters = df['Highlighted_text_length'].mean()
median_of_characters = df['Highlighted_text_length'].median()
maximum_of_characters = df['Highlighted_text_length'].max()
mean_of_word_count = df['Highlighted_text_words'].mean()
median_of_word_count = df['Highlighted_text_words'].median()
maximum_of_word_count = df['Highlighted_text_words'].max()
print('Mean ' + str(mean_of_characters) + " Median " + str(median_of_characters) + " Maximum " + str(maximum_of_characters))
print('Mean ' + str(mean_of_word_count) + " Median " + str(median_of_word_count) + " Maximum " + str(maximum_of_word_count))


print(df['Highlighted_text_length'].idxmax())
print(df['Highlighted_text_words'].idxmax())

df.to_csv('/home/shahla/ProjectWorkHTML/All_3M_per_tags_delete_body_2.csv') # save the file





