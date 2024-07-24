from views.widgets import base
from controllers.controllers import RecipeController, ProductController, RecipeIngredientController, IngredientController
from config.settings import Config
import customtkinter as ctk
from tkinter import messagebox
from utils.utils import only_float_number


class CreateProductFrame(base.BaseFrame):


    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.recipe_controller = RecipeController()
        self.ingredient_controller = IngredientController()
        self.product_controller = ProductController()
        self.recipe_ingredient_controller = RecipeIngredientController()
        validate_float_entry = (self.register(only_float_number), '%P')

        # widgets sizes
        self.size_label = Config.size_label
        self.size_entry = (Config.size_entry[0]+75, Config.size_entry[1])
        self.size_option_menu = (Config.size_option_menu[0]+75, Config.size_option_menu[1])
        self.size_button = Config.size_button

        # Recipes
        self.all_recipes = self.recipe_controller.select_all()
        self.recipes = {recipe.name: recipe.id for recipe in self.all_recipes} if len(self.all_recipes) > 0 else []

        # frame sizes
        self.x_frame_size = self.size_label[0] + self.size_entry[0] + Config.paddings['entry'][0]*4
        self.y_frame_size = self.size_label[1]*2 + self.size_entry[1]*2 + self.size_button[1] + Config.paddings['entry'][1]*8 + Config.paddings['button'][1]*2
        self.frame_size = (self.x_frame_size, self.y_frame_size)

        # Recipes
        self.label_recipe = base.BaseLabel(self, text='Recipe:', width=self.size_label[0], height=self.size_label[1])
        self.label_recipe.grid(row=0, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        self.option_menu_recipes = base.BaseOptionMenu(self, values = list(self.recipes.keys()), width=self.size_option_menu[0], height=self.size_option_menu[1], dynamic_resizing=False, command=self.__cost_of_recipe)
        self.option_menu_recipes.grid(row=0, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        # Recipe Price
        self.label_production_cost = base.BaseLabel(self, text='Custo de Produção:', width=self.size_label[0], height=self.size_label[1], anchor='w')
        self.label_production_cost.grid(row=1, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

        self.__cost_of_recipe()

        # Product Price
        self.label_product_price = base.BaseLabel(self, text='Preço de Venda:', width=self.size_label[0], height=self.size_label[1])
        self.label_product_price.grid(row=2, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        self.entry_product_price = base.BaseEntry(self, placeholder_text='1.00', width=self.size_option_menu[0], height=self.size_option_menu[1], validate='key', validatecommand=validate_float_entry)
        self.entry_product_price.grid(row=2, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])
        self.entry_product_price.bind('<KeyRelease>', self.__expected_profit)

        # Expected Profit
        self.label_expected_profit = base.BaseLabel(self, text='Lucro Esperado:', width=self.size_label[0], height=self.size_label[1])
        self.label_expected_profit.grid(row=3, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        self.__expected_profit()

        # Button
        self.button = base.BaseButton(self, text="Criar Produto", width=self.size_button[0], height=self.size_button[1], command=self.__create_product)
        self.button.grid(row=4, column=0, columnspan=2 , padx=Config.paddings['button'][0], pady=Config.paddings['button'][1])


    def __cost_of_recipe(self, *args) -> None:
            recipe_name = self.option_menu_recipes.get()
            if not recipe_name:
                messagebox.showerror("Erro", "Por favor, selecione uma receita.")
                return

            recipe_id = self.recipes[recipe_name]
            recipe_ingredients = self.recipe_ingredient_controller.select(recipe_id=[recipe_id])
            
            self.total_cost = 0.0

            for recipe_ingredient in recipe_ingredients:
                ingredient = self.ingredient_controller.select(id=[recipe_ingredient.ingredient_id])[0]
                ingredient_cost = (recipe_ingredient.quantity / ingredient.quantity) * ingredient.price
                self.total_cost += ingredient_cost

            if hasattr(self, 'label_cost'):
                 self.label_cost.destroy()

            self.label_cost = base.BaseLabel(self, text=f'R$ {self.total_cost:.2f}', width=self.size_label[0], height=self.size_label[1])
            self.label_cost.grid(row=1, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

            if hasattr(self, 'entry_product_price'):
                self.__expected_profit()

    def __expected_profit(self, *args) -> None:

        if hasattr(self, 'expected_profit'):
            self.expected_profit.destroy()
        
        if self.entry_product_price.get():
            expected_profit = float(self.entry_product_price.get()) - self.total_cost
            self.expected_profit = base.BaseLabel(self, text=f'R$ {expected_profit:.2f}', width=self.size_label[0], height=self.size_label[1])
            self.expected_profit.grid(row=3, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])
        else:
            self.expected_profit = base.BaseLabel(self, text=f'R$ {0:.2f}', width=self.size_label[0], height=self.size_label[1])
            self.expected_profit.grid(row=3, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

    def __create_product(self, *args) -> None:
        
        if len(self.all_recipes) >= 1:
            recipe_id = self.recipes[self.option_menu_recipes.get()]
            product_price = self.entry_product_price.get()
            if product_price:
                self.product_controller.create(recipe_id=recipe_id, price=product_price)
                self.entry_product_price.delete(0, ctk.END)
                self.__expected_profit()
                messagebox.showinfo('Alerta', 'Produto Criado Com Sucesso!')
            else:
                messagebox.showerror('Error', 'Digite o preço do produto!')
        else:
            messagebox.showerror('Error', 'Para criar um produto é necessário possuir uma receita')
        