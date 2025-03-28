### INSTRUCCIONES PARA ENCENDER SERVER TCP Y CLIENTE
#### PASOS A SEGUIR PARA EJECUTAR SERVIDOR:

<b> 1. Abrir terminal. </br>
    2. Escribir este comando "python server-TCP.py". </br>
    3. Dar Enter. </br>
    4. Se sabra que encendio correctamente el SERVIDOR si se muestra este mensaje en la terminal *"SERVER ENCENDIDO EN PUERTO 5000"*. </br>

#### PASOS A SEGUIR PARA EJECUTAR CLIENTE:
<b> 1. Abrir nueva terminal. </br>
    2. Escribir este comando "python client-TCP.py". </br>
    3. Dar Enter o Intro. </br>
    4. Se sabra que encendio correctamente el CLIENTE si se muestra en la terminal *"Manda un mensaje: "*. </br>

</br>

#### PASOS A SEGUIR PARA PRUEBAS MANUALES: </br>

##### PASOS A SEGUIR PARA CONEXION ESTABLECIDA:
<b> 1. Dirijase en la terminal donde se esta ejecutando el SERVIDOR. </br>
    2. Se notara que aparecio un mensaje en la terminal diciendo *"CONEXION CON: (DATOS DE DIRECCION)"*. </br>
    3. Ahora dirijase en la terminal donde se esta ejecutando el CLIENTE. </br>
    4. De click al final de "Manda un mensaje: ". </br>
    5. Escriba el texto que desee que para este ejemplo sera "hola servidor". </br>
    6. Dar Enter o Intro. </br>
    7. Automaticamente se vera un mensaje que viene desde el SERVIDOR en la terminal del CLIENTE que dira *"Servidor responde: HOLA SERVER"* regresara el mensaje enviado desde CLIENTE en mayúsculas. </br>
    8. Dirijase a la terminal donde se esta ejecutando el SERVER. </br>
    9. Se observara un mensaje nuevo que dira *"Cliente envia: hola server"* o dependiendo el mensaje que se envie desde CLIENTE. </br>
    10. Listo la conexion ha sido un exito y se han podido escuchar y responder tanto el server como el cliente.

</br>

##### PASOS A SEGUIR PARA DESCONEXION:
<b> 1. Ya habiendo realizado con exito los pasos anteriores para establecer conexion se puede hacer estos pasos. </br>
    2. Dirijase en la terminal donde se esta ejecutando el CLIENTE. </br>
    3. Ahora se escribira en "Manda un mensaje: " la palabra "DESCONEXION". </br>
    4. Ahora saldra automaticamente un nuevo mensaje en la terminal diciendo *"DESCONECTADO DEL SERVIDOR"* y se terminara de ejecutar el programa. </br>
    5. Ahora dirijase a la terminal donde se esta ejecutando el SERVIDOR y tendra dos mensaje ahi el de "Cliente envia: DESCONEXION" y "CLIENTE DESCONECTADO" lo cual significa que se termino la conexion del CLIENTE con el del SERVIDOR. </br>
    6. Listo ya se termino la conexion de ese CLIENTE al SERVIDOR.

</br>

#### VALORES Y RESULTADOS DE PRUEBAS MANUALES </br>

##### CONEXION ESTABLECIDA
* En terminal del servidor "python server-TCP.py".
* En terminal de cliente "python client-TCP.py".
* Manda un mensaje: hola server.
* Servidor responde: HOLA SERVER.

##### DESCONEXIÓN
* Manda un mensaje: DESCONEXION.
* Servidor responde: DESCONECTADO DEL SERVIDOR
* Servidor aparece Cliente envía: DESCONEXION y CLIENTE DESCONECTADO
* Se cierra la conexión del cliente.