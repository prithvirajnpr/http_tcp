# Http_tcp

This Python script implements an HTTP proxy server that can intercept and cache images requested by clients. It also includes the ability to save the entire HTML response to a file.

## How the Proxy Works

The script does the following:

1. Accepts command-line arguments to specify the target web server, target port, and proxy server details (if available).
2. Establishes a connection to the target web server.
3. Sends an HTTP GET request to the target web server.
4. Receives and saves the HTML response to a file.
5. Parses the HTML response using BeautifulSoup to extract image URLs.
6. If a proxy server is specified, it connects to the proxy server and sends GET requests for each image URL.
7. Caches the image responses in memory, making them available for future client requests.
8. For each client request, the proxy server checks if the requested image is in the cache. If so, it serves the image from the cache. Otherwise, it fetches the image from the target web server and caches it for future requests.
9. The proxy server runs in a threaded fashion, allowing multiple clients to be served simultaneously.

## How to Use the Script

To use the script, you can run it from the command line with the following arguments:

- `target_host`: The host of the target web server.
- `target_port`: The port of the target web server.
- `proxy_host` (optional): The host of the proxy server.
- `proxy_port` (optional): The port of the proxy server.

Here are some example usages:

### Without a Proxy Server

```bash
python proxy_server.py target_host target_port
```

### With a Proxy Server

```bash
python proxy_server.py target_host target_port proxy_host proxy_port
```

## Readme.md

You can create a `readme.md` file to provide documentation for your script. Here's a basic template:

---

# HTTP Proxy Server with Image Caching

This Python script implements an HTTP proxy server that intercepts and caches images requested by clients. It also allows you to save the entire HTML response to a file.

## Features

- Acts as an HTTP proxy server for clients.
- Caches image responses for future requests.
- Allows you to specify a target web server and port.
- Supports the use of a proxy server for requests.
- Multithreaded to serve multiple clients simultaneously.

## Prerequisites

- Python 3.x
- Required Python libraries (can be installed via `pip`):
  - `socket`
  - `bs4` (BeautifulSoup)
  
## Usage

1. Run the script from the command line with the following arguments:

   Without a proxy server:

   ```bash
   python proxy_server.py target_host target_port
   ```

   With a proxy server:

   ```bash
   python proxy_server.py target_host target_port proxy_host proxy_port
   ```

2. The proxy server will start listening for incoming connections.

## Configuration

- Modify the `save_file` variable to specify the file where the HTML response should be saved.

## Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [OpenAI](https://openai.com) for providing the GPT-3.5 model.

---

Feel free to customize and expand the readme as needed for your project.
