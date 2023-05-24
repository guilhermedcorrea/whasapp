from app import db, ma


class DadosCelulares(db.Model):
    __tablename__ = 'T_DadosCelulares'
    __bind_key__ = "smsfire"
    Id = db.Column(db.Integer, primary_key=True, nullable=False)
    CPF = db.Column(db.String(20), nullable=False)
    DDD = db.Column(db.String(2), nullable=False)
    Numero = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<CPF : {self.CPF} >"


class DadosCelularesSchema(ma.Schema):
    class Meta:
        fields = ('CPF',)


dadoscelular_schema = DadosCelularesSchema()
dadoscelulares_schema = DadosCelularesSchema(many=True)


class DadosEnderecos(db.Model):
    __tablename__ = 'T_DadosEnderecos'
    __bind_key__ = "smsfire"
    Id = db.Column(db.Integer, primary_key=True, nullable=False)
    CPF = db.Column(db.String(20), nullable=False)
    CEP = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return f"<CPF : {self.CPF} >"


class DadosEnderecosSchema(ma.Schema):
    class Meta:
        fields = ('CEP',)


dadosendereco_schema = DadosEnderecosSchema()
dadosenderecos_schema = DadosEnderecosSchema(many=True)


class Dados(db.Model):
    __tablename__ = 'T_Dados'
    __bind_key__ = "smsfire"
    Id = db.Column(db.Integer, primary_key=True, nullable=False)
    Nome = db.Column(db.String(200), nullable=False)
    DataNasc = db.Column(db.DateTime, nullable=False)
    Sexo = db.Column(db.String(20), nullable=False)
    CPF = db.Column(db.String(20), nullable=False)
    Status = db.Column(db.String(50), nullable=False)
    Falecido = db.Column(db.Boolean, nullable=False)
    Renda = db.Column(db.DECIMAL(asdecimal=False), nullable=False)
    Risco = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Nome : {self.Nome} >"


class DadosSchema(ma.Schema):
    class Meta:
        fields = ('Sexo', 'DataNasc', 'Status', 'Renda', 'Risco',)


dado_schema = DadosSchema()
dados_schema = DadosSchema(many=True)

