from peewee import Model, CharField, MySQLDatabase

db = MySQLDatabase(
    user='user',
    password='password',
    host='localhost',
    database='database'
)

class BaseModel(Model):
    class Meta:
        database = db

class Course(BaseModel):
    name = CharField(255)
    title = CharField(255)





