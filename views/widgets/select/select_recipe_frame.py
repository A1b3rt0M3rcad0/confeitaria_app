from views.widgets import base
from controllers.controllers import RecipeController, IngredientController, RecipeIngredientController
from config.settings import Config
from tkinter import messagebox

class SelectRecipeFrame(base.BaseFrame):


    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.recipe_controller = RecipeController()
        self.ingredient_controller = IngredientController()
        self.recipe_ingredient_controller = RecipeIngredientController()

        # widgets sizes
        self.size_label = Config.size_label
        self.size_entry = (Config.size_entry[0]+75, Config.size_entry[1])
        self.size_option_menu = (Config.size_option_menu[0]+75, Config.size_option_menu[1])
        self.size_button = Config.size_button
        self.ingredient_list = Config.width_ingredient_list

        # frame sizes
        self.x_frame_size = self.ingredient_list + Config.paddings['text'][0] * 4
        self.y_frame_size = 275
        self.frame_size = (self.x_frame_size, self.y_frame_size)

        # Ingredients
        self.__recipe_cost()

        # Ingredient List
        self.recipe_list = base.BaseScrollableFrame(self, label_text='Receitas:', width=self.ingredient_list)
        self.recipe_list.grid(row=2, column=0, rowspan=2, padx=Config.paddings['text'][0], pady=Config.paddings['text'][1])

        self.__update_recipe_list()
    
    def __recipe_cost(self) -> None:
        self.recipes = [(recipe.id, recipe.name) for recipe in self.recipe_controller.select_all()]
        self.recipe_cost = {recipe[1]: 0 for recipe in self.recipes}
        
        for recipe_id, recipe_name in self.recipes:
            for recipe_ingredient in self.recipe_ingredient_controller.select(recipe_id=[recipe_id]):
                ingredient_id = recipe_ingredient.ingredient_id
                ingredient = self.ingredient_controller.select(id=[ingredient_id])[0]
                recipe_ingredient_quantity = recipe_ingredient.quantity
                ingredienty_cost = (recipe_ingredient_quantity / ingredient.quantity) * ingredient.price
                self.recipe_cost[recipe_name] += ingredienty_cost
    
    def __update_recipe_list(self) -> None:
            # att recipes
            self.__recipe_cost()
            self.recipe_cost_list = [(recipe_name, recipe_cost) for recipe_name, recipe_cost in self.recipe_cost.items()]
            # Clear the current list
            for widget in self.recipe_list.winfo_children():
                widget.destroy()

            # Display each recipe in the list
            for index, (name, cost) in enumerate(self.recipe_cost_list):
                result_name = name if len(name) <= 15 else f'{name[0:16]}...'
                label_text = f"{index} - {result_name}: R${cost:.2f}"
                recipe_label = base.BaseLabel(self.recipe_list, text=label_text, width=self.size_label[0]+220, anchor='w')
                recipe_label.grid(row=index, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

                delete_button = base.BaseButton(self.recipe_list, text="X", width=20, height=20, command=lambda idx=index: self.__delete_recipe(idx))
                delete_button.grid(row=index, column=1, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='e')
            
    def __delete_recipe(self, index:int) -> None:
         recipe_name = self.recipe_cost_list[index][0]
         recipe = self.recipe_controller.select(name=[recipe_name])[0]
         self.recipe_controller.delete(recipe)
         messagebox.showinfo('Alerta', f'Receita: "{recipe_name}" deletada com sucesso!')
         self.__update_recipe_list()
    
    def update_recipe_list(self, *args) -> None:
         self.__update_recipe_list()