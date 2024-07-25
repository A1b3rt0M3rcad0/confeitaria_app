import tkinter as tk
import customtkinter as ctk
from config.settings import Config
from views.widgets.create import create_ingredient_frame, create_invoice_frame, create_product_frame, create_recipe_frame, create_unit_frame
from views.widgets.base import BaseButton


root = ctk.CTk(fg_color=Config.colors['base'])
root.title('Confeitaria')
frame = create_invoice_frame.CreateInvoiceFrame(root)
frame.grid()
root.mainloop()