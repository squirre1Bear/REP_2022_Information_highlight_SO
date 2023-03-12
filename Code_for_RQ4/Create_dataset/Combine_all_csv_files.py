import pandas as pd
import glob
import os

# setting the path for joining multiple files
files = os.path.join("/home/shahla/ProjectWorkHTML/Posts_csv_files/Emphasis_dataset/", "*.csv")

# list of merged files returned
files = glob.glob(files)

print("Resultant CSV after joining all CSV files at a particular location...");

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
print(df)
train = df.sample(frac=0.8, random_state=rng)
test = df.loc[~df.index.isin(train.index)]

train.to_csv('/home/shahla/ProjectWorkHTML/Posts_csv_files/Dataset_files_other_formats/emphasis_data_ver1_train.tsv', sep='\t', encoding='utf-8', index=False)
test.to_csv('/home/shahla/ProjectWorkHTML/Posts_csv_files/Dataset_files_other_formats/emphasis_data_ver1_test.tsv', sep='\t', encoding='utf-8', index=False)