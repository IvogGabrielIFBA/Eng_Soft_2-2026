"""
Interface de Linha de Comando (CLI).

Este módulo define a estrutura de comandos, flags e parâmetros 
utilizando a biblioteca Typer. É responsável por traduzir as 
entradas do terminal em ações para o Core do sistema (RF002).
"""

import typer

# Será utilizado futuramente.
# from typing import Optional


app = typer.Typer(help="CLI para conversão de arquivos de imagem e documentos.")

# Thiago


def execute_conversion_command(caminho_origem: str, formato_destino: str, sobrescrever: bool = False) -> bool:
    """
    Organiza a chamada da conversão validando os parâmetros recebidos pelo CLI.

    Args:
        caminho_origem (str): Caminho completo para o arquivo que será convertido.
        formato_destino (str): Extensão alvo (ex: 'pdf', 'jpg').
        sobrescrever (bool): Define se deve substituir arquivos já existentes.

    Returns:
        bool: Retorna True se o comando for processado com sucesso (Mock).
    """
    pass

# Thiago


@app.command()
def convert_command(
    origem: str = typer.Option(..., "--input", "-i", help="Caminho do arquivo de origem."),
    destino: str = typer.Option(..., "--target", "-t", help="Extensão de destino."),
    force: bool = typer.Option(False, "--force", "-f", help="Forçar a sobrescrita do arquivo.")
):
    """
    Interface de terminal para o processo de conversão (RF002).

    Recebe os inputs do usuário via flags e dispara a lógica de conversão.
    """
    # Aqui chamaremos a função disparar_comando_conversao no futuro.
    pass


if __name__ == "__main__":
    app()
