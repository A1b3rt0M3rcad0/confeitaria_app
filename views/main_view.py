from views.frames import create_unit_frame
import tkinter as tk
import customtkinter as ctk
from config.settings import Config


root = ctk.CTk(fg_color=Config.colors['base'])
frame = create_unit_frame.CreateUnitFrame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)
root.mainloop()