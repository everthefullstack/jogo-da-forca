from peewee import PrimaryKeyField, CharField, Model, SqliteDatabase

db = SqliteDatabase('database/forca.db')

class CategoriaModel(Model):

    idcategoria = PrimaryKeyField(primary_key=True)
    nome = CharField(null=False, unique=True)
    
    class Meta:
        database = db

    def create_categoria(self):

        try:
            self.save()
            return True
        
        except:
            return None
    
    @classmethod
    def read_categoria(cls, idcategoria):

        categoria = cls.get_or_none(cls.idcategoria == idcategoria)
        if categoria:
            return categoria
            
        return None

    @classmethod
    def read_categorias(cls):

        categorias = cls.select()
        if categorias:
            return categorias
            
        return None

    def update_categoria(self, nome):

        try:
            self.nome = nome
            self.save()

            return True
            
        except:

            return None
            
    def delete_categoria(self):
        
        try:
            self.delete_instance()
        except:
            return None
    
    def json(self):

        return {
                'idcategoria': self.idcategoria,
                'nome': self.nome
               }
