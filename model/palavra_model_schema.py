from peewee import PrimaryKeyField, CharField, ForeignKeyField, Model, SqliteDatabase
from model.categoria_model_schema import CategoriaModel

db = SqliteDatabase('database/forca.db', pragmas={'foreign_keys': 1})

class PalavraModel(Model):

    idpalavra = PrimaryKeyField(primary_key=True)
    nome = CharField(null=False, unique=True)
    fkcodcategoria = ForeignKeyField(CategoriaModel, null=False)

    class Meta:
        database = db
