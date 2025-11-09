from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton

class CustomHeader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        
        self.title_label = QLabel("Yarn")
        self.title_label.setStyleSheet("""
    QLabel {
        background-color: #ff4444;
        color: white;
        padding: 5px 20px;
        border: none;
        font-weight: bold;
    }
""")
        self.close_btn = QPushButton("X")
        self.close_btn.setStyleSheet("""
    QPushButton {
        background-color: #ff4444;
        color: white;
        border: none;
        padding: 5px 20px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #ff6666;
    }
    QPushButton:pressed {
        background-color: #cc0000;
    }
""")
        
        layout.addWidget(self.title_label)
        layout.addStretch()
        layout.addWidget(self.close_btn)