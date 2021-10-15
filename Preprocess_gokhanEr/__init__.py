from Preprocess_gokhanEr import utils

__version__ = "0.0.1"

def get_wordcounts(words):
    """
    Word Count

    :param words:
    :return: Word Counts (Number)
    """

    return utils._get_wordcounts(words)

def get_charcounts(words):

    """
    Character Counts

    :param words:
    :return: Character Counts (Number)
    """


    return utils._get_charcounts(words)

def get_avg_wordlength(words):
    """
    Average Word Length

    :param words:
    :return: Average Word Length(Number)
    """

    return utils._get_avg_wordlength(words)

def get_stopwords_counts(words):

    """
    StopWords Counts

    :param words:
    :return: StopWords Counts (Number)
    """

    return utils._get_stopwords_counts(words)

def get_hashtag_counts(words):

    """
    #HashTags Counts

    :param words:
    :return: HashTags Counts
    """

    return utils._get_hashtag_counts(words)

def get_mentions_counts(words):

    """

    @Mentions Counts

    :param words:
    :return: Mentions Counts
    """

    return utils._get_mentions_counts(words)

def get_digit_counts(words):

    """
    Digit Counts

    :param words:
    :return: Digit Counts
    """

    return utils._get_digit_counts(words)

def get_uppercase_counts(words):
    """
    UpperCase Counts

    :param words:
    :return: UpperCase Counts
    """
    return utils._get_uppercase_counts(words)

def get_lower_convert(words):

    """
    Lower Convert


    :param words:
    :return: Lower Convert
    """

    return utils._get_lower_convert(words)

def cont_exp(words):

    """
    Contraction to Expansion

    :param words:
    :return: Contraction to Expansion Words
    """

    return utils._cont_exp(words)

def get_emails(words):
    """
    Emails Counts ,
    Emails List

    :param words:
    :return: emails_length,emails_list
    """

    return utils._get_emails(words)

def get_urls(words):
    """
    Urls List;
    Urls Count


    :param words:
    :return: urls_length,urls_list
    """


    return utils._get_urls(words)

def get_remove_emails(words):

    """
    Remove Emails

    :param words:
    :return: Remove Emails Words
    """

    return utils._get_remove_emails(words)

def remove_urls(words):
    """
    Remove Urls

    :param words:
    :return: Remove Urls Words
    """

    return utils._remove_urls(words)

def remove_rt(words):
    """
    Words contains example ;
    rt @username: hello hirt

    :param words:
    :return: Words rt Counts (Number)
    """


    return utils._remove_rt(words)

def remove_special_chars(words):

    """
    Special Chars Removal or Punctuation Removal ;
    Remove Multiple Spaces

    :param words:
    :return: Words
    """

    return utils._remove_special_chars(words)

def remove_html_tags(words):
    """
    Remove HTML Tags and Strip

    :param words:
    :return: Words
    """


    return utils._remove_html_tags(words)

def remove_accented_chars(words):

    """
    Remove Accented Chars

    Example : 'Áccěntěd těxt' etc.

    :param words:
    :return: Words
    """

    return utils._remove_accented_chars(words)

def remove_stopwords(words):
    """
    Remove StopWords

    :param words:
    :return: Words
    """


    return utils._remove_stopwords(words)

def get_value_counts(dataframe,col_name,n=20,plot = False):

    """
    DataFrame ValueCounts

    :param dataframe: DataFrame Structure
    :param col_name: Select Name
    :param n: Numner
    :param plot: True or False

    :return: Frequence DataFrame
    """

    return utils._get_value_counts(dataframe,col_name,n,plot)

def remove_common_words(words,remove_words):

    """
    Before Using Review DataFrame ValueCounts
    Then Select What You Want to Extract and Send to Function (In List Structure!!)

    :param words:
    :param remove_words:
    :return: Words
    """

    return utils._remove_common_words(words,remove_words)

def remove_rare_words(words,remove_words):
    """
    Before Using Review DataFrame ValueCounts
    Then Select What You Want to Extract and Send to Function (In List Structure!!)

    :param words:
    :param remove_words:
    :return: Words
    """

    return utils._remove_rare_words(words,remove_words)

def get_make_base(words):
    """
    Convert Into Base or Root From of Word

    :param words:
    :return: Words
    """

    return utils._get_make_base(words)

def spelling_correction(words):

    """
    Spelling Correction

    :param words

    :return: Words
    """
    return utils._spelling_correction(words)