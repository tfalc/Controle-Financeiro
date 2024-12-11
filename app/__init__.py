from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa o SQLAlchemy
db = SQLAlchemy()

def create_app():
    """
    Cria e configura o aplicativo Flask.
    """
    app = Flask(__name__)

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dashboard.db'  # Define o caminho do banco SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa notificações de modificações

    # Inicializa o banco de dados com o app
    db.init_app(app)

    # Importa e registra os blueprints
    from app.routes.main import main
    from app.routes.charts import charts
    from app.routes.export import export

    app.register_blueprint(main)  # Registra rotas principais
    app.register_blueprint(charts, url_prefix='/charts')  # Registra rotas de gráficos
    app.register_blueprint(export)  # Registra rota de exportação

    # Cria as tabelas no banco de dados se ainda não existirem
    with app.app_context():
        db.create_all()  # Garante que todas as tabelas sejam criadas

    return app
