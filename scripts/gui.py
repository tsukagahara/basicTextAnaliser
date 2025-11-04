import customtkinter as ctk
import tkinter as tk

class MyApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.app = ctk.CTk()
        self.app.geometry("400x300")
        self.app.title("basicTextAnalyzer")
        self._create_widgets()
    
    def _create_widgets(self):
        main = ctk.CTkFrame(self.app)
        main.pack(pady=20, padx=2, fill="both", expand=True)

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = MyApp()
    app.run()