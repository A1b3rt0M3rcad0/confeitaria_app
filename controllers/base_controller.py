from models.models import Base
from config.logger import init_logger
from typing import List
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from sqlalchemy import select as sqlalchemy_select
from sqlalchemy.exc import IntegrityError, ArgumentError, ProgrammingError
from sqlalchemy.orm.exc import UnmappedInstanceError

logger = init_logger()

class BaseController:

    def __init__(self, engine:Engine) -> None:
        self.engine = engine

    def create(self, **kwargs) -> None:
        with Session(self.engine) as s:
            try: 
                s.add_all([self.model(**kwargs)])
                s.commit()
                logger.info(f"{self} - {kwargs} registry created")
            except IntegrityError:
                """Quando o registro ja existe"""
                logger.info(f"{self} - {kwargs} registry already exists")
            except ProgrammingError:
                """Quando passamos algo que n pode ser um argumento no sql"""
                logger.error(f"{self} - {kwargs} incompatible argument")

    def select(self, **kwargs:List[any]) -> list:

        with Session(self.engine) as s:
            try:
                stmt = sqlalchemy_select(self.model).where(getattr(self.model, list(kwargs.keys())[0]).in_(list(kwargs.values())[0]))
                result = [item for item in s.scalars(stmt)]
                logger.info(f"{self} - {kwargs} registry found")
                return result
            except ArgumentError:
                """Quando o parametro passado para a func não é uma lista"""
                logger.error(f"{self} - {kwargs} passed argument is not an argument list")
                return []
            except ProgrammingError:
                """Quando passamos algo que n pode ser um argumento no sql"""
                logger.error(f"{self} - {kwargs} incompatible argument")
                return []
    
    def delete(self, register:Base) -> None:

        try:
            with Session(self.engine) as s:
                s.delete(register)
                s.commit()
                logger.info(f"{self} - {register} registry deleted")
        except UnmappedInstanceError:
            """Quando a instancia passada não é do tipo Filho de Base"""
            logger.error(f"{self} - ({register}) passed argument is not a model")
    
    def update(self, column_updates: dict, **kwargs) -> None:

        with Session(self.engine) as s:
            try:
                # 1. Busca todos os registros que correspondem aos critérios fornecidos em **kwargs
                registers = s.query(self.model).filter_by(**kwargs).all()
                # 2. Para cada registro encontrado, atualiza as colunas especificadas em column_updates
                for register in registers:
                    for key, value in column_updates.items():
                        setattr(register, key, value)
                # 3. Realiza o commit das alterações no banco de dados
                s.commit()
                logger.info(f"{self} - {registers} registry(is) updated")
            except ProgrammingError:
                """Quando passamos algo que n pode ser um argumento no sql"""
                logger.error(f"{self} - {kwargs} incompatible argument")