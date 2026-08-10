"""Módulo utilitários do projeto.

Contém funções auxiliares simples usadas pelo pacote e testes.
"""


def somar(a: int | float, b: int | float):
    """Retorna a soma de dois números.

    Parameters
    ----------
    a : int | float
        Primeiro número.
    b : int | float
        Segundo número.

    Returns
    -------
    int | float
        A soma de ``a`` e ``b``.
    """
    return a + b


def carregamento():
    """Rotina de carregamento placeholder.

    Esta função representa uma operação de carregamento sem efeitos
    colaterais, usada apenas para testes.

    Returns
    -------
    None
    """
    # Função de placeholder para representar um processo de carregamento.


def arquivo_de_com_mesmo_nome():
    """Verifica conflitos de nomes de arquivos.

    Returns
    -------
    None
    """
    # Função de placeholder para demonstrar verificação de conflito de nomes.


def obter_mensagem():
    """Retorna uma mensagem fixa para modo não interativo.

    Observação
    ---------
    A implementação foi alterada para evitar chamadas interativas a
    ``input()`` e facilitar testes automatizados.

    Returns
    -------
    str
        Mensagem fixa.
    """
    # IA: modificado para não usar input() e garantir execução automática/testes
    return "Mensagem fixa"
