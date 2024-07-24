from views.widgets import base
from controllers.controllers import IngredientController, UnitController
from config.settings import Config
import customtkinter as ctk
from tkinter import messagebox
from utils.utils import only_float_number, not_start_with_space


class CreateIngredientFrame(base.BaseFrame):


    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.unit_controller = UnitController()
        self.ingredient_controller = IngredientController()
        validate_float_entry = (self.register(only_float_number), '%P')
        validade_entry_string = (self.register(not_start_with_space), '%S', '%P')

        # widgets sizes
        self.size_label = Config.size_label
        self.size_entry = Config.size_entry
        self.size_option_menu = Config.size_option_menu
        self.size_button = Config.size_button

        # frame sizes
        self.x_frame_size = self.size_label[0] + self.size_entry[0] + self.size_option_menu[0] + Config.paddings['entry'][0]*4 + Config.paddings['message'][0]*2
        self.y_frame_size = self.size_entry[1]*3 + self.size_button[1] + Config.paddings['entry'][1]*6 + Config.paddings['button'][1]*2
        self.frame_size = (self.x_frame_size, self.y_frame_size)

        # Name Entry
        self.label_name = base.BaseLabel(self, text='Nome:', width=self.size_label[0], height=self.size_label[1])
        self.label_name.grid(row=1, column=0, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1])

        self.entry_name = base.BaseEntry(self, placeholder_text='Digite o nome', validate='key', validatecommand=validade_entry_string, width=self.size_entry[0], height=self.size_entry[1])
        self.entry_name.grid(row=1, column=1, columnspan=2, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        # Price Entry
        self.name_label = base.BaseLabel(self, text='Preço:', width=self.size_label[0], height=self.size_label[1])
        self.name_label.grid(row=2, column=0, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1])

        self.entry_price = base.BaseEntry(self, placeholder_text=99.99, validate='key', validatecommand=validate_float_entry, width=self.size_entry[0], height=self.size_entry[1])
        self.entry_price.grid(row=2, column=1, columnspan=2, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        # Quantity Entry
        self.label_quantity = base.BaseLabel(self, text='Quantidade:', width=self.size_label[0], height=self.size_label[1])
        self.label_quantity.grid(row=3, column=0, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1])

        self.entry_quantity = base.BaseEntry(self, placeholder_text=99.99, validate='key', validatecommand=validate_float_entry, width=self.size_entry[0], height=self.size_entry[1])
        self.entry_quantity.grid(row=3, column=1, columnspan=2 , padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        # Unit Select
        self.units = self.unit_controller.select_all()
        self.units = {unit.name: unit for unit in self.units} if len(self.units) != 0 else []

        self.option_menu_units = base.BaseOptionMenu(self, values = list(self.units.keys()), width=self.size_option_menu[0], height=self.size_option_menu[1])
        self.option_menu_units.grid(row=3, column=3, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        # Button
        self.button = base.BaseButton(self, text="Cadastrar", command=self.__create_ingredient, width=self.size_button[0], height=self.size_button[1])
        self.button.grid(row=4, column=1, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1])


    def __create_ingredient(self) -> None:
         
        # Cria novamente as unidades
        self.units = self.unit_controller.select_all()
        self.units = {unit.name: unit for unit in self.units} if len(self.units) != 0 else []

        # Entrys
        entry_name = self.entry_name.get().lstrip().capitalize()
        entry_price = self.entry_price.get()
        entry_quantity = self.entry_quantity.get()
        entry_unit = self.option_menu_units.get()

        if len(entry_name) <= 1:
            messagebox.showinfo('Alerta', 'Digite o nome do ingrediente!')
            return None

        if len(entry_price) <= 0:
            messagebox.showinfo('Alerta', 'Digite o preço!')
            return None
    
        if len(entry_quantity) <= 0:
            messagebox.showinfo('Alerta', 'Digite a quantidade!')
            return None
        
        self.ingredient_controller.create(name=entry_name, price=entry_price, quantity=entry_quantity, unit=self.units[entry_unit])
        self.entry_price.delete(0, ctk.END)
        self.entry_quantity.delete(0, ctk.END)
        self.entry_name.delete(0, ctk.END)
        messagebox.showinfo('Alerta', f'O ingrediente {entry_name} criado com sucesso!')

