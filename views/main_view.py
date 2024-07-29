import tkinter as tk
import customtkinter as ctk
from config.settings import Config
from views.widgets.create import create_ingredient_frame, create_invoice_frame, create_product_frame, create_recipe_frame, create_unit_frame
from views.widgets.select import select_ingredient_frame, select_recipe_frame
from views.widgets.base import BaseButton


root = ctk.CTk(fg_color=Config.colors['base'])
root.title('Confeitaria')
frame = select_recipe_frame.SelectRecipeFrame(root)
frame.grid()
frame2 = create_recipe_frame.CreateRecipeFrame(root)
frame2.grid()
# frame3 = create_ingredient_frame.CreateIngredientFrame(root)
# frame3.grid()
# root.maxsize(frame.frame_size[0], frame.frame_size[1])
# root.minsize(frame.frame_size[0], frame.frame_size[1])
root.bind('<FocusIn>', frame.update_recipe_list)
root.mainloop()