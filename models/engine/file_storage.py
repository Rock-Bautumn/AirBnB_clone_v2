#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
classes = {
    'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
    }
s_classes = {
    'State': State, 'City': City
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            listDic = {}
            if type(cls) == str:
                for key, value in FileStorage.__objects.items():
                    if classes[cls] == type(value):
                        listDic.update({key: value})
                return listDic
            else:
                for key, value in classes.items():
                    if cls == value or cls.__name__ == key:
                        for key, value in FileStorage.__objects.items():
                            if cls == type(value):
                                listDic.update({key: value})
                return listDic
        return FileStorage.__objects

    def delete(self, obj=None):
        """ Deletes the object from the list of objects """
        if obj:
            for key, value in self.__objects.items():
                if obj == value:
                    delValue = key
            self.__objects.pop(delValue)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[(str(obj.__class__.__name__)) + '.' + obj.id] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, value in self.__objects.items():
                temp.update({key: value})
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """literally just the same exact thing as reload,
        for deserializing the JSON file to objects"""
        self.reload()
