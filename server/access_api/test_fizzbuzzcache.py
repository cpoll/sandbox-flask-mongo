from .fizzbuzzcache import FizzbuzzCache


class FizzbuzzCacheMock:
    def insert_one(self, value):  # TODO: Verify this was called
        return True


class DbMock:
    fizzbuzz_cache = FizzbuzzCacheMock()


class ConnectionWrapperMock:
    db = DbMock()



def test_fizzbuzzcache_caches_result():
    # Given a fizzbuzz value that should be cached
    cache = FizzbuzzCache(ConnectionWrapperMock())

    # When we call cache
    result = cache.cache_fizzbuzz_value(1, [1])

    # Then the value is cached and the method returns true
    assert result
