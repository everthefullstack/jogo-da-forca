from peewee import PrimaryKeyField, CharField, ForeignKeyField, IntegerField,  Model, SqliteDatabase
from model.shop_model_schema import ShopModel
from model.usuario_model_schema import UsuarioModel

db = SqliteDatabase('database/forca.db', pragmas={'foreign_keys': 1})

class CompraModel(Model):

    idcompra = PrimaryKeyField(primary_key=True)
    fkcodshop = ForeignKeyField(ShopModel, null=False)
    fkcodusuario = ForeignKeyField(UsuarioModel, null=False)
    quantidade = IntegerField(null=True, default=0)

    class Meta:
        database = db

    def create_compra(self, fkcodshop, fkcodusuario, quantidade):

        try:
            compra = self.get_or_none(self.fkcodshop == fkcodshop, self.fkcodusuario == fkcodusuario)
            if compra:
                return compra
            else:
                return None
        
        except Exception as erro:
            return erro