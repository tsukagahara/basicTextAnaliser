from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton

class CustomHeader(QWidget):
    def __init__(self, theme=None, parent=None):
        super().__init__(parent)
        self.setFixedHeight(30)
        self.theme = theme
        self.theme = theme or {}

        if not self.theme:  # Проверяем что словарь не пустой
            print("не передались значения темы")  
            self.theme = {'isDark': True, 'bg_dark': '#111111', 'bg_card': '#121212', 'accent_primary': '#202020', 'accent_secondary': '#252525', 'accent_light': '#7a7a7a', 'text_main':
 '#e0e0e0', 'text_muted': '#a0a0a0'}
    #  установить базовую тему, если прошлая не подгрузилась
        # "isDark" "bg_dark" "bg_card" "accent_primary" "accent_secondary" "accent_light" "text_main" "text_muted"
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Убирает внешние отступы
        layout.setSpacing(0)  # Убирает промежутки между виджетами

        self.background = QWidget()
        self.background.setStyleSheet("background-color:" + self.theme["bg_dark"] + ";")
        bg_layout = QHBoxLayout(self.background)
        bg_layout.setContentsMargins(0, 0, 0, 0)
        bg_layout.setSpacing(0)
        
        self.title_label = QLabel("Yarn", self.background)
        self.title_label.setStyleSheet("color: white; font-weight: bold;")

        self.close_btn = QPushButton("X", self.background)
        self.close_btn.setStyleSheet("""
    QPushButton {
        background-color: #ff4444;
        color: white;
        border: none;
        font-weight: bold;
        padding: 10px 20px;
    }
    QPushButton:hover {background-color: #ff6666;}
    QPushButton:pressed {background-color: #cc0000;}
""")
        # Добавляем элементы в layout фона
        bg_layout.addWidget(self.title_label)
        bg_layout.addStretch()
        bg_layout.addWidget(self.close_btn)

        # Добавляем фон в основной layout
        layout.addWidget(self.background)