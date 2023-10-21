import socket

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_sock.bind(('127.0.0.1',12000))

server_sock.listen(1)

while True:
    client,address = server_sock.accept()
    
    msg = client.recv(2048).decode('utf-8').split("\n")
    
    print("------------------------------------------")
    count = 0
    for num in msg:
        print(f"{count}", num)
        count+=1
    print("------------------------------------------")
    request_method = msg[0].split()[0]
    request_url = msg[0].split()[1]
    print("[*] ",request_method," ---> ",request_url)
    
    
