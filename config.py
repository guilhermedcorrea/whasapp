from dotenv import load_dotenv
from sqlalchemy.engine import URL
from urllib.parse import quote
import os

# ARQUIVO DE CONFIGURAÇÕES CHAMADO NO ARQUIVO DE INICIALIZAÇÃO /APP/__INIT__.PY #
# CONFIGURAÇÕES DE CONEXÃO COM O BANCO DE DADOS TANTO PARA DESENVOLVIMENTO/PRODUÇÃO #

# DOTENV/.ENV HAS BEEN USED TO PROTECT SENSIBLE INFORMATION #
load_dotenv()

connection_string_hausz = os.environ.get('CON_STRING')
connection_string_hauszmapa = os.environ.get('CON_HAUSZMAPA_STRING')
print(connection_string_hausz)
print(connection_string_hauszmapa)
connection_url_hausz = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_hausz})

connection_string_smsfire = os.environ.get('CON_FIRE_STRING')
connection_url_smsfire = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_smsfire})

connection_url_hauszmapa = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_hauszmapa})


server = os.environ.get('SERVER')
server_hm = os.environ.get('SERVER_HM')
database_hausz = os.environ.get('DATABASEHAUSZ')
database_smsfire = os.environ.get('DATABASEFIRE')
database_hauszmapa = os.environ.get('DATABASEHAUSZMAPA')

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

# URL PRODUCTION WITH QUOTE, SO CAN WORK ON LINUX UBUNTU 18.04 #
engine_string_hausz = f"mssql+pyodbc://{username}:{quote(password)}@{server}/{database_hausz}?driver=ODBC+Driver+17+for+SQL+Server"
engine_string_fire = f"mssql+pyodbc://{username}:{quote(password)}@{server}/{database_smsfire}?driver=ODBC+Driver+17+for+SQL+Server"

engine_string_hauszmapa = f"mssql+pyodbc://{username}:{quote(password)}@{server_hm}/{database_hauszmapa}?driver=ODBC+Driver+17+for+SQL+Server"

key = os.environ.get('SECRET_KEY')  # --> SECRET KEY FOR CRYPTO TOKENS <-- #

# Development
SQLALCHEMY_DATABASE_URI = connection_url_hausz   # --> CONECTION USED FOR SQL DATABASE <-- #
SQLALCHEMY_BINDS = {
    "smsfire": connection_url_smsfire,
    "HauszMapa": connection_url_hauszmapa
}

# SQLALCHEMY_DATABASE_URI = engine_string_hausz   # --> CONECTION USED FOR SQL DATABASE <-- #
# SQLALCHEMY_BINDS = {
#     "smsfire": engine_string_fire,
#      "HauszMapa": engine_string_hauszmapa
# }


SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
JSON_SORT_KEYS = True
DEBUG = True  # --> CHANGE TO FALSE FOR PRODUCTION <-- #
