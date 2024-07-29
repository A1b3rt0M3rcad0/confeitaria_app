from views.widgets import base
from controllers.controllers import RecipeController, IngredientController, RecipeIngredientController, ProductController
from views.widgets.create.create_product_frame import CreateProductFrame
from config.settings import Config
from tkinter import messagebox

class SelectProductFrame(base.BaseFrame):


    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.recipe_controller = RecipeController()
        self.ingredient_controller = IngredientController()
        self.recipe_ingredient_controller = RecipeIngredientController()
        self.product_controller = ProductController()

        # widgets sizes
        self.size_label = Config.size_label
        self.size_entry = (Config.size_entry[0]+75, Config.size_entry[1])
        self.size_option_menu = (Config.size_option_menu[0]+75, Config.size_option_menu[1])
        self.size_button = Config.size_button
        self.product_list_width = CreateProductFrame().frame_size[0] + 150

        # frame sizes
        self.x_frame_size = self.product_list_width + Config.paddings['text'][0] * 4
        self.y_frame_size = 275
        self.frame_size = (self.x_frame_size, self.y_frame_size)
    
        # Products
        self.__products()

        # Product List
        self.product_list = base.BaseScrollableFrame(self, label_text='Produtos:', width=self.product_list_width)
        self.product_list.grid(row=2, column=0, rowspan=2, padx=Config.paddings['text'][0], pady=Config.paddings['text'][1])

        self.__update_product_list()
    

    def __products(self) -> None:
        self.products = [(self.recipe_controller.select(id=[product.recipe_id])[0].name, product.price) for product in self.product_controller.select_all()]
    
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

    def __update_product_list(self) -> None:
        # att products
        self.__products()
        self.__recipe_cost()
        # Clear the current list
        for widget in self.product_list.winfo_children():
            widget.destroy()

        # Display each products in the list
        for index, (name, price) in enumerate(self.products):
            result_name = name if len(name) <= 20 else f'{name[0:21]}...'
            label_text = f"{index} - {result_name}- Receita: {price - self.recipe_cost[name]:.2f} - Preço: R${price:.2f} "
            recipe_label = base.BaseLabel(self.product_list, text=label_text, width=self.size_label[0]+400, anchor='w')
            recipe_label.grid(row=index, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

            delete_button = base.BaseButton(self.product_list, text="X", width=20, height=20, command=lambda idx=index: self.__delete_product(idx))
            delete_button.grid(row=index, column=1, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='e')
    
    def __delete_product(self, index:int) -> None:
        recipe = self.recipe_controller.select(name=[self.products[index][0]])[0]
        product = self.product_controller.select(recipe_id=[recipe.id])[0]
        self.product_controller.delete(product)
        messagebox.showinfo('Alerta', f'Produto: "{recipe.name}" deletado com sucesso!')
        self.__update_product_list()
    
    def update_product_list(self, *args) -> None:
        self.__update_product_list()