import socket


# Define the server host and port
server_host = "127.0.0.1"  # You can change this to your server's IP address
server_port = 7777

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server.bind((server_host, server_port))

# Listen for incoming connections
server.listen(5)

print(f"Server listening on {server_host}:{server_port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address}")

    # Receive and decode the client's request
    request = client_socket.recv(1024).decode()
    print("##Request:-\n",request)
    # Parse the request to get the requested file path
    request_lines = request.split("\n")
    print(f"--------\n{request_lines}\n-----------")
    print("Length of request lines:- ",len(request_lines))
    if len(request_lines) > 0:
        first_line = request_lines[0]
        file_path = first_line.split(" ")[1][1:]
        print("fileline..",first_line)
        print("file..",file_path)

        # Check if the file exists
        try:
            with open(file_path, "rb") as file:
                content = file.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(content)}\r\n\r\n".encode() + content
        except:
            # If the file doesn't exist, return a 404 Not Found response
            not_found_response = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"
            response = not_found_response.encode()

        # Send the response to the client
        client_socket.send(response)

        # Close the client socket
        client_socket.close()

server.close()



