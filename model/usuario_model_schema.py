from peewee import PrimaryKeyField, CharField, BooleanField, FloatField, Model, SqliteDatabase
from uuid import uuid4

db = SqliteDatabase('database/forca.db')

class UsuarioModel(Model):

    idusuario = PrimaryKeyField(primary_key=True)
    login = CharField(null=False, unique=True)
    senha = CharField(null=False)
    pontuacao = FloatField(null=True, default="0")
    pontuacao_ranking = FloatField(null=True, default="0")
    token = CharField(null=True, default="0")
    admin = BooleanField(null=True, default=False)
    
    class Meta:
        database = db

class Usuario(UsuarioModel):

    class Meta:
        table_name = 'usuariomodel'

    def create_usuario(self):

        try:
            self.save()
            return True
        
        except:
            self.save(force_insert=True)
    
    @classmethod
    def read_usuario(cls, idusuario):

        usuario = cls.get_or_none(cls.idusuario == idusuario)
        if usuario:
            return usuario
            
        return None

    @classmethod
    def read_usuarios(cls):

        usuarios = cls.select()
        if usuarios:
            return usuarios
            
        return None
        
    @classmethod
    def logar(cls, login, senha):
        
        try:
            usuario = cls.get_or_none(cls.login == login, cls.senha == senha)
            if usuario:

                usuario.token = uuid4().hex
                usuario.save()
                return usuario
        except:
            return None
    
    @classmethod
    def autenticar(cls, token):
        try:
            usuario = cls.get(cls.token == token)
            if usuario.token != 0:
                return usuario.token

        except:
            return None

    def update_pontuacao(self, pontuacao):

        try:
            if pontuacao > self.pontuacao_ranking:
                self.pontuacao_ranking = pontuacao
                self.pontuacao = self.pontuacao + pontuacao
                self.save()
            
            else:
                self.pontuacao = self.pontuacao + pontuacao
                self.save()

            return True
        except:
            return None

    def json(self):

        return {
                'idusuario': self.idusuario,
                'login': self.login,
                'senha': self.senha,
                'pontuacao': self.pontuacao,
                'pontuacao_ranking': self.pontuacao_ranking,
                'token': self.token,
                'admin': self.admin
               }

class Admin(Usuario):

    class Meta:
        table_name = 'usuariomodel'

    def update_usuario(self, login, senha, admin):

        try:
            self.login = login
            self.senha = senha
            self.admin = admin
            self.save()

            return True
        except:
            return None
            
    def delete_usuario(self):
        
        try:
            self.delete_instance()
        except:
            return None