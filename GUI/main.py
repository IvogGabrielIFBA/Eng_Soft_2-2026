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


class MidasWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Midas - Conversor de Arquivos")
        self.resize(1180, 760)
        self.setMinimumSize(980, 620)

        root = QWidget()
        root.setObjectName("root")
        self.setCentralWidget(root)

        page = QVBoxLayout(root)
        page.setContentsMargins(56, 32, 56, 48)
        page.setSpacing(0)

        page.addLayout(self.build_header())
        page.addSpacing(108)
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
        nav_layout.setSpacing(28)

        for text in ("Recursos", "Formatos", "Precos", "Ajuda"):
            item = QLabel(text)
            item.setObjectName("navItem")
            item.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        button.clicked.connect(self.select_file)

        upload_layout.addWidget(icon)
        upload_layout.addWidget(instruction)
        upload_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        hero.addWidget(upload, 4)

        return hero

    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar arquivo",
            "",
            "Todos os arquivos (*.*)",
        )
        if path:
            self.statusBar().showMessage(f"Arquivo selecionado: {path}", 6000)

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

        QLabel#navItem {{
            color: {WHITE};
            font-size: 12px;
            font-weight: 700;
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