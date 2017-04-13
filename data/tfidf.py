from os import listdir
from os.path import isfile, join


"""
    Given a path, loads all text files into a dict with key filename and value contents.
"""
def load_all_files(path):

    file_dict = {}

    # Create a list of all txt files in the path
    text_files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".txt")]

    # Add file to dictionary
    for file in text_files:
        filepath = join(path, file)
        with open(filepath, 'r') as myfile:
            file_dict[file] = myfile.read().replace('\n', '')

    return file_dict




"""
    Given a list of strings, returns a dict of every term / their IDF
"""
def calculate_idf():
    pass


"""
    Given a dictionary of filename / value, returns a dictionary of filename / list of word - idf pairs
"""
def create_tfidf_dict():
    pass


if __name__ == "__main__":
    files = load_all_files("./review_polarity/txt_sentoken/pos")

    print("done")
