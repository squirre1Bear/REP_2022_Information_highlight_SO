import spacy
import json
import pandas as pd
import logging
import pickle
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


with open ('/home/shahla/Test_version_spaCy_1/Output_file_bold_test', 'rb') as fp:
    docs = pickle.load(fp)
nlp = spacy.load("/home/shahla/Model/Model_bold_all_3")
from spacy.training import offsets_to_biluo_tags
def get_cleaned_label(label: str):
    if "-" in label:
        # print(label.split("-"))
        label_1 = label.split("-")
        if len(label_1) == 2:
            return label.split("-")[1]
        else:
            return label.split("-")[2]
    else:
        return label
    
def create_total_target_vector(docs):
    target_vector = []
    for doc in docs:
        new = nlp.make_doc(doc[0])
        entities = doc[1]["entities"]
        bilou_entities = offsets_to_biluo_tags(new, entities)
        final = []
        for item in bilou_entities:
            final.append(get_cleaned_label(item))
        target_vector.extend(final)
    return target_vector

def create_prediction_vector(text):
    return [get_cleaned_label(prediction) for prediction in get_all_ner_predictions(text)]

def create_total_prediction_vector(docs: list):
    prediction_vector = []
    for doc in docs:
        prediction_vector.extend(create_prediction_vector(doc[0]))
    return prediction_vector

def get_all_ner_predictions(text):
    doc = nlp(text)
    entities = [(e.start_char, e.end_char, e.label_) for e in doc.ents]
    bilou_entities = offsets_to_biluo_tags(doc, entities)
    return bilou_entities

def get_model_labels():
    labels = list(nlp.get_pipe("ner").labels)
    labels.append("O")
    return sorted(labels)
def get_dataset_labels():
    return sorted(set(create_total_prediction_vector(docs)))

def generate_confusion_matrix(docs): 
    classes = sorted(set(create_total_target_vector(docs)))
    y_true = create_total_target_vector(docs)
    y_pred = create_total_prediction_vector(docs)
    print(classification_report(y_true, y_pred, target_names=classes))
    # print(type(y_true))
    # print(type(y_pred))
    return confusion_matrix(y_true, y_pred, labels=classes)

if __name__ == '__main__':

    cm = generate_confusion_matrix(docs)
    print(cm)