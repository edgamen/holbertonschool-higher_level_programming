import peewee

''' TEST SECTION 1 '''

my_models_db = peewee.SqliteDatabase('my_models.db', pragmas=(('foreign_keys', True), ))
# pragmas: don't know what they are yet 

class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)

    class Meta:
        database = my_models_db
        order_by = ('id', ) # what is this?

class School(BaseModel):
    name = peewee.CharField(128, null=False)

    def __str__(self):
        return "School: %s (%d)" % (self.name, self.id)

class Batch(BaseModel):
    school = peewee.ForeignKeyField(School, related_name="batches", on_delete="CASCADE") # what is related_name?
    name = peewee.CharField(128, null=False)
    
    def __str__(self):
        return "Batch: %s (%d)" % (self.name, self.id)

class User(BaseModel):
    first_name = peewee.CharField(128, default="")
    last_name = peewee.CharField(128, null=False)
    age = peewee.IntegerField(null=False)

    def __str__(self):
        return "User: %s %s (%d)" % (self.first_name, self.last_name, self.id)

class Student(User):
    batch = peewee.ForeignKeyField(Batch, related_name="students", on_delete="CASCADE")

    def __str__(self):
        return "Student: %s %s (%d) part of the batch: %s" % (self.first_name, self.last_name, self.id, self.batch.name)
    
''' TEST SECTION 2 '''
