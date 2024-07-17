from models.models import Base
from database.engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import select as sqlalchemy_select

class BaseController:

    def __init__(self, engine=engine) -> None:
        self.engine = engine

    def create(self, **kwargs) -> None:
        with Session(self.engine) as s: 
            s.add_all([self.model(**kwargs)])
            s.commit()

    def select(self, **kwargs) -> list:

        with Session(self.engine) as s:
            stmt = sqlalchemy_select(self.model).where(getattr(self.model, list(kwargs.keys())[0]).in_(list(kwargs.values())[0]))
            result = [item for item in s.scalars(stmt)]
        
        return result
    
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