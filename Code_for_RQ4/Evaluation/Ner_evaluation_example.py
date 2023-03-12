from __future__ import unicode_literals, print_function
import pickle
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
from spacy.training.example import Example
from tqdm import tqdm
import pandas as pd

df = pd.read_csv('/home/shahla/Test_bert_model/italic_data_ver2_test_lines.csv')
df.drop_duplicates()

nlp2 = spacy.load(output_dir)
result_dataframe = pd.read_csv('/home/shahla/Datasets_all/italic_last_only_another.csv',index_col=0)
List_of_BOE_code = []
for index, row in result_dataframe.iterrows():
    answer_html = str(row['Sentence_without_html'])
    doc2 = nlp2(answer_html)

    # print(doc2)
    tuple_list = []
    for ent in doc2.ents:
        # print(ent.label_, ent.text)
        code_tuple = ent.label_, ent.text
        tuple_list.append(code_tuple)
    List_of_BOE_code.append(tuple_list)
    
result_dataframe['List_of_BOE_code'] = List_of_BOE_code
result_dataframe.to_csv('italic_all_test_sentences_spacy_dataset_2.csv')