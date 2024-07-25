from views.widgets import base
from controllers.controllers import ProductController, InvoiceController, ProductInvoiceController, RecipeController
from config.settings import Config
import customtkinter as ctk
from tkinter import messagebox
from utils.utils import only_float_number, not_start_with_space, only_int_number


class CreateInvoiceFrame(base.BaseFrame):


    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.product_controller = ProductController()
        self.invoice_controller = InvoiceController()
        self.product_invoice_controller = ProductInvoiceController()
        self.recipe_controller = RecipeController()
        validate_float_entry = (self.register(only_float_number), '%P')
        validate_entry_string = (self.register(not_start_with_space), '%S', '%P')
        validate_entry_int = (self.register(only_int_number), '%S', '%P')

        # widgets sizes
        self.size_label = Config.size_label
        self.size_entry = (Config.size_entry[0]+75, Config.size_entry[1])
        self.size_option_menu = (Config.size_option_menu[0]+75, Config.size_option_menu[1])
        self.size_button = Config.size_button
        self.ingredient_list = Config.width_ingredient_list

        # frame sizes
        self.x_frame_size = self.size_label[0] + self.size_entry[0] + Config.paddings['entry'][0]*4
        self.y_frame_size = self.size_label[1]*2 + self.size_entry[1]*2 + self.size_button[1] + Config.paddings['entry'][1]*8 + Config.paddings['button'][1]*2
        self.frame_size = (self.x_frame_size, self.y_frame_size)

        # Added Products
        self.added_products = []

        # Products
        self.all_products = self.product_controller.select_all()
        __select_recipe = lambda product: self.recipe_controller.select(id=[product.recipe_id])[0]
        self.products = {__select_recipe(product).name: {'id': product.id, 'price': product.price} for product in self.all_products} if len(self.all_products) > 0 else {'Vazio': {'id': None, 'price': 0}}

        # Client Name
        self.label_client_name = base.BaseLabel(self, text='Nome:', width=self.size_label[0], height=self.size_label[1])
        self.label_client_name.grid(row=0, column=0, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1], sticky='w')

        self.entry_client_name = base.BaseEntry(self, placeholder_text='Digite o nome do cliente...', width=self.size_entry[0], height=self.size_entry[1], validate='key', validatecommand=validate_entry_string)
        self.entry_client_name.grid(row=0, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='e')

        # Client Phone
        self.label_client_phone = base.BaseLabel(self, text='Telefone:', width=self.size_label[0], height=self.size_label[1])
        self.label_client_phone.grid(row=1, column=0, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1], sticky='w')

        self.entry_client_phone = base.BaseEntry(self, placeholder_text='Digite o telefone do cliente...', width=self.size_entry[0], height=self.size_entry[1], validate='key', validatecommand=validate_entry_string)
        self.entry_client_phone.grid(row=1, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='e')

        # Product List
        self.invoice_products = base.BaseScrollableFrame(self, label_text='Produtos:', width=self.ingredient_list)
        self.invoice_products.grid(row=2, column=0, rowspan=2, padx=Config.paddings['text'][0], pady=Config.paddings['text'][1])

        # Products
        self.option_menu_products = base.BaseOptionMenu(self, values = list(self.products.keys()), width=self.size_option_menu[0], height=self.size_option_menu[1], dynamic_resizing=False, command=self.__cost_of_product)
        self.option_menu_products.grid(row=0, column=2, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        # Products Quantity
        self.label_product_quantity = base.BaseLabel(self, text='Quantidade:', width=self.size_option_menu[0]/2, height=self.size_option_menu[1])
        self.label_product_quantity.grid(row=1, column=2, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

        self.product_quantity = base.BaseEntry(self, placeholder_text='1234', width=self.size_option_menu[0]/2, height=self.size_option_menu[1], validate='key', validatecommand=validate_entry_int)
        self.product_quantity.grid(row=1, column=2, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='e')
        
        # Products Price
        self.label_product_price = base.BaseLabel(self, text='Preço:', width=self.size_label[0], height=self.size_label[1], anchor='nw')
        self.label_product_price.grid(row=2, column=2, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1], sticky='nw')

        self.__cost_of_product()

        # Button Add Product
        self.button_add_product = base.BaseButton(self, text="Adicionar Produto", width=self.size_option_menu[0], height=self.size_option_menu[1], command=self.__add_product)
        self.button_add_product.grid(row=2, column=2, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1])

        # Products Total Price

        self.__label_products_total_cost()

        # Button Create Invoice
        self.button_add_product = base.BaseButton(self, text="Criar Fatura", width=self.size_option_menu[0], height=self.size_option_menu[1])
        self.button_add_product.grid(row=3, column=2, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='nw')

        # Button Create and Print Invoice
        self.button_add_product = base.BaseButton(self, text="Criar/Imprimir Fatura", width=self.size_option_menu[0], height=self.size_option_menu[1])
        self.button_add_product.grid(row=3, column=2, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='w')



    def __cost_of_product(self, *args) -> None:
        
        if hasattr(self, 'label_product_price_info'):
            self.label_product_price_info.destroy()

        product_price = self.products[self.option_menu_products.get()]['price']
        self.label_product_price_info = base.BaseLabel(self, text=f'R$ {product_price:.2f}', width=self.size_label[0], height=self.size_label[1], anchor='n')
        self.label_product_price_info.grid(row=2, column=2, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1], sticky='n')

    def __label_products_total_cost(self, *args) -> None:
        if hasattr(self, 'label_product_total_cost_info'):
            self.label_product_total_cost_info.destroy()
        if not hasattr(self, 'total_cost'):
            self.total_cost = 0.0
        self.label_product_total_cost_info = base.BaseLabel(self, text=f'Total: R${self.total_cost:.2f}', width=self.size_label[0], height=self.size_label[1], anchor='s')
        self.label_product_total_cost_info.grid(row=2, column=2, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1], sticky='s')

    def __add_product(self, *args) -> None:
        product_name = self.option_menu_products.get()
        product = self.products[product_name]
        product_quantity = self.product_quantity.get()

        if not product_quantity:
            messagebox.showerror("Erro", "Por favor, insira a quantidade do produto.")
            return

        # Calculate the cost for the added product
        cost = float(product_quantity) * product['price']

        # Add product to the list
        self.added_products.append((product_name, product_quantity, cost))

        # Update total cost
        self.total_cost += cost

        # Clear the quantity entry field
        self.product_quantity.delete(0, ctk.END)

        # Update the product list display and total cost label
        self.__update_product_list()
        self.__update_total_cost_label()

    def __update_product_list(self) -> None:
        # Clear the current list
        for widget in self.invoice_products.winfo_children():
            widget.destroy()

        # Display each product in the list
        for index, (name, quantity, cost) in enumerate(self.added_products):
            result_name = name if len(name) <= 10 else f'{name[0:11]}...'
            label_text = f"{result_name}: {quantity} - R${cost:.2f}"
            product_label = base.BaseLabel(self.invoice_products, text=label_text, width=self.size_label[0]+220, anchor='w')
            product_label.grid(row=index, column=0, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1], sticky='w')

            delete_button = base.BaseButton(self.invoice_products, text="X", width=20, height=20, command=lambda idx=index: self.__delete_product(idx))
            delete_button.grid(row=index, column=1, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1], sticky='e')

    def __update_total_cost_label(self) -> None:
        if hasattr(self, 'label_product_total_cost_info'):
            self.label_product_total_cost_info.destroy()
        self.__label_products_total_cost()

    def __delete_product(self, index) -> None:
        # Remove the product cost from total cost
        self.total_cost -= self.added_products[index][2]

        # Remove the product from the list
        del self.added_products[index]

        # Update the product list display and total cost label
        self.__update_product_list()
        self.__update_total_cost_label()

    def __delete_all_infos(self) -> None:
        # Reset Products and Cost
        self.added_products = []
        self.total_cost = 0
        # Reset Widgets
        self.__update_product_list()
        self.__update_total_cost_label()
        # Resets Entries
        self.product_quantity.delete(0, ctk.END)
        self.entry_client_name.delete(0, ctk.END)
        self.entry_client_phone.delete(0, ctk.END)