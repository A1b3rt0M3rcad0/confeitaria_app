from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from typing import List
from sqlalchemy import String, Float, Integer, DateTime, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Unit(Base):

    __tablename__ = 'unit'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name:Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=False)

    ## Relations
    ingredients:Mapped[List["Ingredient"]] = relationship("Ingredient", back_populates='unit', cascade='all, delete-orphan')

class Ingredient(Base):

    __tablename__ = 'ingredient'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    unit_id:Mapped[int] = mapped_column(ForeignKey("unit.id"), nullable=False)
    name:Mapped[str] = mapped_column(String(50), nullable=False)
    price:Mapped[float] = mapped_column(Float, nullable=False)
    quantity:Mapped[int] = mapped_column(Integer, nullable=False)
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=False)

    ## Relations
    unit:Mapped["Unit"] = relationship("Unit", back_populates="ingredients")
