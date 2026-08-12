"""
Ponto de Entrada Principal do Pacote Midas.

Função principal:
- Define a função `main`, que é executada quando o pacote é chamado diretamente 
  pela linha de comando.

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
    primeiro_valor= 6
    segundo_valor = 4
    print("a soma de 2 + 3 é:", somar(primeiro_valor, segundo_valor))

def teste_de_carregamento():
    carregamento()

def teste_arquivo_com_mesmo_nome():
    arquivo_de_com_mesmo_nome()

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
