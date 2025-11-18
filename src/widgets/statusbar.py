import os
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPixmap

class StatusBar(QWidget):
    def __init__(self, theme=None, parent=None):
        super().__init__(parent)
        self.bg_color = None
        self.theme = theme
        self.setup_ui()
        self.apply_theme()
        self.count_tabs = 3 #
    
    def setup_ui(self):
        self.setObjectName("statusBar")
        layout = QHBoxLayout(self)
        self.setFixedHeight(30)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.installEventFilter(self)

        self.btn1 = QPushButton("1") #
        self.btn1.setFixedSize(200, 25)
        self.btn1.setCursor(Qt.PointingHandCursor)

        self.btn2 = QPushButton("2") #
        self.btn2.setFixedSize(200, 25)
        self.btn2.setCursor(Qt.PointingHandCursor)

        self.btn3 = QPushButton("3") #
        self.btn3.setFixedSize(200, 25)
        self.btn3.setCursor(Qt.PointingHandCursor)
        
        layout.addWidget(self.btn1) #
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
    
    def apply_theme(self):
        self.bg_color = self.theme.get('bg_card', '#121212')
        self.text_color = self.theme.get('text_main', '#e0e0e0')
        self.accent_color = self.theme.get('accent_primary', '#202020')

        self.update()

        #
        self.btn1.setStyleSheet(f"""
            QPushButton {{
                color: {self.text_color};
                border: none;
                border-radius: 3px;
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #ff555555;
            }}
        """)
        
        self.btn2.setStyleSheet(f"""
            QPushButton {{
                color: {self.text_color};
                border: none;
                border-radius: 3px;
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #ff555555;
            }}
        """)

        self.btn3.setStyleSheet(f"""
            QPushButton {{
                color: {self.text_color};
                border: none;
                border-radius: 3px;
                font-size: 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #ff555555;
            }}
        """)
    
    def paintEvent(self, event):
        if self.bg_color and self.accent_color:
            painter = QPainter(self)
            painter.fillRect(self.rect(), QColor(self.bg_color))

            painter.setPen(QColor(self.accent_color))
            painter.drawLine(0, 0, self.width(), 0)
            
            painter.drawLine(0, self.height()-1, self.width(), self.height()-1)
        super().paintEvent(event)