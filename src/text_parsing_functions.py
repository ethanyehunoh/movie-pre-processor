"""
Text parsing functions for cleaning movie description text.

This module contains functions to transform raw text into cleaned text
suitable for natural language processing tasks like clustering.
"""

from string import punctuation


def load_stopwords(filepath='data/stopwords.txt'):
    """
    Loads stopwords from a text file into a set.

    Stopwords are common words like 'the', 'a', 'and' that don't add
    much meaning to text analysis and are often removed.

    Parameters
    ----------
    filepath : str
        Path to the stopwords file (one word per line)

    Returns
    -------
    stopwords : set of str
        A set containing all stopwords (lowercase)

    Examples
    --------
    >>> stopwords = load_stopwords('data/stopwords.txt')
    >>> 'the' in stopwords
    True
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        # Read all lines, strip whitespace, and convert to set
        return set(line.strip().lower() for line in f if line.strip())


def lowercase_text(text):
    """
    Returns a text string with all characters lower-cased.

    Parameters
    ----------
    text: str

    Returns
    -------
    text_lowercased: str

    Examples
    --------
    >>> lowercase_text('AbC')
    'abc'
    """
    text_lowercased = text.lower()
    return text_lowercased


def remove_punctuation(text, punctuation=punctuation):
    """
    Returns a text string without punctuation.

    Hint: You can iterate through each character in the punctuation string
    and replace it with an empty string '', or use a different approach
    with string methods.

    Parameters
    ----------
    text: str
    punctuation: str
        A string containing all the punctuation characters to remove.

    Returns
    -------
    text_nopunct: str

    Examples
    --------
    >>> remove_punctuation("here's johnny!")
    'heres johnny'
    """
    # TODO: Your code here
    # Hint: Loop through each punctuation character and replace it
    for character in text:
        if character in punctuation:
            text = text.replace(character, "")
    return text

def remove_newline(text):
    """
    Removes all newlines in a line of text.

    Newlines are represented as '\n' in strings. You can use the
    .replace() method or .strip() method to handle them.

    Parameters
    ----------
    text: str

    Returns
    -------
    text_no_nl: str

    Examples
    --------
    >>> remove_newline("\nlife happens when youre busy\n making other plans\n")
    'life happens when youre busy making other plans'
    """
    # TODO: Your code here
    text = text.replace("\n", "").strip()
    return text


def split_text_into_words(text):
    """
    Splits a text string into a word list.

    This function breaks text into individual words. Python strings
    have a built-in method that does exactly this!

    Parameters
    ----------
    text: str

    Returns
    -------
    words: list of str

    Examples
    --------
    >>> split_text_into_words("get started by stop talking and begin doing")
    ['get', 'started', 'by', 'stop', 'talking', 'and', 'begin', 'doing']
    """
    # TODO: Your code here
    word_list = text.split()
    return word_list

def remove_stopwords(word_lst, stopwords_set):
    """
    Removes words from word_lst if they appear in the stopwords_set.

    Stopwords are common words that don't add meaning to analysis.
    This function filters them out.

    Parameters
    ----------
    word_lst: list of str
    stopwords_set: set of str

    Returns
    -------
    word_lst_no_sw: list of str

    Examples
    --------
    >>> remove_stopwords(['tell', 'me', 'and', 'i', 'forget'],
                         set(['and', 'i']))

    ['tell', 'me', 'forget']
    """
    # TODO: Your code here
    removed_stopwords_list = []
    for word in word_lst:
        if word not in stopwords_set:
            removed_stopwords_list.append(word)
    return removed_stopwords_list


def replace_names(word_lst, name_set, replacement_val):
    """
    Replaces names in word_lst with replacement_val.

    Names are identified by checking if they appear in the name_set.

    Parameters
    ----------
    word_lst: list of str
    name_set: set of str
    replacement_val: str
        The string to replace the names with.

    Returns
    -------
    word_lst_replaced_names: list of str

    Examples
    --------
    >>> replace_names(['daryl', 'larry','bob'],
                      set(['larry', 'daryl']),
                      'person')

    ['person', 'person','bob']
    """
    # TODO: Your code here
    # Hint: Use a list comprehension with a conditional
    # If word is in name_set, use replacement_val, otherwise use word
    no_names_list = []
    for word in word_lst:
        if word in name_set:
            no_names_list.append(replacement_val)
        else:
            no_names_list.append(word)
    return no_names_list
            

def create_cleaned_textline_from_words(words):
    """
    Makes a single string from a list of words.

    This function joins words back together into a single line of text.

    Parameters
    ----------
    words: list of str

    Returns
    -------
    cleaned_text: str

    Examples
    --------
    >>> create_cleaned_textline_from_words(
            ['darkest', 'moments', 'focus', 'light']
        )
    'darkest moments focus light'
    """
    # TODO: Your code here
    # Hint: Use the .join() method
    cleaned_text = " ".join(words)
    return cleaned_text


def line_cleaning_pipeline(text, stopwords_set, name_set, replace_val):
    """
    Transforms raw text into clean text using text-cleaning functions above.

    This function applies all the cleaning steps in sequence:
    1. Lowercase the text
    2. Remove punctuation
    3. Remove newlines
    4. Split into words
    5. Remove stopwords
    6. Replace names
    7. Join back into a single line

    Parameters
    ----------
    text: str
        The raw text to clean
    stopwords_set: set of str
        Set of common words to remove
    name_set: set of str
        Set of names to replace
    replace_val: str
        What to replace names with (e.g., 'person')

    Returns
    -------
    line_of_text_cleaned: str
        The cleaned text
    """
    text_lc = lowercase_text(text)
    text_np = remove_punctuation(text_lc)
    text_nnl = remove_newline(text_np)
    words = split_text_into_words(text_nnl)
    words_nsw = remove_stopwords(words, stopwords_set)
    words_cleaned = replace_names(words_nsw, name_set, replace_val)
    line_of_text_cleaned = create_cleaned_textline_from_words(words_cleaned)
    return line_of_text_cleaned


if __name__ == '__main__':
    # Load stopwords from file
    stopwords = load_stopwords('data/stopwords.txt')

    # Test strings to help you test your functions
    text_str1 = ("Seok-woo, a divorced fund manager, is a workaholic and "
                 "absentee father to \nhis")
    text_str2 = ("young daughter, Su-an. For her birthday the next day, "
                 "she wishes for her father\n")
    text_str3 = ("to take her to Busan to see her mother. \n"
                 "They board the KTX at Seoul Station.")

    # Example: Testing the lowercase function
    text = text_str1
    text_lc = lowercase_text(text)
    print(f"Original: {text}")
    print(f"Lowercased: {text_lc}.")

    # TODO: Add your own tests below as you implement each function
    # Example for testing remove_punctuation:
    # text_no_punct = remove_punctuation(text_lc)
    # print(f"No punctuation: {text_no_punct}")
