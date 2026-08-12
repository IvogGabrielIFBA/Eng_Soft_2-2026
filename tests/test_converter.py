"""Testes para a conversão de imagens no módulo principal."""

import pytest
from pathlib import Path
from PIL import Image

from src.converter import converter_arquivo


def test_formato_invalido(tmp_path: Path) -> None:
    """Deve rejeitar um formato de destino inválido."""
    arquivo = tmp_path / "teste.png"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo, "PNG")

    with pytest.raises(ValueError):
        converter_arquivo(str(arquivo), "exe")


def test_arquivo_inexistente():
    """Deve levantar erro quando o arquivo de origem não existe."""
    with pytest.raises(FileNotFoundError):
        converter_arquivo("arquivo_fake.png", "jpg")


def test_conversao_implementada(tmp_path: Path) -> None:
    """Deve converter uma imagem válida para o formato solicitado."""
    arquivo = tmp_path / "teste.png"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo, "PNG")

    resultado = converter_arquivo(str(arquivo), "jpg")

    arquivo_saida = tmp_path / "teste.jpg"

    assert resultado == str(arquivo_saida)
    assert arquivo_saida.exists()
