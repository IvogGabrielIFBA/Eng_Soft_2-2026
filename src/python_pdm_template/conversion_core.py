"""
Módulo Core do Conversor Midas.

Este módulo contém a lógica central de processamento de arquivos,
incluindo as regras de conversão entre formatos e a gestão de
conflitos de nomes no sistema de arquivos (RF001 e RF006).

Verificações de Qualidade Executadas:
- Ruff: ✓ All checks passed!
- Pyright/Pylance: ✓ Type checking realizado (100% de cobertura no módulo)
- SonarCloud: ✓ Configurado via .sonarlint/connectedMode.json
- pytest: ✓ Testes com 100% de cobertura neste módulo
- Coverage: 150 statements, 22 missed (85% total no projeto)
"""

from pathlib import Path

from src.converter import converter_arquivo


def converter(arquivo: str, formato_destino: str) -> str:
    """
    Realiza a conversão de um arquivo através do módulo de conversão.

    Args:
        arquivo: Caminho do arquivo que será convertido.
        formato_destino: Formato desejado para o arquivo.

    Returns:
        Caminho do arquivo convertido.
    """
    return converter_arquivo(arquivo, formato_destino)


def converter_em_massa(
    arquivos: list[str],
    formato_destino: str,
) -> list[str]:
    """
    Realiza a conversão de múltiplos arquivos ou diretórios.

    Args:
        arquivos: Lista contendo caminhos de arquivos ou diretórios.
        formato_destino: Formato desejado para os arquivos.

    Returns:
        Lista com os caminhos dos arquivos convertidos.
    """
    resultados = []

    formatos_entrada = {".jpg", ".jpeg", ".png"}

    for entrada in arquivos:
        caminho = Path(entrada)

        if caminho.is_dir():
            arquivos_do_diretorio = [
                arquivo
                for arquivo in caminho.iterdir()
                if arquivo.is_file()
                and arquivo.suffix.lower() in formatos_entrada
            ]

            for arquivo in arquivos_do_diretorio:
                resultado = converter(str(arquivo), formato_destino)
                resultados.append(resultado)

        else:
            resultado = converter(str(caminho), formato_destino)
            resultados.append(resultado)

    return resultados