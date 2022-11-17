import pytest
from hw4_3 import word_count

FIXTURE = [
    ([
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ], {3: 4, 2: 3}
     )
]

@pytest.mark.parametrize("list_, etalon", FIXTURE)
def test_hw43(list_,etalon):
    result = word_count(list_)
    assert result == etalon