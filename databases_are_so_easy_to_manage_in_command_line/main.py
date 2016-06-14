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

''' delete a requested entry, by id '''
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
        
''' validate number of arguments and then call function if all good'''
def call_core_action(action, args):
    my_models_db.connect()
        
    if action == "create":
	print "Creating tables"
	create_tables()
    elif len(args) == 0:
        print "Please enter the name of the table you wish to print in lowercase."
    else:
        requested_table = args[0]
        model_entries = {'school': School, 'batch': Batch, 'user': User, 'student': Student}
        core_functions = {'print': print_table, 'insert': insert_entry, 'delete': delete_entry}
        
        if requested_table not in model_entries.keys():
            print "Undefined table: %s. Please make sure to use all lowercase to select table." % requested_table
        else:
            core_functions[action](model_entries[requested_table], args[1:])

''' define the print_by actions and validate arguments '''
def printby_action(action, args):
    my_models_db.connect()
    
    if len(args) == 0:
        print "Please provide a id for the school or batch"
    elif not is_number(args[0]):
        print "Please provide a valid integer for the ID of the school or batch."
    elif action == "print_batch_by_school":
        results = Batch.select().where(Batch.school == args[0])
        if results == "":
            print "School not found"
        for row in results:
            print row
    elif action == "print_student_by_batch":
        results = Student.select().where(Student.batch == args[0])
        if results == "":
            print "Batch not found"
        for row in results:
            print row        
    else:
        results = Student.select().join(Batch).where(Batch.school == args[0])
        if results == "":
            print "School not found"
        for row in results:
            print row
            
''' find the age average of students, of a single batch if id provided in first argument '''
def age_average(args):
    if len(args) != 0 and is_number(args[0]):
        batch_id = args[0]
        record = Student.select(Student, peewee.fn.Avg(Student.age).alias('age_average')).where(Student.batch == batch_id).get()
    else:
        record = Student.select(Student, peewee.fn.Avg(Student.age).alias('age_average')).get()
    print record.age_average


''' change the batch of a provided student, using student id as first arg and batch id as second arg  '''
def change_batch(args):
    if len(args) < 2:
        print "Please provide the following arguments: <student id> <batch id>"
        return
    if not is_number(args[0]) or not is_number(args[1]):
        print "Please provide a valid integer for both of the ids."
        return

    try:
        student_to_modify = Student.select().where(Student.id == args[0]).get()
    except:
        print "Student not found"
        return

    student_batch = student_to_modify.batch
    
    try:
        new_batch = Batch.select().where(Batch.id == args[1]).get()
    except:
        print "Batch not found"
        return

    if new_batch == student_batch:
        print "%s already in %s" % (str(student_to_modify), str(student_batch))
    else:
        student_to_modify.batch = args[1]
        student_to_modify.save()
        print "%s has been move to %s" %(str(student_to_modify), str(new_batch))
            
''' show students by a particular last name '''
def print_family(args):

    if len(args) == 0:
        print "Please provide the last name of the family to print."
    else:
        results = Student.select().where(Student.last_name == args[0])
        for row in results:
            print row

'''def print_all():
    schools_and_batches = School.select().join(Batch)
    for school in schools:
        print str(school)
        print "\t%s" % school.batch
        print "\t\t%s" 
'''            
# a hash that lists functions for a given action        
core_actions = ['create', 'print', 'insert', 'delete']
# defines type of printable object and filter for a specific query
printby_actions = ['print_batch_by_school', 'print_student_by_batch', 'print_student_by_school']
more_actions = {'print_family': print_family, 'age_average': age_average, 'change_batch': change_batch}

if len(sys.argv) < 2:
    print "Please enter an action"
elif sys.argv[1] in core_actions:
    call_core_action(sys.argv[1], sys.argv[2:])
elif sys.argv[1] in printby_actions:
    printby_action(sys.argv[1], sys.argv[2:])
elif sys.argv[1] in more_actions.keys():
    more_actions[sys.argv[1]](sys.argv[2:])
else:
    print "Undefined action " + sys.argv[1]
