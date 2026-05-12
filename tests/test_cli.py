"""
Suíte de testes para a Interface de Linha de Comando (CLI).

Este módulo valida o processamento de argumentos, flags e a integração 
dos comandos do terminal com o motor de conversão, garantindo o 
cumprimento do requisito funcional RF002.
"""

from typer.testing import CliRunner

from python_pdm_template.cli_interface import app

runner = CliRunner()

# Thiago


def test_rf002_interface_aceita_flags_obrigatorias():
    """Verifica se o comando 'convert-command' aceita as flags --input e --target."""
    # Simula: python cli_interface.py convert-command --input teste.png --target pdf
    result = runner.invoke(app, ["convert-command", "--input", "teste.png", "--target", "pdf"])

    # Assert: exit_code 0 significa que o Typer aceitou os parâmetros sem erros
    assert result.exit_code == 0

# Thiago


def test_rf002_falha_se_faltar_parametro_obrigatorio():
    """Garante que o sistema reclame se o usuário não passar o arquivo de entrada."""
    # Tenta rodar sem o --input
    result = runner.invoke(app, ["convert-command", "--target", "pdf"])

    # Assert: exit_code diferente de 0 indica erro de uso (Correto para parâmetros obrigatórios)
    assert result.exit_code != 0
