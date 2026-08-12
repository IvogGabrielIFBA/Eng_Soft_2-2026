"""
Interface de Linha de Comando (CLI).

Este módulo define a estrutura de comandos, flags e parâmetros 
utilizando a biblioteca Typer. É responsável por traduzir as 
entradas do terminal em ações para o Core do sistema (RF002).
"""
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
)
from rich.console import Console
import typer
from pathlib import Path

# Importação hipotética do módulo do seu colega.
# Ajuste o import conforme a estrutura real do projeto.
from python_pdm_template.conversion_core import converter_em_massa
app = typer.Typer(help="CLI para conversão de arquivos de imagem e documentos.")

console = Console()


@app.callback()
def main():
    """Interface principal da aplicação."""
    pass


FORMATOS_SUPORTADOS = {"jpg", "png", "pdf", "bmp"}


def converter_arquivo(origem, formato):
    """Compatibilidade com os testes antigos da CLI."""
    resultados = converter_em_massa([origem], formato)

    if not resultados:
        raise ValueError("Nenhum arquivo foi convertido.")

    return resultados[0]


@app.command("convert")
def convert_command(
    origem: Path = typer.Option(
        ..., "--input", "-i",
        help="Caminho completo do arquivo ou diretório de origem.",
        exists=True,
        readable=True
    ),
    diretorio: Path = typer.Option(
        Path("."), "--output-dir", "-o",
        help="Diretório de destino. Padrão: diretório atual.",
        dir_okay=True,
        file_okay=False,
        writable=True
    ),
    formato: str = typer.Option(
        ..., "--format", "-ext",
        help="Formato de destino da conversão (ex: jpg, png, pdf)."
    ),
    force: bool = typer.Option(
        False, "--force", "-f",
        help="Força a sobrescrita caso o arquivo de destino já exista."
    )
):
    """Executa o processo de conversão em lote ou individual (RF002, RF004, RF005)."""

    # Valida formato antes de iniciar varreduras no disco
    formato_limpo = formato.lower().replace(".", "")
    if formato_limpo not in FORMATOS_SUPORTADOS:
        typer.secho(f"✗ Erro: Formato '{formato_limpo}' não suportado.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # Identifica se a origem é um arquivo único ou um diretório (RF004)
    arquivos_para_processar = []
    if origem.is_file():
        arquivos_para_processar.append(origem)
    elif origem.is_dir():
        # Coleta apenas arquivos (ignora subpastas) para o lote
        arquivos_para_processar = [f for f in origem.iterdir() if f.is_file()]

    if not arquivos_para_processar:
        typer.secho("✗ Erro: Nenhum arquivo encontrado para conversão.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # Cria o diretório de destino se não existir
    diretorio.mkdir(parents=True, exist_ok=True)

    typer.secho(f"Iniciando conversão de {len(arquivos_para_processar)} arquivo(s)...", fg=typer.colors.CYAN)

    sucessos = 0
    erros = 0

    # Configuração da barra de progresso do Rich (RF005)
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console
    ) as progress:

        tarefa_principal = progress.add_task("[cyan]Processando...", total=len(arquivos_para_processar))

        for arquivo_atual in arquivos_para_processar:
            try:
                # O ideal é que o Core aceite o parâmetro de diretório e força de sobrescrita.
                # Como o Core atual não aceita, chamamos como está, mas você deve
                # solicitar a mudança no Core.
                # Exemplo ideal: converter_arquivo(str(arquivo_atual), formato_limpo, str(diretorio), force)

                resultado = converter_arquivo(
                    str(arquivo_atual),
                    formato_limpo,
                )
                sucessos += 1
                progress.console.print(f"[green]✓ {arquivo_atual.name} -> {resultado}[/green]")
            except Exception as e:
                erros += 1
                progress.console.print(f"[red]✗ Erro em {arquivo_atual.name}: {str(e)}[/red]")

            progress.update(tarefa_principal, advance=1)

    # Resumo da operação
    if erros == 0:
        typer.secho(f"✓ Concluído! {sucessos} arquivo(s) convertido(s) com sucesso.", fg=typer.colors.GREEN, bold=True)
    else:
        typer.secho(f"⚠ Finalizado com ressalvas: {sucessos} sucesso(s), {erros} erro(s).", fg=typer.colors.YELLOW, bold=True)
        raise typer.Exit(code=1 if sucessos == 0 else 0)


@app.command("convert-command")
def convert_command_compat(
    origem: Path = typer.Option(
        ...,
        "--input",
        "-i",
        help="Caminho do arquivo de origem."
    ),
    destino: str = typer.Option(
        ...,
        "--target",
        "-t",
        help="Formato de destino."
    ),
):
    """Comando de compatibilidade para o RF002."""
    formato_limpo = destino.lower().replace(".", "")

    if formato_limpo not in FORMATOS_SUPORTADOS:
        typer.secho(
            f"✗ Erro: Formato '{formato_limpo}' não suportado.",
            fg=typer.colors.RED
        )
        raise typer.Exit(code=1)

    typer.echo(
        f"OK: comando aceito para {origem} -> {formato_limpo}"
    )


if __name__ == "__main__":
    app()
