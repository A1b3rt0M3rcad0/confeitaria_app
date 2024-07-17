import unittest
from models.models import Unit, Ingredient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Unit

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