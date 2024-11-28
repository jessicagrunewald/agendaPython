from flask import Flask

def create_app():
    # Configurações para o aplicativo Flask
    app = Flask(__name__)
    app.secret_key = "808080"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agenda.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Registro de rotas
    from app.routes import app as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
