from views.frames import base
from controllers.controllers import UnitController
from config.settings import Config
import customtkinter as ctk
import tkinter as tk



class CreateUnitFrame(base.BaseFrame):

    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.unit_controller = UnitController()

        self.label = base.BaseLabel(self, text='Unidade:')
        self.label.grid(row=0, column=0, padx=Config.paddings['text'][0], pady=Config.paddings['text'][1])
        
        self.unit_entry = base.BaseEntry(self, placeholder_text='Digite a unidade', width=150)
        self.unit_entry.grid(row=0, column=1, padx=Config.paddings['entry'][0], pady=Config.paddings['entry'][1])

        self.button = base.BaseButton(self, text="Criar Unidade", width=0, command=self.__create_unit)
        self.button.grid(row=1, column=0, columnspan=2, padx=Config.paddings['button'][0], pady=Config.paddings['button'][1])    

    def __create_unit(self) -> None:
        unit_entry = self.unit_entry.get()

        # Retira o Espaço Vazio da frente
        if unit_entry.startswith(' '):
            unit_entry = unit_entry.lstrip()
            self.unit_controller.create(name=unit_entry)
            self.unit_entry.delete(0, ctk.END)
        else:
            self.unit_controller.create(name=unit_entry)
            self.unit_entry.delete(0, ctk.END)
