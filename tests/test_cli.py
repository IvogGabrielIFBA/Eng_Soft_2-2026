"""
Suíte de testes para a Interface de Linha de Comando (CLI).

Este módulo valida o processamento de argumentos, flags e a integração 
dos comandos do terminal com o motor de conversão, garantindo o 
cumprimento do requisito funcional RF002.
"""

import sys
from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from python_pdm_template.cli_interface import app

# Ajuste do path para execução isolada do pytest
_src_path = str(Path(__file__).parent.parent / "src")
if _src_path not in sys.path:
    sys.path.insert(0, _src_path)


runner = CliRunner()


def test_rf002_interface_aceita_novas_flags_separadas():
    """Valida o comportamento da CLI sob parâmetros nominais corretos."""
    with patch("os.path.exists", return_value=True):
        result = runner.invoke(app, [
            "--input", "teste.png",
            "--output-dir", "resultado_pasta",
            "--format", "jpg"
        ])

    print("\n--- SAÍDA DO TERMINAL ---")
    print(result.output)
    print("-------------------------\n")

    assert result.exit_code == 0
    assert "Processando" in result.output


def test_rf002_falha_se_faltar_parametro_obrigatorio():
    """Verifica se a CLI bloqueia a execução na ausência de opções obrigatórias."""
    result = runner.invoke(app, [
        "--input", "teste.png"
    ])
    assert result.exit_code != 0


def test_rf002_falha_quando_arquivo_origem_nao_existe():
    """Verifica se a CLI encerra com erro quando o arquivo de entrada não é localizado."""
    with patch("os.path.exists", return_value=False):
        result = runner.invoke(app, [
            "--input", "arquivo_fantasma.png",
            "--output-dir", "resultado_pasta",
            "--format", "jpg"
        ])

    assert result.exit_code != 0
    assert "Erro: O arquivo de origem não foi encontrado" in result.output


def test_rf002_falha_quando_formato_destino_nao_suportado():
    """Garante a rejeição de formatos de destino fora do escopo homologado."""
    with patch("os.path.exists", return_value=True):
        result = runner.invoke(app, [
            "--input", "teste.png",
            "--output-dir", "resultado_pasta",
            "--format", "mp3"
        ])

    assert result.exit_code != 0
    assert "Erro: Formato de destino 'mp3' não é suportado" in result.output


def test_rf002_falha_quando_arquivo_origem_tem_extensao_invalida():
    """Garante a rejeição de extensões de entrada não suportadas pelo sistema."""
    with patch("os.path.exists", return_value=True):
        result = runner.invoke(app, [
            "--input", "documento.txt",
            "--output-dir", "resultado_pasta",
            "--format", "jpg"
        ])

    assert result.exit_code != 0
    assert "Erro: Extensão do arquivo de origem '.txt' não é suportada" in result.output


def test_rf002_falha_quando_diretorio_destino_nao_existe():
    """Verifica se o sistema impede a operação caso o diretório alvo seja inválido."""
    def os_exists_mock(path: str) -> bool:
        return path != "pasta_fantasma"

    with patch("os.path.exists", side_effect=os_exists_mock):
        result = runner.invoke(app, [
            "--input", "teste.png",
            "--output-dir", "pasta_fantasma",
            "--format", "jpg"
        ])

    assert result.exit_code != 0
    assert "Erro: O diretório de destino não foi encontrado" in result.output
