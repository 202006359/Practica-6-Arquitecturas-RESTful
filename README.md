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

### Practica 1.2
##### Consultas GET
1. Las consultas GET de la Practica 1.1 ahora verifican que el usuario este autenticado con admin:admin para poder ver todos los resultados. En su defecto se muestran solo 10.

##### Consulta PUT
1. `/actualizar_movimiento`: Permite actualizar el travel_time de una entrada específica.

##### Consulta DELETE
1. `/borrar_movimiento`: Permite borrar una entrada específica.

## Configuración de la Base de Datos
Asegúrese de tener una la de datos MySQL llamada 'ssdd' con las siguientes credenciales:

   Host: localhost
   Usuario: root
   Contraseña: ic@!SQL19
   
## Ejecución del código 
1. Desde Docker, arranca el contenedor donde tengas la base de datos de BiciMad (ssdd).
   
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

*Para ejecutar la Practica 1.2 es exactamente el mismo proceso, salvo que en el paso 3 abrimos la carperta Práctica 1.2 en vez de la carpeta Práctica 1.1*

## Pruebas realizadas (Practica 1.1 & Practica 1.2)
### Practica 1.1
#### Pruebas GET
1. `/fechas_disponibles`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/68a11f88-bee7-456c-b21b-ef577f8dd2ea)
2. `/idunplug_station_origen`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/580cb7a2-f4c2-4b8b-af89-5a4de8541bb6)
3. `/idplug_station_destino`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/b1f6dd26-5a52-4df7-8255-438f56daf08c)
4. `/movimientos_por_dia/<fecha>`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/4fecfd9b-3d95-4e9c-9118-9700ea1ac38e)
5. `/movimientos_por_dia_origen/<fecha>/<idunplug_base>`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/8f0c2208-03e0-47d9-ba81-fc2a71e610eb)
6. `/movimientos_por_dia_destino/<fecha>/<idplug_base>`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/e46a58ee-e21f-40c6-92a6-cd1768b8c4e1)
7. `/movimientos_por_dia_origen_destino/<fecha>/<idunplug_base>/<idplug_base>`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/e89bc148-2707-45c1-ace6-ba3528d002e5)
8. `/movimientos_por_dia_origen_destino_duracion_inferior/<fecha>/<idunplug_base>/<idplug_base>/<max_duracion>`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/44d6c8c3-34d1-421c-b3f2-108aad51374b)
9. `/movimientos_por_dia_origen_destino_duracion_superior/<fecha>/<idunplug_base>/<idplug_base>/<min_duracion>`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/f846ba44-6906-4682-be02-b05f9e932731)

#### Prueba POST con autentificación.
1.1 `/nuevo_movimiento` (*Headers*)
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/ef94d90f-e099-4f33-bd9b-b04383a257d2)
1.2`/nuevo_movimiento` (*JSON*)
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/28d781da-f113-4d3f-8b23-8c390e744b97)
1.3`/verificar_nuevos_movimientos`
![image](https://github.com/202006359/Practica-6-Arquitecturas-RESTful/assets/113789409/27b8a646-2336-4a21-99ba-2a631a6c4a21)

### Practica 1.2
VICENTE



