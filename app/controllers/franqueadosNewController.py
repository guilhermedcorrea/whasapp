import re
import datetime
from app import db
from sqlalchemy import desc
from flask import jsonify, request
from app.utils import utils
from app.controllers import franquiasController
from app.models.franqueadosNewModel import CampanhaFranquia, \
    campanhaFranquia_schema, campanhasFranquia_schema
from app.models.gestaoNewModel import Orcamento, OrcamentoSchema, orcamento_schema, orcamentos_schema


def lead_by_celular(celular: str):
    try:
        result = Franqueados.query.filter(Franqueados.bitAtivo, Franqueados.Celular == celular).first()
    except Exception as err:
        print(err)
        return None

    if not result:
        try:
            result = Franqueados.query.filter(Franqueados.bitAtivo,
                                              Franqueados.Celular == utils.fix_number(celular)).first()
        except Exception as err:
            print(err)
            return None

    return result


def lead_by_id(idd: int):
    try:
        result = Franqueados.query.filter(Franqueados.bitAtivo, Franqueados.IdLead == idd).first()
        return result
    except Exception as err:
        print(err)
        return None


def get_leads():
    try:
        result = Franqueados.query.filter(Franqueados.bitAtivo).all()
    except Exception as err:
        print(err)
        return None
    if result:
        result = franqueados_schema.dump(result)
        return jsonify({'Leads': result}), 200

    return jsonify({}), 204


def get_leads_by_unidade(idunidade: int):
    try:
        result = Franqueados.query.filter(Franqueados.bitAtivo, Franqueados.IdUnidade == idunidade).all()
    except Exception as err:
        print(err)
        return None

    if result:
        result = franqueados_schema.dump(result)
        return jsonify({'Leads': result}), 200

    return jsonify({}), 204


# GET ONE LEAD BY ID #
def get_lead_by_id(idd: int):
    try:
        result = FranqueadosNew.query.filter(Franqueados.bitAtivo, Franqueados.IdLead == idd).first()
    except Exception as err:
        print(err)
        return None

    if result:
        result = franqueado_schema.dump(result)
        return jsonify({'Lead': result}), 200

    return jsonify({'error': 'Lead não encontrado.'}), 404


# GET ONE LEAD BY CELULAR NUMBER #
def get_lead_by_celular(celular: str):
    try:
        result = Franqueados.query.filter(Franqueados.bitAtivo, Franqueados.Celular == celular).first()
    except Exception as err:
        print(err)
        return None

    if not result:
        try:
            result = Franqueados.query.filter(Franqueados.bitAtivo,
                                              Franqueados.Celular == utils.fix_number(celular)).first()
        except Exception as err:
            print(err)
            return None

    if result:
        result = franqueado_schema.dump(result)
        return jsonify({'Lead': result}), 200

    return jsonify({'error': 'Lead não encontrado.'}), 404


# GET ALL LEADS BY COLABORATOR #
def get_leads_by_colab(idcolab: int):
    if not idcolab.isnumeric():
        return jsonify({"error": "Parametros Inválidos"}), 400
    # try:
    #     result = db.session.query(Franqueados, Orcamento) \
    #         .outerjoin(Orcamento, Orcamento.IdPedido == Franqueados.IdOrcamentoGestao)  \
    #         .filter(Franqueados.IdColaborador == idcolab).all()
    try:
        result = Franqueados.query.filter(Franqueados.bitAtivo, Franqueados.IdColaborador == idcolab) \
            .order_by(desc(Franqueados.DataNotificacao)) \
            .all()
    except Exception as err:
        print(err)
        return None
    leads = franqueados_schema.dump(result) if result else None
    # leads = franqueados_schema.dump(result) if result else None
    # orca = orcamentos_schema.dump(result) if result else None
    # print(orca)
    # for i in result:
    #     orc = orcamentos_schema.dump(i) if i else None
    #     if orc:
    #         #(orc['valor_total'])
    #         value = orc[1].get('valor_total')

    #print(orcamento)
    #leads = franqueados_schema.dump(result[0]) if result[0] else None
    #orcamento = orcamento_schema.dump(result[1]) if result[1] else None

    return jsonify({'Leads': leads}), 200


def get_leads_by_fase(idd):
    try:
        result = Franqueados.query.filter(Franqueados.IdPosicao == idd)\
            .order_by(desc(Franqueados.DataNotificacao)).all()
    except Exception as err:
        print(err)
        return None

    if result:
        result = franqueados_schema.dump(result)
        return jsonify({'Leads': result}), 200

    return jsonify({}), 204


def pesquisa_leads_by_colab_nome(idcolab: int, nome: str):
    try:
        result = Franqueados.query.filter(Franqueados.bitAtivo, Franqueados.IdColaborador == idcolab,
                                          Franqueados.Nome.like(f'%{nome}%'))\
            .order_by(desc(Franqueados.DataNotificacao)).all()

    except Exception as err:
        print(err)
        return None

    if result:
        result = franqueados_schema.dump(result)
        return jsonify({'Leads': result}), 200

    return jsonify({}), 204


# FIND FRANCHISE FUNCTION #
def find_franquia(json):
    message = json['messages'][0]
    text = message['body']
    pat = r'(?<=\[).+?(?=\])'
    try:
        text = re.findall(pat, text)
    except Exception as err:
        print(err)

    if not text:
        text = ['Geral cod 1001']

    try:
        campanha = CampanhaFranquia.query.filter(CampanhaFranquia.CodigoCampanha.like(f'{text[0]}')).first()
    except Exception as err:
        print(err)
        return None

    if not campanha:
        return None

    try:
        franquia = franquiasController.franquia_by_id(campanha.IdUnidade)
    except Exception as err:
        print(err)
        return None

    if franquia:
        dict_result = {
            'IdCampanha': campanha.IdCampanha,
            'IdUnidade': franquia.Id
        }

    else:
        dict_result = {
            'IdCampanha': campanha.IdCampanha,
            'IdUnidade': 0
        }

    return dict_result


# CREAT LEAD FUNCTION #
def create_lead(json):
    auxiliar = find_franquia(json)
    if not auxiliar:
        return jsonify({}), 204

    message = json['messages'][0]
    phone = message['author'][2:].replace('@c.us', '') if 'author' in message else None
    lead = lead_by_celular(phone)

    if lead:
        return jsonify({"message": "Lead já cadastrado."}), 405

    id_campanha = auxiliar['IdCampanha']
    id_franquia = auxiliar['IdUnidade']
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    lead = Franqueados(phone, data, id_campanha, id_franquia, None)

    try:
        db.session.add(lead)
        db.session.commit()
        result = franqueado_schema.dump(lead)
        return jsonify({"message": "Lead Cadastrado com Sucesso.", "data": result}), 201
    except Exception as err:
        print(err)
        return jsonify({"error": "Não foi possivel cadastrar."}), 500


# UPDATE LEAD FUNCTION #
def retuupdate_lead(idd: int):
    lead = Franqueados.query.filter(Franqueados.bitAtivo, Franqueados.IdLead == idd).first()
    body = request.json

    if not lead:
        return jsonify({}), 204

    if lead:
        try:
            if 'Celular' in body:
                lead.Celular = body['Celular']
            if 'Cep' in body:
                lead.Cep = body['Cep']
            if 'IdCampanha' in body:
                lead.IdCampanha = body['IdCampanha']
            if 'IdUnidade' in body:
                lead.IdUnidade = body['IdUnidade']
            if 'IdColaborador' in body:
                lead.IdColaborador = body['IdColaborador']
            if 'IdOrcamentoGestao' in body:
                lead.IdOrcamentoGestao = body['IdOrcamentoGestao']
            if 'Nome' in body:
                lead.Nome = body['Nome']
            if 'bitNotificacao' in body:
                lead.bitNotificacao = body['bitNotificacao']
            if 'DataAgenda' in body:
                lead.DataAgenda = body['DataAgenda']
            if 'ObsInterna' in body:
                lead.ObsInterna = body['ObsInterna']
            if 'FaseObra' in body:
                lead.FaseObra = body['FaseObra']
            if 'TamanhoObra' in body:
                lead.TamanhoObra = body['TamanhoObra']
            if 'IdMotivoInsucesso' in body:
                lead.IdMotivoInsucesso = body['IdMotivoInsucesso']
            if 'IdPosicao' in body:
                lead.IdPosicao = body['IdPosicao']

            db.session.commit()
            result = franqueado_schema.dump(lead)
            return jsonify({'message': 'Atualizado com sucesso.', 'data': result}), 200
        except Exception as err:
            print(err)
            return jsonify({'error': 'Não foi possivel atualizar.', 'data': {}}), 500


#Create Lead
def create_lead_from_choris(cel: str):
    body = request.json
    lead = Franqueados.query.filter(Franqueados.bitAtivo, Franqueados.Celular == cel).first()

    if not lead:
        lead = Franqueados.query.filter(Franqueados.bitAtivo,
                                          Franqueados.Celular == utils.fix_number(cel)).first()

    if not lead:
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        celular = body['celular']
        id_campanha = body['idCampanha']
        id_franquia = body['idFranquia']
        id_colaborador = body['idColaborador']
        try:
            _lead = Franqueados(celular, data, id_campanha, id_franquia, id_colaborador)
            db.session.add(_lead)
            db.session.commit()
            result = franqueado_schema.dump(_lead)
            return jsonify({'message': 'Inserido com sucesso.', 'data': result}), 201
        except Exception as err:
            print(err)
            return jsonify({'error': 'Não foi possivel inserir.', 'data': {}}), 500
    else:
        return jsonify({'message': 'Lead já existe'}), 200


# UPDATE ONLY LEAD NOTIFICATION #
def update_notificacao(celular: str):
    try:
        lead = lead_by_celular(celular)
    except Exception as err:
        print(err)
        return None

    if not lead:
        return jsonify({'error': "Lead nao encontrado", 'data': {}}), 404
    try:
        if not lead.bitInteragiu or lead.bitInteragiu == 'null':
            lead.bitInteragiu = True
        if not lead.bitNotificacao or lead.bitNotificacao == 'null':
            lead.bitNotificacao = True
        else:
            lead.bitNotificacao = False

        db.session.commit()
        return jsonify({'message': "Usuario Interagiu com Sucesso."}), 200

    except Exception as err:
        print(err)
        return jsonify({'error': "Nao foi possivel atualizar.", 'data': {}}), 500


# WEBSOCKET PROCESSING #
def processing(json=None):
    _json = json
    message = _json['messages'][0]
    instance_id = _json['instanceId'] if "instanceId" in _json else None
    phone = message['author'][2:].replace('@c.us', '') if 'author' in message else None

    try:
        lead = lead_by_celular(phone)
    except Exception as err:
        print(err)
        return None

    if not lead.IdColaborador:
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
            "IdColaborador": None if not lead else lead.IdColaborador
        }
        msg = dict_response

        update_notificacao(phone)
        return msg

    else:
        return None


# GET ALL CAMPANHAS, IN HERE CUZ IM KINDA LAZZY TODAY #
def get_campanhas():
    try:
        campanhas = CampanhaFranquia.query.all()
    except Exception as err:
        print(err)
        return None

    if campanhas:
        result = campanhasFranquia_schema.dump(campanhas)
        return jsonify({"campanhas": result})

    return jsonify({}), 204


# GET CAMPANHA BY ID, IN HERE CUZ IM KINDA LAZZY TODAY #
def get_campanha_by_id(idd: int):
    try:
        campanha = CampanhaFranquia.query.filter(CampanhaFranquia.IdCampanha == idd).one()
    except Exception as err:
        print(err)
        return None
    if campanha:
        result = campanhaFranquia_schema.dump(campanha)
        return jsonify({"campanha": result})

    return jsonify({'error': 'Campanha nao encontrada.'}), 404
