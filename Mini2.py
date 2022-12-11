import http.server

import socketserver

# Définissez les routes et les contrôleurs

routes = {

    '/': 'index',

    '/about': 'about',

}

controllers = {

    'index': 'IndexController',

    'about': 'AboutController',

}

# Classe de contrôleur de base

class BaseController:

    def __init__(self, request, response):

        self.request = request

        self.response = response

    def get_html(self):

        return '<h1>Page non trouvée</h1>'

# Classe de contrôleur pour l'accueil

class IndexController(BaseController):

    def get_html(self):

        # Récupérez le modèle et générez la vue

        model = IndexModel()

        view = IndexView(model)

        return view.get_html()

# Classe de contrôleur pour la page "À propos"

class AboutController(BaseController):

    def get_html(self):

        # Récupérez le modèle et générez la vue

        model = AboutModel()

        view = AboutView(model)

        return view.get_html()

# Classe de modèle pour l'accueil

class IndexModel:

    def __init__(self):

        self.title = 'Accueil'

        self.message = 'Bienvenue sur la page d\'accueil'

# Classe de modèle pour la page "À propos"

class AboutModel:

    def __init__(self):

        self.title = 'À propos'

        self.message = 'Bienvenue sur la page "À propos"'

# Classe de vue pour l'accueil

class IndexView:

    def __init__(self, model):

        self.model = model

    def get_html(self):

        return '<h1>{}</h1><p>{}</p>'.format(self.model.title, self.model.message)

# Classe de vue pour la page "À propos"

class AboutView:

    def __init__(self, model):

        self.model = model

    def get_html(self):

        return '<h1>{}</h1><p>{}</p>'.format(self.model.title, self.model.message)

# Classe de contrôleur pour gérer les requêtes entrantes

class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Récupérez le contrôleur en fonction de la route

        if self.path in routes:

            controller_name = controllers[routes[self.path]]

        else:

            controller_name = controllers['default']

        # Créez une instance de contrôleur et obtenez le code HTML

        controller = globals()[controller_name](self.request, self.response)

