from flask import Flask
from flask_mysqldb import MySQL
from config import config
from Routes import loadRoutes

app = Flask(__name__)

app.config.from_object(config)
mysql = MySQL(app)


app.mysql = mysql

loadRoutes(app)

app.run(debug=True, port=3000, host="0.0.0.0")