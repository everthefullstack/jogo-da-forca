from peewee import PrimaryKeyField, CharField, FloatField, Model, SqliteDatabase

db = SqliteDatabase('database/forca.db')

class ShopModel(Model):

    idshop = PrimaryKeyField(primary_key=True)
    nome = CharField(null=False, unique=True)
    valor = FloatField(null=False, default=0)
    imagem = CharField(null=False)

    class Meta:
        database = db

    def create_shop(self):

        try:
            self.save()
            return True
        
        except:
            return None
    
    @classmethod
    def read_shop(cls, idshop):

        shop = cls.get_or_none(cls.idshop == idshop)
        if shop:
            return shop
            
        return None

    @classmethod
    def read_shops(cls):

        shops = cls.select()
        if shops:
            return shops
            
        return None

    def update_shop(self, nome, valor, imagem):

        try:
            self.nome = nome
            self.valor = valor
            self.imagem = imagem
            self.save()

            return True

        except:
            return None
            
    def delete_shop(self):
        
        try:
            self.delete_instance()
        except:
            return None
    
    def json(self):

        return {
                'idshop': self.idshop,
                'nome': self.nome,
                'valor': self.valor,
                'imagem': self.imagem
               }