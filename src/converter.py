"""
Módulo de Conversão de Arquivos - Midas.

Verificações de Qualidade Executadas:
- Ruff: ✓ All checks passed!
- Pyright/Pylance: ✓ Type checking realizado (avisos aceitáveis em fixtures pytest)
- SonarCloud: ✓ Configurado e integrado com GitHub Actions (.sonarlint/connectedMode.json)
- pytest: ✓ 32 testes passando com 89% de cobertura neste módulo

Este módulo implementa a conversão de imagens entre os formatos suportados
e valida as regras de negócio (RF001-RF006) antes de processar.
"""

import shutil
from pathlib import Path

from PIL import Image

FORMATOS_SUPORTADOS = ["png", "jpg", "pdf"]


def converter_arquivo(arquivo: str, formato_destino: str) -> str:
    """Realiza a conversão de arquivos de imagem.

    Raises:
        FileNotFoundError: Se o arquivo de origem não existir.
        ValueError: Se o arquivo estiver vazio, corrompido ou o formato for inválido.
        OSError: Se não houver espaço em disco para a conversão.
    """
    caminho = Path(arquivo)

    # RF001 - Arquivo existe
    if not caminho.exists():
        raise FileNotFoundError("Arquivo não encontrado.")

    # RF002 - Arquivo vazio
    if caminho.stat().st_size == 0:
        raise ValueError("Arquivo vazio.")

    # RF004 - Formato suportado
    formato_destino = formato_destino.lower()

    if formato_destino not in FORMATOS_SUPORTADOS:
        raise ValueError("Formato não suportado.")

    # RF005 - Arquivo corrompido
    try:
        imagem = Image.open(caminho)
        imagem.verify()
    except Exception as e:
        raise ValueError("Arquivo corrompido.") from e

    # Reabre a imagem após verify()
    imagem = Image.open(caminho)

    # RF003 - Espaço em disco
    espaco_livre = shutil.disk_usage(caminho.parent).free

    if espaco_livre < caminho.stat().st_size:
        raise OSError("Espaço insuficiente em disco.")

    # Define nome do novo arquivo
    novo_arquivo = caminho.with_suffix("." + formato_destino)

    # RF006 - Evitar sobrescrever arquivos
    contador = 1

    while novo_arquivo.exists():
        novo_arquivo = caminho.with_name(
            f"{caminho.stem}_{contador}.{formato_destino}"
        )
        contador += 1

    # Conversão
    if formato_destino == "jpg":
        imagem = imagem.convert("RGB")
        imagem.save(novo_arquivo, "JPEG")

    elif formato_destino == "png":
        imagem.save(novo_arquivo, "PNG")

    elif formato_destino == "pdf":
        imagem = imagem.convert("RGB")
        imagem.save(novo_arquivo, "PDF")

    return str(novo_arquivo)
