# Practica 6 - Arquitecturas-RESTful

## Introducción
El objetivo de esta práctica es mejorar los mecanismos de comunicación entre cliente y servidor implementados en las prácticas anteriores utilizando multithreading.

## Explicación del código
El código desarrollado se divide en dos partes: el Practica 1.1 y Practica 1.2.

### Practica 1.1
#### 1. Servidor (`server.ipynb`)

## Ejecución del código 
1. Desde Docker, arranca el contenedor donde tengas la base de datos de BiciMad.
   
2. Abre una terminal o línea de comandos en tu sistema.

3. Clona el repositorio con el siguiente comando:

    ```
    git clone https://github.com/202006359/Practica-6-Arquitecturas-RESTful
    ```

4. Dirigete a la carpeta donde hayas clonado el proyecto y abre la carpeta Practica 1.1

5. Una vez en la carpeta, desde la terminal ejecuta el siguiente comando para arrancar el servidor:

    ```
    py "server.py"
    ```

6. Con el servidor ya arrancado, se recomienda usar la aplicación Postman, o similar, para probar las funcionalidades descritas en el apartado *Explicación del código*.

*Para ejecutar la practica 1.2 es exactamente el mismo proceso, salvo que en el paso 3 abrimos la carperta Práctica 1.2 en vez de la carpeta Práctica 1.1*

## Capturas de pantalla (Practica 1.1 & Practica 1.2)
### Practica 1.1
#### Servidor
*Se observa que los mensajes de los clientes NO han seguido el orden correcto de impresión*
<img width="595" alt="image" src="https://github.com/202006359/Practica-5-Multithreading/assets/113789409/52ab0952-24f8-40d3-a513-5f47ca13dab9">


### Apartado 1.2
#### Servidor
*Se observa que los mensajes de los clientes SI han seguido el orden correcto de impresión*
<img width="595" alt="image" src="https://github.com/202006359/Practica-5-Multithreading/assets/113789409/d1d37ad4-48a8-45d5-92c1-d6d14d96fceb">

#### Emulador de clientes.
<img width="595" alt="image" src="https://github.com/202006359/Practica-5-Multithreading/assets/113789409/8afd2c96-bad0-419f-bcda-e65fb320fc29">



