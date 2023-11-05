import socket
import sys
# Define the target web server and the file to save the response

def sysargs():
    global serverhost
    global serverport
    global proxyhost
    global proxyport
    
    try:

        if len(sys.argv)>=5:
            
            serverhost = sys.argv[1]
            serverport = sys.argv[2]
            proxyhost = sys.argv[3]
            proxyport = sys.argv[4]
            
            serverport = int(serverport)
            proxyport = int(proxyport)
            
            # Create a socket object:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
            # Connect to the server
            client.connect((proxyhost, proxyport))
            
            # Send an HTTP GET request
            request = f"GET /helloworld.html HTTP/1.1\r\nHost: {serverhost}:{serverport}\r\n\r\n"
            response = senddata(client,request)
            # Extract the HTTP response headers and body
            headers, body = response.split(b"\r\n\r\n", 1)
            
            # Print the HTTP response headers
            print(headers.decode())
            return body,client
            
        elif len(sys.argv)>=3:
            
            serverhost = sys.argv[1]
            serverport = sys.argv[2]
            
            serverport = int(serverport)
            
            
            # Create a socket object:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the server
            client.connect((serverhost, serverport))
            
            # Send an HTTP GET request
            request = f"GET /helloworld.html HTTP/1.1\r\nHost: {serverhost}:{serverport}\r\n\r\n"
            response = senddata(client,request)
            # Extract the HTTP response headers and body
            headers, body = response.split(b"\r\n\r\n", 1)
            
            # Print the HTTP response headers
            print(headers.decode())
            return body,client
            
        
        else:
            print("Invalid arguments!!")
            sys.exit()
    except:
        print("unable to create socket")
    
def senddata(client,request):
    
    client.send(request.encode())
    
    # Receive and save the response
    response = client.recv(4096)
    print("......")
    # Close the connection
    client.close()
    return response

def savefile(body,save_file):
    
    # Save the response body to a file
    with open(save_file, "wb") as f:
        f.write(body)
    print(f"HTTP response saved to {save_file}")
    return save_file

from bs4 import BeautifulSoup

def objextract(body,save_file):

    soup = BeautifulSoup(body, 'html.parser')
    
    images = soup.find_all('img')
    
    try:

        if len(sys.argv)>=5:
            
            for img in images:
            	img_url = img.get('src')
            	print(img_url)
            	client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            	client1.connect((proxyhost, proxyport))
            	# Send an HTTP GET request
            	request = f"GET /{img_url} HTTP/1.1\r\nHost: {serverhost}:{serverport}\r\n\r\n"
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
                	client1.connect((serverhost, serverport))
                	# Send an HTTP GET request
                	request = f"GET /{img_url} HTTP/1.1\r\nHost: {serverhost}:{serverport}\r\n\r\n"
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
    except:
        print("unable to parse")
        
proxyhost= None
proxyport= None
serverhost = None
serverport = None

def main():
    save_file = "response1.html"
    body,client = sysargs()
    save_file = savefile(body,save_file)
    objextract(body, save_file)
    
    # Close the connection
    client.close()
    
if __name__ == '__main__':
    main()
    
