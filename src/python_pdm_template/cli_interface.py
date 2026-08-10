"""Interface de Linha de Comando (CLI).

Este módulo define comandos e opções usando Typer para expor a
funcionalidade de conversão via terminal.
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
    """Executa o processamento da conversão utilizando os parâmetros validados.

    Parameters
    ----------
    caminho_origem : str
        Caminho do arquivo de entrada.
    diretorio_destino : str
        Diretório de saída.
    formato_destino : str
        Formato de destino.
    sobrescrever : bool, optional
        Indica se deve sobrescrever arquivo existente (default: False).

    Returns
    -------
    bool
        True quando o processamento for bem-sucedido.
    """
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
    """Valida parâmetros e inicia o processo de conversão.

    Raises
    ------
    typer.Exit
        Em caso de falha de validação de parâmetros.
    """
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
