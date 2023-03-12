import logging
import argparse
import sys
import os
import json
import pickle
from csv import reader,DictWriter
from itertools import islice
import pandas as pd
import glob
import os


def word_to_sentence(input_path,output_path): 
    try: 
        read_file = open(input_path,'r',encoding="utf8")
#         file_write = open(output_path, 'w')
        with open(output_path, 'w', newline='',encoding="utf8") as csvfile:
            fieldnames = ['text','labels']
            writer = DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            text_string = ''
            labels_string = ''


#             for line in read_file:
            for line in islice(read_file, 1, None):

                if line[0:len(line)-1]!='.\tO':
                    word,entity = line.split('\t')
                    entity = entity.replace('\t', '')
                    entity = entity.replace('\n', '')
                    text_string +=word+" "
                    labels_string += entity + " "
#                     print(entity)
                else:
                    labels_string_2 = labels_string.replace('\t', '')
                    writer.writerow({fieldnames[0]: text_string,fieldnames[1]:labels_string_2})
                    text_string = ""
                    labels_string = ''
#                     print("n")
    except Exception as e:
        logging.exception("Unable to process file" +line+ "\n" + "error = " + str(e))
        return None

if __name__ == '__main__':

    filename_1 = "/home/shahla/ProjectWorkHTML/Posts_csv_files/Dataset_files_other_formats/All_only_last.tsv"
    filename_2 = "/home/shahla/ProjectWorkHTML/Posts_csv_files/Dataset_files_other_formats/All_only_last_line.csv"
    word_to_sentence(filename_1,filename_2)