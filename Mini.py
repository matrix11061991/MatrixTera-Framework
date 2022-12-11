import http.server

import socketserver

# Définissez les routes et les contrôleurs

routes = {

    '/': 'index',

    '/about': 'about',

}

controllers = {

    'index': lambda: '<h1>Accueil</h1>',

    'about': lambda: '<h1>À propos</h1>',

}

# Classe de contrôleur de base

class BaseController:

    def __init__(self, request, response):

        self.request = request

        self.response = response

    def get_html(self):

        return '<h1>Page non trouvée</h1>'

# Classe de contrôleur pour gérer les requêtes entrantes

class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Récupérez le contrôleur en fonction de la route

        if self.path in routes:

            controller = controllers[routes[self.path]]

        else:

            controller = controllers['default']

        # Créez une instance de contrôleur et obtenez le code HTML

        c = BaseController(self.request, self.response)

        html = c.get_html()

        # Envoyez la réponse

        self.send_response(200)

        self.send_header('Content-type', 'text/html')

        self.end_headers()

        self.wfile.write(bytes(html, 'utf-8'))

# Exécutez le serveur

with socketserver.TCPServer(('', 8000), RequestHandler) as httpd:

    httpd.serve_forever()

