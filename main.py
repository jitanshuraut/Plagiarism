import json
from flask import Flask, render_template, request, jsonify
from PlagiarismChecker_sent import check
import os
import torch
from keras.utils import pad_sequences
from transformers import BertTokenizer,  AutoModelForSequenceClassification
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from tqdm import tqdm
import pandas as pd
from Plagr_sourceCode import plagerised_ratio,plagiarismCheck_Winn
DEVELOPMENT_ENV = True


model_path = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_path, do_lower_case=True)
model = AutoModelForSequenceClassification.from_pretrained(
    model_path, output_attentions=False, output_hidden_states=True)
def create_vector_from_text(tokenizer, model, text, MAX_LEN=510):

    input_ids = tokenizer.encode(
        text,
        add_special_tokens=True,
        max_length=MAX_LEN,
    )

    results = pad_sequences([input_ids], maxlen=MAX_LEN, dtype="long",
                            truncating="post", padding="post")

    input_ids = results[0]

    attention_mask = [int(i > 0) for i in input_ids]

    input_ids = torch.tensor(input_ids)
    attention_mask = torch.tensor(attention_mask)

    input_ids = input_ids.unsqueeze(0)
    attention_mask = attention_mask.unsqueeze(0)

    model.eval()

    with torch.no_grad():
        logits, encoded_layers = model(
            input_ids=input_ids,
            token_type_ids=None,
            attention_mask=attention_mask,
            return_dict=False)

    layer_i = 12
    batch_i = 0
    token_i = 0

    # Embedding.
    vector = encoded_layers[layer_i][batch_i][token_i]

    vector = vector.detach().cpu().numpy()

    return (vector)


def create_vector_database(data):
    vectors = []
    source_data = data.text.values
    for text in tqdm(source_data):
        vector = create_vector_from_text(tokenizer, model, text)
        vectors.append(vector)
    data["vectors"] = vectors
    data["vectors"] = data["vectors"].apply(lambda emb: np.array(emb))
    data["vectors"] = data["vectors"].apply(lambda emb: emb.reshape(1, -1))

    return data


def process_document(text):
    text_vect = create_vector_from_text(tokenizer, model, text)
    text_vect = np.array(text_vect)
    text_vect = text_vect.reshape(1, -1)
    return text_vect


def is_plagiarism(similarity_score, plagiarism_threshold):
    is_plagiarism = False
    if (similarity_score >= plagiarism_threshold):
        is_plagiarism = True
    return is_plagiarism


def run_plagiarism_analysis(query_text, data, plagiarism_threshold=0.8):
    top_N = 3
    query_vect = process_document(query_text)
    data["similarity"] = data["vectors"].apply(
        lambda x: cosine_similarity(query_vect, x))
    data["similarity"] = data["similarity"].apply(lambda x: x[0][0])

    similar_articles = data.sort_values(
        by='similarity', ascending=False)[0:top_N+1]
    formated_result = similar_articles[[
        "id", "similarity", "text"]].reset_index(drop=True)
    similarity_score = formated_result.iloc[0]["similarity"]
    most_similar_article = formated_result.iloc[0]["text"]
    whole_text = formated_result.iloc[0]["text"]
    is_plagiarism_bool = is_plagiarism(similarity_score, plagiarism_threshold)

    plagiarism_decision = {'similarity_score': similarity_score,
                           'is_plagiarism': is_plagiarism_bool,
                           'most_similar_article': most_similar_article,
                           'article_submitted': query_text,
                           'content': whole_text
                           }

    return plagiarism_decision


app = Flask(__name__)


@app.route("/Folder/Distance", methods=['POST'])
def Folder():
    try:
        req_data = request.get_json()

        string1 = req_data['examined_file']
        string2 = req_data['reference_files']

        result = []
        for i in range(len(string1)):
            temp = check(string1[i], string2, 0.8, None, False)
            for elm2 in temp:
                result.append(elm2)

        return str(result)
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request.'}), 500


@app.route("/Folder/BERT/TRAIN", methods=['POST'])
def Folder_TRAIN():
    try:
        req_data = request.get_json()

        string1 = req_data['examined_file']
        output_file = 'output.json'
        json_data = []
        id=0
        for i in range(0, len(string1)):
         with open(string1[i], 'r') as file:
          lines = file.read().splitlines()


        for j, line in enumerate(lines):
         if(len(line)==0):
            line="Random"

         json_object = {'id': id, 'text': line}
         id=id+1
         json_data.append(json_object)


        with open(output_file, 'w') as json_file:
         json.dump(json_data, json_file, indent=4)



        df=pd.read_json("output.json")
        df.to_csv("ext.csv",index=False)
        df = pd.read_csv('ext.csv')
        
        return ("true")

    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request.'}), 500




@app.route("/Folder/BERT_TEST", methods=['POST'])
def Folder_TEST():
    try:
        req_data = request.get_json()
        df = pd.read_csv('ext.csv')
        vector_database = create_vector_database(df)

        string1 = req_data['Test']
        result=run_plagiarism_analysis(string1, vector_database, plagiarism_threshold=0.8)

        return str(result)
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request.'}), 500




@app.route("/Folder/Source_Code/Winn", methods=['POST'])
def Folder_TEST_Source():
    try:
        req_data = request.get_json()
        string1 = req_data['examined_file']
        string2 = req_data['reference_files']

        return str(plagiarismCheck_Winn(string1,string2))
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request.'}), 500




@app.route("/Folder/Source_Code/Seq", methods=['POST'])
def Folder_TEST_Source_Seq():
    try:
        req_data = request.get_json()
        string1 = req_data['examined_file']
        string2 = req_data['reference_files']

        return str(plagerised_ratio(string1,string2))
    except Exception as e:
        return jsonify({'error': 'An error occurred while processing the request.'}), 500



if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)
