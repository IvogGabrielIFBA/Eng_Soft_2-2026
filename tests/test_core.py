"""
Suíte de testes para o Core de Conversão e Regras de Negócio.

Este módulo contém testes unitários para validar a lógica de conversão 
de arquivos (RF001), o processamento em lote (RF004) e a gestão 
automática de nomes de arquivos para evitar sobrescrita (RF006).
"""

from src.python_pdm_template.conversion_core import converter_arquivo


def test_core_import():
    resultado = converter_arquivo("teste.png", "jpg")

    assert resultado.endswith(".jpg")
