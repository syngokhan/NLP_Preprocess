from Preprocess_gokhanEr import utils

__version__ = "0.0.1"

def get_wordcounts(words):
    return utils._get_wordcounts(words)

def get_charcounts(words):
    return utils._get_charcounts(words)

def get_avg_wordlength(words):
    return utils._get_avg_wordlength(words)

def get_stopwords_counts(words):
    return utils._get_stopwords_counts(words)

def get_hashtag_counts(words):
    return utils._get_hashtag_counts(words)

def get_mentions_counts(words):
    return utils._get_mentions_counts(words)

def get_digit_counts(words):
    return utils._get_digit_counts(words)

def get_uppercase_counts(words):
    return utils._get_uppercase_counts(words)

def get_lower_convert(words):
    return utils._get_lower_convert(words)

def cont_exp(words):
    return utils._cont_exp(words)

def get_emails(words):
    return utils._get_emails(words)

def get_urls(words):
    return utils._get_urls(words)

def get_remove_emails(words):
    return utils._get_remove_emails(words)

def remove_urls(words):
    return utils._remove_urls(words)

def remove_rt(words):
    return utils._remove_rt(words)

def remove_special_chars(words):
    return utils._remove_special_chars(words)

def remove_html_tags(words):
    return utils._remove_html_tags(words)

def remove_accented_chars(words):
    return utils._remove_accented_chars(words)

def remove_stopwords(words):
    return utils._remove_stopwords(words)

def get_value_counts(dataframe,col_name,n=20,plot = False):
    return utils._get_value_counts(dataframe,col_name,n,plot)

def remove_common_words(words,remove_words):
    return utils._remove_common_words(words,remove_words)

def remove_rare_words(words,remove_words):
    return utils._remove_rare_words(words,remove_words)

def get_make_base(words):
    return utils._get_make_base(words)

def spelling_correction(words):
    return utils._spelling_correction(words)