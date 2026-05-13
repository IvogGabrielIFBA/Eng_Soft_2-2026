from pathlib import Path


FORMATOS_SUPORTADOS = ["png", "jpg", "pdf", "docx"]


def converter_arquivo(arquivo: str, formato_destino: str) -> str:
    """
    Realiza validações iniciais para conversão de arquivos.
    """

    caminho = Path(arquivo)

    if not caminho.exists():
        raise FileNotFoundError("Arquivo não encontrado.")

    if formato_destino.lower() not in FORMATOS_SUPORTADOS:
        raise ValueError("Formato não suportado.")

    raise NotImplementedError("Conversão ainda não implementada.")