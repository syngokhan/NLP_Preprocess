import re
import os
import sys
import json

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

    """
    True False dönüyor zaten Startswith("#")
    """

    hashtags_length = len([word for word in words if word.startswith("#")])

    return hashtags_length

def _get_mentions_counts(words):

    mentions_length = len([word for word in words if word.startswith("@")])

    return mentions_length

def _get_digit_counts(words):


    digit = re.findall(r"[0-9,.]+",words)
    digit_length = len(digit)

    return digit_length

def _get_uppercase_counts(words):

    uppercase_length = len([word for word in words if word.isupper()])

    return uppercase_length

def _get_lower_convert(words):

    lower_words = str(words).lower()

    return lower_words

def _cont_exp(words):

    contractions = {
        "€": "euro",
        "4ao": "for adults only",
        "a.m": "before midday",
        "a3": "anytime anywhere anyplace",
        "aamof": "as a matter of fact",
        "acct": "account",
        "adih": "another day in hell",
        "afaic": "as far as i am concerned",
        "afaict": "as far as i can tell",
        "afaik": "as far as i know",
        "afair": "as far as i remember",
        "afk": "away from keyboard",
        "app": "application",
        "approx": "approximately",
        "apps": "applications",
        "asap": "as soon as possible",
        "asl": "age, sex, location",
        "atk": "at the keyboard",
        "ave.": "avenue",
        "aymm": "are you my mother",
        "ayor": "at your own risk",
        "b&b": "bed and breakfast",
        "b+b": "bed and breakfast",
        "b.c": "before christ",
        "b2b": "business to business",
        "b2c": "business to customer",
        "b4": "before",
        "b4n": "bye for now",
        "b@u": "back at you",
        "bae": "before anyone else",
        "bak": "back at keyboard",
        "bbbg": "bye bye be good",
        "bbc": "british broadcasting corporation",
        "bbias": "be back in a second",
        "bbl": "be back later",
        "bbs": "be back soon",
        "be4": "before",
        "bfn": "bye for now",
        "blvd": "boulevard",
        "bout": "about",
        "brb": "be right back",
        "bros": "brothers",
        "brt": "be right there",
        "bsaaw": "big smile and a wink",
        "btw": "by the way",
        "bwl": "bursting with laughter",
        "c/o": "care of",
        "cet": "central european time",
        "cf": "compare",
        "cia": "central intelligence agency",
        "csl": "can not stop laughing",
        "cu": "see you",
        "cul8r": "see you later",
        "cv": "curriculum vitae",
        "cwot": "complete waste of time",
        "cya": "see you",
        "cyt": "see you tomorrow",
        "dae": "does anyone else",
        "dbmib": "do not bother me i am busy",
        "diy": "do it yourself",
        "dm": "direct message",
        "dwh": "during work hours",
        "e123": "easy as one two three",
        "eet": "eastern european time",
        "eg": "example",
        "embm": "early morning business meeting",
        "encl": "enclosed",
        "encl.": "enclosed",
        "etc": "and so on",
        "faq": "frequently asked questions",
        "fawc": "for anyone who cares",
        "fb": "facebook",
        "fc": "fingers crossed",
        "fig": "figure",
        "fimh": "forever in my heart",
        "ft.": "feet",
        "ft": "featuring",
        "ftl": "for the loss",
        "ftw": "for the win",
        "fwiw": "for what it is worth",
        "fyi": "for your information",
        "g9": "genius",
        "gahoy": "get a hold of yourself",
        "gal": "get a life",
        "gcse": "general certificate of secondary education",
        "gfn": "gone for now",
        "gg": "good game",
        "gl": "good luck",
        "glhf": "good luck have fun",
        "gmt": "greenwich mean time",
        "gmta": "great minds think alike",
        "gn": "good night",
        "g.o.a.t": "greatest of all time",
        "goat": "greatest of all time",
        "goi": "get over it",
        "gps": "global positioning system",
        "gr8": "great",
        "gratz": "congratulations",
        "gyal": "girl",
        "h&c": "hot and cold",
        "hp": "horsepower",
        "hr": "hour",
        "hrh": "his royal highness",
        "ht": "height",
        "ibrb": "i will be right back",
        "ic": "i see",
        "icq": "i seek you",
        "icymi": "in case you missed it",
        "idc": "i do not care",
        "idgadf": "i do not give a damn fuck",
        "idgaf": "i do not give a fuck",
        "idk": "i do not know",
        "ie": "that is",
        "i.e": "that is",
        "ifyp": "i feel your pain",
        "IG": "instagram",
        "iirc": "if i remember correctly",
        "ilu": "i love you",
        "ily": "i love you",
        "imho": "in my humble opinion",
        "imo": "in my opinion",
        "imu": "i miss you",
        "iow": "in other words",
        "irl": "in real life",
        "j4f": "just for fun",
        "jic": "just in case",
        "jk": "just kidding",
        "jsyk": "just so you know",
        "l8r": "later",
        "lb": "pound",
        "lbs": "pounds",
        "ldr": "long distance relationship",
        "lmao": "laugh my ass off",
        "lmfao": "laugh my fucking ass off",
        "lol": "laughing out loud",
        "ltd": "limited",
        "ltns": "long time no see",
        "m8": "mate",
        "mf": "motherfucker",
        "mfs": "motherfuckers",
        "mfw": "my face when",
        "mofo": "motherfucker",
        "mph": "miles per hour",
        "mr": "mister",
        "mrw": "my reaction when",
        "ms": "miss",
        "mte": "my thoughts exactly",
        "nagi": "not a good idea",
        "nbc": "national broadcasting company",
        "nbd": "not big deal",
        "nfs": "not for sale",
        "ngl": "not going to lie",
        "nhs": "national health service",
        "nrn": "no reply necessary",
        "nsfl": "not safe for life",
        "nsfw": "not safe for work",
        "nth": "nice to have",
        "nvr": "never",
        "nyc": "new york city",
        "oc": "original content",
        "og": "original",
        "ohp": "overhead projector",
        "oic": "oh i see",
        "omdb": "over my dead body",
        "omg": "oh my god",
        "omw": "on my way",
        "p.a": "per annum",
        "p.m": "after midday",
        "pm": "prime minister",
        "poc": "people of color",
        "pov": "point of view",
        "pp": "pages",
        "ppl": "people",
        "prw": "parents are watching",
        "ps": "postscript",
        "pt": "point",
        "ptb": "please text back",
        "pto": "please turn over",
        "qpsa": "what happens",
        "ratchet": "rude",
        "rbtl": "read between the lines",
        "rlrt": "real life retweet",
        "rofl": "rolling on the floor laughing",
        "roflol": "rolling on the floor laughing out loud",
        "rotflmao": "rolling on the floor laughing my ass off",
        "rt": "retweet",
        "ruok": "are you ok",
        "sfw": "safe for work",
        "sk8": "skate",
        "smh": "shake my head",
        "sq": "square",
        "srsly": "seriously",
        "ssdd": "same stuff different day",
        "tbh": "to be honest",
        "tbs": "tablespooful",
        "tbsp": "tablespooful",
        "tfw": "that feeling when",
        "thks": "thank you",
        "tho": "though",
        "thx": "thank you",
        "tia": "thanks in advance",
        "til": "today i learned",
        "tl;dr": "too long i did not read",
        "tldr": "too long i did not read",
        "tmb": "tweet me back",
        "tntl": "trying not to laugh",
        "ttyl": "talk to you later",
        "u": "you",
        "u2": "you too",
        "u4e": "yours for ever",
        "utc": "coordinated universal time",
        "w/": "with",
        "w/o": "without",
        "w8": "wait",
        "wassup": "what is up",
        "wb": "welcome back",
        "wtf": "what the fuck",
        "wtg": "way to go",
        "wtpa": "where the party at",
        "wuf": "where are you from",
        "wuzup": "what is up",
        "wywh": "wish you were here",
        "yd": "yard",
        "ygtr": "you got that right",
        "ynk": "you never know",
        "zzz": "sleeping bored and tired",
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
        "ur": "your",
        "n": "and",
        "won't": "would not",
        "dis": "this",
        "brng": "bring"}

    if type(words) is str:
        for key in contractions:
            values = contractions[key]
            raw_text = r"\b" + key + r"\b"
            words = re.sub(raw_text,values,words)

        return words

    else:

        return words

def _get_emails(words) :

    emails_list = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', words)

    emails_length = len(emails_list)

    return emails_length, emails_list

def _get_urls(words):

    urls_list = re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', words)
    urls_length = len(urls_list)

    return urls_length, urls_list

def _remove_emails(words):

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

    words = re.sub(r"[^\w ]+","",words)
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

def _remove_dups_char(words):

    """
    * lllooooovvveeee youuuu
    * love you
    """

    words = re.sub("(.)\\1{2,}","\\1",words)
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

def _get_basic_features(dataframe):

    if type(dataframe) == pd.pandas.core.frame.DataFrame :

        dataframe['char_counts'] = dataframe['text'].apply(lambda x: _get_charcounts(x))
        dataframe['word_counts'] = dataframe['text'].apply(lambda x: _get_wordcounts(x))
        dataframe['avg_wordlength'] = dataframe['text'].apply(lambda x: _get_avg_wordlength(x))
        dataframe['stopwords_counts'] = dataframe['text'].apply(lambda x: _get_stopwords_counts(x))
        dataframe['hashtag_counts'] = dataframe['text'].apply(lambda x: _get_hashtag_counts(x))
        dataframe['mentions_counts'] = dataframe['text'].apply(lambda x: _get_mentions_counts(x))
        dataframe['digits_counts'] = dataframe['text'].apply(lambda x: _get_digit_counts(x))
        dataframe['uppercase_counts'] = dataframe['text'].apply(lambda x: _get_uppercase_counts(x))
    else:

        print("ERROR : This functions takes only Pandas DataFrame")

    return dataframe
