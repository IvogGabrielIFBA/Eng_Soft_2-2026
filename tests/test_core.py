"""
Suíte de testes para o Core de Conversão e Regras de Negócio.

Este módulo contém testes unitários para validar a lógica de conversão
de arquivos (RF001), o processamento em lote (RF004) e a gestão
automática de nomes de arquivos para evitar sobrescrita (RF006).
"""

from pathlib import Path

from PIL import Image

from python_pdm_template.conversion_core import converter, converter_em_massa


def test_converter_deve_converter_imagem_para_png(tmp_path: Path) -> None:
    arquivo_entrada = tmp_path / "imagem.jpg"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo_entrada, "JPEG")

    resultado = converter(str(arquivo_entrada), "png")

    arquivo_saida = Path(resultado)

    assert arquivo_saida.exists()
    assert arquivo_saida.suffix == ".png"


def test_converter_deve_rejeitar_arquivo_inexistente():
    arquivo_inexistente = "arquivo_que_nao_existe.jpg"

    try:
        converter(arquivo_inexistente, "png")
        assert False, "Era esperado FileNotFoundError."
    except FileNotFoundError as erro:
        assert str(erro) == "Arquivo não encontrado."

def test_converter_deve_evitar_sobrescrever_arquivo_existente(tmp_path: Path) -> None:
    arquivo_entrada = tmp_path / "imagem.jpg"
    arquivo_existente = tmp_path / "imagem.png"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo_entrada, "JPEG")

    # Cria previamente um arquivo com o nome que seria utilizado.
    imagem.save(arquivo_existente, "PNG")

    resultado = converter(str(arquivo_entrada), "png")

    arquivo_saida = Path(resultado)

    assert arquivo_saida.exists()
    assert arquivo_saida.name == "imagem_1.png"
    assert arquivo_existente.exists()


def test_converter_deve_rejeitar_arquivo_vazio(tmp_path: Path) -> None:
    arquivo_vazio = tmp_path / "vazio.jpg"
    arquivo_vazio.touch()

    try:
        converter(str(arquivo_vazio), "png")
        assert False, "Era esperado ValueError."
    except ValueError as erro:
        assert str(erro) == "Arquivo vazio."


def test_converter_deve_rejeitar_formato_nao_suportado(tmp_path: Path) -> None:
    arquivo_entrada = tmp_path / "imagem.jpg"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo_entrada, "JPEG")

    try:
        converter(str(arquivo_entrada), "gif")
        assert False, "Era esperado ValueError."
    except ValueError as erro:
        assert str(erro) == "Formato não suportado."


def test_converter_deve_rejeitar_arquivo_corrompido(tmp_path: Path) -> None:
    arquivo_corrompido = tmp_path / "corrompido.jpg"

    arquivo_corrompido.write_text("Este arquivo não é uma imagem válida.")

    try:
        converter(str(arquivo_corrompido), "png")
        assert False, "Era esperado ValueError."
    except ValueError as erro:
        assert str(erro) == "Arquivo corrompido."


def test_converter_em_massa_deve_converter_multiplos_arquivos(tmp_path: Path) -> None:
    arquivo_1 = tmp_path / "imagem1.jpg"
    arquivo_2 = tmp_path / "imagem2.jpg"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo_1, "JPEG")
    imagem.save(arquivo_2, "JPEG")

    resultados = converter_em_massa(
        [str(arquivo_1), str(arquivo_2)],
        "png",
    )

    assert len(resultados) == 2
    assert Path(resultados[0]).exists()
    assert Path(resultados[1]).exists()
    assert Path(resultados[0]).suffix == ".png"
    assert Path(resultados[1]).suffix == ".png"


def test_converter_em_massa_deve_converter_arquivos_de_um_diretorio(tmp_path: Path) -> None:
    diretorio = tmp_path / "imagens"
    diretorio.mkdir()

    arquivo_1 = diretorio / "imagem1.jpg"
    arquivo_2 = diretorio / "imagem2.jpg"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo_1, "JPEG")
    imagem.save(arquivo_2, "JPEG")

    resultados = converter_em_massa(
        [str(diretorio)],
        "png",
    )

    assert len(resultados) == 2
    assert all(Path(resultado).exists() for resultado in resultados)
    assert all(Path(resultado).suffix == ".png" for resultado in resultados)


def test_converter_em_massa_deve_ignorar_arquivos_nao_suportados(tmp_path: Path) -> None:
    diretorio = tmp_path / "imagens"
    diretorio.mkdir()

    arquivo_1 = diretorio / "imagem.jpg"
    arquivo_2 = diretorio / "documento.txt"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo_1, "JPEG")

    arquivo_2.write_text("Este não é um arquivo de imagem.")

    resultados = converter_em_massa(
        [str(diretorio)],
        "png",
    )

    assert len(resultados) == 1
    assert Path(resultados[0]).exists()
    assert Path(resultados[0]).name == "imagem.png"

def test_converter_em_massa_deve_aceitar_arquivos_e_diretorio(
    tmp_path: Path,
) -> None:
    diretorio = tmp_path / "imagens"
    diretorio.mkdir()

    arquivo_1 = tmp_path / "imagem1.jpg"
    arquivo_2 = diretorio / "imagem2.jpg"
    arquivo_3 = diretorio / "imagem3.jpg"

    imagem = Image.new("RGB", (100, 100), "red")

    imagem.save(arquivo_1, "JPEG")
    imagem.save(arquivo_2, "JPEG")
    imagem.save(arquivo_3, "JPEG")

    resultados = converter_em_massa(
        [str(arquivo_1), str(diretorio)],
        "png",
    )

    assert len(resultados) == 3

    for resultado in resultados:
        assert Path(resultado).exists()
        assert Path(resultado).suffix == ".png"


def test_converter_em_massa_deve_rejeitar_arquivo_corrompido(tmp_path: Path) -> None:
    arquivo_valido = tmp_path / "imagem.jpg"
    arquivo_corrompido = tmp_path / "corrompida.jpg"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo_valido, "JPEG")

    arquivo_corrompido.write_text("arquivo inválido")

    try:
        converter_em_massa(
            [str(arquivo_valido), str(arquivo_corrompido)],
            "png",
        )
        assert False, "Era esperado ValueError."
    except ValueError as erro:
        assert str(erro) == "Arquivo corrompido."


def test_converter_em_massa_deve_retornar_lista_de_resultados(tmp_path: Path) -> None:
    arquivo_1 = tmp_path / "imagem1.jpg"
    arquivo_2 = tmp_path / "imagem2.jpg"

    imagem = Image.new("RGB", (100, 100), "red")
    imagem.save(arquivo_1, "JPEG")
    imagem.save(arquivo_2, "JPEG")

    resultados = converter_em_massa(
        [str(arquivo_1), str(arquivo_2)],
        "png",
    )

    assert isinstance(resultados, list)
    assert len(resultados) == 2
