from peewee import PrimaryKeyField, CharField, ForeignKeyField, Model, SqliteDatabase
from model.shop_model_schema import ShopModel
from model.usuario_model_schema import UsuarioModel

db = SqliteDatabase('database/forca.db', pragmas={'foreign_keys': 1})

class CompraModel(Model):

    idcompra = PrimaryKeyField(primary_key=True)
    fkcodshop = ForeignKeyField(ShopModel, null=False)
    fkcodusuario = ForeignKeyField(UsuarioModel, null=False)
    quantidade = CharField(null=True, default=0)

    class Meta:
        database = db
