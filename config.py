import os
from dotenv import load_dotenv

# encuentra y carga el archivo .env
load_dotenv()

class config:
    MYSQL_HOST     =  os.getenv('MYSQL_HOST')
    MYSQL_USER     =  os.getenv('MYSQL_USER')
    MYSQL_PASSWORD =  os.getenv('MYSQL_PASSWORD')
    MYSQL_DB       =  os.getenv('MYSQL_DB')
    MYSQL_PORT     =  int( os.getenv('MYSQL_PORT'))

    MYSQL_SSL = {
        "ca": "/etc/secrets/aiven-ca.pem",
    }

# esta clase sirve para cargar la configuracion de la base
# de datos desde un archivo .env y almacenarla en variables de clases  