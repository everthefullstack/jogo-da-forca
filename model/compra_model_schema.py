from peewee import PrimaryKeyField, ForeignKeyField, IntegerField,  Model, SqliteDatabase
from model.shop_model_schema import ShopModel
from model.usuario_model_schema import UsuarioModel

db = SqliteDatabase('database/forca.db', pragmas={'foreign_keys': 1})

class CompraModel(Model):

    idcompra = PrimaryKeyField(primary_key=True)
    fkcodshop = ForeignKeyField(ShopModel, null=False, on_delete="CASCADE")
    fkcodusuario = ForeignKeyField(UsuarioModel, null=False, on_delete="CASCADE")
    quantidade = IntegerField(null=True, default=0)

    class Meta:
        database = db

    def create_compra(self):

        try:
            compra = CompraModel.get_or_none(CompraModel.fkcodshop == self.fkcodshop, CompraModel.fkcodusuario == self.fkcodusuario)
            if compra:
                compra.quantidade = compra.quantidade + self.quantidade
                compra.save()
                return True

            else:
                self.save()
                return True
        
        except Exception as erro:
            return str(erro)
    
    @classmethod
    def read_compra(cls, idcompra):

        try:
            shop = cls.get_or_none(cls.idcompra == idcompra)
            if shop:
                return shop
                
            return None

        except:
            return None

    @classmethod
    def read_compras_usuario(cls, fkcodusuario):

        try:
            shops = cls.select().where(cls.fkcodusuario == fkcodusuario)
            if shops:
                return shops
                
            return None

        except:
            return None
    
    def update_compra(self):

        try:
            if self.quantidade > 0:
                self.quantidade = self.quantidade - 1
                self.save()
                return True
            
            else:
                return None

        except:
            return None

    def json(self):

        return {
                'idcompra': self.idcompra,
                'fkcodshop': self.fkcodshop.idshop,
                'fkcodusuario': self.fkcodusuario.idusuario,
                'quantidade': self.quantidade,
               }