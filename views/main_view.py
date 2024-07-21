from views.widgets import create_unit_frame, create_ingredient_frame
import tkinter as tk
import customtkinter as ctk
from config.settings import Config


root = ctk.CTk(fg_color=Config.colors['base'])
root.title('Confeitaria')
frame = create_ingredient_frame.CreateIngredientFrame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)
root.mainloop()