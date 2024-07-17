from sqlalchemy import create_engine
from sqlalchemy import Engine
from ..config.settings import Config


def engine() -> Engine:
    
    return create_engine(Config.database_connection)