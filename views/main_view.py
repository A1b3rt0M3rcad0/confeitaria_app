import tkinter as tk
import customtkinter as ctk
from config.settings import Config
from views.widgets.create import create_ingredient_frame, create_invoice_frame, create_product_frame, create_recipe_frame, create_unit_frame
from views.widgets.select import select_ingredient_frame, select_recipe_frame, select_product_frame
from views.widgets.base import BaseButton


root = ctk.CTk(fg_color=Config.colors['base'])
root.title('Confeitaria')
frame = create_product_frame.CreateProductFrame(root)
frame.grid()
frame2 = select_product_frame.SelectProductFrame(root)
frame2.grid()
frame4 = select_recipe_frame.SelectRecipeFrame(root)
frame4.grid(row= 0, column=1)
frame3 = create_recipe_frame.CreateRecipeFrame(root)
frame3.grid(row=1, column=1)
# root.maxsize(frame.frame_size[0], frame.frame_size[1])
# root.minsize(frame.frame_size[0], frame.frame_size[1])
root.bind('<FocusOut>', lambda x: (frame2.update_product_list(x), frame4.update_recipe_list(x)))
root.mainloop()