from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton
from PySide6.QtCore import Qt
# from PySide6.QtGui import

class aside(QWidget):
    def __init__(self, parent=None, theme=None):
        super().__init__(parent)
        self.theme = theme
        self.setMouseTracking(True)
        self.width_aside = 300
        self.setFixedWidth(self.width_aside)
        self.setup_ui()
        self.apply_theme()
    
    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        self.content_frame = QFrame()
        
        content_layout = QHBoxLayout(self.content_frame)
        content_layout.setAlignment(Qt.AlignTop)
        content_layout.setSpacing(0)
        content_layout.setContentsMargins(0, 0, 0, 0)

        widget1 = QFrame()
        widget1.setFixedWidth(int(self.width_aside // 6))
        btn_a = QPushButton(">>")
        btn_b = QPushButton(">>")
        btn_c = QPushButton(">>")
        btn_d = QPushButton(">>")
        btn_e = QPushButton(">>")
        widget1_layout = QVBoxLayout(widget1)
        widget1_layout.addWidget(btn_a)
        widget1_layout.addWidget(btn_b)
        widget1_layout.addWidget(btn_c)
        widget1_layout.addWidget(btn_d)
        widget1_layout.addWidget(btn_e)
        
        widget2 = QFrame()
        widget2.setFixedWidth(int(self.width_aside * 5 // 6))
        label2 = QLabel("self.width_aside * 5 // 6")
        widget2_layout = QVBoxLayout(widget2)
        widget2_layout.addWidget(label2)
        
        content_layout.addWidget(widget1)
        content_layout.addWidget(widget2)
        
        main_layout.addWidget(self.content_frame)

    def apply_theme(self):
        self.bg_card = self.theme.get('bg_card')
        self.bg_color = self.theme.get('bg_color')
        self.accent_color = self.theme.get('accent_color')
        self.accent_primary =  self.theme.get('accent_primary')
        self.text_main = self.theme.get('text_main')
        self.btn_bg_color = self.theme.get('btn_bg_color')
        self.btn_hover_bg_color = self.theme.get('btn_hover_bg_color')

        self.update()
        
        self.setStyleSheet(f"""
                background-color: {self.bg_card}; 
                color: {self.text_main};
                border: 1px solid #444;
            """)
        self.content_frame.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.btn_bg_color};
                color: {self.text_main};
                border: 1px solid {self.accent_color};
                padding: 5px;
                border-radius: 3px;
            }}
            
            QPushButton:hover {{
                background-color: {self.btn_hover_bg_color};
                border: 1px solid {self.accent_primary};
            }}
            
            QPushButton:pressed {{
                background-color: {self.accent_primary};
            }}
        """)