#!/usr/bin/python3
from contextlib import redirect_stdout
import contextlib
import io
import os
import sys
import json
import inspect
import unittest
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



'''
   Tests for the square module
'''


class test_square_c(unittest.TestCase):
    '''
        Tests square
    '''

    def setUp(self):
        '''
           Creating an instance with width and height parameters.
        '''
        self.s = Square(4)

    def tearDown(self):
        '''
            Deletes instance
        '''
        try:
            os.remove("Square.json")
        except:
            pass
        del self.s

    def test_width_g(self):
        '''
            Tests the width getter
        '''
        self.assertEqual(4, self.s.width)

    def test_height_g(self):
        '''
            Tests height getter
        '''
        self.assertEqual(4, self.s.height)
    
    def test_x_p(self):
        '''
            Tests square x getter and setter
        '''

        self.s.x = 46
        self.assertEqual(46, self.s.x)
        self.assertEqual(0, self.s.y)


    def test_width_str(self):
        '''
            Tests for non int
        '''
        with self.assertRaises(TypeError):
            sq = Square("1")
   


    def test_y_p(self):
        '''
            Tests y getter and setter
        '''

        self.s.y = 46
        self.assertEqual(46, self.s.y)
        self.assertEqual(0, self.s.x)

    def test_asquare_id_s(self):
        '''
            Tests id for square
        '''
        squ = Square(4, 0, 0, 99)
        self.assertEqual(99, sq.id)


    def test_width_bool_b(self):
        '''
            Tests for non int
        '''
        with self.assertRaises(TypeError):
            squ = Square(True)

    def test_width_list_s(self):
        '''
             Tests for non int
        '''
        with self.assertRaises(TypeError):
            squ = Square([10, 6])

    def test_x_string_s(self):
        '''
             Tests for non int
        '''
        with self.assertRaises(TypeError):
            squ = Square(1, "66")

    def test_x_bool(self):
        '''
             Tests for non int
        '''
        with self.assertRaises(TypeError):
            squ = Square(3, True)

    def test_x_list_s(self):
        '''
            Tests for non int
        '''
        with self.assertRaises(TypeError):
            squ = Square(1, [10, 6])

    def test_y_ne(self):
        '''
            Tests with negative int
        '''
        with self.assertRaises(ValueError):
            squ = Square(8, 4, -6)

    def test_y_s(self):
        '''
             Tests for non int
        '''
        with self.assertRaises(TypeError):
            squ = Square(1, 7, "46")

    def test_y_b(self):
        '''
             Tests for non int
        '''
        with self.assertRaises(TypeError):
            squ = Square(1, 7, True)

    def test_y_l(self):
        '''
             Tests for non int
        '''
        with self.assertRaises(TypeError):
            squ = Square(4, 6, [20, 12])

    def test_width_ne(self):
        '''
            Tests with negative int
        '''
        with self.assertRaises(ValueError):
            squ = Square(-6)

    def test_x_ne(self):
        '''
            Tests with negative int
        '''
        with self.assertRaises(ValueError):
            squ = Square(8, -9)


    def test_width_z(self):
        '''
            Tests with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(0, 10)

    def test_width_f(self):
        '''
            Tests not an int
        '''
        with self.assertRaises(TypeError):
            sq = Square(3.07, 6)

    def test_x_fl(self):
        '''
            Tests not an int
        '''
        with self.assertRaises(TypeError):
            sq = Square(5, 1.07)

    def test_y_float(self):
        '''
             Tests not an int
        '''
        with self.assertRaises(TypeError):
            squ = Square(5, 8, 1.07)

    def test_area(self):
        '''
            Tests area of the square
        '''
        self.assertEqual(self.s.area(), 6 * 6)
        sq = Square(4, 6, 6, 8)
        self.assertEqual(sq.area(), 3 * 3)

    def test_str_overload(self):
        s = Square(7, 6, 5, 99)
        self.assertEqual(s.__str__(), "[Square] (99) 7/6 - 5")

    def test_update_id(self):
        '''
            Tests update method
        '''
        self.s.update(64)
        self.assertEqual(64, self.s.id)

    def test_updt_width(self):
        '''
            Teststhe update method
        '''
        self.s.update(54, 30)
        self.assertEqual(5, self.s.width)

    def test_updt_height(self):
        '''
            Tests the update method
        '''
        self.s.update(54, 10)
        self.assertEqual(5, self.s.height)

    def test_updt_x(self):
        '''
            Tests the update method
        '''
        self.s.update(64, 60, 20)
        self.assertEqual(20, self.s.x)

    def test_updt_y(self):
        '''
            Tests the update method
        '''
        self.s.update(44, 20, 3, 1)
        self.assertEqual(1, self.s.y)

    def test_updt_dict(self):
        '''
            Tests the update method with **kwargs
        '''
        self.s.update(y=1, size=2, x=3, id=89)
        self.assertEqual(1, self.s.y)
        self.assertEqual(2, self.s.size)
        self.assertEqual(3, self.s.x)
        self.assertEqual(89, self.s.id)

    def test_update_dict_list(self):
        '''
            Tests the update method with  *args and **kwargs
        '''
        self.s.update(1000, y=1, width=2, x=3, id=89)
        self.assertEqual(1000, self.s.id)

    def test_updt_dict_nkey(self):
        '''
            Tests the update method with **kwargs
        '''
        self.s.update(y=1, size=2, xox=3, id=89)

    def test_update_string(self):
        '''
            Testing the update method with **kwargs
        '''
        # self.assertEqual(self.s.id, "str")
        with self.assertRaises(TypeError):
           self.s.update("str") 

    def test_to_dict(self):
        '''
            Testing the type that is returned from the to_dictionary method
        '''
        r1 = Square(5)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dict_print(self):
        '''
            Testing the dict that will be printed
        '''
        r1 = Square(5, 0, 0, 410)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict,
                         {'size': 5, 'id': 410, 'x': 0, 'y': 0})

    def test_missing_height(self):

        with self.assertRaises(TypeError):
            Square()

    def test_saving_to_file(self):

        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file([r1])

        with open("Square.json", "r") as file:
            content = file.read()
        t = [{"id": 346, "x": 0, "size": 5, "y": 0}]
        self.assertEqual(t, json.loads(content))

    def test_saving_to_file_no_iter(self):

        with self.assertRaises(TypeError):
            Square.save_to_file(self.s)

    def test_saving_to_file_None(self):

        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual("[]", content)

    def test_saving_to_file_type(self):

        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file([r1])

        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual(str, type(content))
        try:
            os.remove("Square.json")
        except:
            pass

    def test_json_string_type(self):

            list_input = [
                {'id': 2089, 'size': 10},
                {'id': 2712, 'size': 1}]
            json_list_input = Square.to_json_string(list_input)
            list_output = Square.from_json_string(json_list_input)
            self.assertEqual(type(list_input), list)

    def test_json_string(self):

            list_input = [
                {'id': 2089, 'size': 10},
                {'id': 2712, 'size': 7}]
            json_list_input = Square.to_json_string(list_input)
            list_output = Square.from_json_string(json_list_input)
            s1 = {'id': 2089, 'size': 10}
            s2 = {'size': 7, 'id': 2712}
            self.assertEqual(list_input[0], s1)
            self.assertEqual(list_input[1], s2)

    def test_dict_to_instance(self):

        r1 = Square(5)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_isnot_dict_to_instance(self):

        r1 = Square(109)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_load_from_file_not_the_same(self):

        r1 = Square(10)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertNotEqual(id(r1), id(list_squares_output[0]))

    def test_load_from_file_same_width(self):

        r1 = Square(10)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(r1.width, list_squares_output[0].size)

    def test_load_from_file_same_height(self):

        r1 = Square(10)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(r1.size, list_squares_output[0].size)

    def test_load_from_file_same_x(self):

        r1 = Square(10, 2, 8)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(r1.x, list_squares_output[0].x)

    def test_load_from_file_same_y(self):

        r1 = Square(10, 2, 8)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(r1.y, list_squares_output[0].y)

    def test_display_square(self):

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10)
        r1.display()
        sys.stdout = sys.__stdout__

        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(1)
        r1.display()
        sys.stdout = sys.__stdout__

        output = ("#\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__

        output = '###\n###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square(self):

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10)
        r1.display()
        sys.stdout = sys.__stdout__

        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):


        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(1)
        r1.display()
        sys.stdout = sys.__stdout__

        output = ("#\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):


        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__

        output = '###\n###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), output)

class TestSquare(unittest.TestCase):



    @classmethod
    def setUpClass(cls):


        cls.setup = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstring(self):


        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):


        self.assertTrue(len(Square.__doc__) >= 1)

    def test_wrong_inputted_values(self):


        with self.assertRaises(ValueError):
            S = Square(0, 0)
        with self.assertRaises(ValueError):
            S = Square(-4, -5)
        with self.assertRaises(ValueError):
            S = Square(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            S = Square()
        with self.assertRaises(TypeError):
            S = Square(1, 2, 3, 4, 5, 6, 7)

    def test_inputted_types(self):


        with self.assertRaises(TypeError):
            S = Square('width', 'height')
        with self.assertRaises(TypeError):
            S = Square(2.4, 1.3)
        with self.assertRaises(TypeError):
            S = Square(1, 2, 'x value', 'y value')
        with self.assertRaises(TypeError):
            S = Square(1, 2, 2.4, 1.3)
        with self.assertRaises(TypeError):
            S = Square(True, False)
        with self.assertRaises(TypeError):
            S = Square(1, 2, True, False)
        with self.assertRaises(TypeError):
            S = Square([1, 1], 2, 3, 4)
        with self.assertRaises(TypeError):
            S = Square((1, 2), 'x value', 'y value')
        with self.assertRaises(TypeError):
            S = Square({1: 3, 2: 4}, 5, 6)

    def test_a(self):


        S = Square(10, 10)
        self.assertEqual(S.area(), 100)
        with self.assertRaises(TypeError):
            A = S.area(1)

    def test_string(self):


        S = Square(2, 4, 6, 8)
        self.assertEqual("[Square] (8) 4/6 - 1", str(S))

    def test_update_args(self):

        S = Square(1, 2, 3, 4)
        S.update(6)
        self.assertEqual(6, S.id)
        S.update(6, 7)
        self.assertEqual(7, S.size)
        S.update(6, 7, 8)
        self.assertEqual(8, S.x)
        S.update(6, 7, 8, 9)
        self.assertEqual(9, S.y)

    def test_display(self):

        S = Square(2, 0, 0, 4)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            S.display()
            output = bufferIO.getvalue()
            self.assertEqual(output, ('#' * 2 + '\n') * 2)
        S = Square(2, 3, 4, 5)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            S.display()
            output = bufferIO.getvalue()
            self.assertEqual(output,
                             ('\n' * 4 + (' ' * 3 + '#' * 2 + '\n') * 2))

    def test_update_kwargs(self):

        S = Square(1, 2, 3, 4)
        S.update(6, id=7)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 1, 2, 3])
        S.update(6, 7, x=9, y=10)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 2, 3])
        S.update(width=7, id=6, height=8)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 2, 3])
        S.update(x=40, y=5)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 40, 5])

    def test_dictionary(self):
        S = Square(100, 300, 400, 500)
        S_dict = S.to_dictionary()
        self.assertEqual(S_dict['size'], 100)
        self.assertEqual(S_dict['x'], 300)
        self.assertEqual(S_dict['y'], 400)
        self.assertEqual(S_dict['id'], 500)


class TestSquare(unittest.TestCase):
 
 

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_pZero(self):


        ss = Square(1)
        self.assertEqual(ss.id, 1)
        s = Square(5, 3, 4)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 2)

    def test_ten_one(self):
   

        s1 = Square(9, 8, 10, 6)
        self.assertEqual(str(s1), "[Square] (6) 4/5 - 9")

    def test_ten_two(self):
    

        s_1 = Square(6)
        self.assertTrue(isinstance(s_1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s_1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    # def test_10_3(self):
    #     """Test Sqr class: check for  args."""

    #     with self.assertRaises(TypeError) as x:
    #         s_1 = Square()
    #     self.assertEqual(
    #         "__init__() missing 1 required positional argument: 'size'", str(
    #             x.exception))

    def test_ten_four(self):

        sx = Square(8)
        self.assertEqual(sx.area(), 61)
        ss = Square(4, 1, 2, 5)
        ss.update(7)
        self.assertEqual(ss.id, 7)
        fi = io.StringIO()
        sss = Square(8)
        with contextlib.redirect_stdout(fi):
            sss.display()
        s = fi.getvalue()
        res = "####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_11_0(self):
     

        s1 = Square(8)
        self.assertEqual(s1.size, 8)
        s2 = Square(9, 8, 7, 2)
        self.assertEqual(s2.size, 9)

    def test_elev_o(self):
      

        with self.assertRaises(TypeError) as x:
            s = Square("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(2, "World")
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(1, 2, "Foo", 3)
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(-1)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, -3)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, 5, -5, 6)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_twel_1(self):
      

        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)
        s1.update()
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

    def test_twel_t(self):
  

        s_1 = Square(6)
        with self.assertRaises(TypeError) as x:
            s_1.update(4, 6, 8, "hello")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s_1.update("hello", 8, 9)
        self.assertEqual("id must be an integer", str(x.exception))

    def test_fou_0(self):
      

        s_1 = Square(10, 4, 1)
        s_1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(s_1_dictionary), len(s_dictionary))
        self.assertEqual(type(s_1_dictionary), dict)
        s_2 = Square(1, 1)
        s_2.update(**s_1_dictionary)
        s_2_dictionary = s_2.to_dictionary()
        self.assertEqual(len(s_1_dictionary), len(s_2_dictionary))
        self.assertEqual(type(s_2_dictionary), dict)
        self.assertFalse(s_1 == s_2)

    # def test_14_1(self):
    #     """Test for pub meth to_dictionary with  args."""

    #     s = "to_dictionary() takes 1 positional argument but 2 were given"
    #     with self.assertRaises(TypeError) as x:
    #         s1 = Square(10, 4, 1, 9)
    #         s1_dictionary = s1.to_dictionary("Hi")
    #     self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
