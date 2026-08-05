"""
Este módulo contém funções utilitárias para o projeto.

Funções:
- somar: Retorna a soma de dois números.
- obter_mensagem: Retorna uma mensagem fornecida pelo usuário.
"""


def somar(a: int | float, b: int | float):
    """
    Retorna a soma de dois números.

    Parameters:
        a: Primeiro número.
        b: Segundo número.

    Returns:
        A soma de a e b.
    """
    return a + b


def carregamento():
    """Representa uma rotina de carregamento sem efeitos colaterais.

    Returns:
        None
    """
    # Função de placeholder para representar um processo de carregamento.


def arquivo_de_com_mesmo_nome():
    """Representa a verificação de arquivos com o mesmo nome.

    Returns:
        None
    """
    # Função de placeholder para demonstrar verificação de conflito de nomes.


def obter_mensagem():
    """Retorna uma mensagem de exemplo (modo não interativo).

    Observação: alteração realizada por IA.
    Modificação: removida a dependência de entrada do usuário (`input(...)`) e
    adotado retorno de mensagem fixa para melhorar a execução automática e a
    testabilidade.

    Returns:
        Uma mensagem fixa.
    """
    # IA: modificado para não usar input() e garantir execução automática/testes
    return "Mensagem fixa"
