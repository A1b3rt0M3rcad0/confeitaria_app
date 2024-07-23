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
        self.recipe_ingredient_controller = RecipeIngredientController()
        self.unit_controller = UnitController()

        # Store added ingredients
        self.added_ingredients = []

        # Validates
        validate_float_entry = (self.register(only_float_number), '%P')
        validade_entry_string = (self.register(not_start_with_space), '%S', '%P')

        # Created ingredient list
        self.units = {unit.id: unit.name for unit in self.unit_controller.select_all()} if len(self.unit_controller.select_all()) > 0 else []
        self.ingredients = {ingredient.name: (ingredient.id, ingredient.price, ingredient.quantity, self.units[ingredient.unit_id]) for ingredient in self.ingredient_controller.select_all()} if len(self.ingredient_controller.select_all()) > 0 else []

        # widgets sizes
        self.size_label = Config.size_label
        self.size_entry = Config.size_entry
        self.size_option_menu = Config.size_option_menu
        self.size_button = Config.size_button
        self.ingredient_list = Config.width_ingredient_list

        # frame sizes
        self.x_frame_size = self.size_label[0]*2 + Config.paddings['entry'][0]*4 + self.ingredient_list + Config.paddings['entry'][0] * 2
        self.y_frame_size = self.size_entry[1]*10 + Config.paddings['message'][1]*2 + Config.paddings['text'][1]*2 - 15
        self.frame_size = (self.x_frame_size, self.y_frame_size)

        # Recipe Entry
        self.label_recipe_name = base.BaseLabel(self, text='Nome:', width=self.size_label[0], height=self.size_label[1])
        self.label_recipe_name.grid(row=0, column=0, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1])

        self.entry_recipe_name = base.BaseEntry(self, placeholder_text='Nome da Receita', width=self.size_entry[0], height=self.size_entry[1], validate='key', validatecommand=validade_entry_string)
        self.entry_recipe_name.grid(row=0, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        # LIST INGREDIENTS
        self.recipe_ingredients = base.BaseScrollableFrame(self, label_text='Ingredientes:', width=self.ingredient_list)
        self.recipe_ingredients.grid(row=1, column=0, rowspan=2, padx=Config.paddings['text'][0], pady=Config.paddings['text'][1])

        # Ingredient Select
        self.label_ingredient_register = base.BaseLabel(self, text='Ingredientes:', width=self.size_label[0], height=self.size_label[1], anchor='w')
        self.label_ingredient_register.grid(row=1, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='nw')

        self.option_menu_ingredients = base.BaseOptionMenu(self, values = list(self.ingredients.keys()), width=self.size_option_menu[0]+50, height=self.size_option_menu[1], command=self.__entry_ingredienty_unit, dynamic_resizing=False)
        self.option_menu_ingredients.grid(row=1, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

        self.entry_ingredient_quantity = base.BaseEntry(self, placeholder_text='1.0', width=self.size_option_menu[0]-90, height=self.size_option_menu[1], validate='key', validatecommand=validate_float_entry)
        self.entry_ingredient_quantity.grid(row=1, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='sw')

        self.__entry_ingredienty_unit()

        self.button = base.BaseButton(self, text="Adicionar Ingrediente", width=self.size_button[0], height=self.size_button[1], command=self.__add_ingredients)
        self.button.grid(row=2, column=1, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='nw')

        # Total Cost
        self.__label_ingredients_total_cost()

        self.button = base.BaseButton(self, text="Criar Receita", width=self.size_button[0], height=self.size_button[1], command=self.__create_recipe)
        self.button.grid(row=2, column=1, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='sw')


    def __entry_ingredienty_unit(self, *args) -> None:
        self.selected_unit = self.ingredients[self.option_menu_ingredients.get()][3]
        if hasattr(self, 'entry_ingredient_quantity_unit'):
            self.entry_ingredient_quantity_unit.destroy()
        self.entry_ingredient_quantity_unit = base.BaseLabel(self, text=self.selected_unit, width=self.size_option_menu[0]-100, height=self.size_option_menu[1], anchor='w')
        self.entry_ingredient_quantity_unit.grid(row=1, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='s')
    
    def __label_ingredients_total_cost(self, *args) -> None:
        if hasattr(self, 'label_ingredient_total_cost'):
            self.label_ingredient_total_cost.destroy()
        if not hasattr(self, 'total_cost'):
            self.total_cost = 0.0
        self.label_ingredient_total_cost = base.BaseLabel(self, text=f'Custo Total: R${self.total_cost:.2f}', width=self.size_label[0], height=self.size_label[1], anchor='w')
        self.label_ingredient_total_cost.grid(row=2, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

    def __add_ingredients(self, *args) -> None:
        ingredient_name = self.option_menu_ingredients.get()
        ingredient = self.ingredients[ingredient_name]
        ingredient_quantity = self.entry_ingredient_quantity.get()

        if not ingredient_quantity:
            messagebox.showerror("Erro", "Por favor, insira a quantidade do ingrediente.")
            return

        # Calculate the cost for the added ingredient
        cost = float(ingredient_quantity) * ingredient[1] / ingredient[2]

        # Add ingredient to the list
        self.added_ingredients.append((ingredient_name, ingredient_quantity, self.selected_unit, cost))

        # Update total cost
        self.total_cost += cost

        # Clear the quantity entry field
        self.entry_ingredient_quantity.delete(0, ctk.END)

        # Update the ingredient list display and total cost label
        self.__update_ingredient_list()
        self.__update_total_cost_label()

    def __update_ingredient_list(self) -> None:
        # Clear the current list
        for widget in self.recipe_ingredients.winfo_children():
            widget.destroy()

        # Display each ingredient in the list
        for index, (name, quantity, unit, cost) in enumerate(self.added_ingredients):
            label_text = f"{name}: {quantity} {unit} - R${cost:.2f}"
            ingredient_label = base.BaseLabel(self.recipe_ingredients, text=label_text, width=300, anchor='w')
            ingredient_label.grid(row=index, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

            delete_button = base.BaseButton(self.recipe_ingredients, text="X", width=20, height=20, command=lambda idx=index: self.__delete_ingredient(idx))
            delete_button.grid(row=index, column=1, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='e')

    def __update_total_cost_label(self) -> None:
        if hasattr(self, 'label_ingredient_total_cost'):
            self.label_ingredient_total_cost.destroy()
        self.__label_ingredients_total_cost()

    def __delete_ingredient(self, index) -> None:
        # Remove the ingredient cost from total cost
        self.total_cost -= self.added_ingredients[index][3]

        # Remove the ingredient from the list
        del self.added_ingredients[index]

        # Update the ingredient list display and total cost label
        self.__update_ingredient_list()
        self.__update_total_cost_label()
    
    def __delete_all_infos(self) -> None:
        # Reset Ingredients and Cost
        self.added_ingredients = []
        self.total_cost = 0
        # Reset Widgets
        self.__update_ingredient_list()
        self.__update_total_cost_label()
        # Resets Entrys
        self.entry_ingredient_quantity.delete(0, ctk.END)
        self.entry_recipe_name.delete(0, ctk.END)
    
    def __create_recipe(self) -> None:

        recipe_name = self.entry_recipe_name.get().capitalize()

        if len(recipe_name) >= 3:

            if len(self.added_ingredients) >= 1:

                recipe = self.recipe_controller.select(name=[recipe_name])

                if len(recipe) == 0:
                    self.recipe_controller.create(name=recipe_name)
                    recipe_id = self.recipe_controller.select(name=[recipe_name])[0].id

                else:
                    messagebox.showerror("Erro", "Receita já existe.")
                    return 
                
                for ingredient in self.added_ingredients:
                    ingredient_name = ingredient[0]
                    ingredient_id = self.ingredients[ingredient_name][0]
                    self.recipe_ingredient_controller.create(ingredient_id=ingredient_id, recipe_id=recipe_id, quantity=ingredient[1])

                self.__delete_all_infos()
                messagebox.showinfo("Alerta", f'Receita "{recipe_name}" criada com sucesso.')

            else:
                messagebox.showerror("Erro", "Por favor, adicione um ingrediente à receita.")

        else:
            messagebox.showinfo("Alerta", "O nome da receita pe muito curto.")