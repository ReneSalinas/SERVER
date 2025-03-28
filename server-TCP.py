import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(5)
print("SERVER ENCENDIDO EN PUERTO 5000")
    
while True:
    connection, address = server.accept()
    print(f"CONEXION CON: {address}")
        
    while True:
        msg = connection.recv(1024).decode('utf-8')
        if not msg:
            break
        print(f"Cliente envia: {msg}")
            
        if msg.upper() == "DESCONEXION":
            connection.close()
            print("CLIENTE DESCONECTADO")
            break
        else:
            response = msg.upper()
            connection.send(response.encode('utf-8'))
