import pytest
from hw4_2 import filter_unique

FIXTURE = [
    ({'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]},
     [98, 35, 15, 213, 54, 119])
]

@pytest.mark.parametrize("dict_, etalon", FIXTURE)
def test_hw42(dict_,etalon):
    result = filter_unique(dict_)
    assert result == etalon