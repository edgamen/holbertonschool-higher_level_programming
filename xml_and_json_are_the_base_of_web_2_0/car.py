import json

''' describe an object that represents a car '''
class Car:

    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], dict):
            hash = args[0]
            name = hash.get('name')
            brand = hash.get('brand')
            nb_doors = hash.get('nb_doors')
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        if name == None or not isinstance(name, str):
            raise Exception("name is not a string")
        if brand == None or not isinstance(brand, str):
            raise Exception("brand is not a string")
        if not isinstance(nb_doors, int) or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")
        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    ''' overloading method to define object when cast as String '''
    def __str__(self):
        return "%s %s (%s)" % (self.__name, self.__brand, self.__nb_doors)

    ''' public methods to retrieve private attributes '''
    def get_name(self):
        return self.__name
    def get_brand(self):
        return self.__brand
    def get_nb_doors(self):
        return self.__nb_doors

    ''' public method to update the private attribuet nb_doors '''
    def set_nb_doors(self, number):
        if not isinstance(number, int) or number <= 0:
            raise Exception("provided number is not > 0")
        self.__nb_doors = number

    ''' public method to return a hash describing the object '''
    def to_hash(self):
        return {'name': self.__name, 'brand': self.__brand, 'nb_doors': self.__nb_doors}

    ''' public method to return a string in json format '''
    def to_json_string(self):
        return json.dumps(self.to_hash())
