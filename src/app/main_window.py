import os
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication
from PySide6.QtGui import QIcon, Qt
import src.core as core
import src.utils.helpers as helpers
from widgets.header import CustomHeader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_main_app()
        self.path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).replace('\\', '/')

        self.theme_default = helpers.get_json_property(
            self.path + '/resources/themes/' + 
            f'{core.get_instruction_as_json('./config/config.json', "theme")}' + 
            '.json'
        )

        self.font_default = helpers.get_json_property(
            self.path + '/resources/fonts/' + 
            f'{core.get_instruction_as_json('./config/config.json', "fonts")}' + 
            '.json'
        )
        self.main_font_style = self.font_default["main"]
        self.monospace_font_style = self.font_default["monospace"]
        # "family" "size" "weight" "style" "line_height" "letter_spacing" "color"

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.header = CustomHeader(theme=self.theme_default, parent=self)
        self.setMenuWidget(self.header)

        self.header.close_btn.clicked.connect(self.close)

        # "isDark" "bg_dark" "bg_card" "accent_primary" "accent_secondary" "accent_light" "text_main" "text_muted"

        self.is_color_suitable = (self.theme_default["isDark"] == self.main_font_style["fontIsDark"])

        if self.is_color_suitable:
            dialog = helpers.colors_is_suitable(self.theme_default, self.main_font_style, self.path)
            dialog.exec()
        

    def setup_main_app(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Yarn")
        
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                "resources", "icons", "ico", "Yarn-256.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            self.setStyleSheet("background-color: #000000; padding: none")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        
    
    def create_widgets(self):
        self.setMenuWidget(self.header)
    
    def on_close(self):
        self.close()
    
    def run(self):
        self.show()