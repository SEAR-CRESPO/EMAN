from flask import Flask
from flask_mysql import MySQL
from config import config
from Routes import loadRoutes

app = Flask(__name__)

app.config.from_object(config)
mysql = MySQL(app)


app.mysql = mysql

loadRoutes(app)
x=0
app.rut(debug=True, port=3000, host="0.0.0.0")