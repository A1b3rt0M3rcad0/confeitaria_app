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
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=False, onupdate=func.now())

    ## Relations
    ingredients:Mapped[List["Ingredient"]] = relationship("Ingredient", back_populates='unit', cascade='all, delete-orphan')

class Ingredient(Base):

    __tablename__ = 'ingredient'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    unit_id:Mapped[int] = mapped_column(ForeignKey("unit.id"), nullable=False)
    name:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price:Mapped[float] = mapped_column(Float, nullable=False)
    quantity:Mapped[int] = mapped_column(Integer, nullable=False)
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=False, onupdate=func.now())

    ## Relations
    unit:Mapped["Unit"] = relationship("Unit", back_populates="ingredients")
    recipe_ingredients:Mapped[List["RecipeIngredient"]] = relationship("RecipeIngredient", back_populates="ingredient", cascade="all, delete-orphan")

class Recipe(Base):

    __tablename__ = 'recipe'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=False, onupdate=func.now())

    # Relations
    recipe_ingredients:Mapped[List["RecipeIngredient"]] = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")
    products:Mapped[List["Product"]] = relationship("Product", back_populates="recipe", cascade="all, delete-orphan")


class RecipeIngredient(Base):

    __tablename__ = 'recipe_ingredient'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    ingredient_id:Mapped[int] = mapped_column(ForeignKey("ingredient.id"), nullable=False)
    recipe_id:Mapped[int] = mapped_column(ForeignKey("recipe.id"), nullable=False)
    quantity:Mapped[float] = mapped_column(Float, nullable=False)

    # Relations
    recipe:Mapped["Recipe"] = relationship("Recipe", back_populates="recipe_ingredients")
    ingredient:Mapped["Ingredient"] = relationship("Ingredient", back_populates="recipe_ingredients")

class Product(Base):

    __tablename__ = 'product'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    recipe_id = mapped_column(ForeignKey("recipe.id"), unique=True,  nullable=False)
    price:Mapped[float] = mapped_column(Float, nullable=False)
    created_at:Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=False, onupdate=func.now())

    # Relations
    recipe:Mapped["Recipe"] = relationship("Recipe", back_populates="products")