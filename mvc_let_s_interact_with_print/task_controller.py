from task_model import TaskModel
from task_view import TaskView

''' Describe a class that controls the View
    and Model instances '''
class TaskController:

    def __init__(self, master, model):
        if master.__class__.__name__ != "Tk":
            raise Exception("master is not a tk.Tk()")

        if not isinstance(model, TaskModel):
            raise Exception("model is not a TaskModel")
        self.__model = model
        self.__view = TaskView(master)

        ''' Update the TaskView to show the string
            currently represented by the TaskModel '''
        self.__view.update_title(model)

        ''' When the button is clicked, we want it to also update the view's label '''
        self.__model.set_callback_title(self.__view.update_title)
        self.__view.toggle_button.config(command = self.__model.toggle)
