"""
Este arquivo é o ponto de entrada principal do pacote `python_pdm_template`.

Função principal:
- Define a função `main`, que é executada quando o pacote é chamado diretamente 
  pela linha de comando.

Como construir e usar:
1. Certifique-se de que o projeto está configurado corretamente com o PDM.
2. Instale seu pacote no ambiente virtual usando:
   ```bash
    python -m pdm install
   ```
3. Execute o comando abaixo para rodar o pacote diretamente:
   ```bash
   python -m pdm run python src/NOME_DO_PROJETO/__main__.py
   ```
"""

from python_pdm_template.utils import somar
from python_pdm_template.utils import carregamento

def main():
    """Função principal que exibe uma mensagem de boas-vindas."""

    print()
    primeiro_valor= 6
    segundo_valor = 4
    print("a soma de 2 + 3 é:", somar(primeiro_valor, segundo_valor))

def test():
    carregamento()


# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
