from views.widgets import create_unit_frame, create_ingredient_frame
import tkinter as tk
import customtkinter as ctk
from config.settings import Config


root = ctk.CTk(fg_color=Config.colors['base'])
root.title('Confeitaria')
frame = create_unit_frame.CreateUnitFrame(root)
frame.grid(row=0, column=0)
root.mainloop()