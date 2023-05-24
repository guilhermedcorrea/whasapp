from flask import jsonify
from ..models.waResponsavelModel import *

# CONTROLLER RESPONSAVEIS LEADS EXPANSÃO #


# PEGAR UM RESPONSAVEL POR TOKEN #
# GET ONE RESPONSIBLE BY TOKEN #
def get_waresponsavel_by_token(token):
    try:
        responsavel = WaResponsavel.query.filter(WaResponsavel.TokenBot == token).one()
    except:
        return None

    if responsavel:
        result = waresponsavel_schema.dump(responsavel)
        return result

    return jsonify({'message': 'Responsavel nao encontrado.'}), 404