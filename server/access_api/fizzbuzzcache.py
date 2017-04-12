"""
    Methods used to store and retrieve permanently cached values
    for the 'computationally expensive'* fizzbuzz algorithm.
    *obviously not actually true or a good idea.
"""

from .connectionwrapper import ConnectionWrapper


class FizzbuzzCache:
    def __init__(self):
        self.cache = ConnectionWrapper().get_collection('fizzbuzz_cache')

    def get_fizzbuzz_value(self, number):
        fizzbuzz_entry = self.cache.find_one({"number": number})
        if fizzbuzz_entry and "fizzbuzz_result" in fizzbuzz_entry:
            return fizzbuzz_entry["fizzbuzz_result"]
        else:
            return False

    def cache_fizzbuzz_value(self, number, fizzbuzz_result):
        fizzbuzz_entry = {
            "number": number,
            "fizzbuzz_result": fizzbuzz_result
        }
        cache_id = self.cache.insert_one(fizzbuzz_entry)
        return cache_id
