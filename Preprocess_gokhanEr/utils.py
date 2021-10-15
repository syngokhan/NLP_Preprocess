import re
import os
import sys

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import spacy
from spacy.lang.en.stop_words import  STOP_WORDS as stopwords
from textblob import TextBlob
from bs4 import BeautifulSoup
import unicodedata

nlp = spacy.load("en_core_web_sm")

def _get_wordcounts(words):

    s = str(words).split()
    word_length = len(s)

    return word_length

def _get_charcounts(words):

    s = str(words).split()
    words = "".join(s)
    char_length = len(words)

    return char_length

def _get_avg_wordlength(words):

    avg = _get_charcounts(words) / _get_wordcounts(words)

    return avg

def _get_stopwords_counts(words):

    length = ([word for word in words.split() if word in stopwords])

    return length

def _get_hashtag_counts(words):

    hashtags_length = len([word for word in words if word.startswith("#")])

    return hashtags_length

def _get_mentions_counts(words):

    mentions_length = len([word for word in words if word.startswith("@")])

    return mentions_length

def _get_digit_counts(words):

    digit_length = len([word for word in words if word.isdigit()])

    return digit_length

def _get_uppercase_counts(words):

    uppercase_length = len([word for word in words if word.isupper()])

    return uppercase_length

def _get_lower_convert(words):

    lower_words = str(words).lower()

    return lower_words

def _cont_exp(words):

    contractions = {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "can't've": "cannot have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'd've": "he would have",
        "he'll": "he will",
        "he'll've": "he will have",
        "he's": "he is",
        "how'd": "how did",
        "how'd'y": "how do you",
        "how'll": "how will",
        "how's": "how does",
        "i'd": "i would",
        "i'd've": "i would have",
        "i'll": "i will",
        "i'll've": "i will have",
        "i'm": "i am",
        "i've": "i have",
        "isn't": "is not",
        "it'd": "it would",
        "it'd've": "it would have",
        "it'll": "it will",
        "it'll've": "it will have",
        "it's": "it is",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "mightn't've": "might not have",
        "must've": "must have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "needn't": "need not",
        "needn't've": "need not have",
        "o'clock": "of the clock",
        "oughtn't": "ought not",
        "oughtn't've": "ought not have",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "shan't've": "shall not have",
        "she'd": "she would",
        "she'd've": "she would have",
        "she'll": "she will",
        "she'll've": "she will have",
        "she's": "she is",
        "should've": "should have",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "so've": "so have",
        "so's": "so is",
        "that'd": "that would",
        "that'd've": "that would have",
        "that's": "that is",
        "there'd": "there would",
        "there'd've": "there would have",
        "there's": "there is",
        "they'd": "they would",
        "they'd've": "they would have",
        "they'll": "they will",
        "they'll've": "they will have",
        "they're": "they are",
        "they've": "they have",
        "to've": "to have",
        "wasn't": "was not",
        " u ": " you ",
        " ur ": " your ",
        " n ": " and ",
        "won't": "would not",
        'dis': 'this',
        'bak': 'back',
        'brng': 'bring'}

    if type(words) is str:
        for key in contractions:
            value = contractions[key]
            words = words.replace(key,value)
        return words

    else:

        return words

def _get_emails(words) :

    emails_list = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)', words)
    emails_length = len(emails_list)

    return emails_length, emails_list

def _get_urls(words):

    urls_list = re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', words)
    urls_length = len(urls_list)

    return urls_length, urls_list

def _get_remove_emails(words):

    words = re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"",words)

    return words

def _remove_urls(words):

    words = re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',"",words)

    return words

def _remove_rt(words):

    words = re.sub("r\brt\b","",words)

    return words

def _remove_special_chars(words):

    """
    Special Chars Removal or Punctuation Removal ;
    Remove Multiple Spaces

    """

    words = re.sub(r"[^\w ]","",words)
    words = " ".join(words.split())

    return words

def _remove_html_tags(words):

    words = BeautifulSoup(words,"lxml").get_text().strip()

    return words

def _remove_accented_chars(words):

    words = unicodedata.normalize("NFKD",words).encode("ascii","ignore").decode("utf-8","ignore")

    return words

def _remove_stopwords(words):

    words_list = [word for word in words.split() if word not in stopwords]
    words = " ".join(words_list)

    return words

def _get_value_counts(dataframe,col_name,n=20,plot = False):

    texts  = " ".join(dataframe[col_name])
    texts = texts.split()
    frequence = pd.Series(texts).value_counts().reset_index()
    frequence.columns = ["Name","Counts"]
    frequence = frequence.sort_values(by = "Counts",
                                      ascending=False)
    if plot:

        plt.figure(figsize = (15,8))
        sns.barplot(x = "Counts", y = "Name", data = frequence.head(n))
        plt.title("Frequence Names" , fontsize = 15)
        plt.xlabel("Counts",fontsize = 15)
        plt.ylabel("Name",fontsize = 15)
        plt.show()

    return frequence

def _remove_common_words(words,remove_words):

    words_list = [word for word in words.split() if word not in remove_words ]
    words = " ".join(words_list)

    return words

def _remove_rare_words(words,remove_words):

    words_list = [word for word in words.split() if word not in remove_words ]
    words = " ".join(words_list)

    return words

def _get_make_base(words):

    words = str(words)
    words_list = []
    doc = nlp(words)

    for token in doc:
        lemma = token.lemma_
        if lemma == "-PRON-" or lemma == "be":
            lemma = token.text

        words_list.append(lemma)

    return " ".join(words_list)

def _spelling_correction(words):

    correct_words = TextBlob(words).correct()

    return correct_words