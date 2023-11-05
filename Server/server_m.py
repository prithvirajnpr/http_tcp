import socket
import threading

def fun(client_socket, client_address,server):
    # Receive and decode the client's request
    request = client_socket.recv(1024).decode()
    # Parse the request to get the requested file path
    lines = request.split("\n")
    
    if len(lines) > 0:
        first = lines[0]
        filepath = first.split(" ")[1]
        
        filepath=filepath[1:]
        response = readfile(filepath)
    sndclose(response,client_socket)
    

def sndclose(response,client_socket):
    # Send the response to the client
    client_socket.send(response)

    # Close the client socket
    client_socket.close()
    
    
def socketdet():

    global serverip
    global serverport
    
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return server

def readfile(file_path):
         
    # Check if the file exists
    try:
        with open(file_path, "rb") as file:
            content = file.read()
            response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(content)}\r\n\r\n".encode() + content
    except:
        # If the file doesn't exist, return a 404 Not Found response
        not_found_response = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"
        response = not_found_response.encode()
        
    return response
        

def connection(server,li,cn):
    while True:
        # Accept a connection from a client
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")
        cn=cn+1
        li.append(threading.Thread(target=fun,args=(client_socket, client_address,server)))
        li[cn-1].start()
        
    for i in range(0,cn):
        li[i].join()
    server.close()

serverip = "127.0.0.1"  
serverport = 7777

def main():
    server = socketdet()
    # Bind the socket to the host and port
    server.bind((serverip, serverport))
    # Listen for incoming connections
    server.listen(5)
    print(f"Server listening on {serverip}:{serverport}")
    lst=[]
    cnt=0
    connection(server,lst,cnt)
    

if __name__ == '__main__':
    main()

