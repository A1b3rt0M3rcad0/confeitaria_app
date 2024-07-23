from views.widgets import base
from controllers.controllers import IngredientController, RecipeController, RecipeIngredientController, UnitController
from config.settings import Config
import customtkinter as ctk
from tkinter import messagebox
from utils.utils import only_float_number, not_start_with_space


class CreateRecipeFrame(base.BaseFrame):

    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.ingredient_controller = IngredientController()
        self.recipe_controller = RecipeController()
        self.recipe_ingredient_controlelr = RecipeIngredientController()
        self.unit_controller = UnitController()

        # Created ingredient list
        self.units = {unit.id: unit.name for unit in self.unit_controller.select_all()} if len(self.unit_controller.select_all()) > 0 else []
        self.ingredients = {ingredient.name: (ingredient.price, ingredient.quantity, self.units[ingredient.unit_id]) for ingredient in self.ingredient_controller.select_all()} if len(self.ingredient_controller.select_all()) > 0 else []

        # widgets sizes
        self.size_label = Config.size_label
        self.size_entry = Config.size_entry
        self.size_option_menu = Config.size_option_menu
        self.size_button = Config.size_button

        # Recipe Entry
        self.label_recipe_name = base.BaseLabel(self, text='Nome:', width=self.size_label[0], height=self.size_label[1])
        self.label_recipe_name.grid(row=0, column=0, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1])

        self.entry_recipe_name = base.BaseEntry(self, placeholder_text='Digite o nome', width=self.size_entry[0], height=self.size_entry[1])
        self.entry_recipe_name.grid(row=0, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        # LIST INGREDIENTS
        self.recipe_ingredients = base.BaseScrollableFrame(self, label_text='Ingredientes:')
        self.recipe_ingredients.grid(row=1, column=0, rowspan=2)

        # Ingredient Select
        self.label_ingredient_register = base.BaseLabel(self, text='Ingredientes:', width=self.size_label[0], height=self.size_label[1], anchor='w')
        self.label_ingredient_register.grid(row=1, column=1, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1], sticky='nw')

        self.option_menu_ingredients = base.BaseOptionMenu(self, values = list(self.ingredients.keys()), width=self.size_option_menu[0]+50, height=self.size_option_menu[1], command=self.__entry_ingredienty_unit, dynamic_resizing=False)
        self.option_menu_ingredients.grid(row=1, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

        self.entry_ingredient_quantity = base.BaseEntry(self, placeholder_text='Qtd', width=self.size_option_menu[0]-90, height=self.size_option_menu[1])
        self.entry_ingredient_quantity.grid(row=1, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='sw')

        self.__entry_ingredienty_unit()

        self.button = base.BaseButton(self, text="Adicionar Ingrediente", width=self.size_button[0], height=self.size_button[1])
        self.button.grid(row=2, column=1, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='nw')  


    def __entry_ingredienty_unit(self, *args) -> None:
        self.selected_unit = self.ingredients[self.option_menu_ingredients.get()][2]
        self.entry_ingredient_quantity_unit = base.BaseLabel(self, text=self.selected_unit, width=self.size_option_menu[0]-100, height=self.size_option_menu[1], anchor='w')
        self.entry_ingredient_quantity_unit.grid(row=1, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='s')