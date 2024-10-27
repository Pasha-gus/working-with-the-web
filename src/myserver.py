from http.server import BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    """
    Класс отвечающий за обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("contacts.html", "r", encoding="utf-8") as file:
            page = file.read()
        self.wfile.write(bytes(page, "utf-8"))
