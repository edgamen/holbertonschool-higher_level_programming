''' Class '''
class Square():

    ''' Constructor '''
    def __init__(self, side_length):
        # private attributes
        self.__side_length = side_length
        self.__center = None
        self.__color = "The color has not been set yet."
        self.__topbottom = ("*" * self.__side_length) 
        self.__side = "*" + (" " * (self.__side_length - 2)) + "*" + "\n"
        
        # public attributes
        self.name = "The name has not been set yet."

    ''' This function deletes the object from memory '''    
    def __del__(self):
        pass

    ''' This function specifies behavior when the object is called as
        a function: it returns a string representation of a square of
        the appropriate size and area '''    
    def __call__(self):
        return self.__topbottom + "\n" + self.__side * 2 + self.__topbottom

    ''' This function returns the color of the square (string) '''    
    def get_color(self):
        return self.__color

    ''' This function sets the color of the square (string) '''    
    def set_color(self, color):
        self.__color = color

    ''' This function returns the center of the square (should be array of
        2 ints) '''    
    def get_center(self):
        return self.__center
    
    ''' This function sets the center of the square (should be array
        of 2 ints) '''    
    def set_center(self, center):
        self.__center = center

        ''' This function returns the area of the square '''    
    def area(self):
        return self.__side_length**2
