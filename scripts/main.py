import gui as gui
from gui import MyApp

# Базовые цвета
BG_DARK = '#1e1e1e'      # Основной фон
BG_CARD = '#121212'      # Карточки, панели

# Акцентные (тускло-синие)
ACCENT_PRIMARY = "#252525"   # Основной акцент
ACCENT_SECONDARY = '#3a5a7d' # Второстепенный
ACCENT_LIGHT = "#7a7a7a"     # Светлый акцент

# Текст
TEXT_MAIN = '#e0e0e0'    # Основной текст
TEXT_MUTED = '#a0a0a0'   # Второстепенный текст

if __name__ == "__main__":
    app = MyApp()
    app.run()