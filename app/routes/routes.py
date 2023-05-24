from app import app, socketio
from flask import jsonify, request, render_template
from flask_socketio import send
from flask_cors import cross_origin
from app.controllers import authController, leadsController, expansaoController, franqueadosNewController, \
    franquiasController, usersController, gestaoNewController, leadsNewController, \
    campanhasController

# ROUTES FILE #
# ROOT ROUTE #
@app.route('/api', methods=['GET'])
@cross_origin(headers=['Content-Type', 'Authorization'])
#@authController.token_requiredcurrent_user
def root():
    data = jsonify({'message': f'Hello World!'})
    return data


##################################################################################################
##################################### AUTHENTICATION #############################################
##################################################################################################
# AUTH ROUTE FOR AUTHENTICATION #
@app.route('/api/v1/auth', methods=['POST'])
@cross_origin()
def auth_user():
    return authController.authentication()


##################################################################################################
######################################## SELLERS #################################################
##################################################################################################

# GET ALL SELLERS BY FRANQUIA #
# @app.get('/api/v1/vendedores/<franquia>')
# @cross_origin()
# def users_by_franquia(franquia):
#     result = usersController.get_vendedores_by_franquia(franquia)
#     return result


##################################################################################################
##################################### FRANQUIAS NEW ##############################################
##################################################################################################

# GET ALL FRANCHISES #
# @app.get('/api/v1/franqueados/franquias')
# @cross_origin()
# def get_franquias_all():
#     return franquiasController.get_franquias()
#
#
# # GET ONE FRANCHISE BY ID #
# @app.get('/api/v1/franqueados/franquia/<idd>')
# @cross_origin()
# def get_franquia_by_id(idd: int):
#     return franquiasController.get_franquia_by_id(idd)

##################################################################################################
################################### FRANQUEADOS NEW LEADS ############################################
##################################################################################################

# GET ALL LEADS FRANCHISE #
@app.route('/api/v1/franqueados/leadsNew', methods=['GET'])
@cross_origin()
def get_leads_new():
    return leadsNewController.get_leads()

# GET ONE LEAD BY PHONE NUMBER #
@app.get('/api/v1/franqueados/leadNew/<celular>')
@cross_origin()
def get_lead_by_celular_new(celular):
    return leadsNewController.get_leadNew_by_telefone(celular)



##################################################################################################
###################################### CAMPANHAS NEW MODEL #################################################
##################################################################################################

# GET ALL CAMPANHAS #
#@authController.token_required
@app.get('/api/v1/campanhas')
#@authController.token_required
@cross_origin()
def get_campanhas():
    return campanhasController.get_campanhas()


# GET ONE CAMPANHA BY ID #
@app.get('/api/v1/campanha/<idd>')
@cross_origin()
def get_campanha_by_id(idd: int):
    return campanhasController.get_campanha_by_id(idd)

##################################################################################################
################################### FRANQUEADOS LEADS ############################################
##################################################################################################

# GET ALL LEADS FRANCHISE #
# @app.route('/api/v2/franqueados/leads', methods=['GET'])
# @cross_origin()
# def get_leads():
#     return franqueadosNewController.get_leads()


# @app.route('/api/v2/franqueados/leadsOrc', methods=['GET'])
# @cross_origin()
# def get_leads():
#     return franqueadosController.get_leads()


# @app.route('/api/v2/franqueados/leads/u/<idUnidade>', methods=['GET'])
# @cross_origin()
# def get_lead_by_unidade(idUnidade):
#     return franqueadosNewController.get_leads_by_unidade(idUnidade)
#
#
# @app.get('/api/v2/franqueados/leads/fase/<idd>')
# @cross_origin()
# def get_leads_by_fase(idd):
#     return franqueadosNewController.get_leads_by_fase(idd)
#
#
# # GET ALL LEADS BY COLABORATOR #
# @app.get('/api/v2/franqueados/leads/<idcolab>')
# @cross_origin()
# def get_leads_by_colabs(idcolab):
#     return franqueadosNewController.get_leads_by_colab(idcolab)
#
#
# GET ONE LEAD BY ID #
@app.route('/api/v1/franqueados/lead/i/<idd>', methods=['GET', 'PUT'])
@cross_origin()
def update_lead_by_id(idd):
    if request.method == 'GET':
        return franqueadosNewController.get_lead_by_id(idd)
    if request.method == 'PUT':
        return franqueadosNewController.update_lead(idd)

#
# # INSERT LEAD APENAS E SOMENTE #
# @app.post('/api/v2/franqueados/lead/<cel>')
# @cross_origin()
# def insert_lead(cel: str):
#     body = request.json
#     return franqueadosNewController.create_lead_from_choris(cel)
#
#
# # GET ONE LEAD BY PHONE NUMBER #
# @app.get('/api/v2/franqueados/lead/<celular>')
# @cross_origin()
# def get_lead_by_celular(celular):
#     return franqueadosNewController.get_lead_by_celular(celular)
#
#
# # SEARCH LEADS BY ID COLABORATOR AND NAME #
# @app.get('/api/v2/franqueados/leads/<idcolab>/<nome>')
# @cross_origin()
# def pesquisa_leads_by_colab_nome(idcolab: int, nome: str):
#     return franqueadosNewController.pesquisa_leads_by_colab_nome(idcolab, nome)
#

##################################################################################################
######################################## GESTAO ##################################################
##################################################################################################


# GET INFO GESTAO BY CODIGO #
@app.get('/api/v1/gestao/info/orcamentos')
@cross_origin()
def get_info_orcamentos():
    return gestaoNewController.get_gestao_info_orcamentos()

#TODO
@app.get('/api/v2/gestao/info/<codigo>')
@cross_origin()
def get_info_gestao(codigo):
    return gestaoNewController.get_gestao_info(codigo)

#TODO
@app.get('/api/v2/gestao/orcamentos/<clienteid>')
@cross_origin()
def get_orcamentos_idclient(clienteid):
    return gestaoNewController.get_orcamentos_idclient(clienteid)


@app.get('/api/v1/gestao/orcamentos/vendedor/<idColaborador>')
@cross_origin()
def get_orcamento_valor(idColaborador):
    return gestaoNewController.get_orcamento_valor(idColaborador)


@app.get('/api/v1/gestao/orcamento/<CodigoOrcamento>')
@cross_origin()
def get_info_gestao_orcamento(CodigoOrcamento):
    return gestaoNewController.get_gestao_info_orcamento(CodigoOrcamento)


@app.get('/api/v2/gestao/orcamentos/items/<idpedido>')
@cross_origin()
def get_items_orcamentos(idpedido):
    return gestaoNewController.get_items_orcamento(idpedido)

@app.get('/api/v1/gestao/pedidos')
@cross_origin()
def get_pedidos():
    return gestaoNewController.get_pedidos()


@app.get('/api/v2/gestao/pedidos/<clienteid>')
@cross_origin()
def get_pedidos_idclient(clienteid):
    return gestaoNewController.get_pedidos_idclient(clienteid)


@app.get('/api/v2/gestao/pedidos/items/<idpedido>')
@cross_origin()
def get_items_pedido(idpedido):
    return gestaoNewController.get_items_pedido(idpedido)


##################################################################################################
####################################### SOCKET ###################################################
##################################################################################################

# SOCKET EMITER EXPANSAO #
@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


# SOCKET EMITER FRANQUEADOS #
@socketio.on('message-f')
def handle_message_f(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


# SIMPLE RENDER ROUTE FOR TESTING #
@app.route('/api/v2/develop')
@cross_origin()
def develop_view_socket():
    return render_template('develop.html')


# SIMPLE RENDER ROUTE FOR Controlling #
@app.route('/api/v2/listen')
@cross_origin()
def listen_view_socket():
    return render_template('listen.html')

