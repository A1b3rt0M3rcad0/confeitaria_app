from models.models import Unit, Ingredient, Invoice, Product, Recipe, RecipeIngredient, ProductInvoice
from database.engine import engine
from controllers.base_controller import BaseController


class UnitController(BaseController):

    def __init__(self, engine=engine()) -> None:
        super().__init__(engine=engine)
        self.model = Unit

class IngredientController(BaseController):

    def __init__(self, engine=engine()) -> None:
        super().__init__(engine=engine)
        self.model = Ingredient