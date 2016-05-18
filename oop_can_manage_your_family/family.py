''' Class definition '''
class Person:

    ''' class attributes? '''
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
           or not (genre == self.GENRES[0] or genre == self.GENRES[1]):
            raise Exception("genre is not valid")
        else:
            self.__genre = genre
        self.__eyes_color = eyes_color

        ''' public attributes '''
        self.last_name = "Has not been set yet."
