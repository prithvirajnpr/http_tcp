import socket
import sys

# Define the target web server and the file to save the response
"""
proxy_host="127.0.0.1"
proxy_port=8888
target_host = "127.0.0.1"
target_port = 7777
"""
save_file = "response1.html"

if len(sys.argv)>=5:
    target_host = sys.argv[1]
    target_port = sys.argv[2]
    proxy_host = sys.argv[3]
    proxy_port = sys.argv[4]
    
    target_port = int(target_port)
    proxy_port = int(proxy_port)
    
    # Create a socket object:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client.connect((proxy_host, proxy_port))
    
    # Send an HTTP GET request
    request = f"GET /helloworld.html HTTP/1.1\r\nHost: {target_host}:{target_port}\r\n\r\n"
    
elif len(sys.argv)>=3:
    target_host = sys.argv[1]
    target_port = sys.argv[2]
    
    target_port = int(target_port)
    
    
    # Create a socket object:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client.connect((target_host, target_port))
    
    # Send an HTTP GET request
    request = f"GET /helloworld.html HTTP/1.1\r\nHost: {target_host}:{target_port}\r\n\r\n"

else:
    print("Invalid arguments!!")
    sys.exit()
    
    
client.send(request.encode())

# Receive and save the response
response = client.recv(4096)
print("......")
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

if len(sys.argv)>=5:
    

    for img in images:
    	img_url = img.get('src')
    	print(img_url)
    	client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	client1.connect((proxy_host, proxy_port))
    	# Send an HTTP GET request
    	request = f"GET /{img_url} HTTP/1.1\r\nHost: {target_host}:{target_port}\r\n\r\n"
    	client1.send(request.encode())
    
    	# Receive and save the response
    	response = client1.recv(1048576)
    	
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
        
elif len(sys.argv)>=3:
    
        for img in images:
        	img_url = img.get('src')
        	print(img_url)
        	client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	client1.connect((target_host, target_port))
        	# Send an HTTP GET request
        	request = f"GET /{img_url} HTTP/1.1\r\nHost: {target_host}:{target_port}\r\n\r\n"
        	client1.send(request.encode())
        
        	# Receive and save the response
        	response = client1.recv(1048576)
        	
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
else:
    print("unable to parse objects")
    sys.exit()
    

# Close the connection
client.close()
