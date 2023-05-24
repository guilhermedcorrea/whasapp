import re
import datetime
from app import db
from sqlalchemy import desc
from flask import jsonify, request
from app.utils import utils
from app.controllers import franquiasController
from app.models.franqueadosNewModel import CampanhaFranquia,\
    campanhaFranquia_schema, campanhasFranquia_schema




# GET ALL CAMPANHAS #
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


# GET CAMPANHA BY ID#
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