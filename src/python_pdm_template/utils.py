"""
Este módulo contém funções utilitárias para o projeto.

Funções:
- somar: Retorna a soma de dois números.
- obter_mensagem: Retorna uma mensagem fornecida pelo usuário.
"""


def somar(a: int | float, b: int | float):
    """
    Retorna a soma de dois números.

    :param a: Primeiro número.
    :param b: Segundo número.
    :return: A soma de a e b.
    """
    return a + b


def carregamento():
    pass



def arquivo_de_com_mesmo_nome():
    pass

def obter_mensagem():
    """Retorna uma mensagem de exemplo (modo não interativo).

    Alteração efetuada por IA: removi a dependência de entrada do usuário
    (antes fazia ``input(...)``) e passei a retornar um valor fixo para melhorar
    a execução automática e a testabilidade.

    :return: Uma mensagem fixa.
    """

    return "Mensagem fixa"

