import pytest
from morse import decode


@pytest.mark.parametrize('s, exp', [
    ('.- ...- .. - --- -....- .- -.-. .- -.. . -- -.--', 'AVITO-ACADEMY'),
    ('.. - ...   -... .-. .. - -. . -.--   -... .. - -.-. ....', 'ITSBRITNEYBITCH'),
    ('-- --- ... -.-. --- .-- ..--- ----- ..--- ..---', 'MOSCOW2022')
])
def test_decode_regular(s, exp):
    assert decode(s) == exp
