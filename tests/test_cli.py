"""
Suíte de testes para a Interface de Linha de Comando (CLI).

Este módulo valida o processamento de argumentos, flags e a integração 
dos comandos do terminal com o motor de conversão, garantindo o 
cumprimento do requisito funcional RF002.
"""

"""
Suíte de testes para a Interface de Linha de Comando (CLI).
Valida RF002, RF004 e RF005.
"""

from unittest.mock import patch

from typer.testing import CliRunner
import pytest

from python_pdm_template.cli_interface import app

runner = CliRunner()

# Fixtures para criar cenários de teste reais no disco
@pytest.fixture
def mock_arquivo(tmp_path):
    """Cria um arquivo de imagem fictício para testes."""
    arquivo = tmp_path / "teste.png"
    arquivo.write_text("conteudo falso")
    return arquivo

@pytest.fixture
def mock_pasta(tmp_path):
    """Cria uma pasta com múltiplos arquivos para teste de lote."""
    pasta = tmp_path / "lote"
    pasta.mkdir()
    (pasta / "1.png").write_text("falso 1")
    (pasta / "2.png").write_text("falso 2")
    return pasta

def test_rf002_interface_falha_sem_parametros_obrigatorios():
    """Garante que a CLI rejeite execução sem os parâmetros mínimos."""
    result = runner.invoke(app, ["convert", "--input", "teste.png"])
    assert result.exit_code != 0
    assert "Missing option" in result.output

def test_rf002_interface_rejeita_formato_invalido(mock_arquivo):
    """Garante que formatos fora de FORMATOS_SUPORTADOS sejam barrados."""
    result = runner.invoke(app, [
        "convert", 
        "--input", str(mock_arquivo), 
        "--format", "mp3"
    ])
    assert result.exit_code != 0
    assert "não suportado" in result.output.lower()

@patch("python_pdm_template.cli_interface.converter_arquivo")
def test_rf002_interface_sucesso_arquivo_unico(mock_converter, mock_arquivo):
    """Valida o fluxo nominal com um único arquivo, mockando o Core."""
    mock_converter.return_value = "resultado.jpg"
    
    result = runner.invoke(app, [
        "convert",
        "--input", str(mock_arquivo),
        "--format", "jpg"
    ])
    
    assert result.exit_code == 0
    assert "1 arquivo(s) convertido(s) com sucesso" in result.output
    # Garante que o Core foi chamado corretamente
    mock_converter.assert_called_once_with(str(mock_arquivo), "jpg")

@patch("python_pdm_template.cli_interface.converter_arquivo")
def test_rf004_interface_conversao_em_lote(mock_converter, mock_pasta):
    """Verifica se o CLI processa diretórios inteiros (RF004)."""
    mock_converter.return_value = "resultado.jpg"
    expected_calls = 2

    result = runner.invoke(app, [
        "convert",
        "--input", str(mock_pasta),
        "--format", "jpg"
    ])

    assert result.exit_code == 0
    assert "2 arquivo(s) convertido(s)" in result.output
    assert mock_converter.call_count == expected_calls
