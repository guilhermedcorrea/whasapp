import jwt
import datetime
from app import app
from flask import request
from functools import wraps
from .usersController import *
from .franquiasController import *
from .waResponsavelController import *


# DECORATOR PARA PROTEGER AS ROTAS COM O TOKEN #

#Para utilizar esse decorator,
# precisamos apenas incluí-lo nas funções que queremos restringir o acesso.
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'authorization' in request.headers:
            token = request.headers['authorization']
        if not token:
            return jsonify({'alert': 'Token não informado.'}), 403
        if "Bearer" not in token:
            return jsonify({'error': 'Token invalido.'}), 403
        try:
            token_pure = token.replace("Bearer ", "")
            data = jwt.decode(token_pure, app.config['SECRET_KEY'], algorithms="HS256")
            if 'user' in data:
                current_user = user_by_username(data['user'])
            else:
                current_user = None
        except Exception as err:
            print(err)
            return jsonify({'error': 'Token invalido.'}), 403

        return f(current_user, *args, **kwargs)

    return decorated


# MÉTODO PARA AUTHENTICAR USUARIO RETORNANDO JWT TOKEN #
def authentication():
    auth = request.get_json()
    if 'username' not in auth or 'password' not in auth:
        return jsonify({'message': 'Sem permissão', 'WWW-Authenticate': 'Basic auth="Login requerido"'}), 401

    username = auth['username']
    password = auth['password']

    user = user_by_username(username)

    if not user:
        return jsonify({'message': 'Não encontrado'}), 404

    if user and user.Senha == password:
        result_user = get_user_by_username(username)
        result_franquia = get_franquia_by_id(user.IdUnidade)
        result_responsavel = get_waresponsavel_by_token(user.WppInstancia)

        token = jwt.encode({'user': user.Usuario, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8)},
                           app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({"message": "Logado com sucesso", "token": token,
                        "exp": datetime.datetime.now() + datetime.timedelta(hours=12),
                        "data": result_user,
                        "franquia": result_franquia,
                        "IdResponsavel": result_responsavel}), 200

    return jsonify({'message': 'Sem permissão', 'WWW-Authenticate': 'Basic auth="Login requerido"'}), 401
