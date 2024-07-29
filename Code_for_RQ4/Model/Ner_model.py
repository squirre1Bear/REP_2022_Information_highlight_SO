#!/usr/bin/env python
# coding: utf-8

# Training additional entity types using spaCy
from __future__ import unicode_literals, print_function
import pickle
import random
from pathlib import Path
import spacy
from spacy.util import minibatch
from spacy.training.example import Example
from tqdm import tqdm
from sklearn.model_selection import train_test_split

# New entity labels
# Specify the new entity labels which you want to add here
# LABEL = ['BoldStartTag', 'BoldStopTag', 'ItalicStartTag', 'ItalicStopTag', 'HeadingStartTag', 'HeadingStopTag', 'DeleteStartTag', 'DeleteStopTag', 'CodeStartTag', 'CodeStopTag']
# LABEL = ['B-code','I-code']
# LABEL = ['B-italic','I-italic','E-italic','O']
LABEL = ['B-bold','I-bold','E-bold','O']
# LABEL = ['B-bold','I-bold','O','B-italic','I-italic','B-heading','I-heading','B-code','I-code','B-del','I-del']

# Loading training data 
"'下面这个是bold类型正确的代码'"
# training_data_path = 'home/shahla/ProjectWorkHTML/Posts_csv_files/Dataset_files/TrainingSet/Output_file_bold_train'
training_data_path = 'home/shahla/ProjectWorkHTML/Posts_csv_files/Dataset_files/TrainingSet/Output_file_heading_train'
# 这边发现编码应该是'ISO-8859-1'，而不是utf-8
# 这里直接读取的数据集应该是正确的，其中包含了 I-bold、B-bold等标记。
# with open(training_data_path, 'r', encoding='ISO-8859-1') as file:
#     content = file.read()
#     print(content)

with open(training_data_path, 'rb') as fp:
    Total_DATA = pickle.load(fp)    # 这边的数据结果是正确的
    # Splitting data into train and test sets
    TRAIN_DATA, test_d = train_test_split(Total_DATA, test_size=0.20, random_state=0)

"'这里的n_iter应该是5'"

def main(model=None, new_model_name='ner_model_bold_all', output_dir=None, n_iter=1):
    """Setting up the pipeline and entity recognizer, and training the new entity."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spacy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")

    ner = nlp.add_pipe('ner')
    nlp.add_pipe('sentencizer')

    for label in LABEL:
        ner.add_label(label)   # Add new entity labels to entity recognizer

    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.entity.create_optimizer()

    # Get names of other pipes to disable them during training to train only NER
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
         for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            batches = minibatch(TRAIN_DATA, size=32)
            for batch in tqdm(batches):
# 这句是我新家的
                losses = {}
            # 下面的texts是单纯文本，annotations记录标记（B-bold、I-bold等），以及出现的位置信息
                texts, annotations = zip(*batch)
                # print(" ")
                # print("下面输出69行的annotations:")
                # print(annotations)
                example = []
                # Update the model with iterating each text
                for i in range(len(texts)):
                    doc = nlp.make_doc(texts[i])
                    example.append(Example.from_dict(doc, annotations[i]))
                    
                # Update the model
                nlp.update(example, drop=0.35, losses=losses)
                print('   Losses',losses)     # 每it输出一个losses值

            print('Losses', losses)

    # Save model 
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)
    
    if output_dir is None:
        print("output_dir is none!")

    # Evaluate model
    if test_d:
        print("hi!!!")
        example_2 = []
        for text_text, annotations in tqdm(test_d):
            doc2 = nlp.make_doc(text_text)
            example_2.append(Example.from_dict(doc2, annotations))
        print(nlp.evaluate(example_2))

if __name__ == '__main__':
    main(output_dir="/home/shahla/ProjectWorkHTML/Models/Model_heading") 