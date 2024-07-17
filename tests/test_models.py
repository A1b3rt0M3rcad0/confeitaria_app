import unittest
from models.models import Unit, Ingredient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Unit, Recipe, RecipeIngredient, Product, Invoice

class ModelsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Cria um banco de dados em memória para testes
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
    
    @classmethod
    def tearDownClass(cls):
        # Destroi o banco de dados em memória após os testes
        Base.metadata.drop_all(cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    ## Unit Model
    def test_create_unit(self):
        unit = Unit(name='kg')
        self.session.add(unit)
        self.session.commit()

        retrieved_unit = self.session.query(Unit).filter_by(name='kg').one()
        self.assertEqual(retrieved_unit.name, 'kg')
    
    ## Ingredient Model
    def test_create_ingredient(self):
            unit = Unit(name='un')
            self.session.add(unit)
            self.session.commit()

            retrieved_unit = self.session.query(Unit).filter_by(name='un').one()

            ingredient = Ingredient(name='ingredient_test', price=40.00, quantity=10, unit=retrieved_unit)
            self.session.add(ingredient)
            self.session.commit()

            retrieved_ingredient = self.session.query(Ingredient).filter_by(name='ingredient_test').one()
            self.assertEqual(retrieved_ingredient.name, 'ingredient_test')
    
    ## Recipe Model
    def test_create_recipe(self):
        recipe = Recipe(name='recipe')
        self.session.add(recipe)
        self.session.commit()

        retrieved_unit = self.session.query(Recipe).filter_by(name='recipe').one()
        self.assertEqual(retrieved_unit.name, 'recipe')
    
    ## RecipeIngredient Model
    def test_create_recipe_ingredients(self):
        unit = Unit(name='unit_test')
        ingredient = Ingredient(name='ingredient_test_name', price=5.29, quantity=1, unit=unit)
        recipe = Recipe(name='recipe_test')
        recipe_ingredient = RecipeIngredient(recipe=recipe, ingredient=ingredient, quantity=10.5)
        self.session.add_all([unit, ingredient, recipe, recipe_ingredient])
        self.session.commit()
        retrieved_recipe_ingredient = self.session.query(RecipeIngredient).filter_by(recipe=recipe).one()
        self.assertEqual(retrieved_recipe_ingredient.quantity, recipe_ingredient.quantity)
    
    ## Product Model
    def test_create_product(self):

        recipe = Recipe(name='recipe_test_product')
        product = Product(recipe=recipe, price=10)

        self.session.add_all([recipe, product])
        self.session.commit()

        retrieved_product = self.session.query(Product).filter_by(recipe=recipe).one()
        self.assertEqual(retrieved_product.price, product.price)
    
    ## Invoice Model
    def test_create_invoice(self):

        invoice = Invoice(client_name='Alberto', client_phone='numero_celular', total_price=450.52)
        self.session.add_all([invoice])
        self.session.commit()

        retrieved_invoice = self.session.query(Invoice).filter_by(client_name='Alberto').one()

        self.assertEqual(retrieved_invoice.client_name, invoice.client_name)