#!/usr/bin/python3
"""This module contains a class to serve as base for other classes"""

import os
import json
import csv
import turtle




class Base:
    """Base class for other classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize objects created"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns serialized Python objects (list_dictionaries)"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("input must be a list")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes JSON repre to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """gets the list of JSON string repre"""
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("input must be a str")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """gets an instance with already set attributes """
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        elif cls.__name__ == 'Square':
            new = cls(1)

        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list"""

        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs then save in a file"""
        """ 
        if (type(list_objs) != list and list_objs is not None
           or not all(isinstance(i, cls) for i in list_objs)):

            raise TypeError("list_objs must be a list of instances")

        file_name = cls.__name__ + ".csv"
        with open(file_name, 'w') as my_file:
            if list_objs is not None:
                list_objs = [i.todictionary for i in list_objs]
                if cls.__name__ == 'Rectangle':
                    records = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    records = ['id', 'size', 'x', 'y']
                script = csv.DictWriter(my_file, fieldnames=records)
                script.writeheader()
                script.writerows(list_objs)
        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""
        """
        file_name = cls.__name__ + ".csv"
        list_of_instances = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                reader = csv.reader(my_file, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    records = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    records = ['id', 'size', 'x', 'y']
                for i, row in enumerate(reader):
                    if i > 0:
                        a = cls(1, 1)
                        for i, b in enumerate(row):
                            if b:
                                setattr(a, records[i], int(b))
                        list_of_instances.append(a)
        return list_of_instances
        """ 

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([key, int(value)] for key, value in i.items())
                              for i in list_dicts]
                return [cls.create(**i) for i in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares with turtle module.
        Args:
            list_rectangles (list): Rectangle list objects to draw.
            list_squares (list):Square list objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for re in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(re.x, re.y)
            turt.down()
            for i in range(2):
                turt.forward(re.width)
                turt.left(90)
                turt.forward(re.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for s in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(s.x, s.y)
            turt.down()
            for i in range(2):
                turt.forward(s.width)
                turt.left(90)
                turt.forward(s.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
