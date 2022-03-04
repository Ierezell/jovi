from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import os
from pathlib import Path

os.chdir(Path(__file__).parent.joinpath("./dist"))
httpd = HTTPServer(('127.0.0.1', 4443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile=Path(__file__).parent.joinpath(
                                   "127.0.0.1-key.pem"),
                               certfile=Path(__file__).parent.joinpath(
                                   "127.0.0.1.pem"),
                               server_side=True)

httpd.serve_forever()
