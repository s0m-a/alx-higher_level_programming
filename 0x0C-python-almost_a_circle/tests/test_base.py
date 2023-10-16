#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

'''
    Creating test cases for the base module
'''


class test_base(unittest.TestCase):
    '''
     Unittests for testing of the Base class
    '''
    def test_id_none(self):
        '''
           No id
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id_zero(self):
        '''
            id =  0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_norm(self):
        '''
            With id
        '''
        b = Base(10)
        self.assertEqual(10, b.id)

    def test_id_list(self):
        '''
            list id
        '''
        b = Base([2, 4, 6])
        self.assertEqual([2, 4, 6], b.id)

    def test_id_negative(self):
        '''
           Negative id
        '''
        b = Base(-15)
        self.assertEqual(-15, b.id)

    def test_id_tup(self):
        '''
           tuple id
        '''
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_id_str(self):
        '''
           string id
        '''
        b = Base("john")
        self.assertEqual("john", b.id)

    def test_id_dic(self):
        '''
          dict id
        '''
        b = Base({"id": 35})
        self.assertEqual({"id": 35}, b.id)

    def test_to_json_type(self):
        '''
          json string
        '''
        s = Square(6)
        json_d = s.to_dictionary()
        json_s = Base.to_json_string([json_d])
        self.assertEqual(type(json_s), str)

        
    def test_to_json_Empty(self):
        '''
           more json string
        '''
        sq = Square(2, 0, 0, 49)
        json_d = sq.to_dictionary()
        json_s = Base.to_json_string([])
        self.assertEqual(json_s, "[]")


    def test_to_json_value(self):
        '''
            another json string
        '''
        sq = Square(2, 0, 0, 49)
        json_d = sq.to_dictionary()
        json_s = Base.to_json_string([json_d])
        self.assertEqual(json.loads(json_s),
                         [{"id": 49, "y": 0, "size": 2, "x": 0}])

    def test_to_json_None(self):
        '''
            more json string
        '''
        sq = Square(2, 0, 0, 49)
        json_d = sq.to_dictionary()
        json_s = Base.to_json_string(None)
        self.assertEqual(json_s, "[]")


class TestSquare(unittest.TestCase):
    """
    
    Test for  Base class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for test
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)
       
    def test_class_docstr(self):
        """
        Tests to see if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_module_docstr(self):
        """
        Tests to see if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)



    def test_func_docstr(self):
        """
        Tests to see if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
