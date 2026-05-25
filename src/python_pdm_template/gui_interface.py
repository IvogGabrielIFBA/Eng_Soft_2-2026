"""
Interface Gráfica de Usuário (GUI).

Este módulo implementa uma *interface testável* que espelha a abordagem do CLI:

- Em produção, a GUI real seria implementada com PySide6.
- Para fins de testes automatizados, expomos um comando Typer testável via
  `typer.testing.CliRunner`, sem abrir janela.

Requisitos simulados:
- RF003: navegação estilo SPA (validar `--page`).
- RF005: métricas/progresso (validar `--progress`).
"""

from __future__ import annotations

import typer

app = typer.Typer(help="Interface (GUI testável) para conversão de imagens/documentos.")


_VALID_PAGES = {"tela1"}


def execute_gui_command(
    caminho_origem: str,
    formato_destino: str,
    page: str = "tela1",
    progress: int = 0,
    sobrescrever: bool = False,
) -> bool:
    """Executa validações de fluxo para simular GUI (sem PySide6)."""

    # RF003: navegação estilo SPA
    if page not in _VALID_PAGES:
        raise typer.BadParameter("page inválida. Use uma página suportada.")

    # RF005: progresso/métricas
    if not (0 <= progress <= 100):
        raise typer.BadParameter("progress inválido. Deve estar entre 0 e 100.")

    # Mantém comportamento simples e determinístico para os testes.
    _ = (caminho_origem, formato_destino, sobrescrever)
    return True


@app.command()
def convert_command(
    origem: str = typer.Option(..., "--input", "-i", help="Caminho do arquivo de origem."),
    destino: str = typer.Option(..., "--target", "-t", help="Extensão de destino."),
    page: str = typer.Option("tela1", "--page", help="Página atual (SPA) para simulação."),
    progress: int = typer.Option(0, "--progress", help="Progresso (0-100) para simulação."),
    force: bool = typer.Option(False, "--force", "-f", help="Forçar sobrescrita."),
):
    """Command testável que simula a lógica de GUI."""

    execute_gui_command(
        caminho_origem=origem,
        formato_destino=destino,
        page=page,
        progress=progress,
        sobrescrever=force,
    )

    # Saída fixa para tornar o comportamento verificável se necessário.
    typer.echo(f"OK page={page} progress={progress}")


if __name__ == "__main__":
    app()

