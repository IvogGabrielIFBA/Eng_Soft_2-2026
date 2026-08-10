"""Módulo core do conversor Midas.

Contém a lógica central de processamento de arquivos, incluindo regras de
conversão entre formatos e gestão de conflitos de nomes no sistema de
arquivos (RF001 e RF006).
"""

from src.converter import converter_arquivo

__all__ = ["converter_arquivo"]
