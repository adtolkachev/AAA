import pytest
from morse import decode


@pytest.mark.parametrize('s, exp', [
    ('.- ...- .. - --- -....- .- -.-. .- -.. . -- -.--', 'AVITO-ACADEMY'),
    ('.. - ...   -... .-. .. - -. . -.--   -... .. - -.-. ....', 'ITS BRITNEY BITCH'),
    ('-- --- ... -.-. --- .-- ..--- ----- ..--- ..---', 'MOSCOW2022')
])
def test_decode_regular(s, exp):
    assert decode(s) == exp
