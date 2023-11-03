import socket

server_host = "127.0.0.1"  
server_port = 8888

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
	print(request)
	# Parse the request to get the requested file path
	request_lines = request.split("\n")
	if len(request_lines)>0 :
		first_line = request_lines[1]
		ipport = first_line.split(" ")[1]
		ip,port = ipport.split(":")
		port=int(port)
		print("fileline..",first_line)
		print("ip..",ip)
		print("port..",port)


		pclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# Connect to the server
		pclient.connect((ip, port))
		pclient.send(request.encode())
		response = pclient.recv(1048576)
		
		print(response)

		client_socket.send(response)

		# Close the connection
		pclient.close()

	
server.close()

