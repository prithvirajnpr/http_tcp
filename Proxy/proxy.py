import socket
import threading

class proxy:
    def __init__(self):
        self.serverip = "127.0.0.1" 
        self.serverport = 8888
        primary(self.serverip,self.serverport)
               


def funct(client_socket, client_address,server):
    # Receive and decode the client's request
    request = client_socket.recv(1024).decode()
    print(request)
    # Parse the request to get the requested file path
    lines = request.split("\n")
    if len(lines)>0 :
        #extracting the first line
        first = lines[1]
        ipport = first.split(" ")[1]
        ip,port = ipport.split(":")
        port=int(port)
        print("ip: ",ip)
        print("port: ",port)
        
        proxyclient(ip,port,request,client_socket)
        
    else:
        print("invalid request from client")
        
def connection(server,li,ct):
        
    while True:
        # Accept a connection from a client
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")
        ct=ct+1
        li.append(threading.Thread(target=funct,args=(client_socket, client_address,server)))
        li[ct-1].start()
    
    for i in range(0,ct):
        li[i].join()
    
    
    server.close()


def proxyclient(ip,port,request,client_socket):
    pclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    pclient.connect((ip, port))
    pclient.send(request.encode())
    response = pclient.recv(1048576)
    
    print(response)
    
    client_socket.send(response)
    
    # Close the connection
    pclient.close()

 

def createsock(serverip,serverport):

    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server.bind((serverip, serverport))
    return server


def primary(serverip,serverport):
    #global serverip
    #global serverport
    serverport = serverport
    serverip = serverip
    
    server = createsock(serverip,serverport)
    # Listen for incoming connections
    server.listen(5)
    
    print(f"Server listening on {serverip}:{serverport}")
    lst=[]
    cnt=0
    connection(server,lst,cnt)
    
proxy()



