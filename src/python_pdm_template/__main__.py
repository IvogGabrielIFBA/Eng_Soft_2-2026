"""Ponto de entrada do pacote `python_pdm_template`.

Este módulo define a função `main` usada para executar o pacote como
um script e fornece pequenas rotinas auxiliares usadas pelos testes.

Como usar
--------
1. Certifique-se de que o projeto está configurado corretamente com o PDM.
2. Instale o pacote no ambiente virtual::

    python -m pdm install

3. Execute o pacote diretamente::

    python -m pdm run python src/NOME_DO_PROJETO/__main__.py
"""

from python_pdm_template.utils import arquivo_de_com_mesmo_nome, carregamento, somar


def main():
    """Função principal que exibe uma mensagem de boas-vindas."""
    print()
    primeiro_valor = 6
    segundo_valor = 4
    print("a soma de 2 + 3 é:", somar(primeiro_valor, segundo_valor))


def teste_de_carregamento():
    """Executa a rotina de carregamento usada pelos testes."""
    carregamento()


def teste_arquivo_com_mesmo_nome():
    """Executa a rotina de verificação de arquivos homônimos."""
    arquivo_de_com_mesmo_nome()


# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
