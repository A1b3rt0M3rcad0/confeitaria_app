from models.models import Base
from typing import List
from database.engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import select as sqlalchemy_select
from sqlalchemy.exc import IntegrityError, ArgumentError, ProgrammingError

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
                pass
            except ProgrammingError:
                """Quando passamos algo que n pode ser um argumento no sql"""
                pass

    def select(self, **kwargs:List[any]) -> list:

        with Session(self.engine) as s:
            try:
                stmt = sqlalchemy_select(self.model).where(getattr(self.model, list(kwargs.keys())[0]).in_(list(kwargs.values())[0]))
                result = [item for item in s.scalars(stmt)]
                return result
            except ArgumentError:
                """Quando o parametro passado para a func não é uma lista"""
                return []
            except ProgrammingError:
                """Quando passamos algo que n pode ser um argumento no sql"""
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