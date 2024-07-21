import os
from config.settings import Config
from models.models import Base
from database.engine import engine

# Checa se o banco de dados existe, caso não, cria um local
if not os.path.exists(Config.database_path):
    Base.metadata.create_all(engine())



from views import main_view