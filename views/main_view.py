from views.widgets import create_unit_frame, create_ingredient_frame, create_recipe_frame
import tkinter as tk
import customtkinter as ctk
from config.settings import Config


root = ctk.CTk(fg_color=Config.colors['base'])
root.title('Confeitaria')
# unit_frame = create_unit_frame.CreateUnitFrame(root)
# unit_frame.grid(row=0, column=0)
# ingredient_frame = create_ingredient_frame.CreateIngredientFrame(root)
# ingredient_frame.grid(row=0, column=1)
recipe_frame = create_recipe_frame.CreateRecipeFrame(root)
recipe_frame.grid(row=0, column=2)

root.maxsize(recipe_frame.frame_size[0], recipe_frame.frame_size[1])
root.mainloop()