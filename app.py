import os
from config.settings import Config
from models.models import Base
from database.engine import engine
from controllers.controllers import UnitController

# Checa se o banco de dados existe, caso não, cria um local
if not os.path.exists(Config.database_path):
    Base.metadata.create_all(engine())
    __units = ["Kg(s)", 'Litro(s)', 'Grama(s)', 'Unidade(s)', 'Mililitro(s)']
    for __unit in __units:
        UnitController().create(name=__unit)



from views import main_view