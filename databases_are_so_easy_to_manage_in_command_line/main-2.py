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
def print_table(table, args):

    for row in table.select():
        print row

''' insert a new entry into the database table requested '''
def insert_entry(table, args):
    
    if table == School:
        if len(args) != 1:
	    print "Please provide the following arguments for school: <name>"
            return
	
	new_entry = School.create(name=args[0])
	print "New school: " + str(new_entry)
            
    elif table == Batch:
	if len(args) != 2:
	    print "Please provide the following arguments for batch: <school id> <name>"
            return
        elif is_number(args[0]):
	    new_entry = Batch.create(school=args[0], name=args[1])
        else:
            print "Please provide a valid integer for the school foreign key."
            return
            
   	print "New batch: " + str(new_entry)    

    elif table == Student:
        if len(args) < 3 or len(args) > 4:
	    print "Please provide the following arguments for student: <batch id> <age> <last_name> (<first_name>)"
            return
      
        elif len(args) == 3:
            if is_number(args[0]) and is_number (args[1]):
                new_entry = Student.create(batch=args[0], age=args[1], last_name=args[2])
            else:
                print "Please provide a valid integer for the batch foreign key / age of the student."
                return

        elif len(args) == 4:
            if is_number(args[0]) and is_number (args[1]):
                new_entry = Student.create(batch=args[0], age=args[1], last_name=args[2], first_name=args[3])
            else:
                print "Please provide a valid integer for the batch foreign key / age of the student."
                return
    
        print "New student: " + str(new_entry)
        
    else:
	print "Can't insert into User table. Use 'student' if you'd like to insert an entry into Student table."

def delete_entry(table, args):
    if args == 0:
        print "Please provide an id for the entry to delete."
    elif not is_number(args[0]):
        print "Please provide a valid integer for the id to delete."
    else:
        try:
            entry = table.select().where(table.id == args[0]).get()
            print "Delete: %s" % str(entry)
            entry.delete_instance()
        except:
            print "Nothing to delete"
        
        
# a hash that lists functions for a given action        
actions = {'create': insert_entry, 'print': print_table, 'insert': insert_entry, 'delete': delete_entry}

if len(sys.argv) < 2:
    print "Please enter an action"
elif sys.argv[1] not in actions.keys():
    print "Undefined action " + sys.argv[1]
else:
    my_models_db.connect()
    selected_action = sys.argv[1]
    
    if selected_action == "create":
	print "Creating tables"
	create_tables()
    elif len(sys.argv) < 3:
        print "Please enter the name of the table you wish to print in lowercase."
    else:
        requested_table = sys.argv[2]
        model_entries = {'school': School, 'batch': Batch, 'user': User, 'student': Student}
        
        if requested_table not in model_entries.keys():
            print "Undefined table: %s. Please make sure to use all lowercase to select table." % requested_table
        else:
            actions[selected_action](model_entries[requested_table], sys.argv[3:])
