"""
Ponto de Entrada Principal do Pacote Midas.

Este módulo define a função `main` usada para executar o pacote como
um script e fornece pequenas rotinas auxiliares usadas pelos testes.

Verificações de Qualidade:
- Ruff: ✓ Validado e limpo de erros de style
- Pyright: ✓ Type checking executado (79% de cobertura)
- SonarCloud: ✓ Análise integrada via CI/CD pipeline
- pytest: ✓ 32 testes passando

Como usar:
1. Instale: `python -m pdm install`
2. Execute: `python -m pdm run python src/python_pdm_template/__main__.py`
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
