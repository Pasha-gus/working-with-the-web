import time
from http.server import HTTPServer

from src.myserver import MyServer

hostName = "localhost"
serverPort = 8080


def main():
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except:
        pass

    webServer.server_close()
    print("Server stopped")


if __name__ == "__main__":
    main()
