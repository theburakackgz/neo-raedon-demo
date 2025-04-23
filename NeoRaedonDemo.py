
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog,
                             QListWidget, QTextEdit)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

class NeoRaedonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NeoRaedon Demo v1.0.0")
        self.setGeometry(300, 150, 600, 400)

        # Tema rengi: Mavi-Gri
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#e6ecf3"))
        palette.setColor(QPalette.Button, QColor("#3a6ea5"))
        palette.setColor(QPalette.ButtonText, Qt.white)
        self.setPalette(palette)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Yolum yoktu. Ama yine de vardım.")
        self.label.setFont(QFont("Arial", 14, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)

        self.btn = QPushButton("PDF / XML Dosyası Yükle")
        self.btn.setFont(QFont("Arial", 11))
        self.btn.clicked.connect(self.loadFiles)

        self.fileList = QListWidget()

        self.status = QTextEdit()
        self.status.setReadOnly(True)
        self.status.setText("Sistem hazır. Dosya yüklemeyi bekliyor...")

        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        layout.addWidget(self.fileList)
        layout.addWidget(self.status)

        self.setLayout(layout)

    def loadFiles(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Dosya Seç", "", "PDF/XML Files (*.pdf *.xml)")
        if files:
            self.fileList.clear()
            self.fileList.addItems(files)
            self.status.append(f"{len(files)} dosya yüklendi. İncelemeye hazır.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = NeoRaedonDemo()
    demo.show()
    sys.exit(app.exec_())
