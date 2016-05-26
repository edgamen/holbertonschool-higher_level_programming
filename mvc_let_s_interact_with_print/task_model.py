''' Class that will handle callback functions
    in a MVC framework '''
class TaskModel:

    def __init__(self, title):

        ''' private attributes '''
        if type(title) is not str or title == "":
            raise Exception("title is not a string")
        else:
            self.__title = title
        self.__callback_title = None

    ''' public methods '''
    def get_title(self):
        return self.__title
    def set_callback_title(self, callback):
        self.__callback_title = callback
    ''' reverse a string '''
    def toggle(self):
        self.__title = self.__title[::-1]
        self.__callback_title(self.__title)

    ''' overloading method '''
    def __str__(self):
        return self.__title
