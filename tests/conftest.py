"""
Arquivo de configuracao do pytest para o pacote de testes.

Este arquivo pode ser usado para:
- Definir fixtures globais para os testes.
- Configurar hooks do pytest.
- Adicionar opcoes de linha de comando personalizadas.
- Realizar configuracoes iniciais antes da execucao dos testes.

Para mais informacoes, consulte a documentacao do pytest:
https://docs.pytest.org/
"""

from pathlib import Path
import sys

import pytest


# Garante que o pacote em `src/` possa ser importado pelos testes.
SRC_PATH = Path(__file__).resolve().parents[1] / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


@pytest.fixture
def exemplo_fixture():
    """Uma fixture de exemplo que pode ser usada em testes."""
    return "dados de exemplo"
