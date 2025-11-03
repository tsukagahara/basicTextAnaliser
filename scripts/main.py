import tkinter as tk

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

root = tk.Tk()

root['bg'] = BG_DARK
root.title('basicTextAnalyzer')
root.minsize(1000, 500)
root.overrideredirect(True)

main_frame = tk.Frame(root, bg=BG_DARK)
main_frame.place(relwidth=1, relheight=1)

# Боковая панель внутри main_frame
aside = tk.Frame(main_frame, bg=BG_CARD)
aside.place(relx=0, rely=0, width=40, relheight=1)

aside_settings_header_container = tk.Frame(aside, bg=ACCENT_LIGHT)
aside_settings_header_container.place(width=40, height=27)

aside_settings = tk.Frame(aside_settings_header_container)
aside_settings.place(x=0, y=0, width=38, height=25)

# Контентная область внутри main_frame (справа от aside)
content = tk.Frame(main_frame, bg=BG_DARK)
content.place(relx=0, x=43, rely=0, relwidth=1, relheight=1)

# Остальные элементы внутри content
header = tk.Frame(content, bg=ACCENT_PRIMARY)
header.place(relwidth=1, height=27)

header_container = tk.Frame(header, width=190, bg=ACCENT_LIGHT)
header_container.pack(side=tk.RIGHT, fill=tk.Y)
header_container.pack_propagate(False)


# --------------------------------------

header_container_btn1 = tk.Frame(header_container, width=50, height=25)
header_container_btn1.place(x=2, y=0)
# 
minimize_btn = tk.Button(header_container_btn1, text="—", command=root.iconify)
minimize_btn.place(width=50, height=25)


header_container_btn2 = tk.Frame(header_container, width=50, height=25)
header_container_btn2.place(x=50, y=0)
# 
def toggle_maximize():
    if root.state() == 'zoomed':
        root.state('normal')
    else:
        root.state('zoomed')
# 
maximize_btn = tk.Button(header_container_btn2, text="❒", command=toggle_maximize, pady=0)
maximize_btn.place(width=52, height=25)

header_container_btn3 = tk.Frame(header_container, width=50, height=25)
header_container_btn3.place(x=100, y=0)
# 
close_button = tk.Button(header_container_btn3, text="X", command=root.destroy, pady=2)
close_button.place(width=50, height=25)

# --------------------------------------

textarea = tk.Frame(content, bg=BG_CARD)
textarea.place(relx=0, y=53, relwidth=1, relheight=0.89)

footer = tk.Frame(content, bg=BG_CARD)
footer.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)

footer_annotations = tk.Frame(footer, bg=ACCENT_PRIMARY)
footer_annotations.place(relx=0.001, rely=0.02, relwidth=0.68, relheight=0.96)

footer_stat = tk.Frame(footer, bg=ACCENT_PRIMARY)
footer_stat.place(relx=0.702, rely=0.02, relwidth=0.7, relheight=0.96)

root.mainloop()