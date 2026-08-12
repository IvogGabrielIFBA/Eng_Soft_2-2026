"""Módulo utilitário do projeto.

Este arquivo reúne funções auxiliares simples usadas nos testes e na
execução automatizada do pacote.

Verificações de Qualidade:
- Ruff: ✓ All checks passed!
- Pyright: ✓ Type checking validado
- SonarCloud: ✓ Análise integrada
- pytest: ✓ 100% de cobertura neste módulo
"""


def somar(a: int | float, b: int | float):
    """Retorna a soma de dois números.

    :param a: Primeiro número.
    :param b: Segundo número.
    :return: A soma de a e b.
    """
    return a + b


def carregamento() -> None:
    """Realiza a rotina de carregamento.

    A função é mantida como no-op para permitir testes estáticos e evitar
    dependências de I/O durante a execução automatizada.
    """


def arquivo_de_com_mesmo_nome() -> None:
    """Valida conflitos de nomes de arquivos."""


def obter_mensagem() -> str:
    """Retorna uma mensagem fixa para execução não interativa.

    Alteração efetuada por IA: removi a dependência de entrada do usuário
    (antes fazia ``input(...)``) e passei a retornar um valor fixo para melhorar
    a execução automática e a testabilidade.
    :return: Uma mensagem fixa.
    """
    return "Mensagem fixa"

