from .fizzbuzzcache import FizzbuzzCache
from.connectionwrapper import ConnectionWrapper


class FizzbuzzCollectionMock:
    def insert_one(self, value):  # TODO: Verify this was called
        return True


def test_fizzbuzzcache_caches_result(monkeypatch):
    # Given a fizzbuzz value that should be cached
    monkeypatch.setattr(ConnectionWrapper, '__init__', lambda self: None)
    monkeypatch.setattr(ConnectionWrapper, 'get_collection', lambda self, collection: FizzbuzzCollectionMock())
    cache = FizzbuzzCache()

    # When we call cache
    result = cache.cache_fizzbuzz_value(1, [1])

    # Then the value is cached and the method returns true
    assert result
