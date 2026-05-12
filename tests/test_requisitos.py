"""
Mapeamento Geral de Requisitos Funcionais (RF).

Este módulo atua como uma suíte de integração para validar a cobertura 
de todos os requisitos funcionais do projeto. Ele garante que cada 
funcionalidade planejada possua um ponto de verificação automatizado, 
servindo como guia para o progresso do desenvolvimento (Red State).
"""

from typer.testing import CliRunner

from python_pdm_template.cli_interface import app

runner = CliRunner()


def test_rf002_sistema_prove_comandos_via_terminal():
    """
    Testa o Requisito Funcional 002: Suporte a flags e parâmetros tipados.
    """

    # Executa o comando definido na sua interface CLI
    result = runner.invoke(app, ["convert-command", "--input", "arquivo.png", "--target", "pdf"])

    # Valida se a interface aceitou a estrutura das flags (Estado RED esperado)
    assert result.exit_code == 0


def test_rf002_sistema_obriga_parametros_entrada():
    """Valida se a tipagem e obrigatoriedade do RF002 estão funcionando."""

    # Tenta rodar sem a flag obrigatória --input
    result = runner.invoke(app, ["convert-command", "--target", "pdf"])

    # Deve retornar um erro de uso (exit_code diferente de 0), o que é o comportamento correto.
    assert result.exit_code != 0
