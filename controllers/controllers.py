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

class RecipeController(BaseController):

    def __init__(self, engine=engine()) -> None:
        super().__init__(engine=engine)
        self.model = Recipe

class RecipeIngredientController(BaseController):

    def __init__(self, engine=engine()) -> None:
        super().__init__(engine=engine)
        self.model = RecipeIngredient

class ProductController(BaseController):

    def __init__(self, engine=engine()) -> None:
        super().__init__(engine=engine)
        self.model = Product

class InvoiceController(BaseController):

    def __init__(self, engine=engine()) -> None:
        super().__init__(engine=engine)
        self.model = Invoice

class ProductInvoiceController(BaseController):

    def __init__(self, engine=engine()) -> None:
        super().__init__(engine=engine)
        self.model = ProductInvoice