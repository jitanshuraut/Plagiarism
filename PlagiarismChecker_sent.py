
import json
import re
from collections import defaultdict
from itertools import product
import numpy as np
import os

from similarity import jaccard_similarity, cosine_similarity, jaro_winkler_similarity, overlap_similarity, sorensen_dice_similarity, tversky_similarity, _jaro_similarity,levenshtein

LEV=[]
def _text_to_sentences(text):
    """Split the text into sentences using regex"""
    return re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)

def lev(examined_file,reference_files):
    
 
      with open(examined_file, 'r') as file:
          data = file.read().replace('\n', '')
          str1=data.replace(' ', '')
 
      with open(reference_files, 'r') as file:
          data = file.read().replace('\n', '')
          str2=data.replace(' ', '')
 
      if(len(str1)>len(str2)):
          length=len(str1)
      else:
          length=len(str2)
      
      n = 100-round((levenshtein(str1,str2)/length)*100,2)
      return n

def _split_texts_to_sentences(input_doc, reference_docs):
    input_sents = _text_to_sentences(input_doc)
    ref_doc_sents = defaultdict(list)
    for ref_doc, ref_content in reference_docs.items():
        ref_sents = _text_to_sentences(ref_content.replace("\n", " ").strip())
        ref_doc_sents[ref_doc].extend(ref_sents)
    return input_sents, ref_doc_sents


def _cross_check_sentences(
    input_sents, tempfile, ref_doc_sents, results, similarity_threshold, quiet
):
    CTN=0
    for input_sent, (ref_doc, ref_sents) in product(input_sents, ref_doc_sents.items()):
        input_tokens = set(re.findall(r"\b\w+\b", input_sent.lower()))
        for ref_sent in ref_sents:

            ref_tokens = set(re.findall(r"\b\w+\b", ref_sent.lower()))

            similarity_score = cosine_similarity(input_tokens, ref_tokens)+jaccard_similarity(input_tokens, ref_tokens)+overlap_similarity(input_tokens,ref_tokens)+sorensen_dice_similarity(input_tokens,ref_tokens)
            print((input_tokens))
            if similarity_score > similarity_threshold:
                similarity = {
                    "input_sentence": input_sent,
                    "reference_sentence": ref_sent,
                    "reference_document": ref_doc,
                    "similarity_score": similarity_score/4,
                    "examinfile": tempfile
                }
                results.append(similarity)
                if not quiet:
                    _display_similar_sentence(similarity)


def _display_similar_sentence(similarity_dict):
    print("Input Sentence:    ", similarity_dict["input_sentence"])
    print("Reference Sentence:", similarity_dict["reference_sentence"])
    print("Reference Document:", similarity_dict["reference_document"])
    print("Similarity Score: {:.4f}".format(
        similarity_dict["similarity_score"]))
    print()


def _get_all_files_content(examined_file, reference_files):

    with open(examined_file, "r", encoding="utf-8") as f:
        input_text_content = f.read().replace("\n", " ").strip()

    reference_docs = {}
    for ref_doc in reference_files:
        with open(ref_doc, "r", encoding="utf-8") as f:
            reference_docs[ref_doc] = f.read().replace("\n", " ").strip()
    return input_text_content, reference_docs


def check(examined_file, reference_files, similarity_threshold, output_file=None, quiet=False):
    # placeholder for the list of dictionaries
    results = []
    tempfile = examined_file

    input_doc, reference_docs = _get_all_files_content(examined_file, reference_files)
    input_sents, ref_doc_sents = _split_texts_to_sentences(
        input_doc, reference_docs)

    _cross_check_sentences(input_sents, tempfile,
                           ref_doc_sents, results, similarity_threshold, quiet)
    

    return results
