from app import db, ma


class CampanhaFranquia(db.Model):
    __tablename__ = 'CampanhaFranquia'
    __bind_key__ = "HauszMapa"
    __table_args__ = {"schema": "Wpp"}

    IdCampanha = db.Column(db.Integer, nullable=False, primary_key=True)
    NomeCampanha = db.Column(db.String(50), nullable=False)
    CodigoCampanha = db.Column(db.String(50), nullable=False)
    Cidade = db.Column(db.String(100), nullable=False)
    IdUnidade = db.Column(db.Integer, nullable=False)
    IdMarca = db.Column(db.Integer, nullable=False)
    IdCategoria = db.Column(db.Integer, nullable=False)
    IdOrigem = db.Column(db.Integer, nullable=False)
    bitAtivo = db.Column(db.Boolean, nullable=False)
    DataInserido = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Campanha : {self.IdCampanha}, {self.Cidade} >"


class CampanhaFranquiaSchema(ma.Schema):
    class Meta:
        fields = ('IdCampanha', 'NomeCampanha', 'CodigoCampanha', 'Cidade', 'IdUnidade', 'IdMarca', 'IdCategoria',
                  'IdOrigem', 'DataInserido')


campanhaFranquia_schema = CampanhaFranquiaSchema()
campanhasFranquia_schema = CampanhaFranquiaSchema(many=True)
