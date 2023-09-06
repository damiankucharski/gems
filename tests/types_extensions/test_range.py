from gems.types_extensions.range import Range

import numpy as np


# define test suit class for test cases below and import required modules
class TestRange:
    def test_single_number(self):
        r = Range(2, 5)
        assert 3 in r
        assert 1 not in r
        assert 5 not in r

    def test_list(self):
        r = Range(2, 5)
        result = r.__contains__([1, 2, 3, 5])
        assert result == [False, True, True, False]

    def test_numpy_array(self):
        r = Range(2, 5)
        arr = np.array([1, 2, 3, 5])
        result = r.__contains__(arr)
        assert np.array_equal(result, np.array([False, True, True, False]))
