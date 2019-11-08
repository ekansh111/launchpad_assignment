from peewee import *

resortdb = SqliteDatabase("resort.db")

class User(Model):
	username = CharField()
	password = CharField()

	class Meta:
		database = resortdb


class Room(Model):
	owner = ForeignKeyField(User)
	#rid = IntegerField()
	rname = CharField()
	cost = FloatField()
	duration = FloatField()

	class Meta:
		database = resortdb



class Food(Model):
	owner = ForeignKeyField(User)
	ftype = CharField()
	cost = FloatField()

	class Meta:
		database = resortdb


class Activity(Model):

	owner = ForeignKeyField(User)
	aname = TextField()
	#aid = IntegerField()
	cost = FloatField()
	#duration = FloatField()

	class Meta:
		database = resortdb


if __name__ == '__main__':
	resortdb.connect()
	resortdb.create_tables([User, Room, Food, Activity])