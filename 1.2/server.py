from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
import mysql.connector
import pandas as pd

auth = HTTPBasicAuth()

app = Flask(__name__)

# Configurar la conexión a la base de datos MySQL
connection = mysql.connector.connect(host='localhost',
                                     database='ssdd',
                                     user='root',
                                     password='ic@!SQL19')

# Función para autenticar el usuario
@auth.verify_password
def verify(user, password):                         
    if user == 'admin' and password == 'admin':
        return True
    return False

# Función para ejecutar consultas SQL
def execute_query(query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
# 1. Ruta para consultar la cantidad de fechas disponibles en la base de datos
@app.route('/fechas_disponibles', methods=['GET'])
def get_fechas_disponibles():
    query = "SELECT COUNT(DISTINCT fecha) FROM bicimad"
    result = execute_query(query)
    return jsonify({'Numero de fechas disponibles': result[0][0]})

# 2. Ruta para consultar los códigos de las "idunplug_station" de origen
@app.route('/idunplug_station_origen', methods=['GET'])
def get_base_stations_origen():
    limite = "" if auth.current_user() else " LIMIT 10"
    query = f"SELECT DISTINCT idunplug_station FROM bicimad {limite}"
    result = execute_query(query)
    return jsonify({'Codigos de las Estaciones de origen': [row[0] for row in result]})

# 3. Ruta para consultar los códigos de las "idplug_station" de destino
@app.route('/idplug_station_destino', methods=['GET'])
def get_base_stations_destino():
    limite = "" if auth.current_user() else " LIMIT 10"
    query = f"SELECT DISTINCT idplug_station FROM bicimad {limite}"
    result = execute_query(query)
    return jsonify({'Codigos de las Estaciones destino': [row[0] for row in result]})

# 4. Ruta para recuperar todos los movimientos para un determinado día
@app.route('/movimientos_por_dia/<string:fecha>', methods=['GET'])
def get_movimientos_por_dia(fecha):
    # Se aplica un límite de 10 resultados si el usuario no está autenticado como administrador
    limite = "" if auth.current_user() else " LIMIT 10"
    query = f"SELECT * FROM bicimad WHERE fecha = '{fecha}'{limite}"
    result = execute_query(query)
    return jsonify({'Movimientos de la fecha ' + fecha: result})

# 5. Ruta para recuperar todos los movimientos para un determinado día que hagan un trayecto iniciado en una determinada base de origen
@app.route('/movimientos_por_dia_origen/<string:fecha>/<int:idunplug_base>', methods=['GET'])
def get_movimientos_por_dia_origen(fecha, idunplug_base):
    limite = "" if auth.current_user() else " LIMIT 10"
    query = f"SELECT * FROM bicimad WHERE fecha = '{fecha}' AND idunplug_base = {idunplug_base} {limite}"
    result = execute_query(query)
    return jsonify({'Movimientos de la fecha ' + fecha + ' en la base de origen ' + str(idunplug_base): result})

# 6. Ruta para recuperar todos los movimientos para un determinado día que hagan un trayecto finalizado en una determinada base de destino
@app.route('/movimientos_por_dia_destino/<string:fecha>/<int:idplug_base>', methods=['GET'])
def get_movimientos_por_dia_destino(fecha, idplug_base):
    limite = "" if auth.current_user() else " LIMIT 10"
    query = f"SELECT * FROM bicimad WHERE fecha = '{fecha}' AND idplug_base = {idplug_base}{limite}"
    result = execute_query(query)
    return jsonify({'Movimientos de la fecha ' + fecha + ' en la base destino ' + str(idplug_base): result})

# 7. Ruta para recuperar todos los movimientos para un determinado día que hagan un trayecto iniciado en una determinada base de origen y finalizado en una determinada base de destino
@app.route('/movimientos_por_dia_origen_destino/<string:fecha>/<int:idunplug_base>/<int:idplug_base>', methods=['GET'])
def get_movimientos_por_dia_origen_destino(fecha, idunplug_base, idplug_base):
    limite = "" if auth.current_user() else " LIMIT 10"
    query = f"SELECT * FROM bicimad WHERE fecha = '{fecha}' AND idunplug_base = {idunplug_base} AND idplug_base = {idplug_base} {limite}"
    result = execute_query(query)
    return jsonify({'Movimientos de la fecha ' + fecha + ' en la base origen ' + str(idunplug_base) + ' y en la base destino ' + str(idplug_base): result})


# 8.1 Ruta para recuperar todos los movimientos para un determinado día que hagan un trayecto iniciado en una determinada base de origen y finalizado en una determinada base de destino y con una duración de trayecto inferior a un determinado valor
@app.route('/movimientos_por_dia_origen_destino_duracion_inferior/<string:fecha>/<int:idunplug_base>/<int:idplug_base>/<int:max_duracion>', methods=['GET'])
def get_movimientos_por_dia_origen_destino_duracion_inferior(fecha, idunplug_base, idplug_base, max_duracion):
    limite = "" if auth.current_user() else " LIMIT 10"
    query = f"SELECT * FROM bicimad WHERE fecha = '{fecha}' AND idunplug_base = {idunplug_base} AND idplug_base = {idplug_base} AND travel_time < {max_duracion}{limite}"
    result = execute_query(query)
    return jsonify({'Movimientos de la fecha ' + fecha + ' en la base origen ' + str(idunplug_base) + ' y en la base destino ' + str(idplug_base)
                    + " con una duración de trayecto inferior a " + str(max_duracion): result})

# 8.2 Ruta para recuperar todos los movimientos para un determinado día que hagan un trayecto iniciado en una determinada base de origen y finalizado en una determinada base de destino y con una duración de trayecto superior a un determinado valor
@app.route('/movimientos_por_dia_origen_destino_duracion_superior/<string:fecha>/<int:idunplug_base>/<int:idplug_base>/<int:min_duracion>', methods=['GET'])
def get_movimientos_por_dia_origen_destino_duracion_superior(fecha, idunplug_base, idplug_base, min_duracion):
    limite = "" if auth.current_user() else " LIMIT 10"
    query = f"SELECT * FROM bicimad WHERE fecha = '{fecha}' AND idunplug_base = {idunplug_base} AND idplug_base = {idplug_base} AND travel_time > {min_duracion}{limite}"
    result = execute_query(query)
    return jsonify({'Movimientos de la fecha ' + fecha + ' en la base origen ' + str(idunplug_base) + ' y en la base destino ' + str(idplug_base)
                    + " con una duración de trayecto superior a " + str(min_duracion): result})



# 9. Ruta para introducir una nueva línea en la base de datos
@app.route('/nuevo_movimiento', methods=['POST'])
@auth.login_required
def agregar_movimiento():
    if request.json:
        fecha = request.json['fecha']
        ageRange = request.json['ageRange']
        user_type = request.json['user_type']
        idunplug_station = request.json['idunplug_station']
        idplug_station = request.json['idplug_station']
        idunplug_base = request.json['idunplug_base']
        idplug_base = request.json['idplug_base']
        travel_time = request.json['travel_time']
        fichero = request.json['fichero'] #Establecido segun el enunciado
        
        query = f"INSERT INTO bicimad (fecha, ageRange, user_type, idunplug_station, idplug_station, idunplug_base, idplug_base, travel_time, Fichero) VALUES ('{fecha}', '{ageRange}', '{user_type}', '{idunplug_station}', '{idplug_station}', '{idunplug_base}', '{idplug_base}', '{travel_time}', '{fichero}')"
        execute_query(query)
        return jsonify({'message': 'Movimiento agregado correctamente.'}), 201
    else:
        return jsonify({'error': 'Datos incorrectos.'}), 400

# EXTRA Ruta para verificar si se ha agregado una nueva línea en la base de datos
@app.route('/verificar_nuevos_movimientos', methods=['GET'])
def verificar_nuevo_movimiento():
    query = "SELECT * FROM bicimad WHERE Fichero = 0"
    result = execute_query(query)
    return jsonify({'message': result})

#Actualizar el tiempo de una entrada específica
@app.route('/actualizar_movimiento', methods=['PUT'])
@auth.login_required
def actualizar_movimiento():
    data = request.json
    query = f"""
    UPDATE bicimad
    SET travel_time = {data['travel_time']}
    WHERE fecha = '{data['fecha']}' AND ageRange = '{data['ageRange']}' AND user_type = '{data['user_type']}'
    AND idunplug_station = '{data['idunplug_station']}' AND idplug_station = '{data['idplug_station']}'
    AND idunplug_base = '{data['idunplug_base']}' AND idplug_base = '{data['idplug_base']}'
    """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    if cursor.rowcount == 0:
        return jsonify({'message': 'No se encontró la entrada para actualizar.'}), 404
    return jsonify({'message': 'Movimiento actualizado correctamente.'}), 200  
#Eliminar una entrada específica
@app.route('/borrar_movimiento', methods=['DELETE'])
@auth.login_required
def eliminar_movimiento():
    parametros = request.json
    condiciones = " AND ".join([f"{k} = '{v}'" for k, v in parametros.items() if v is not None])
    query = f"DELETE FROM bicimad WHERE {condiciones}"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    if cursor.rowcount == 0:
        return jsonify({'message': 'No se encontraron entradas para eliminar.'}), 404
    return jsonify({'message': f'Se eliminaron {cursor.rowcount} entradas.'}), 200

if __name__ == '__main__':
    app.run(port=6878, debug=True)
