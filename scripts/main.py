from tkinter import *

# Базовые цвета
BG_DARK = '#121212'      # Основной фон
BG_CARD = '#1e1e1e'      # Карточки, панели

# Акцентные (тускло-синие)
ACCENT_PRIMARY = '#2a4a6d'   # Основной акцент
ACCENT_SECONDARY = '#3a5a7d' # Второстепенный
ACCENT_LIGHT = '#4a6a8d'     # Светлый акцент

# Текст
TEXT_MAIN = '#e0e0e0'    # Основной текст
TEXT_MUTED = '#a0a0a0'   # Второстепенный текст

root = Tk()

root['bg'] = '#000000'
root.title('basicTextAnalyzer')
root.minsize(500, 500)

main_frame = Frame(root, bg=BG_DARK)
main_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

# Боковая панель внутри main_frame
aside = Frame(main_frame, bg=BG_CARD)
aside.place(relx=0, rely=0, width=100, relheight=1)

# Контентная область внутри main_frame (справа от aside)
content = Frame(main_frame, bg=BG_DARK)
content.place(relx=0, x=105, rely=0, relwidth=1, relheight=1)

# Остальные элементы внутри content
header = Frame(content, bg=BG_CARD)
header.place(relx=0, rely=0, relwidth=1, relheight=0.05)

textarea = Frame(content, bg=BG_CARD)
textarea.place(relx=0, rely=0.055, relwidth=1, relheight=0.89)

footer = Frame(content, bg=BG_CARD)
footer.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)

footer_annotations = Frame(footer, bg=ACCENT_PRIMARY)
footer_annotations.place(relx=0.001, rely=0.02, relwidth=0.7, relheight=0.96)

footer_stat = Frame(footer, bg=ACCENT_PRIMARY)
footer_stat.place(relx=0.702, rely=0.02, relwidth=0.7, relheight=0.96)

root.mainloop()