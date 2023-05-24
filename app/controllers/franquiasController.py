from flask import jsonify
import random
from sqlalchemy import desc, func
from app.models.franquiasModel import Franquias, franquia_schema, franquias_schema


def random_franquia(cidade):
    try:
        franquia = Franquias.query.filter(Franquias.bitInaugurada, Franquias.Cidade.like(f'{cidade}')).all()
    except Exception as err:
        print(err)
        return None

    if franquia:
        result = random.choice(franquia)
        return result

    return None


def franquia_by_id(idd):
    try:
        franquia = Franquias.query.filter(Franquias.bitInaugurada, Franquias.Id == idd).one()
    except Exception as err:
        print(err)
        return None

    if franquia:
        return franquia

    return None


def get_franquias():
    try:
        franquia = Franquias.query.all()
    except Exception as err:
        print(err)
        return None

    if franquia:
        result = franquias_schema.dump(franquia)
        return jsonify({'Franquias': result}), 200

    return jsonify({'message': 'Nao Encontrado'}), 404


# PEGAR UM LEAD POR ID #
# GET ONE LEAD BY ID #
def get_franquia_by_id(idd):
    try:
        franquia = Franquias.query.filter(Franquias.Id == idd).one()
    except Exception as err:
        print(err)
        return None

    if franquia:
        result = franquia_schema.dump(franquia)
        return result

    return jsonify({'error': 'Franquia nao encontrada'}), 404
