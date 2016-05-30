import Tkinter as tk

''' Class that will handle generating the user
	interface that is shown to the user.
	This class inherits from (is a subclass of)
	the Tkinter Toplevel Widget (class) '''
class TaskView(tk.Toplevel):

	''' private attributes '''
	__title_var = tk.StringVar()
	__title_label 

	def __init__(self, master):
		''' Check if master is a root Tk() '''
		if type(master) is not tk.Tk():
			raise Exception("master is not a tk.Tk()")

		''' Initialize default values of parent '''
		tk.Toplevel.__init__(self, master)
		''' Set policies for what happens when window is closed '''
		self.protocol('WM_DELETE_WINDOW', self.master.destroy)
		
		self.__title_label = tk.Label(master, text=self.__title_var)
		self.__title_label.pack(side=right)

	''' public method to update the text in the table '''
	def update_title(self, title):
		if type(title) is not str:
			raise Exception("title is not a string")
		else:
			self.__title_var.set(title)
