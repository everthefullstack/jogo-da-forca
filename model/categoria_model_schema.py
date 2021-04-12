from peewee import PrimaryKeyField, CharField, Model, SqliteDatabase

db = SqliteDatabase('database/forca.db')

class CategoriaModel(Model):

    idcategoria = PrimaryKeyField(primary_key=True)
    nome = CharField(null=False, unique=True)
    
    class Meta:
        database = db
