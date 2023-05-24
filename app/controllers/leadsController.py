from flask import jsonify, request
from app.utils import utils
from sqlalchemy import desc
from ..models.leadsModel import *
from ..models.usersModel import *

# CONTROLLER LEADS FRANQUEADOS #
# PEGAR TODOS OS LEADS
def get_leads():
    leads = Leads.query.all()
    if leads:
        result = leads_schema.dump(leads)
        return jsonify({'Leads': result})
    return jsonify({'message': 'Lead não encontrado'}), 404


# PEGAR LEAD POR TELEFONE SEM RETORNAR COMO RESPOSTA #
# GET ONE LEAD BY TELEPHONE NUMBER WITHOUT RESPONSE CODE RETURN #
def lead_by_telefone(wpp):
    try:
        lead = Leads.query.filter(Leads.bitAtivo, Leads.wppContato == wpp).first()
    except Exception as err:
        print(err)
        return None

    if not lead:
        try:
            lead = Leads.query.filter(Leads.bitAtivo, Leads.wppContato == utils.fix_number(wpp)).first()
        except Exception as err:
            print(err)
            return None

    return lead


# PEGAR UM LEAD POR TELEFONE #
# GET LEAD BY TELEPHONE NUMBER WITH RESPONSE CODE #
def get_lead_by_telefone(wpp):
    lead = Leads.query.filter(Leads.bitAtivo, Leads.wppContato == wpp).first()
    if not lead:
        return jsonify({'message': 'Lead não encontrado'}), 404
    result = lead_schema.dump(lead)
    return jsonify({'Lead': result})


# ATUALIZA UM LEAD POR TELEFONE #
# UPDATE ONE LEAD BY TELEPHONE NUMBER #
def update_lead_enviado_wpp(wpp):
    enviado_wpp = request.json['EnviadoWpp']
    lead = get_lead_by_telefone(wpp)
    if not lead:
        return jsonify({'message': "Lead nao existe", 'data': {}}), 404

    if lead:
        try:
            lead.EnviadoWpp = enviado_wpp
            db.session.commit()
            result = lead_schema.dump(lead)
            return jsonify({'message': "EnviadoWpp Atualizado com Sucesso.", 'data': result}), 201
        except:
            return jsonify({'message': "Nao foi possivel atualizar.", 'data': {}}), 500


def update_lead_notificacoes(wpp):
    lead = lead_by_telefone(wpp)
    if not lead:
        return jsonify({'message': "Lead nao existe", 'data': {}}), 404
    try:
        if not lead.Interagiu or lead.Interagiu == 'null':
            lead.Interagiu = True
        if not lead.Notificacao or lead.Notificacao == 'null':
            lead.Notificacao = True
        else:
            lead.Notificacao = False

        db.session.commit()

        # utils.update_lead_pipefy(str(lead.IdCardPipefy), '311090269')

        return jsonify({'message': "Usuario Interagiu com Sucesso."}), 200

    except Exception as err:
        print(err)
        return jsonify({'message': "Nao foi possivel atualizar.", 'data': {}}), 500


def processing(json=None):
    _json = json
    message = _json['messages'][0]
    instance_id = _json['instanceId'] if "instanceId" in _json else None
    phone = message['author'][2:].replace('@c.us', '') if 'author' in message else None
    print(phone)
    try:
        lead = lead_by_telefone(phone)
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
        msg = str(dict_response)
        print('Passou na função func!')

        # update_lead_notificacoes(phone)

        return msg