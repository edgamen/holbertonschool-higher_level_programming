''' Class '''
class Circle():

    ''' Constructor '''
    def __init__(self, radius):
        # private attributes
        self.__center = None
        self.__radius = radius
        self.__color = "The color has not been set yet."

        # public attributes
        self.name = "The name has not been set yet."

    def __del__(self):
        pass

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_center(self):
        return self.__center

    def set_center(self, center):
        self.__center = center

    def area(self):
        return 3.14 * self.__radius**2
