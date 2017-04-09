"""
    Methods used to store and retrieve permanently cached values
    for the 'computationally expensive'* fizzbuzz algorithm.
    *obviously not actually true or a good idea.
"""

from pymongo import MongoClient


class FizzbuzzCache:
    def __init__(self):
        mongo_client = MongoClient('mongodb://localhost:27017/')
        db = mongo_client.test_database
        self.cache = db.fizzbuzz_cache

    def get_fizzbuzz_value(self, number):
        fizzbuzz_entry = self.cache.find_one({"number": number})
        if fizzbuzz_entry and fizzbuzz_entry["fizzbuzz_result"]:
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
