# http_tcp

# HTTP Proxy

This Python script is designed to perform several tasks, including making HTTP requests to a target web server either directly or through a proxy server, saving the response to a file, and downloading images from the target server. It uses the `socket` library for network communication and `BeautifulSoup` for HTML parsing.

## Usage

Before running the script, make sure you have the necessary dependencies installed, such as `socket` and `BeautifulSoup`. You can install `BeautifulSoup` using pip:

```bash
pip install beautifulsoup4
```

To run the script, use the following command-line arguments:

- For direct HTTP requests:
  ```bash
  python client.py <target_host> <target_port>
  ```

- For HTTP requests through a proxy:
  ```bash
  python client.py <target_host> <target_port> <proxy_host> <proxy_port>
  ```

## How the Script Works

1. The script first checks the command-line arguments provided to determine whether to make a direct request to the target server or through a proxy.

2. It creates a socket object and connects to the specified server (either the target or the proxy).

3. It sends an HTTP GET request to the server, requesting the "/helloworld.html" page. The request is constructed with the host and port provided as command-line arguments.

4. The script then receives and saves the response in a file named "response1.html."

5. It uses `BeautifulSoup` to parse the HTML response and extracts all image URLs (img src attributes).

6. If the script was executed with proxy parameters, it proceeds to download each image using separate HTTP GET requests through the proxy server. For each image, it connects to the proxy server, sends an HTTP GET request, receives and saves the response to a file, and repeats this process for all images.

7. If no proxy parameters were provided, the script will download the images directly from the target server.

8. The script saves each image response in a separate file with the name corresponding to the image URL.

9. The HTTP response headers for both the main request and image requests are printed to the console.

10. The script closes the connections and ends.

## Note

- Be sure to provide valid command-line arguments to run the script successfully.

- Make sure that the `BeautifulSoup` library is installed and accessible.

- The script saves the main HTTP response in a file named "response1.html" and image responses with filenames corresponding to their URLs. If you want to change the save locations or filenames, you can modify the code accordingly.

- The script does not handle various error cases and may not work perfectly in all scenarios. Additional error handling and improvements can be added for production use.

- Ensure you have appropriate permissions to write files in the working directory.

- Make sure the target server and proxy server (if used) are running and accessible.
