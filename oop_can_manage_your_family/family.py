import os.path
import json

''' Class definition '''
class Person:

    ''' class attributes '''
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]
    
    ''' defines what class is initialized with '''
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        ''' private attributes '''
        if type(id) is not int or id < 0:
            raise Exception("id is not an integer")
        else:
            self.__id = id

        if type(first_name) is not str or first_name == "":
            raise Exception("string is not a string")
        else:
            self.__first_name = first_name
            
        if type(date_of_birth) is not list \
           or len(date_of_birth) != 3 \
           or not (1 <= date_of_birth[0] <= 12) \
           or not (1 <= date_of_birth[1] <= 31):                        
            raise Exception("date_of_birth is not a valid date")
        else:
            self.__date_of_birth = date_of_birth

        if type(genre) is not str \
           or not genre in Person.GENRES:
            raise Exception("genre is not valid")
        else:
            self.__genre = genre

        if type(eyes_color) is not str \
           or not eyes_color in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        else:
            self.__eyes_color = eyes_color

        ''' public attributes '''
        self.last_name = "Has not been set yet."
        self.is_married_to = 0
        self.children = []

    ''' base class descriptions '''
    def __str__(self):
        return self.__first_name + " " + self.last_name
        
    ''' public methods to retrieve private attributes'''
    def get_id(self):
        return self.__id
    def get_eyes_color(self):
        return self.__eyes_color
    def get_genre(self):
        return self.__genre
    def get_date_of_birth(self):
        return self.__date_of_birth
    def get_first_name(self):
        return self.__first_name

    ''' public method to generate a hash from Person attributes'''
    def json(self):
        return {'id': self.__id, 'kind': self.__class__.__name__, 'first_name': \
                self.__first_name, 'last_name': self.last_name, 'is_married_to': \
                self.is_married_to, 'eyes_color': self.__eyes_color, 'genre': \
                self.__genre, 'date_of_birth': self.__date_of_birth}

    ''' public method to store values from a hash as Person attributes '''
    def load_from_json(self, json):
        if type(json) is not dict:
            raise Exception("json is not valid")
        else:
            if 'id' in json:
                self.__id = json['id']
            if 'eyes_color' in json:
                self.__eyes_colors = json['eyes_color']
            if 'genre' in json:
                self.__genre = json['genre']
            if 'date_of_birth' in json:
                self.__date_of_birth = json['date_of_birth']
            if 'first_name' in json:
                self.__first_name = json['first_name']
            if 'first_name' in json:
                self.__first_name = json['first_name']
            if 'last_name' in json:
                self.last_name = json['last_name']
            if 'is_married_to' in json:
                self.is_married_to = json['is_married_to']
    
    ''' public method to check if Person is married'''
    def is_married(self):
        return (self.is_married_to != 0)

    ''' public method to unlink two people and reset is_married_to status '''
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0

    ''' public method to link two people together using is_married_to attribute '''
    def just_married_with(self, p):
        if self.is_married() or p.is_married():
            raise Exception("Already married")
        elif not self.can_be_married() or not p.can_be_married():
            raise Exception("Can't be married")
        else:
            self.is_married_to = p.get_id()
            p.is_married_to = self.get_id()
            if self.get_genre() == "Female" and p.get_genre() == "Male":
                self.last_name = p.last_name
            elif self.get_genre() == "Male" and p.get_genre() == "Female":
                p.last_name = self.last_name

    ''' public method to create a new Baby and link id to children list for parents '''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
        if self.can_have_child == False:
            raise Exception("Can't have a child")
        if p is None or p.can_have_child == False:
            raise Exception("p can't have a child")
        else:
            baby = Baby(id, first_name, date_of_birth, genre, eyes_color)
            self.children.append(baby.get_id())
            p.children.append(baby.get_id())

    ''' public method to link id of a child to an adult '''
    def adopt_child(self, c):
        if self.can_have_child() == False:
            raise Exception("Can't adopt a person")
        if not (c.__class__.__name__ == "Baby" or c.__class__.__name__ == "Teenager"):
            raise Exception("c can't be adopted")
        else:
            self.children.append(c.get_id())

            
    ''' public method to check if Person is Male '''
    def is_male(self):
        return self.__genre == "Male"

    ''' public method to calculate age in years based 
        on the date 05/20/16 '''
    def age(self):
        age = 2016 - self.__date_of_birth[2]
        if self.__date_of_birth > 5:
            age = age - 1
        elif self.__date_of_birth[1] == 5 \
             and self.__date_of_birth[0] > 20:
            age = age - 1
        return age

    ''' magic methods to overload operators w/ respect to age '''
    def __eq__(self, other):
        return self.age() == other.age()
    def __ne__(self, other):
        return self.age() != other.age()
    def __lt__(self, other):
        return self.age() < other.age()
    def __gt__(self, other):
        return self.age() > other.age()
    def __le__(self, other):
        return self.age() <= other.age()
    def __ge__(self, other):
        return self.age() >= other.age()

''' Define a Baby class '''
class Baby(Person):
    ''' public methods '''
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return True
    def can_vote(self):
        return False
    def can_be_married(self):
        return False
    def can_have_child(self):
        return False

''' Define a Teenager class '''
class Teenager(Person):
    ''' public methods '''
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return True
    def can_vote(self):
        return False
    def can_be_married(self):
        return False
    def can_have_child(self):
        return False

''' Define a Adult class '''
class Adult(Person):
    ''' public methods '''
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return False
    def can_vote(self):
        return True
    def can_be_married(self):
        return True
    def can_have_child(self):
        return True

''' Define a Senior class '''
class Senior(Person):
    ''' public methods '''
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return False
    def can_vote(self):
        return True
    def can_be_married(self):
        return True
    def can_have_child(self):
        return False

    
''' Take a list of Person or subclass instances and write a JSON file '''
def save_to_file(list, filename):
    if type(filename) is not str \
       or not os.path.isfile(filename):
        raise Exception("filename is not valid or does not exist")
    # convert each item of the list into a hash of its attributes
    else:
        for i in range(len(list)):
            list[i] = list[i].json()
        json_string = json.dumps(list)
        f = open(filename, 'w')
        f.write(json_string)
        f.close()

''' Takes a JSON-formatted string and converts it into a list
    of Person or subclasses (Baby, Senior, etc.) instances '''
def load_from_file(filename):
    if type(filename) is not str \
       or not os.path.isfile(filename):
        raise Exception("filename is not valid or does not exist")
    else:
        f = open(filename, 'r')
        list = json.loads(f.read())
        f.close()

        # alternatively: create a new list and append each person to the new list
        for i in range(len(list)):
            if 'kind' in list[i]:
                if list[i]['kind'] == "Baby":
                    someone = Baby(0, "first_name", [01, 01, 1000], "Male", "Brown")
                elif list[i]['kind'] == "Teenager":
                    someone = Teenager(0, "first_name", [01, 01, 1000], "Male", "Brown")
                elif list[i]['kind'] == "Adult":
                    someone = Adult(0, "first_name", [01, 01, 1000], "Male", "Brown")
                elif list[i]['kind'] == "Senior":
                    someone = Senior(0, "first_name", [01, 01, 1000], "Male", "Brown")
            else:
                someone = Person(0, "first_name", [01, 01, 1000], "Male", "Brown")
            someone.load_from_json(list[i])
            list[i] = someone
        return list
