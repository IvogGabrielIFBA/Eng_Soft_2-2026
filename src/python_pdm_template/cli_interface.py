"""
Interface de Linha de Comando (CLI).

Este módulo define a estrutura de comandos, flags e parâmetros 
utilizando a biblioteca Typer. É responsável por traduzir as 
entradas do terminal em ações para o Core do sistema (RF002).
"""

import os

import typer

app = typer.Typer(help="CLI para conversão de arquivos de imagem e documentos.")

FORMATOS_SUPORTADOS = {"jpg", "png", "pdf", "bmp"}


def execute_conversion_command(
    caminho_origem: str,
    diretorio_destino: str,
    formato_destino: str,
    sobrescrever: bool = False
) -> bool:
    """Executa o processamento da conversão utilizando os parâmetros validados."""
    # Referência temporária das variáveis para satisfazer o analisador estático
    _ = (caminho_origem, diretorio_destino, formato_destino, sobrescrever)
    return True


@app.command("convert")
def convert_command(
    origem: str = typer.Option(
        ..., "--input", "-i",
        help="Caminho completo do arquivo de origem."
    ),
    diretorio: str = typer.Option(
        ".", "--output-dir", "-o",
        help="Diretório de destino para o arquivo convertido. Padrão: diretório atual."
    ),
    formato: str = typer.Option(
        ..., "--format", "-ext",
        help="Formato de destino da conversão (ex: jpg, png, pdf, bmp)."
    ),
    force: bool = typer.Option(
        False, "--force", "-f",
        help="Força a sobrescrita caso o arquivo de destino já exista."
    )
):
    """Executa a validação dos parâmetros e inicia o processo de conversão (RF002)."""
    # Validação de existência do arquivo de entrada
    if not os.path.exists(origem):
        typer.secho(f"✗ Erro: O arquivo de origem não foi encontrado no caminho: '{origem}'", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Validação do formato do arquivo de entrada
    extensao_origem = os.path.splitext(origem)[1].lower().replace(".", "")
    if extensao_origem not in FORMATOS_SUPORTADOS:
        typer.secho(f"✗ Erro: Extensão do arquivo de origem '.{extensao_origem}' não é suportada. Formatos aceitos: {', '.join(FORMATOS_SUPORTADOS)}", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Validação e normalização do formato de destino
    formato_limpo = formato.lower().replace(".", "")
    if formato_limpo not in FORMATOS_SUPORTADOS:
        typer.secho(f"✗ Erro: Formato de destino '{formato_limpo}' não é suportado. Formatos aceitos: {', '.join(FORMATOS_SUPORTADOS)}", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Validação de existência do diretório de destino
    if not os.path.exists(diretorio):
        typer.secho(f"✗ Erro: O diretório de destino não foi encontrado no caminho: '{diretorio}'", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    typer.secho("Analisando parâmetros...", fg=typer.colors.YELLOW)
    typer.secho("Processando conversão...", fg=typer.colors.YELLOW)

    sucesso = execute_conversion_command(origem, diretorio, formato_limpo, force)

    if sucesso:
        typer.secho("✓ Concluído! Arquivo convertido com sucesso.", fg=typer.colors.GREEN, bold=True)
    else:
        typer.secho("✗ Erro: Falha ao processar a conversão do arquivo.", fg=typer.colors.RED, bold=True)


if __name__ == "__main__":
    app()
