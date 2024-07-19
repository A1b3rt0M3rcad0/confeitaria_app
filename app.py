from models.models import Base
from database.engine import engine
from controllers.controllers import UnitController, IngredientController, RecipeController, RecipeIngredientController, ProductController, InvoiceController, ProductInvoiceController

Base.metadata.create_all(engine())

UnitController().select(name=UnitController)