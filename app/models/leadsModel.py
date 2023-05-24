from app import db, ma


class Leads(db.Model):
    __tablename__ = 'Relacionamento'
    __table_args__ = {"schema": "Franquia"}
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    tipoId = db.Column(db.Integer, nullable=False)
    statusId = db.Column(db.Integer, nullable=False)
    IdMarca = db.Column(db.Integer, nullable=True)
    NomeCampanha = db.Column(db.String(200), nullable=True)
    Campanha = db.Column(db.String(300), nullable=True)
    nomeContato = db.Column(db.String(300), nullable=True)
    emailContato = db.Column(db.String(300), nullable=True)
    telefoneContato = db.Column(db.String(300), nullable=True)
    wppContato = db.Column(db.String(300), nullable=True)
    dataCadastro = db.Column(db.DateTime, nullable=False)
    dataRetorno = db.Column(db.DateTime, nullable=True)
    dataUltimaInteracao = db.Column(db.DateTime, nullable=True)
    obs = db.Column(db.String(500), nullable=True)
    IdMotivoInsucesso = db.Column(db.Integer, nullable=True)
    IdOrcamentoGestao = db.Column(db.Integer, nullable=True)
    usuarioId = db.Column(db.Integer, nullable=True)
    unidadeId = db.Column(db.Integer, nullable=True)
    bitAtivo = db.Column(db.Boolean, nullable=True)
    IdResponsavel = db.Column(db.Integer, nullable=True)
    EnviadoWpp = db.Column(db.Integer, nullable=True)
    Cidade = db.Column(db.String(80), nullable=True)
    IdFranquia = db.Column(db.Integer, nullable=True)
    Endereco = db.Column(db.String(200), nullable=True)
    Cep = db.Column(db.String(50), nullable=True)
    CPF = db.Column(db.String(50), nullable=True)
    DataNasc = db.Column(db.DateTime, nullable=True)
    LeadPipefy = db.Column(db.Integer, nullable=True)
    PosicaoPipefy = db.Column(db.String(80), nullable=True)
    InseridoPipefy = db.Column(db.DateTime, nullable=True)
    DataInstalacao = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<User : {self.nomeContato} >"


class LeadsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tipoId', 'statusId', 'IdMarca', 'NomeCampanha', 'Campanha', 'nomeContato', 'emailContato',
                  'telefoneContato', 'wppContato', 'dataCadastro', 'dataRetorno', 'dataUltimaInteracao',
                  'dataUltimaInteracao', 'obs', 'IdMotivoInsucesso', 'IdOrcamentoGestao', 'usuarioId',
                  'unidadeId', 'bitAtivo', 'IdResponsavel', 'EnviadoWpp', 'Cidade', 'IdFranquia', 'Endereco', 'Cep',
                  'CPF', 'DataNasc', 'LeadPipefy', 'PosicaoPipefy', 'InseridoPipefy', 'DataInstalacao')


lead_schema = LeadsSchema()
leads_schema = LeadsSchema(many=True)
