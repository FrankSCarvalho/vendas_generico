from peewee import *

db = SqliteDatabase('sistema_vendas.db')

class BaseModel(Model):
    class Meta:
        database = db

class Produto(BaseModel):
    nome = CharField()
    preco = DecimalField(decimal_places=2)
    estoque = IntegerField()

class Venda(BaseModel):
    produto = ForeignKeyField(Produto, backref='vendas')
    quantidade = IntegerField()
    data_venda = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

# Inicializa o banco e as tabelas
db.connect()
db.create_tables([Produto, Venda])