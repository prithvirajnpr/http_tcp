import socket
import threading

class ProxyServer:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((host,port))
        self.server_socket.listen(3)
        
        self.client_threads = []
        
        
    def start(self):
        while True:
            client_socket,client_address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client,args=(client_socket,client_address))
            self.client_threads.append(client_thread)
            client_thread.start()
            
    def handle_client(self,client_socket,client_address):
        #receive request from the client
        request = client_socket.recv(1024)
        
        #parse the request
        request_lines = request.decode().split("\r\n")
        #request_method = request_lines[0].split([0])
        request_url = request_lines[0].split()[1]
        print("-->",request_url)
        
        # Check for conditional headers
        if_modified_since = None
        for header in request_lines:
            if header.startswith("If-Modified-Since: "):
                if_modified_since = header.split(": ")[1]
                break
    
        # Forward the request to the web server
        web_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        web_server_socket.connect((request_url, 80))
    
        # Add the If-Modified-Since header to the request
        if if_modified_since is not None:
            web_server_socket.sendall(f"If-Modified-Since: {if_modified_since}\r\n".encode())
    
        # Send the rest of the request
        web_server_socket.sendall(request[len(request_lines[0]) + 2:])
    
        # Receive the response from the web server
        response = web_server_socket.recv(1024)
    
        # Parse the response
        response_lines = response.decode().split("\r\n")
        response_code = int(response_lines[0].split()[1])
    
        # Handle the response code
        if response_code == 200:
            # Forward the response to the client
            client_socket.sendall(response)
        elif response_code == 304:
            # Simply forward the response to the client
            client_socket.sendall(response)
        elif response_code == 404:
            # Return a custom 404 page to the client
            client_socket.sendall(b"<!DOCTYPE html><html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1><p>The requested page could not be found.</p></body></html>")
        else:
            # Handle other response codes as needed
            pass
    
        # Close the sockets
        client_socket.close()
        web_server_socket.close()
        
    def stop(self):
        for thread in self.client_threads:
            thread.join()
        self.server_socket.close()

proxy_server = ProxyServer("localhost",12801)
proxy_server.start()
