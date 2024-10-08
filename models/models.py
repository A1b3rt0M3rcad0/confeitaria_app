from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from typing import List
from sqlalchemy import String, Float, Integer, Date, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):

    def __repr__(self):
        primary_key = ', '.join(f"{key}={value!r}" for key, value in self.__dict__.items() if not key.startswith('_'))
        return f"<{self.__class__.__name__}({primary_key})>"
    
    def __str__(self):
        return self.__repr__()


class Unit(Base):

    __tablename__ = 'unit'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name:Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    created_at:Mapped[Date] = mapped_column(Date, default=func.current_date(), nullable=False, onupdate=func.current_date())

    ## Relations
    ingredients:Mapped[List["Ingredient"]] = relationship("Ingredient", back_populates='unit', cascade='all, delete-orphan')

class Ingredient(Base):

    __tablename__ = 'ingredient'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    unit_id:Mapped[int] = mapped_column(ForeignKey("unit.id"), nullable=False)
    name:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price:Mapped[float] = mapped_column(Float, nullable=False)
    quantity:Mapped[int] = mapped_column(Integer, nullable=False)
    created_at:Mapped[Date] = mapped_column(Date, default=func.current_date(), nullable=False, onupdate=func.current_date())

    ## Relations
    unit:Mapped["Unit"] = relationship("Unit", back_populates="ingredients")
    recipe_ingredients:Mapped[List["RecipeIngredient"]] = relationship("RecipeIngredient", back_populates="ingredient", cascade="all, delete-orphan")

class Recipe(Base):

    __tablename__ = 'recipe'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    created_at:Mapped[Date] = mapped_column(Date, default=func.current_date(), nullable=False, onupdate=func.current_date())

    # Relations
    recipe_ingredients:Mapped[List["RecipeIngredient"]] = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")
    products:Mapped[List["Product"]] = relationship("Product", back_populates="recipe", cascade="all, delete-orphan")


class RecipeIngredient(Base):

    __tablename__ = 'recipe_ingredient'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    ingredient_id:Mapped[int] = mapped_column(ForeignKey("ingredient.id", ondelete='CASCADE'), nullable=False)
    recipe_id:Mapped[int] = mapped_column(ForeignKey("recipe.id", ondelete='CASCADE'), nullable=False)
    quantity:Mapped[float] = mapped_column(Float, nullable=False)

    # Relations
    recipe:Mapped["Recipe"] = relationship("Recipe", back_populates="recipe_ingredients")
    ingredient:Mapped["Ingredient"] = relationship("Ingredient", back_populates="recipe_ingredients")

class Product(Base):

    __tablename__ = 'product'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    recipe_id = mapped_column(ForeignKey("recipe.id", ondelete='CASCADE'), unique=True,  nullable=False)
    price:Mapped[float] = mapped_column(Float, nullable=False)
    created_at:Mapped[Date] = mapped_column(Date, default=func.current_date(), nullable=False, onupdate=func.current_date())

    # Relations
    recipe:Mapped["Recipe"] = relationship("Recipe", back_populates="products")
    product_invoices:Mapped[List["ProductInvoice"]] = relationship("ProductInvoice", back_populates="product", cascade="all, delete-orphan")

class Invoice(Base):

    __tablename__ = "invoice"

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    client_name:Mapped[str] = mapped_column(String(50), nullable=False)
    client_phone:Mapped[str] = mapped_column(String(30), nullable=False)
    total_price:Mapped[float] = mapped_column(Float, nullable=False)
    created_at:Mapped[Date] = mapped_column(Date, default=func.current_date(), nullable=False, onupdate=func.current_date())

    # Relations
    product_invoices:Mapped[List["ProductInvoice"]] = relationship("ProductInvoice", back_populates="invoice", cascade="all, delete-orphan")


class ProductInvoice(Base):

    __tablename__ = 'product_invoice'

    id:Mapped[int] = mapped_column(primary_key=True, nullable=False)
    product_id:Mapped[int] = mapped_column(ForeignKey("product.id", ondelete='CASCADE'), nullable=False)
    invoice_id:Mapped[int] = mapped_column(ForeignKey("invoice.id", ondelete='CASCADE'), nullable=False)
    quantity:Mapped[float] = mapped_column(Integer, nullable=False)

    ## Relations
    invoice:Mapped[Invoice] = relationship("Invoice", back_populates="product_invoices")
    product:Mapped[Product] = relationship("Product", back_populates="product_invoices")
