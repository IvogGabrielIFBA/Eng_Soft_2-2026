"""
Módulo Core do Conversor Midas.

Este módulo contém a lógica central de processamento de arquivos, 
incluindo as regras de conversão entre formatos e a gestão de 
conflitos de nomes no sistema de arquivos (RF001 e RF006).
"""

from src.converter import converter_arquivo

__all__ = ["converter_arquivo"]
