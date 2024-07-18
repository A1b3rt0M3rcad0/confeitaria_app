from controllers.controllers import UnitController, IngredientController
from models.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest

class ControllersTestCase(unittest.TestCase):

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
    
    # Unit Controller
    def test_create_select_unit_controller(self):
        unit_name = 'kg'
        UnitController(engine=self.engine).create(name=unit_name)
        r = UnitController(engine=self.engine).select(name=[unit_name])
        self.assertEqual(r[0].name, unit_name)
    
    def test_multi_select_unit_controller(self):
        unit_names = ['ab', 'ac', 'ad']
        for unit_name in unit_names:
            UnitController(engine=self.engine).create(name=unit_name)
        r = UnitController(engine=self.engine).select(name=unit_names)
        for i in range(3):
            self.assertEqual(r[i].name, unit_names[i])
    
    def test_delete_unit_controller(self):
        unit_name = ['af']
        UnitController(engine=self.engine).create(name=unit_name[0])
        r = UnitController(engine=self.engine).select(name=unit_name)
        UnitController(engine = self.engine).delete(r[0])
        t = UnitController(engine=self.engine).select(name=unit_name)
        self.assertEqual(t, [])

    def test_update_unit_controller(self):
        unit_name = ['af']
        UnitController(engine=self.engine).create(name=unit_name[0])
        UnitController(engine=self.engine).update(column_updates={'name':'50'}, name='af')
        t = UnitController(engine=self.engine).select(name=['50'])
        self.assertEqual(t[0].name, '50')
    
    # Ingredient Controller
    def test_create_select_ingredient_controller(self):
        ingredient_name = 'ingredient_test'
        ingredient_price = 5.55
        ingredient_quantity = 2.5
        unit_name = ['kg_teste']
        UnitController(engine=self.engine).create(name=unit_name[0])
        result_unit = UnitController(engine=self.engine).select(name=unit_name)
        id = result_unit[0].id
        IngredientController(engine=self.engine).create(name=ingredient_name, price=ingredient_price, quantity=ingredient_quantity, unit=result_unit[0])
        result_ingredient = IngredientController(engine=self.engine).select(unit_id=[id])
        self.assertEqual(result_ingredient[0].name, ingredient_name)
    
    def test_multi_select_ingredient_controller(self):
        ingredient_name = 'ingredient_test8'
        ingredient_price = 5.55
        ingredient_quantity = 2.5
        unit_controller = UnitController(engine=self.engine)
        ingredient_controller = IngredientController(engine=self.engine)
        unit_name = ['kg009']
        unit_controller.create(name=unit_name[0])
        unit = unit_controller.select(name=unit_name)
        id = unit[0].id
        ingredient_controller.create(unit=unit[0], name=ingredient_name, price=ingredient_price, quantity=ingredient_quantity)
        ingredient = ingredient_controller.select(unit_id=[id], name=[ingredient_name])
        self.assertEqual(ingredient[0].name, ingredient_name)
    
    def test_delete_ingredient_controller(self):
        ingredient_name = 'ingredient_test88'
        ingredient_price = 5.55
        ingredient_quantity = 2.5
        unit_controller = UnitController(engine=self.engine)
        ingredient_controller = IngredientController(engine=self.engine)
        unit_name = ['kg00009']
        unit_controller.create(name=unit_name[0])
        unit = unit_controller.select(name=unit_name)
        id = unit[0].id
        ingredient_controller.create(unit=unit[0], name=ingredient_name, price=ingredient_price, quantity=ingredient_quantity)
        ingredient = ingredient_controller.select(unit_id=[id], name=[ingredient_name])
        ingredient_controller.delete(ingredient[0])
        ingredient = ingredient_controller.select(unit_id=[id], name=[ingredient_name])
        self.assertEqual(ingredient, [])
    
    def test_update_ingredient_controller(self):
        ingredient_name = 'ingredient_t21est8'
        ingredient_price = 5.55
        ingredient_quantity = 2.5
        unit_name = ['kg008009']
        UnitController(engine=self.engine).create(name=unit_name[0])
        r = UnitController(engine=self.engine).select(name=unit_name)
        IngredientController(engine=self.engine).create(name=ingredient_name, price=ingredient_price, quantity=ingredient_quantity, unit=r[0])
        IngredientController(engine=self.engine).update(column_updates={'name':'190'}, name=ingredient_name)
        t = IngredientController(engine=self.engine).select(name=['190'])
        self.assertEqual(t[0].name, '190')

        