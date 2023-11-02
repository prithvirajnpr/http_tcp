import socket

# Define the target web server and the file to save the response
target_host = "127.0.0.1"
target_port = 7777
save_file = "response1.html"

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((target_host, target_port))

# Send an HTTP GET request
request = f"GET /helloworld.html HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
client.send(request.encode())

# Receive and save the response
response = b""
while True:
    data = client.recv(4096)
    if not data:
        break
    response += data

# Close the connection
client.close()

# Extract the HTTP response headers and body
headers, body = response.split(b"\r\n\r\n", 1)

# Print the HTTP response headers
print(headers.decode())

# Save the response body to a file
with open(save_file, "wb") as f:
    f.write(body)

print(f"HTTP response saved to {save_file}")

from bs4 import BeautifulSoup


soup = BeautifulSoup(body, 'html.parser')

images = soup.find_all('img')

for img in images:
	img_url = img.get('src')
	print(img_url)
	client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client1.connect((target_host, target_port))
	# Send an HTTP GET request
	request = f"GET /{img_url} HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
	client1.send(request.encode())

	# Receive and save the response
	response = b""
	while True:
	    data = client1.recv(4096)
	    if not data:
	    	break
	    response += data


	print(response)
	# Extract the HTTP response headers and body
	headers, body = response.split(b"\r\n\r\n", 1)

	# Print the HTTP response headers
	print(headers.decode())

	# Save the response body to a file
	with open(img_url, "wb") as f:
	    f.write(body)

	print(f"HTTP response saved to {save_file}")
	# Close the connection
	client1.close()

# Close the connection
client.close()
