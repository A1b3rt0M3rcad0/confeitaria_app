from views.widgets import base
from controllers.controllers import IngredientController, RecipeController, RecipeIngredientController
from config.settings import Config
import customtkinter as ctk
from tkinter import messagebox
from utils.utils import only_float_number, not_start_with_space