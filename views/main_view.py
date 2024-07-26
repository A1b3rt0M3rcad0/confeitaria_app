import tkinter as tk
import customtkinter as ctk
from config.settings import Config
from views.widgets.create import create_ingredient_frame, create_invoice_frame, create_product_frame, create_recipe_frame, create_unit_frame
from views.widgets.select import select_ingredient_frame
from views.widgets.base import BaseButton


root = ctk.CTk(fg_color=Config.colors['base'])
root.title('Confeitaria')
frame = select_ingredient_frame.SelectIngredientFrame(root)
frame.grid()
frame2 = create_ingredient_frame.CreateIngredientFrame(root)
frame2.grid()

root.bind('<FocusOut>', frame.update_ingredient_list)
# root.maxsize(frame.frame_size[0], frame.frame_size[1])
# root.minsize(frame.frame_size[0], frame.frame_size[1])

root.mainloop()