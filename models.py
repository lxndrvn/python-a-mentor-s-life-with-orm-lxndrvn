from peewee import *
# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase('lxndrvn', user='lxndrvn')

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db

class CodecoolClass(BaseModel):
    location = CharField()
    year = IntegerField()

    def mentors(self):
        return Mentor.select().where(Mentor.codecool_class == self)

    def students(self):
        return Student.select().where(Student.codecool_class == self)

class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()
    year_of_birth = DateField()
    gender = CharField()
    codecool_class = ForeignKeyField(CodecoolClass)

class Mentor(Person):
    nickname = CharField()

class Student(Person):
    knowledge_level = IntegerField()
    energy_level = IntegerField()

