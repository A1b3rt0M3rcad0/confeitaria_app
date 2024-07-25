import customtkinter as ctk
import tkinter as tk
from config.settings import Config


class BaseFrame(ctk.CTkFrame):
    
    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.config = {
            'fg_color': Config.colors['base']
        }
        self.configure(**self.config)

class BaseButton(ctk.CTkButton):

    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.config = {
            'fg_color': Config.colors['hover'],
            'text_color': Config.colors['base'],
            'hover_color': Config.colors['emphasis'],
            'font': (Config.font, Config.font_sizes['button'])   
        }
        self.configure(**self.config)

class BaseEntry(ctk.CTkEntry):

    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.config = {
            'fg_color': Config.colors['main'], 
            'text_color': Config.colors['emphasis'],
            'placeholder_text_color': Config.colors['emphasis'], 
            'font': (Config.font, Config.font_sizes['entry'])
        }
        self.configure(**self.config)

class BaseLabel(ctk.CTkLabel):

    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.config = {
            'fg_color': Config.colors['base'], 
            'text_color': Config.colors['emphasis'], 
            'font': (Config.font, Config.font_sizes['entry'])
        }
        self.configure(**self.config)

class BaseOptionMenu(ctk.CTkOptionMenu):

    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.config = {
            'fg_color': Config.colors['hover'], 
            'text_color': Config.colors['base'], 
            'button_color': Config.colors['hover'],
            'button_hover_color': Config.colors['emphasis'],
            'dropdown_hover_color': Config.colors['emphasis'], 
            'dropdown_fg_color': Config.colors['hover'], 
            'font': (Config.font, Config.font_sizes['entry']), 
            'dropdown_font': (Config.font, Config.font_sizes['entry']) 
        }
        self.configure(**self.config)

class BaseScrollableFrame(ctk.CTkScrollableFrame):

    def __init__(self, master=None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.config = {
            'fg_color': Config.colors['main'],
            'label_text_color': Config.colors['base'],
            'scrollbar_button_color': Config.colors['hover'], 
            'scrollbar_button_hover_color': Config.colors['emphasis'], 
            'label_fg_color':Config.colors['hover'],
            'border_width': 1,
            'border_color': Config.colors['hover']
        }
        self.configure(**self.config)