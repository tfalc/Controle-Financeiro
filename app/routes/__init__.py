"""
Este arquivo inicializa o pacote `routes` e organiza as rotas do aplicativo.
"""

# Não há necessidade de adicionar código diretamente aqui, mas você pode usar o arquivo para gerenciar as importações de rotas
# e evitar que elas sejam feitas separadamente em outros lugares do projeto.

# Exemplo:
# Caso queira importar os blueprints diretamente daqui, faça o seguinte:
from .main import main
from .charts import charts
from .export import export

# Agora, em vez de importar cada rota individualmente em `app/__init__.py`, você pode usar:
# from app.routes import main, charts, export
