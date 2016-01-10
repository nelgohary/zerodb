import itertools
import pytest

from zerodb.util.iter import Sliceable


def test_sliceable():
    it = Sliceable(lambda: itertools.imap(str, itertools.count()))
    assert it[500] == "500"
    assert it[505] == "505"
    it1 = it.iterator
    it.cache.clear()
    assert it[0] == "0"
    assert it[2] == "2"
    assert it1 is not it.iterator

    assert it[10:15:3] == map(str, range(10, 15, 3))
    assert it[101:200:5] == map(str, range(101, 200, 5))
    assert it[20:25:3] == map(str, range(20, 25, 3))

    assert it[5:100] == map(str, range(5, 100))
    it1 = it.iterator
    assert it[10:20] == map(str, range(10, 20))
    assert it.iterator is it1

    with pytest.raises(KeyError):
        it[-1]
    with pytest.raises(KeyError):
        it["raise"]

    it = Sliceable(lambda: xrange(10))

    assert len([i for i in it]) == 10
    assert len(it) == 10
