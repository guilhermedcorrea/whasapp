from flask import jsonify
from sqlalchemy.orm import load_only
from ..models.usersModel import *
from ..models.colaboratorModel import *
# CONTROLLER USUARIOS HAUSZ #


# PEGAR UM LEAD POR USUARIO SEM ENVIAR COMO RESPOSTA HTTP #
# GET ONE LEAD BY USERNAME WITHOUT RETURN AS HTTP RESPONSE #
def user_by_username(username):
    try:
        return Users.query.filter(Users.Usuario == username).one()
    except Exception as err:
        print(err)
        return None


# PEGAR TODOS OS USUARIOS #
# GET ALL USERS #
# BE CAREFUL #
def get_users():
    try:
        users = Users.query.all()
    except Exception as err:
        print(err)
        return None

    if users:
        result = users_schema.dump(users)
        return jsonify({'usuarios': result})
    return jsonify({'error': 'Nao Encontrado.'}), 404


# PEGAR LEAD POR USUARIO/EMAIL #
# GET LEAD BY USERNAME EX: USER@EMAIL.COM.BR #
def get_user_by_username(username):
    try:
        user = Users.query.filter(Users.Usuario == username).one()
    except Exception as err:
        print(err)
        return None

    if user:
        result = user_schema.dump(user)
        return result
    return jsonify({'error': 'Nao Encontrado.'}), 404


def get_vendedores_by_franquia(franquia):
    fields = ('Id', 'Nome', 'Email', 'IdUnidade')
    try:
        users = Users.query.filter(Users.bitAtivo, Users.BitVendedor, Users.IdUnidade == franquia)\
            .options(load_only(*fields))\
            .all()
    except Exception as err:
        print(err)
        return None

    if users:
        result = users_schema.dump(users)
        return jsonify({"vendedores": result})

    return jsonify({}), 204
