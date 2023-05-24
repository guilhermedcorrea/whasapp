from app import db, ma


class WaResponsavel(db.Model):
    __tablename__ = 'T_Responsavel'
    __table_args__ = {"schema": "Wa"}
    ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Nome = db.Column(db.String(200), nullable=False)
    Numero = db.Column(db.String(300), nullable=False)
    IdResponsavel = db.Column(db.Integer, nullable=False)
    UrlFoto = db.Column(db.String(300), nullable=False)
    InstanciaBot = db.Column(db.String(300), nullable=False)
    TokenBot = db.Column(db.String(300), nullable=False)
    DataInserido = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<User : {self.Nome} >"


class WaResponsavelSchema(ma.Schema):
    class Meta:
        fields = ('IdResponsavel',)


waresponsavel_schema = WaResponsavelSchema()
waresponsavaeis_schema = WaResponsavelSchema(many=True)
