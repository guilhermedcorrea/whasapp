from app import db, ma


class Users(db.Model):
    __tablename__ = 'T_Login'
    __table_args__ = {"schema": "Franquia"}
    Id = db.Column(db.Integer, primary_key=True, nullable=False)
    Nome = db.Column(db.String(100), nullable=True)
    Usuario = db.Column(db.String(100), nullable=True)
    Senha = db.Column(db.String(100), nullable=True)
    Email = db.Column(db.String(100), nullable=True)
    IdUnidade = db.Column(db.Integer, nullable=True)
    DataCriacao = db.Column(db.DateTime, nullable=True)
    DataUltimoLogin = db.Column(db.DateTime, nullable=True)
    Admin = db.Column(db.Boolean, nullable=True)
    Matriz = db.Column(db.Boolean, nullable=True)
    bitAtivo = db.Column(db.Boolean, nullable=True)
    WppToken = db.Column(db.String(200), nullable=True)
    WppInstancia = db.Column(db.String(200), nullable=True)
    BitVendedor = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f"<User : {self.Usuario} >"


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('Id', 'Nome', 'Usuario', 'Email', 'IdUnidade', 'Admin', 'Matriz', 'bitAtivo', 'WppContato','WppToken', 'WppInstancia',
                  'BitVendedor')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
