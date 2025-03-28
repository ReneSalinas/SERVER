import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))

while True:
    msg = input("Manda un mensaje: ")
    client.send(msg.encode('utf-8'))
    
    if msg.upper() == "DESCONEXION":
        client.close()
        print("DESCONECTADO DEL SERVIDOR")
        break
    
    response = client.recv(1024).decode('utf-8')
    print(f"Servidor responde: {response}")