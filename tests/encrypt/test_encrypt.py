from challenges.challenge_encrypt_message import encrypt_message
import pytest


mock = [
    ('Teste', 2, "ets_eT"),
    ('Teste', 3, "seT_et"),
    ('Teste', 9, "etseT"),
]


def test_encrypt_message():
    for m, k, r in mock:
        result = encrypt_message(m , k)
        assert r == result

    with pytest.raises(
        TypeError, match="tipo inválido para key"
    ):
        encrypt_message(2, 'dois')
