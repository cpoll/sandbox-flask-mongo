from .tfidf import calculate_idf, create_tfidf_dict


def test_calculate_idf():
    result = calculate_idf(["hello hello hello my darling"])

    #assert sorted(list(result.keys())) == sorted(["hello", "my", "darling"])
    assert list(result.values()).sort() == [3, 1, 1].sort() # TODO: sorting is a crappy test


def test_create_tfidf_dict():
    string = "hello hello hello my darling"
    idf_dict = {"hello" : 10, "my" : 1, "darling" : 5}

    result = create_tfidf_dict(string, idf_dict)

    #assert list(result.keys()).sort() == ["hello", "my", "darling"].sort()
    assert sorted(list(result.values())) == sorted([10 * 3, 1 * 1, 5 * 1])  # TODO: sorting is a crappy test
