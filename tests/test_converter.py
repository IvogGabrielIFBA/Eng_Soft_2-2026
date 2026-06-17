import pytest

from src.converter import converter_arquivo


def test_formato_invalido():
    with pytest.raises(ValueError):
        converter_arquivo("teste.png", "exe")


def test_arquivo_inexistente():
    with pytest.raises(FileNotFoundError):
        converter_arquivo("arquivo_fake.png", "jpg")


def test_conversao_real():
    resultado = converter_arquivo("teste.png", "jpg")

    assert resultado.endswith(".jpg")
