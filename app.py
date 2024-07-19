from models.models import Base
from database.engine import engine
from controllers.controllers import UnitController

Base.metadata.create_all(engine())

UnitController().create(name='kg')