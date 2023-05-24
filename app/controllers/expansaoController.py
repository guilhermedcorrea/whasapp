from flask import jsonify, request
from app.utils import utils
#from ..models.expansaoModel import *
from ..models.dadosCelularesModel import *


# CONTROLLER LEADS EXPANSÃO #
# CONTÉM LOGICA PARA ACESSO DE DADOS NO BANCO DE DADOS #
def lead_expansao_by_telefone(wpp):
    try:
        expansao = Expansao.query.filter(Expansao.BitAtivo, Expansao.CelularFormatado == wpp).first()
    except Exception as err:
        print(err)
        return None

    if not expansao:
        try:
            expansao = Expansao.query.filter(Expansao.BitAtivo,
                                             Expansao.CelularFormatado == utils.fix_number(wpp)).first()
        except Exception as err:
            print(err)
            return None

    return expansao


# PEGAR TODOS LEADS #
# GET ALL LEADS #
def get_leads_expansao():
    expansoes = Expansao.query.all()
    if expansoes:
        result = expansoes_schema.dump(expansoes)
        return jsonify({'Leads': result})
    return jsonify({'message': 'Leads não encontrados'}), 404


# PEGAR UM LEAD POR ID #
# GET ON LEAD BY ID #
def get_lead_expansao_by_id(idd):
    expansao = Expansao.query.filter(Expansao.BitAtivo, Expansao.Id == idd).first()
    if expansao:
        result = expansao_schema.dump(expansao)
        return jsonify({'Lead': result})
    return jsonify({'message': 'Leads não encontrados'}), 404


# Lead por nome #
def pesquisa_lead_expansao_by_wpp(idresponsavel, wpp):
    expansao = Expansao.query.filter(Expansao.IdResponsavel == str(idresponsavel),
                                     Expansao.CelularFormatado == str(wpp)).first()
    if expansao:
        result = expansao_schema.dump(expansao)
        return jsonify({'Lead': result})
    return jsonify({'message': 'Lead não encontrado'}), 404


# PEGAR UM LEAD POR TELEFONE #
# GET ONE LEAD BY TELEPHONE NUMBER #
def get_full_lead(wpp):
    lead = lead_expansao_by_telefone(wpp)
    if lead:
        dados_celular = DadosCelulares.query.filter(
            DadosCelulares.Numero == lead.CelularFormatado[2:],
            DadosCelulares.DDD == lead.CelularFormatado[:2]).first()

        lead = expansao_schema.dump(lead)

        if dados_celular:
            dados_celular = dadoscelular_schema.dump(dados_celular)
        else:
            dados_celular = {"CPF": None}

        dados = Dados.query.filter(Dados.CPF == dados_celular['CPF']).first()
        if dados:
            if dados.Falecido:
                return jsonify({"message": "† R.I.P †"}), 451
            else:
                dados = dado_schema.dump(dados)
        else:
            dados = {
                'Sexo': None,
                'DataNasc': None,
                'Risco': None,
                'Renda': None,
                'Status': None
            }

        dados_endereco = DadosEnderecos.query.filter(DadosEnderecos.CPF == dados_celular['CPF']).first()
        if dados_endereco:
            dados_endereco = dadosendereco_schema.dump(dados_endereco)
        else:
            dados_endereco = {'CEP': None}

        result = {**lead, **dados_celular, **dados, **dados_endereco}
        return jsonify({'Lead': result})

    return jsonify({'message': None}), 404


def get_lead_expansao_by_telefone(wpp):
    expansao = Expansao.query.filter(Expansao.CelularFormatado == wpp).first()
    if expansao:
        result = expansao_schema.dump(expansao)
        return jsonify({'Lead': result})
    return jsonify({'message': 'Lead não encontrado'}), 404


# PEGAR TODOS OS LEADS POR RESPONSAVEL #
# GET ALL LEADS BY RESPONSIBLE #
def get_leads_expansao_by_responsavel(idresponsavel):
    expansao = Expansao.query.filter(Expansao.IdResponsavel == idresponsavel).all()
    if expansao:
        result = expansoes_schema.dump(expansao)
        return jsonify({'Leads': result})
    return jsonify({'message': 'Lead não encontrado'})


# ATUALIZA UM LEAD POR ID #
# UPDATE ONE LEAD BY TELEPHONE NUMBER #
def update_lead_expansao_pipefy(idd):
    expansao = Expansao.query.filter(Expansao.BitAtivo, Expansao.Id == idd).first()
    body = request.json

    if not expansao:
        return jsonify({'message': "Lead nao existe", 'data': {}}), 404

    if expansao:
        try:
            if 'Nome' in body:
                expansao.Nome = body['Nome']
            if 'Email' in body:
                expansao.Email = body['Email']
            if 'Celular' in body:
                expansao.Celular = body['Celular']
            if 'UF' in body:
                expansao.UF = body['UF']
            if 'Cidade' in body:
                expansao.Cidade = body['Cidade']
            if 'Atua' in body:
                expansao.Atua = body['Atua']
            if 'Mensagem' in body:
                expansao.Mensagem = body['Mensagem']
            if 'Data' in body:
                expansao.Data = body['Data']
            if 'Origem' in body:
                expansao.Origem = body['Origem']
            if 'IP' in body:
                expansao.IP = body['IP']
            if 'Navegador' in body:
                expansao.Navegador = body['Navegador']
            if 'IdResponsavel' in body:
                expansao.IdResponsavel = body['IdResponsavel']
            if 'InseridoPipefy' in body:
                expansao.InseridoPipefy = body['InseridoPipefy']
            if 'EnviadoWpp' in body:
                expansao.EnviadoWpp = body['EnviadoWpp']
            if 'FormPreenchido' in body:
                expansao.FormPreenchido = body['FormPreenchido']
            if 'BitAtivo' in body:
                expansao.BitAtivo = body['BitAtivo']
            if 'IdCampanha' in body:
                expansao.IdCampanha = body['IdCampanha']
            if 'NomeCampanha' in body:
                expansao.NomeCampanha = body['NomeCampanha']
            if 'CelularFormatado' in body:
                expansao.CelularFormatado = body['CelularFormatado']
            if 'Interagiu' in body:
                expansao.Interagiu = body['Interagiu']
            if 'Notificacao' in body:
                expansao.Notificacao = body['Notificacao']
            if 'Enriquecido' in body:
                expansao.Enriquecido = body['Enriquecido']
            if 'IdCardPipefy' in body:
                expansao.IdCardPipefy = body['IdCardPipefy']
            if 'IdPosicaoPipefy' in body:
                utils.update_lead_pipefy(str(expansao.IdCardPipefy), str(body['IdPosicaoPipefy']))
            if 'PosicaoNomePipefy' in body:
                expansao.PosicaoNomePipefy = body['PosicaoNomePipefy']
            db.session.commit()
            result = expansao_schema.dump(expansao)
            return jsonify({'message': 'Atualizado com sucesso', 'data': result}), 200
        except Exception as err:
            print(err)
            return jsonify({'message': 'Não foi possivel atualizar', 'data': {}}), 500


# ATUALIZA NOTIFICAÇÕES E INTERAGIU DO LEAD DE EXPANSÃO#
# UPDATE ONE LEAD #
def update_lead_notificacoes(wpp):
    expansao = lead_expansao_by_telefone(wpp)
    if not expansao:
        return jsonify({'message': "Lead nao existe", 'data': {}}), 404
    try:
        if not expansao.Interagiu or expansao.Interagiu == 'null':
            expansao.Interagiu = True
        if not expansao.Notificacao or expansao.Notificacao == 'null':
            expansao.Notificacao = True
        else:
            expansao.Notificacao = False

        db.session.commit()

        if expansao.IdPosicaoPipefy in (311093716, 311141009, 311093648, 311093649,
                                        311093698, 311093699, 311093715, 311186037, 311090279):
            return jsonify({"error": "Não foi possivel atualizar Card.",
                            "message": "Card pode estar em 'reciclagem' ou na 'lixeira' ou outro lugar xD."}), 405
        else:
            utils.update_lead_pipefy(str(expansao.IdCardPipefy), '311090269')
            return jsonify({'message': "Card Pipefy atualizado de Primeira interação para interagindo."}), 200

    except Exception as err:
        print(err)
        return jsonify({'message': "Nao foi possivel atualizar.", 'data': {}}), 500


# PROCESSAMENTO WEBSOCKET #
def processing(json=None):
    _json = json
    message = _json['messages'][0]
    instance_id = _json['instanceId'] if "instanceId" in _json else None
    phone = message['author'][2:].replace('@c.us', '') if 'author' in message else None
    try:
        lead = lead_expansao_by_telefone(phone)
    except Exception as err:
        print(err)
        return None

    if not message['fromMe']:
        dict_response = {
            "ID": message['id'] if "id" in message else None,
            "Nome": message['senderName'] if "senderName" in message else None,
            "Numero": phone,
            "Mensagem": message['body'] if "body" in message else None,
            "chatName": message['chatName'] if "chatName" in message else None,
            "chatId": message['chatId'] if "chatId" in message else None,
            "WppInstancia": instance_id,
            "IdResponsavel": None if not lead else lead.IdResponsavel
        }
        msg = dict_response

        update_lead_notificacoes(phone)

        return msg
    else:
        return None
