#!/usr/bin/env python
# coding: utf-8


# Training additional entity types using spaCy
from __future__ import unicode_literals, print_function
import pickle
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
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

"""
Bold = strong,b
Italic = em,i
Heading = h1,h2,h3
Delete = s,del
Code = code
"""
# Loading training data 
with open ('/home/shahla/ProjectWorkHTML/Posts_csv_files/Dataset_files/bold_data_ver2_train', 'rb') as fp:
    Total_DATA = pickle.load(fp)
    TRAIN_DATA,test_d = train_test_split(TRAIN_DATA, test_size=0.20, random_state=0)  



def main(model=None, new_model_name='ner_model_bold_all', output_dir=None, n_iter=5):
    """Setting up the pipeline and entity recognizer, and training the new entity."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spacy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")

    ner = nlp.add_pipe('ner')
    nlp.add_pipe('sentencizer')

    for i in LABEL:
        ner.add_label(i)   # Add new entity labels to entity recognizer

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
            print(batches)
            for batch in tqdm(batches):
                texts, annotations = zip(*batch)
#                 nlp.update(texts, annotations, sgd=optimizer, drop=0.35,losses=losses)
                example = []
                # Update the model with iterating each text
                for i in range(len(texts)):
                    doc = nlp.make_doc(texts[i])
                    example.append(Example.from_dict(doc, annotations[i]))

                # Update the model
                nlp.update(example, drop=0.35, losses=losses)
#                 print('Losses', losses)

            print('Losses', losses)

    # Save model 
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)
    example_2 = []
    
    for text_text, annotations in tqdm(test_d):
        doc2 = nlp.make_doc(text_text)

        example_2.append(Example.from_dict(doc2, annotations))
    print(nlp.evaluate(example_2))

if __name__ == '__main__':
    main(output_dir="/home/shahla/ProjectWorkHTML/Models/Model_bold_all_5_it_32_different_dataset_ev")
