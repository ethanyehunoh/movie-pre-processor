from argparse import ArgumentParser
import io
import text_parsing_functions as tpf
tpf.load_stopwords('data/stopwords.txt')


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
   
    """
    text_lc = tpf.lowercase_text(text)
    text_np = tpf.remove_punctuation(text_lc)
    text_nnl = tpf.remove_newline(text_np)
    words = tpf.split_text_into_words(text_nnl)
    words_nsw = tpf.remove_stopwords(words, stopwords_set)
    words_cleaned = tpf.replace_names(words_nsw, name_set, replace_val)
    line_of_text_cleaned = tpf.create_cleaned_textline_from_words(words_cleaned)
    return line_of_text_cleaned


def read_file_by_line(filepath, stopwords_set, name_set, replace_val):
    cleaned_lines = []
    with io.open(filepath, "r") as f:
        for line in f:
            cleaned_line = line_cleaning_pipeline(line, stopwords_set, name_set, replace_val)
            cleaned_lines.append(cleaned_line)
    return cleaned_lines

def write_to_file(cleaned_lines, output_filepath):
    with io.open(output_filepath, "w") as f:
        for line in cleaned_lines:
            f.write(line + '\n')

    












if __name__ == '__main__':
    # Load stopwords from file
    stopwords = tpf.load_stopwords('data/stopwords.txt')

    # Character names that should be replaced with 'person'
    replace = 'person'
    names = set(
        ['suan', 'seongkyeong', 'yonsuk', 'seokwoo',
         'ingil', 'yonghuk', 'jinhee', 'sanghwa', 'jongil', 'yongguk', 'jonggil']
    )

    parser = ArgumentParser()
    parser.add_argument("-i", "--input", type = str, required = True)
    parser.add_argument("-o", "--output", type = str, required = True)

    args = parser.parse_args()

    cleaned_lines = read_file_by_line(args.input, stopwords, names, replace)
    write_to_file(cleaned_lines, args.output)

    print("Successfully saved output to file")