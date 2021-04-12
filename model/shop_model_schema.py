from peewee import PrimaryKeyField, CharField, Model, SqliteDatabase

db = SqliteDatabase('database/forca.db')

class ShopModel(Model):

    idshop = PrimaryKeyField(primary_key=True)
    nome = CharField(null=False, unique=True)
    valor = CharField(null=False, default=0)

    class Meta:
        database = db
