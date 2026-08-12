import pytest
from PIL import Image

from src.converter import converter_arquivo


def test_formato_invalido(tmp_path):
    arquivo = tmp_path / "teste.png"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo, "PNG")

    with pytest.raises(ValueError):
        converter_arquivo(str(arquivo), "exe")


def test_arquivo_inexistente():
    with pytest.raises(FileNotFoundError):
        converter_arquivo("arquivo_fake.png", "jpg")


def test_conversao_implementada(tmp_path):
    arquivo = tmp_path / "teste.png"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo, "PNG")

    resultado = converter_arquivo(str(arquivo), "jpg")

    arquivo_saida = tmp_path / "teste.jpg"

    assert resultado == str(arquivo_saida)
    assert arquivo_saida.exists()
