from views.widgets import base
from controllers.controllers import IngredientController, UnitController
from config.settings import Config
from tkinter import messagebox

class SelectIngredientFrame(base.BaseFrame):


    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.unit_controller = UnitController()
        self.ingredient_controller = IngredientController()

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
        self.ingredients = [(ingredient.name, ingredient.quantity, self.unit_controller.select(id=[ingredient.unit_id])[0].name, ingredient.price) for ingredient in self.ingredient_controller.select_all()]

        # Ingredient List
        self.ingredient_list = base.BaseScrollableFrame(self, label_text='Ingredientes:', width=self.ingredient_list)
        self.ingredient_list.grid(row=2, column=0, rowspan=2, padx=Config.paddings['text'][0], pady=Config.paddings['text'][1])

        self.__update_ingredient_list()


    def __update_ingredient_list(self) -> None:
        # att ingredients
        self.ingredients = [(ingredient.name, ingredient.quantity, self.unit_controller.select(id=[ingredient.unit_id])[0].name, ingredient.price) for ingredient in self.ingredient_controller.select_all()]
        # Clear the current list
        for widget in self.ingredient_list.winfo_children():
            widget.destroy()

        # Display each product in the list
        for index, (name, quantity, unit, price) in enumerate(self.ingredients):
            result_name = name if len(name) <= 10 else f'{name[0:11]}...'
            label_text = f"{index} - {result_name}: {quantity} {unit} - R${price:.2f}"
            product_label = base.BaseLabel(self.ingredient_list, text=label_text, width=self.size_label[0]+220, anchor='w')
            product_label.grid(row=index, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

            delete_button = base.BaseButton(self.ingredient_list, text="X", width=20, height=20, command=lambda idx=index: self.__delete_product(idx))
            delete_button.grid(row=index, column=1, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='e')

    def __delete_product(self, index) -> None:

        self.ingredient_controller.delete(self.ingredient_controller.select(name=[self.ingredients[index][0]])[0])
        messagebox.showinfo('Alerta', f'Ingredient: "{self.ingredients[index][0]}" deletado com sucesso!')
        self.__update_ingredient_list()
    
    def update_ingredient_list(self, *args) -> None:
        self.__update_ingredient_list()
