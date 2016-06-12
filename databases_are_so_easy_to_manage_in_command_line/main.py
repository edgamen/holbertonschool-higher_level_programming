from models import *
import peewee
import sys

''' return if string can be successfully cast as int '''
def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

''' create all tables related to all models form models file '''
def create_tables():
    my_models_db.create_tables([School, Batch, User, Student])

''' print requested table line by line '''
def print_table(args):
    model_entries = {'school': School, 'batch': Batch, 'user': User, 'student': Student}
    if len(args) == 0:
        print "Please enter the name of the table you wish to print in lowercase."
        return

    requested_table = args[0]

    if requested_table not in model_entries.keys():
        print "Undefined table: %s. Please make sure to use all lowercase to select table." % selected_table
        return

    for row in model_entries[requested_table].select():
        print row

''' insert a new entry into the database table requested '''
def insert_entry(args):
    if len(args) == 0:
        print "Please enter the name of the table you wish to modify in lowercase."
        return

    requested_table = args[0]
    
    if requested_table == "school":
        if len(args) < 2:
	    print "Please provide the following arguments for school: <name>"
            return
	
	new_entry = School.create(name=args[1])
	print "New school: " + str(new_entry)
            
    elif requested_table == "batch":
	if len(args) != 3:
	    print "Please provide the following arguments for batch: <school id> <name>"
            return
        elif len(args) == 3 and is_number(args[1]):
	    new_entry = Batch.create(school=args[1], name=args[2])
        else:
            print "Please provide a valid integer for the school foreign key."
            return
            
   	print "New batch: " + str(new_entry)    

    elif requested_table == "student":
        if len(args) < 4 or len(args) > 5:
	    print "Please provide the following arguments for student: <batch id> <age> <last_name> (<first_name>)"
            return
      
        elif len(args) == 4:
            if is_number(args[1]) and is_number (args[2]):
                new_entry = Student.create(batch=args[1], age=args[2], last_name=args[3])
            else:
                print "Please provide a valid integer for the batch foreign key / age of the student."
                return

        elif len(args) == 5:
            if is_number(args[1]) and is_number (args[2]):
                new_entry = Student.create(batch=args[1], age=args[2], last_name=args[3], first_name=args[4])
            else:
                print "Please provide a valid integer for the batch foreign key / age of the student."
                return
    
        print "New student: " + str(new_entry)
        
    else:
	print "Undefined table: %s. Please make sure to use all lowercase to select table." % args[0]

action_list = ["create", "print", "insert", "delete"]

if len(sys.argv) == 1:
    print "Please enter an action"
elif sys.argv[1] not in action_list:
    print "Undefined action " + sys.argv[1]
else:
    my_models_db.connect()
    # print sys.argv[1]
    if sys.argv[1] == "create":
	print "Creating tables"
	create_tables()
    elif sys.argv[1] == "print":
        print_table(sys.argv[2:])
    elif sys.argv[1] == "insert":
        insert_entry(sys.argv[2:])
        
       
