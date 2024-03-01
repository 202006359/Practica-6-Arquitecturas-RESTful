# Practica 6 - Arquitecturas-RESTful

## Introducción
En esta práctica, se ha implementado un ejemplo real de una arquitectura RESTful que permite acceder a los datos almacenados en una base de datos. Se ha utilizado el lenguaje de programación Python y el framework Flask para construir un servidor REST con un API que permite consultar una base de datos que contiene el archivo bicimad.csv.

## Explicación del código
El código desarrollado se divide en dos partes: el Practica 1.1 y Practica 1.2.

### Practica 1.1
#### 1. Servidor (`server.ipynb`)
##### Autenticación de Usuario

Se implementa un sistema de autenticación de usuario utilizando HTTP Basic Auth. Actualmente, solo se permite la autenticación de un usuario administrador ('admin'/'admin'). 

##### Consultas GET

1. `/fechas_disponibles`: Consulta la cantidad de fechas disponibles en la base de datos.
2. `/idunplug_station_origen`: Consulta los códigos de las estaciones de origen.
3. `/idplug_station_destino`: Consulta los códigos de las estaciones de destino.
4. `/movimientos_por_dia/<fecha>`: Recupera todos los movimientos para una fecha específica.
5. `/movimientos_por_dia_origen/<fecha>/<idunplug_base>`: Recupera los movimientos para una fecha que inician en una estación de origen específica.
6. `/movimientos_por_dia_destino/<fecha>/<idplug_base>`: Recupera los movimientos para una fecha que terminan en una estación de destino específica.
7. `/movimientos_por_dia_origen_destino/<fecha>/<idunplug_base>/<idplug_base>`: Recupera los movimientos para una fecha que inician en una estación de origen y terminan en una estación de destino específicas.
8. `/movimientos_por_dia_origen_destino_duracion_inferior/<fecha>/<idunplug_base>/<idplug_base>/<max_duracion>`: Recupera los movimientos para una fecha que inician en una estación de origen, terminan en una estación de destino y tienen una duración de trayecto inferior a un valor específico.
9. `/movimientos_por_dia_origen_destino_duracion_superior/<fecha>/<idunplug_base>/<idplug_base>/<min_duracion>`: Recupera los movimientos para una fecha que inician en una estación de origen, terminan en una estación de destino y tienen una duración de trayecto superior a un valor específico.
10. `/verificar_nuevos_movimientos`: Ruta adicional para verificar si se ha agregado una nueva línea en la base de datos.

##### Consulta POST

1. `/nuevo_movimiento`: Permite introducir una nueva línea en la base de datos con información específica sobre un movimiento de bicicleta. Requiere autenticación de usuario administrador.
## Ejecución del código 
1. Desde Docker, arranca el contenedor donde tengas la base de datos de BiciMad.
   
2. Abre una terminal o línea de comandos en tu sistema.

3. Clona el repositorio con el siguiente comando:

    ```
    git clone https://github.com/202006359/Practica-6-Arquitecturas-RESTful
    ```

4. Dirigete a la carpeta donde hayas clonado el proyecto y abre la carpeta Practica 1.1

5. Una vez en la carpeta, desde la terminal ejecuta el siguiente comando para arrancar el servidor (asegurate de tener Python instalado):

    ```
    py "server.py"
    ```

6. Con el servidor ya arrancado, se recomienda usar la aplicación Postman, o similar, para probar las funcionalidades descritas en el apartado *Explicación del código*.

*Para ejecutar la practica 1.2 es exactamente el mismo proceso, salvo que en el paso 3 abrimos la carperta Práctica 1.2 en vez de la carpeta Práctica 1.1*

## Pruebas realizadas (Practica 1.1 & Practica 1.2)
### Practica 1.1
#### Pruebas GET
*Se observa que los mensajes de los clientes NO han seguido el orden correcto de impresión*
<img width="595" alt="image" src="https://github.com/202006359/Practica-5-Multithreading/assets/113789409/52ab0952-24f8-40d3-a513-5f47ca13dab9">

#### Prueba POST con autentificación.

### Apartado 1.2
#### Servidor
*Se observa que los mensajes de los clientes SI han seguido el orden correcto de impresión*
<img width="595" alt="image" src="https://github.com/202006359/Practica-5-Multithreading/assets/113789409/d1d37ad4-48a8-45d5-92c1-d6d14d96fceb">

#### Emulador de clientes.
<img width="595" alt="image" src="https://github.com/202006359/Practica-5-Multithreading/assets/113789409/8afd2c96-bad0-419f-bcda-e65fb320fc29">



