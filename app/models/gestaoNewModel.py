from app import db, ma
from sqlalchemy.orm import relationship
from marshmallow import fields


class Orcamento(db.Model):
    __tablename__ = 'Orcamento'
    __bind_key__ = "HauszMapa"
    __table_args__ = {"schema": "Produtos"}

    IdOrcamento = db.Column(db.Integer, nullable=False, primary_key=True)
    CodigoOrcamento = db.Column(db.Integer, nullable=False)
    IdStatusOrcamento = db.Column(db.Integer, nullable=True)
    IdCliente = db.Column(db.Integer, db.ForeignKey("Cadastro.OrcamentoCliente.IdClienteOrcamento"),nullable=False)
    IdUnidade = db.Column(db.Integer, nullable=True)
    IdColaborador = db.Column(db.Integer, nullable=True)
    ValorTotal = db.Column(db.Float, nullable=True)
    valorCusto = db.Column(db.Float, nullable=True)
    Frete = db.Column(db.Float, nullable=True)
    Desconto = db.Column(db.Float, nullable=True)
    Comissao = db.Column(db.Float, nullable=True)
    bitAtivo = db.Column(db.Boolean, nullable=False)
    PrevisaoEntrega = db.Column(db.DateTime, nullable=True)
    DataOrcamento = db.Column(db.DateTime, nullable=True)

    orcamento_cliente = relationship("OrcamentoCliente", foreign_keys=[IdCliente])
    pedidos = relationship("Pedido", back_populates="orcamento")
    itens = relationship("OrcamentoItem", primaryjoin="and_(Orcamento.CodigoOrcamento == OrcamentoItem.CodigoOrcamento, "
                                                      " OrcamentoItem.bitAtivo == 1)", backref="Orcamento")
                         #,back_populates="orcamento", lazy='dynamic')

    def __repr__(self):
        return f"<Orcamento - CodigoOrcamento : {self.CodigoOrcamento}, Valortotal : {self.ValorTotal} >"


class OrcamentoSchema(ma.Schema):
    pedidos = fields.Nested(lambda: PedidoSchema(exclude=("IdOrcamento",), many=True))
    itens = fields.Nested(lambda: OrcamentoItemSchema(exclude=("CodigoOrcamento",)), many=True)

    class Meta:
        fields = ('CodigoOrcamento', 'IdStatusOrcamento', 'IdCliente', 'IdUnidade',
                  'IdColaborador', 'ValorTotal', 'ValorCusto', 'Frete', 'Desconto',
                  'Comissao', 'bitAtivo', 'PrevisaoEntrega', 'DataOrcamento', 'pedidos', 'itens')


orcamento_schema = OrcamentoSchema()
orcamentos_schema = OrcamentoSchema(many=True)


class OrcamentoItem(db.Model):
    __tablename__ = 'OrcamentoItens'
    __bind_key__ = "HauszMapa"
    __table_args__ = {"schema": "Produtos"}

    IdOrcamentoItens = db.Column(db.Integer, nullable=False, primary_key=True)
    CodigoOrcamento = db.Column(db.Integer, db.ForeignKey("Produtos.Orcamento.CodigoOrcamento"))
    SKU = db.Column(db.String(100), nullable=False)
    Quantidade = db.Column(db.Float, nullable=False)
    ValorCusto = db.Column(db.Float, nullable=False)
    ValorVenda = db.Column(db.Float, nullable=False)
    Desconto = db.Column(db.Float, nullable=True)
    IdEstoque = db.Column(db.Integer, nullable=True)
    bitAtivo = db.Column(db.Boolean, nullable=False)
    OrdemGrupos = db.Column(db.Integer, nullable=True)
    PrevisaoEntrega = db.Column(db.DateTime, nullable=True)

    #orcamento = relationship("Orcamento", foreign_keys=[CodigoOrcamento])

    def __repr__(self):
        return f"<Orcamento - CodigoOrcamento: {self.CodigoOrcamento} - SKU: {self.SKU} >"


class OrcamentoItemSchema(ma.Schema):
    class Meta:
        fields = ('IdOrcamentoItens', 'CodigoOrcamento', 'SKU', 'Quantidade', 'ValorCusto',
                  'ValorVenda', 'Desconto', 'IdEstoque', 'bitAtivo', 'OrdemGrupos', 'PrevisaoEntrega')


orcamentoitem_schema = OrcamentoItemSchema()
orcamentoitems_schema = OrcamentoItemSchema(many=True)


class OrcamentoCliente(db.Model):
    __tablename__ = 'OrcamentoCliente'
    __bind_key__ = "HauszMapa"
    __table_args__ = {"schema": "Cadastro"}

    IdClienteOrcamento = db.Column(db.Integer, nullable=False, primary_key=True)
    NomeCliente = db.Column(db.String(100), nullable=True)
    Celular = db.Column(db.String(20), nullable=True)
    CEP = db.Column(db.String(20), nullable=True)
    DataInserido = db.Column(db.DateTime, nullable=True)
    DataUltimoOrcamento = db.Column(db.DateTime, nullable=True)
    NomeArquiteto = db.Column(db.String(100), nullable=True)
    IdArquiteto = db.Column(db.Integer, nullable=True)

    orcamento = relationship("Orcamento", primaryjoin="and_(OrcamentoCliente.IdClienteOrcamento == Orcamento.IdCliente, "
                                                      " Orcamento.bitAtivo == 1, Orcamento.IdStatusOrcamento == 1)",
                                          backref="Orcamento")
                         #,back_populates="orcamento", lazy='dynamic')


class OrcamentoClienteSchema(ma.Schema):
    class Meta:
        fields = ('IdClienteOrcamento', 'NomeCliente', 'Celular', 'CEP', 'DataInserido', 'DataUltimoOrcamento',
                  'NomeArquiteto', 'IdArquiteto')


orcamentocliente_schema = OrcamentoClienteSchema()
orcamentoclientes_schema = OrcamentoClienteSchema(many=True)


class Pedido(db.Model):
    __tablename__ = 'PedidoFlexy'
    __bind_key__ = "HauszMapa"
    __table_args__ = {"schema": "Pedidos"}

    IdPedidoFlexy = db.Column(db.Integer, nullable=False, primary_key=True)
    IdOrcamento = db.Column(db.Integer, db.ForeignKey('Produtos.Orcamento.CodigoOrcamento'))
    CodigoPedido = db.Column(db.Integer, nullable=True)
    IdCliente = db.Column(db.Integer, nullable=True)
    IdColaborador = db.Column(db.Integer, nullable=True)
    Comissao = db.Column(db.Float, nullable=True)
    IdUnidade = db.Column(db.Integer, nullable=True)
    IdFormaPagamento = db.Column(db.Integer, nullable=True)
    PrevisaoEntrega = db.Column(db.DateTime, nullable=True)
    ValorTotal = db.Column(db.Float, nullable=True)
    IdEtapaFlexy = db.Column(db.Integer, nullable=True)
    Desconto = db.Column(db.Float, nullable=True)
    DataInserido = db.Column(db.DateTime, nullable=True)
    BitSplit = db.Column(db.Boolean, nullable=True)
    BitOmie = db.Column(db.Boolean, nullable=True)
    ValorTotalDescontado = db.Column(db.Float, nullable=True)
    Split = db.Column(db.Float, nullable=True)
    Margem = db.Column(db.Float, nullable=True)
    WmsEtapa = db.Column(db.Integer, nullable=True)

    orcamento = relationship("Orcamento", foreign_keys=[IdOrcamento])

    def __repr__(self):
        return f"<Pedido - CodigoPedido : {self.CodigoPedido} >"


class PedidoSchema(ma.Schema):
    orcamento = fields.Nested(lambda: OrcamentoSchema(only=("ValorTotalDescontado")))
    class Meta:
        fields = ('IdPedidoFlexy', 'IdOrcamento', 'CodigoPedido','IdColaborador', 'IdCliente',
                  'Comissao', 'IdUnidade', 'IdFormaPagamento', 'PrevisaoEntrega',
                  'ValorTotal', 'Desconto', 'DataInserido')


pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)


class PedidoItem(db.Model):
    __tablename__ = 'ItensFlexy'
    __bind_key__ = "HauszMapa"
    __table_args__ = {"schema": "Pedidos"}

    IdPedidoItensFlexy = db.Column(db.Integer, nullable=False, primary_key=True)
    CodigoPedido = db.Column(db.Integer, nullable=False)
    Quantidade = db.Column(db.Float, nullable=False)
    PrecoUnitario = db.Column(db.Float, nullable=False)
    SKU = db.Column(db.String(100), nullable=False)
    DataMinimaEntrega = db.Column(db.DateTime, nullable=True)
    DataMaximaEntrega = db.Column(db.DateTime, nullable=True)
    IdEstoque = db.Column(db.Integer, nullable=False)
    DescontoItem = db.Column(db.Float, nullable=False)
    PrecoUnitarioDescontado = db.Column(db.Float, nullable=False)
    DataInserido = db.Column(db.DateTime, nullable=True)
    CodigoPedidoCompra = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"<Pedido - CodigoPedido: {self.CodigoPedido} - SKU: {self.SKU}>"


class PedidoItemSchema(ma.Schema):
    class Meta:
        fields = ('CodigoPedido', 'SKU', 'Quantidade', 'PrecoUnitario', 'PrecoUnitarioDescontado','IdEstoque',
                  'DataMinimaEntrega', 'DataMaximaEntrega', 'DescontoItem', 'DataInserido')

pedidoitem_schema = PedidoItemSchema()
pedidoitems_schema = PedidoItemSchema(many=True)