from peewee import *
from playhouse.sqlite_ext import *

peopleDB = SqliteDatabase('People.db')

class BaseModel(Model):
    class Meta:
        database = peopleDB

class Person(BaseModel):
    name = CharField()
    surname = CharField()
    contact = JSONField()
    info = JSONField()
    index = AutoField()

class Specialization(BaseModel):
    name = CharField()
    owner = ForeignKeyField(Person, backref='specialization')
    info = JSONField()

class Merit(BaseModel):

    name = CharField()
    date = DateField()
    info = JSONField()
    owner = ForeignKeyField(Person, backref='merit')


def addPerson(name, surname, contact={}, info={}):
    if len(name) > 0:
        newP = Person(name=name, surname=surname, contact=contact, info=info)
        newP.save()

if __name__ == "__main__":
    peopleDB.create_tables([Person, Specialization, Merit])
