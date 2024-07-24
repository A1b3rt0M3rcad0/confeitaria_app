from views.widgets import base
from controllers.controllers import ProductController, InvoiceController, ProductInvoiceController, RecipeController
from config.settings import Config
import customtkinter as ctk
from tkinter import messagebox
from utils.utils import only_float_number, not_start_with_space


class CreateInvoiceFrame(base.BaseFrame):


    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.product_controller = ProductController()
        self.invoice_controller = InvoiceController()
        self.product_invoice_controller = ProductInvoiceController()
        self.recipe_controller = RecipeController()
        validate_float_entry = (self.register(only_float_number), '%P')
        validade_entry_string = (self.register(not_start_with_space), '%S', '%P')

        # widgets sizes
        self.size_label = Config.size_label
        self.size_entry = (Config.size_entry[0]+75, Config.size_entry[1])
        self.size_option_menu = (Config.size_option_menu[0]+75, Config.size_option_menu[1])
        self.size_button = Config.size_button

        # Products
        self.all_products = self.product_controller.select_all()
        __select_recipe = lambda product: self.recipe_controller.select(id=[product.recipe_id])[0]
        self.products = {__select_recipe(product).name: {'id': product.id, 'price': product.price} for product in self.all_products} if len(self.all_products) > 0 else []