# TODO

## GUI interface (Typer testável) + testes
- [ ] Atualizar `src/python_pdm_template/gui_interface.py` para exportar `app` com comandos testáveis via `typer.testing.CliRunner`.
- [ ] Corrigir bug `if name == "main":` para `if __name__ == "__main__":`.
- [ ] Implementar um comando (ex.: `convert-command`) com flags obrigatórias `--input/-i` e `--target/-t` e opcional `--force/-f`.
- [ ] Implementar validações/fluxo mock para simular RF003 (navegação) e RF005 (progresso/métricas) sem abrir PySide6.
- [ ] Atualizar `tests/test_gui.py` com testes usando `CliRunner`, espelhando os testes de `tests/test_cli.py`.
- [ ] Rodar `pytest` e garantir que `tests/test_gui.py` passe.

