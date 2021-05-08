from peewee import PrimaryKeyField, CharField, ForeignKeyField, Model, SqliteDatabase
from model.categoria_model_schema import CategoriaModel

db = SqliteDatabase('database/forca.db', pragmas={'foreign_keys': 1})

class PalavraModel(Model):

    idpalavra = PrimaryKeyField(primary_key=True)
    nome = CharField(null=False, unique=True)
    fkcodcategoria = ForeignKeyField(CategoriaModel, null=False, on_delete="SET NULL")

    class Meta:
        database = db

    def create_palavra(self):

        try:
            self.save()
            return True
        
        except:
            self.save(force_insert=True)
    
    @classmethod
    def read_palavra(cls, idpalavra):

        palavra = cls.get_or_none(cls.idpalavra == idpalavra)
        if palavra:
            return palavra
            
        return None

    @classmethod
    def read_palavras(cls):

        palavras = cls.select()
        if palavras:
            return palavras
            
        return None

    @classmethod
    def read_palavras_por_categoria(cls, fkcodcategoria):

        palavras = cls.select().where(cls.fkcodcategoria == fkcodcategoria)
        if palavras:
            return palavras
            
        return None
        
    def update_palavra(self, nome, fkcodcategoria):

        try:
            self.nome = nome
            self.fkcodcategoria = fkcodcategoria
            self.save()

            return True

        except:
            return None
            
    def delete_palavra(self):
        
        try:
            self.delete_instance()
        except:
            return None
    
    def json(self):

        return {
                'idpalavra': self.idpalavra,
                'nome': self.nome,
                'fkcodcategoria': self.fkcodcategoria.idcategoria,
               }