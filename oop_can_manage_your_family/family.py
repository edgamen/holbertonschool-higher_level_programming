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

    ''' public method to check if person is Male '''
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

    ''' magic methods to overload operators in respect to age '''
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

''' Define a Baby class '''
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

''' Define a Baby class '''
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

''' Define a Baby class '''
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

    
