from views.widgets.create import create_unit_frame
import tkinter as tk
import customtkinter as ctk
from config.settings import Config
from views.widgets.create import create_ingredient_frame, create_invoice_frame, create_product_frame, create_recipe_frame


root = ctk.CTk(fg_color=Config.colors['base'])
root.title('Confeitaria')
# unit_frame = create_unit_frame.CreateUnitFrame(root)
# unit_frame.grid(row=0, column=0)
ingredient_frame = create_ingredient_frame.CreateIngredientFrame(root)
ingredient_frame.grid(row=0, column=1)
recipe_frame = create_recipe_frame.CreateRecipeFrame(root)
recipe_frame.grid(row=0, column=2)
product_frame = create_product_frame.CreateProductFrame(root)
product_frame.grid(row=0, column=3)

invoice_frame = create_invoice_frame.CreateInvoiceFrame(root)
invoice_frame.grid(row=0, column=4)

# root.maxsize(product_frame.frame_size[0], product_frame.frame_size[1])
root.mainloop()