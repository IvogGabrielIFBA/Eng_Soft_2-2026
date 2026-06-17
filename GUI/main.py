import sys
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "logo-midas.png"

GOLD = "#c58b10"
BLACK = "#000000"
WHITE = "#ffffff"
DARK_BUTTON = "#1f1f1f"
PANEL_BG = "#080808"

MENU_CONTENT = {
    "Recursos": {
        "title": "Recursos",
        "body": (
            "Conversao rapida para arquivos do dia a dia.\n\n"
            "- Conversao local, direto pelo computador\n"
            "- Arquivos preservados sem sobrescrever o original\n"
            "- Fluxo simples: selecionar, escolher formato e converter\n"
            "- Interface escura com foco no arquivo"
        ),
    },
    "Formatos": {
        "title": "Formatos suportados",
        "body": (
            "Imagem\n"
            "PNG, JPG\n\n"
            "Documento\n"
            "PDF\n\n"
            "Em breve\n"
            "DOCX, MP4, MP3 e outros formatos populares"
        ),
    },
    "Precos": {
        "title": "Precos",
        "body": (
            "Plano atual: gratuito.\n\n"
            "- Sem mensalidade\n"
            "- Sem planos de adesao nesta versao\n"
            "- Conversoes locais pelo proprio aplicativo\n"
            "- Ideal para uso academico e demonstracao"
        ),
    },
    "Ajuda": {
        "title": "Ajuda",
        "body": (
            "Como usar\n\n"
            "1. Clique em Selecionar arquivo\n"
            "2. Escolha o arquivo desejado\n"
            "3. Selecione o formato de saida quando a opcao estiver disponivel\n"
            "4. Clique em Converter agora\n\n"
            "O arquivo convertido sera salvo sem alterar o original."
        ),
    },
}


class MidasWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Midas - Conversor de Arquivos")
        self.resize(1180, 760)
        self.setMinimumSize(980, 620)
        self.status_bar = self.statusBar()
        self.active_menu = None
        self.nav_buttons = {}

        root = QWidget()
        root.setObjectName("root")
        self.setCentralWidget(root)

        page = QVBoxLayout(root)
        page.setContentsMargins(56, 32, 56, 48)
        page.setSpacing(0)

        page.addLayout(self.build_header())
        page.addSpacing(32)
        page.addWidget(
            self.build_info_panel(),
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        page.addSpacing(76)
        page.addLayout(self.build_hero())
        page.addStretch(1)

        self.setStyleSheet(self.stylesheet())

    def build_header(self):
        header = QHBoxLayout()
        header.setSpacing(24)

        logo = QLabel()
        logo.setObjectName("logo")
        logo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        pixmap = QPixmap(str(LOGO_PATH))
        if not pixmap.isNull():
            logo.setPixmap(
                pixmap.scaled(
                    128,
                    86,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        else:
            logo.setText("MIDAS")

        header.addWidget(logo)
        header.addStretch(1)

        nav = QFrame()
        nav.setObjectName("nav")
        nav_layout = QHBoxLayout(nav)
        nav_layout.setContentsMargins(24, 0, 24, 0)
        nav_layout.setSpacing(20)

        for text in ("Recursos", "Formatos", "Precos", "Ajuda"):
            item = QPushButton(text)
            item.setObjectName("navItem")
            item.setProperty("active", False)
            item.setCursor(Qt.CursorShape.PointingHandCursor)
            item.clicked.connect(
                lambda checked=False, menu_name=text: self.toggle_menu_info(menu_name)
            )
            self.nav_buttons[text] = item
            nav_layout.addWidget(item)

        header.addWidget(nav)
        header.addStretch(1)

        login = QPushButton("Entrar")
        login.setObjectName("loginButton")
        login.setCursor(Qt.CursorShape.PointingHandCursor)

        convert = QPushButton("Converter agora")
        convert.setObjectName("convertButton")
        convert.setCursor(Qt.CursorShape.PointingHandCursor)

        header.addWidget(login)
        header.addWidget(convert)

        return header

    def build_info_panel(self):
        self.info_panel = QFrame()
        self.info_panel.setObjectName("infoPanel")
        self.info_panel.setFixedWidth(620)
        self.info_panel.setMinimumHeight(164)
        self.info_panel.hide()

        panel_layout = QVBoxLayout(self.info_panel)
        panel_layout.setContentsMargins(32, 24, 32, 24)
        panel_layout.setSpacing(12)

        self.info_title = QLabel()
        self.info_title.setObjectName("infoTitle")
        self.info_title.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.info_body = QLabel()
        self.info_body.setObjectName("infoBody")
        self.info_body.setWordWrap(True)
        self.info_body.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        panel_layout.addWidget(self.info_title)
        panel_layout.addWidget(self.info_body)

        return self.info_panel

    def build_hero(self):
        hero = QHBoxLayout()
        hero.setSpacing(70)

        copy = QVBoxLayout()
        copy.setSpacing(12)

        title = QLabel("Transforme qualquer\narquivo em segundos.")
        title.setObjectName("title")
        title.setWordWrap(True)

        description = QLabel(
            "Converta PDF, Word, Excel, imagens, videos e muito mais.\n"
            "Rapido, seguro e gratuito."
        )
        description.setObjectName("description")
        description.setWordWrap(True)

        copy.addWidget(title)
        copy.addWidget(description)
        copy.addStretch(1)

        hero.addLayout(copy, 5)

        upload = QFrame()
        upload.setObjectName("uploadArea")
        upload.setAcceptDrops(False)
        upload.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        upload.setMinimumHeight(250)

        upload_layout = QVBoxLayout(upload)
        upload_layout.setContentsMargins(24, 0, 24, 0)
        upload_layout.setSpacing(16)
        upload_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icon = QLabel("^")
        icon.setObjectName("uploadIcon")
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        instruction = QLabel("Arraste e solte seu arquivo aqui\nou clique para selecionar")
        instruction.setObjectName("instruction")
        instruction.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instruction.setWordWrap(True)

        button = QPushButton("Selecionar arquivo")
        button.setObjectName("fileButton")
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.clicked.connect(self.on_select_file_clicked)

        upload_layout.addWidget(icon)
        upload_layout.addWidget(instruction)
        upload_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        hero.addWidget(upload, 4)

        return hero

    def toggle_menu_info(self, menu_name):
        if self.active_menu == menu_name and self.info_panel.isVisible():
            self.active_menu = None
            self.info_panel.hide()
            self.update_nav_state()
            return

        content = MENU_CONTENT[menu_name]
        self.active_menu = menu_name
        self.info_title.setText(content["title"])
        self.info_body.setText(content["body"])
        self.info_panel.show()
        self.update_nav_state()

    def update_nav_state(self):
        for name, button in self.nav_buttons.items():
            button.setProperty("active", name == self.active_menu)
            button.style().unpolish(button)
            button.style().polish(button)

    def on_select_file_clicked(self):
        self.select_file()

    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar arquivo",
            "",
            "Todos os arquivos (*.*)",
        )
        if path:
            self.status_bar.showMessage(f"Arquivo selecionado: {path}", 6000)

    def stylesheet(self):
        return f"""
        QWidget#root {{
            background: {BLACK};
        }}

        QLabel {{
            color: {WHITE};
        }}

        QLabel#logo {{
            color: {GOLD};
            font-size: 27px;
            font-weight: 700;
        }}

        QFrame#nav {{
            background: {DARK_BUTTON};
            border-radius: 28px;
            min-height: 56px;
        }}

        QPushButton#navItem {{
            color: {WHITE};
            background: transparent;
            border: none;
            border-radius: 14px;
            min-height: 32px;
            padding: 0 4px;
            font-size: 12px;
            font-weight: 700;
        }}

        QPushButton#navItem:hover,
        QPushButton#navItem[active="true"] {{
            color: {GOLD};
        }}

        QFrame#infoPanel {{
            background: {PANEL_BG};
            border: 1px solid {GOLD};
            border-radius: 18px;
        }}

        QLabel#infoTitle {{
            color: {WHITE};
            font-family: Georgia, "Times New Roman", serif;
            font-size: 30px;
            font-weight: 600;
        }}

        QLabel#infoBody {{
            color: {WHITE};
            font-family: Arial;
            font-size: 14px;
            line-height: 1.35;
        }}

        QPushButton {{
            border: none;
            font-size: 12px;
            font-weight: 700;
        }}

        QPushButton#loginButton {{
            color: {WHITE};
            background: {DARK_BUTTON};
            border-radius: 28px;
            min-width: 86px;
            min-height: 56px;
        }}

        QPushButton#loginButton:hover {{
            background: #2a2a2a;
        }}

        QPushButton#convertButton {{
            color: #000000;
            background: {GOLD};
            border-radius: 28px;
            min-width: 142px;
            min-height: 56px;
        }}

        QPushButton#convertButton:hover,
        QPushButton#fileButton:hover {{
            background: #d69c18;
        }}

        QLabel#title {{
            color: {WHITE};
            font-family: Georgia, "Times New Roman", serif;
            font-size: 49px;
            font-weight: 500;
            line-height: 1.0;
        }}

        QLabel#description {{
            color: {WHITE};
            font-family: Georgia, "Times New Roman", serif;
            font-size: 20px;
            line-height: 1.25;
        }}

        QFrame#uploadArea {{
            background: transparent;
            border: none;
        }}

        QLabel#uploadIcon {{
            color: {GOLD};
            font-size: 68px;
            font-weight: 700;
        }}

        QLabel#instruction {{
            color: {WHITE};
            font-family: Georgia, "Times New Roman", serif;
            font-size: 19px;
            line-height: 1.25;
        }}

        QPushButton#fileButton {{
            color: #000000;
            background: {GOLD};
            border-radius: 28px;
            min-width: 160px;
            min-height: 56px;
        }}

        QStatusBar {{
            color: {WHITE};
            background: {BLACK};
        }}
        """


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Arial"))

    window = MidasWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
