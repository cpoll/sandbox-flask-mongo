from os import listdir
from os.path import isfile, join
import math
from scipy import spatial


def split_string_into_terms(string):
    return string.lower().split()

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

    IDF(t) = log_e( total docs / number of docs with term t )
"""
def calculate_idf(strings):
    doc_count = len(strings)

    term_counts = {}

    # Get how many files a term appears in
    for string in strings:
        terms = split_string_into_terms(string)
        unique_terms = set(terms)

        for term in unique_terms:
            if term in term_counts:
                term_counts[term] += 1
            else:
                term_counts[term] = 1

    #Create IDF dict
    # IDF(t) = log_e( total docs / number of docs with term t )
    idf_dict = {}
    for term in term_counts.keys():
        idf_dict[term] = math.log(doc_count / term_counts[term]) #TODO: Is this ln or log2?


    return idf_dict


"""
    Given a string and idf dict, returns a dictionary of word / tfidf
"""
def create_tfidf_dict(string, idf_dict):
    terms = split_string_into_terms(string)

    term_count = {}
    for term in terms:
        if term in term_count:
            term_count[term] += 1
        else:
            term_count[term] = 1

    tfidf_dict = {}
    for term in term_count.keys():
        tfidf_dict[term] = term_count[term] * idf_dict[term]

    return tfidf_dict

"""
    Given two TFIDF dictionaries, return the delta
"""
def get_tfidf_delta(one, two):

    all_words = list(one.keys()) + list(two.keys())

    a1 = []
    a2 = []
    #Create two ordered arrays of values, where a1[i] and a2[i] are the value of the same word
    for word in all_words:
        if word in one:
            a1.append(one[word])
        else:
            a1.append(0)

        if word in two:
            a2.append(two[word])
        else:
            a2.append(0)

    result = 1 - spatial.distance.cosine(a1, a2)
    return result


def get_key_with_value(dict, value):
    for key in dict:
        if dict[key] == value:
            return key

def search_for_files(search_term, idf_dict):
    # Compile results
    search_results = {}
    for file in file_tfidfs:
        value = get_tfidf_delta(search_term_tfidf, file_tfidfs[file])
        search_results[file] = value

    # Get the top 10 from the search results
    top_scores = list(reversed(sorted(list(search_results.values()))))
    top_results = {}
    for score in top_scores[:10]:
        name = get_key_with_value(search_results, score)
        top_results[name] = score

    print(top_results)

if __name__ == "__main__":
    file_contents = load_all_files("./review_polarity/txt_sentoken/min")

    #file_contents_pos = load_all_files("./review_polarity/txt_sentoken/pos")
    #file_contents_neg = load_all_files("./review_polarity/txt_sentoken/neg")
    #file_contents = {**file_contents_pos, **file_contents_neg}

    idf_dict = calculate_idf(file_contents.values())

    # Calculate tfidf for every file
    file_tfidfs = {}
    for file in file_contents:
        file_tfidfs[file] = create_tfidf_dict(file_contents[file], idf_dict)


    # Calculate tfidf for search term
    search_term = "tony flashback"
    search_term_tfidf = create_tfidf_dict(search_term, idf_dict)

    # Compile results
    search_results = {}
    for file in file_tfidfs:
        value = get_tfidf_delta(search_term_tfidf, file_tfidfs[file])
        search_results[file] = value

    # Get the top 10 from the search results
    top_scores = list(reversed(sorted(list(search_results.values()))))
    top_results = {}
    for score in top_scores[:10]:
        name = get_key_with_value(search_results, score)
        top_results[name] = score

    print(top_results)
    print("done")
