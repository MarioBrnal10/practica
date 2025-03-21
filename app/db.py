from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # Cargar variables de entorno

# Depuración: Imprimir configuración antes de conectar
print("MySQL Config:", os.getenv('MYSQL_HOST'), os.getenv('MYSQL_USER'), os.getenv('MYSQL_DB'))

# Configuración de MySQL
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')  # Asegurar que toma una cadena vacía
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 3306))
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Conexión con MySQL
mysql = MySQL(app)
