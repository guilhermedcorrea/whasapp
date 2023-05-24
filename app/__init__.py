from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_socketio import SocketIO


# ARQUIVO DE INICIALIZAÇÃO #
# CONTEM A INSTANCIA DO FLASK, SOCKETIO, SQLALCHEMY E MARSHMALLOW #
# CONTEM CONFIGURAÇÕES DE CORS E CHAMADA PARA AS CONFIGURAÇÕES DO APP FLASK #

app = Flask(__name__)
app.config.from_object('config')
socketio = SocketIO(app, cors_allowed_origins="*")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db = SQLAlchemy(app)
ma = Marshmallow(app)


# NÃO SUBIR ESSES IMPORTS PARA NÃO CRIAR REFERENCIA CIRCULAR #
# DO NOT MOVE THESES IMPORT #
from .models import usersModel
from .routes import routes


