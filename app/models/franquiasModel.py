from app import db, ma


class Franquias(db.Model):
    __tablename__ = 'T_Franquias'
    __table_args__ = {"schema": "Franquia"}
    Id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(200), nullable=True)
    NomeUrl = db.Column(db.String(200), nullable=True)
    FotoUrl = db.Column(db.String(200), nullable=True)
    NomePipefy = db.Column(db.String(200), nullable=True)
    Ordem = db.Column(db.Integer, nullable=True)
    CNPJ = db.Column(db.String(14), nullable=True)
    IE = db.Column(db.String(20), nullable=True)
    Endereco = db.Column(db.String(500), nullable=True)
    Numero = db.Column(db.String(50), nullable=True)
    Bairro = db.Column(db.String(100), nullable=True)
    CEP = db.Column(db.String(9), nullable=True)
    Cidade = db.Column(db.String(80), nullable=True)
    Uf = db.Column(db.String(2), nullable=True)
    Telefone = db.Column(db.String(200), nullable=True)
    WhatsApp = db.Column(db.String(200), nullable=True)
    Email = db.Column(db.String(50), nullable=True)
    Latitude = db.Column(db.Float, nullable=True)
    Longitude = db.Column(db.Float, nullable=True)
    HorarioSemana = db.Column(db.String(200), nullable=True)
    HorarioSabado = db.Column(db.String(200), nullable=True)
    bitAtivo = db.Column(db.Boolean, nullable=True)
    bitInaugurada = db.Column(db.Boolean, nullable=True)
    bitFranquia = db.Column(db.Boolean, nullable=True)
    DescontoFrete = db.Column(db.Float, nullable=True)
    EstoqueId = db.Column(db.Integer, nullable=True)
    IdPipefy = db.Column(db.Integer, nullable=True)
    AccessToken = db.Column(db.String(100), nullable=True)
    SecretAccessToken = db.Column(db.String(100), nullable=True)
    IdStatusPago = db.Column(db.Integer, nullable=True)
    IdStatusCancelado = db.Column(db.Integer, nullable=True)
    EnviadoWpp = db.Column(db.Boolean, nullable=True)
    DataInserido = db.Column(db.DateTime, nullable=True)
    WppInstancia = db.Column(db.String(100), nullable=True)
    WppToken = db.Column(db.String(100), nullable=True)
    DownloadOrcamento = db.Column(db.DateTime, nullable=True)
    bitBaixandoOrcamentos = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f"<Nome : {self.Nome} >"


class FranquiasSchema(ma.Schema):
    class Meta:
        fields = ('Id', 'Nome', 'bitAtivo', 'bitInaugurada', 'bitFranquia', 'WppToken', 'WppInstancia')


franquia_schema = FranquiasSchema()
franquias_schema = FranquiasSchema(many=True)