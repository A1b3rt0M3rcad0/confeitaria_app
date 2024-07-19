import logging
from config.settings import Config
from models.models import Base
from typing import List
from database.engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import select as sqlalchemy_select
from sqlalchemy.exc import IntegrityError, ArgumentError, ProgrammingError

# logger
logger = logging.getLogger(**Config.logger)
logger.setLevel(logging.DEBUG)  # Definindo o nível de log

# Criando um manipulador para escrever logs em um arquivo
file_handler = logging.FileHandler('app.log')

# Criando um manipulador para exibir logs no console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Todos os logs serão exibidos no console

# Criando um formatador e adicionando-o aos manipuladores
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adicionando os manipuladores ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class BaseController:

    def __init__(self, engine=engine) -> None:
        self.engine = engine

    def create(self, **kwargs) -> None:
        with Session(self.engine) as s:
            try: 
                s.add_all([self.model(**kwargs)])
                s.commit()
            except IntegrityError:
                """Quando o registro ja existe"""
                logger.info(f"{self} registry already exists")
            except ProgrammingError:
                """Quando passamos algo que n pode ser um argumento no sql"""
                logger.error(f"{self} incompatible argument")
                pass

    def select(self, **kwargs:List[any]) -> list:

        with Session(self.engine) as s:
            try:
                stmt = sqlalchemy_select(self.model).where(getattr(self.model, list(kwargs.keys())[0]).in_(list(kwargs.values())[0]))
                result = [item for item in s.scalars(stmt)]
                return result
            except ArgumentError:
                """Quando o parametro passado para a func não é uma lista"""
                logger.error(f"{self} passed argument is not an argument list")
                return []
            except ProgrammingError:
                """Quando passamos algo que n pode ser um argumento no sql"""
                logger.error(f"{self} incompatible argument")
                return []
    
    def delete(self, register:Base) -> None:

        with Session(self.engine) as s:
            s.delete(register)
            s.commit()
    
    def update(self, column_updates: dict, **kwargs) -> None:

        with Session(self.engine) as s:
            # 1. Busca todos os registros que correspondem aos critérios fornecidos em **kwargs
            registers = s.query(self.model).filter_by(**kwargs).all()
            # 2. Para cada registro encontrado, atualiza as colunas especificadas em column_updates
            for register in registers:
                for key, value in column_updates.items():
                    setattr(register, key, value)
            # 3. Realiza o commit das alterações no banco de dados
            s.commit()