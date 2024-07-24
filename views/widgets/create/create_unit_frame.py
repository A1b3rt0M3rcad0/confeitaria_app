from views.widgets import base
from controllers.controllers import UnitController
from config.settings import Config
import customtkinter as ctk
from tkinter import messagebox
from utils.utils import not_start_with_space



class CreateUnitFrame(base.BaseFrame):

    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.unit_controller = UnitController()
        validade_entry_string = (self.register(not_start_with_space), '%S', '%P')

        # widgets sizes
        self.size_label = Config.size_label
        self.size_entry = Config.size_entry
        self.size_option_menu = Config.size_option_menu
        self.size_button = Config.size_button

        # frame sizes
        self.x_frame_size = self.size_label[0] + self.size_entry[0] + Config.paddings['entry'][0]*2 + Config.paddings['message'][0]*2
        self.y_frame_size = self.size_entry[1] + self.size_button[1] + Config.paddings['message'][1]*2 + Config.paddings['button'][1]*2
        self.frame_size = (self.x_frame_size, self.y_frame_size)

        # Entry Namme
        self.label = base.BaseLabel(self, text='Unidade:', width=self.size_label[0], height=self.size_label[1])
        self.label.grid(row=0, column=0, padx=Config.paddings['message'][0], pady=Config.paddings['message'][1])
        
        self.unit_entry = base.BaseEntry(self, placeholder_text='Digite a unidade', validate='key', validatecommand=validade_entry_string, width=self.size_entry[0], height=self.size_entry[1])
        self.unit_entry.grid(row=0, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        # Button
        self.button = base.BaseButton(self, text="Criar Unidade", command=self.__create_unit, width=self.size_button[0], height=self.size_button[1],)
        self.button.grid(row=1, column=0, columnspan=2, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1])    

    def __create_unit(self) -> None:
        unit_entry = self.unit_entry.get().lstrip().capitalize()

        if unit_entry != '':
            # Retira o Espaço Vazio da frente
            if unit_entry.startswith(' '):
                unit_entry = unit_entry.lstrip()
                self.unit_controller.create(name=unit_entry)
                self.unit_entry.delete(0, ctk.END)
                messagebox.showinfo('Alerta', f'Unidade : "{unit_entry}" cadastrada com sucesso!')
            # caso não tenha o valor vazio apenas registra
            else:
                self.unit_controller.create(name=unit_entry)
                self.unit_entry.delete(0, ctk.END)
                messagebox.showinfo('Alerta', f'Unidade : "{unit_entry}" cadastrada com sucesso!')
        # caso a entrada seja vazia
        else:
            messagebox.showinfo('Alerta', f'A unidade não pode conter um valor vazio!')
