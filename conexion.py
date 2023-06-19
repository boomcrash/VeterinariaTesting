#import database for mysql
import aiomysql

#libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion

async def getConexion():
    conn = await aiomysql.connect(host=configuracion['development'].MYSQL_HOST, user=configuracion['development'].MYSQL_USER, password=configuracion['development'].MYSQL_PASSWORD, db=configuracion['development'].MYSQL_DB, charset='utf8', cursorclass=aiomysql.DictCursor)
    return conn