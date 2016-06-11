from models import *
import peewee
import sys

''' create all tables related to all models form models file '''
def create_tables():
    my_models_db.create_tables([School, Batch, User, Student])

''' print requested table line by line '''
def print_table(args):
    model_entries = {'school': School.select(), 'batch': Batch.select(), 'user': User.select(), 'student': Student.select()}
    if len(args) == 0:
        print "Please enter the name of the table you wish to print in lowercase."
        return

    selected_table = args[1]

    if selected_table not in model_entries.keys():
        print "Undefined table: %s. Please make sure to use all lowercase to select table." % selected_table
        return

    for row in model_entries[selected_table]:
        print row

def insert_entry(args):
    if len(args) == 0:
        print "Please enter the name of the table you wish to modify in lowercase."
        return

    if args[0] == "school":
        if len(args) < 2:
	    print "Please provide the following arguments for school: <name>"
            return
	
	new_entry = School.create(name=args[1])
	print "New school: " + str(new_entry)
            
    elif args[0] == "batch":
	if len(args) != 2 && len(args) != 3:
	    print "Please provide the following arguments for batch: (<school id>) <name>"
            return
	elif len(args) == 2:
	    school_id = int(args[1])
	    new_entry = Batch.create(name=args[1])
        elif len(args) == 3:
	    try:
		school_id = int(args[3])
		new_entry = Batch.create(school=school_id, name=args[4])
	    except ValueError:
		print "Please provide a valid integer for the school id."
                return

   	print "New batch: " + str(new_entry)    

    elif args[0] == "student":
        if len(args) < 3 or len(args) > 5:
	    print "Please provide the following arguments for student: (<batch id>) <age> <last_name> (<first_name>)"
            return

        if len(args) == 3:



            try:
		batch_id = int(args[3])
		student_age = int(args[4])
		new_entry = Student.create(batch=batch_id, age=student_age, last_name=args[5], first_name=args[6])
		print "New student: " + str(new_entry)
	    except ValueError:
		print "Please provide a valid integer for the batch id and age."
	else:
	    try:
		batch_id = int(args[3])
		student_age = int(args[4])
		new_entry = Student.create(batch=batch_id, age=student_age, last_name=args[5])
		print "New student: " + str(new_entry)
	    except ValueError:
		print "Please provide a valid integer for the batch id and age."
    else:
	print "Undefined table: %s. Please make sure to use all lowercase to select table." % args[2]'''

''' TEST SECTION 0 '''

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

''' TEST SECTION 1 '''
        
       