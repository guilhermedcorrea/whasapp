from app import db, ma
from sqlalchemy.orm import relationship
from marshmallow import fields
from app.models.gestaoNewModel import (
    Orcamento,
    orcamento_schema,
    orcamentos_schema,
    OrcamentoItem,
    orcamentoitems_schema,
    OrcamentoCliente,
    orcamentocliente_schema,
    orcamentoclientes_schema
    )


class OrcamentoClienteLead(db.Model):
    __tablename__ = 'OrcamentoClienteLead'
    __bind_key__ = 'HauszMapa'
    __table_args__ = {"schema": "Produtos"}

    IdOrcamentoClienteLead = db.Column(db.Integer, nullable=False, primary_key=True)
    IdLead = db.Column(db.Integer, db.ForeignKey("Wpp.LeadFranquia.IdLead"), nullable=False)
    IdClienteOrcamento = db.Column(db.Integer, db.ForeignKey("Cadastro.OrcamentoCliente.IdClienteOrcamento"),
                                   nullable=False)
    DataInserido = db.Column(db.DateTime, nullable=True)

    lead = relationship("LeadsNew", foreign_keys=[IdLead])
    orcamento_cliente = relationship("OrcamentoCliente", foreign_keys=[IdClienteOrcamento])

    def __repr__(self):
        return f"<IdLead: {self.IdLead}, IdClienteOrcamento: {self.IdClienteOrcamento}>"


class OrcamentoClienteLeadSchema(ma.Schema):
    class Meta:
        fields = ('IdOrcamentoClienteLead', 'IdLead', 'IdClienteOrcamento', 'DataInserido')


orcamentoclienteLead_schema = OrcamentoClienteLeadSchema()
orcamentoclientesLead_schema = OrcamentoClienteLeadSchema(many=True)


class LeadsNew(db.Model):
    __tablename__ = 'LeadFranquia'
    __bind_key__ = "HauszMapa"
    __table_args__ = {"schema": "Wpp"}

    IdLead = db.Column(db.Integer, nullable=False, primary_key=True)
    Celular = db.Column(db.String(20), nullable=True)
    Cep = db.Column(db.String(20), nullable=True)
    IdCampanha = db.Column(db.Integer, nullable=True)
    IdUnidade = db.Column(db.Integer, nullable=True)
    IdColaborador = db.Column(db.Integer, nullable=True)
    Nome = db.Column(db.String(300), nullable=True)
    bitAtivo = db.Column(db.Boolean, nullable=True)
    bitNotificacao = db.Column(db.Boolean, nullable=True)
    bitInteragiu = db.Column(db.Boolean, nullable=True)
    DataNotificacao = db.Column(db.DateTime, nullable=True)
    DataInserido = db.Column(db.DateTime, nullable=True)
    dataAgenda = db.Column(db.DateTime, nullable=True)
    IdMotivoInsucesso = db.Column(db.Integer, nullable=True)
    IdPosicao = db.Column(db.Integer, nullable=True)

    cliente_lead = relationship("OrcamentoClienteLead", back_populates="lead")
    # orcamento_cliente
    def __repr__(self):
        return f"<User : {self.Nome} >"


class LeadsNewSchema(ma.Schema):
    class Meta:
        fields = ('IdLead', 'Celular', 'Cep', 'IdCampanha', 'IdUnidade', 'IdColaborador',
                  'Nome', 'bitAtivo', 'bitNotificacao', 'bitInteragiu', 'DataNotificacao',
                  'DataInserido', 'dataAgenda', 'IdMotivoInsucesso', 'IdPosicao')


leadNew_schema = LeadsNewSchema()
leadsNew_schema = LeadsNewSchema(many=True)


