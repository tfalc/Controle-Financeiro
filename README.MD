Dashboard Web
Visão Geral
Este sistema é um dashboard web desenvolvido com Flask para gerenciamento de transações financeiras. Ele permite:

Adicionar, editar, excluir e visualizar transações.
Gerar gráficos interativos (barras, linhas e pizza).
Exportar os dados em formato CSV.
Estrutura do Projeto
project/
├── app/
│   ├── __init__.py        # Inicialização do app Flask e configuração do banco de dados
│   ├── models.py          # Modelo do banco de dados
│   ├── routes/            # Rotas da aplicação
│   │   ├── __init__.py    # Inicialização das rotas
│   │   ├── main.py        # Rotas principais (CRUD)
│   │   ├── charts.py      # Rotas para gráficos
│   │   ├── export.py      # Rotas para exportação de dados
│   ├── templates/         # Templates HTML (frontend)
│   │   ├── index.html     # Página inicial
│   │   ├── add_transaction.html  # Página para adicionar transações
│   │   ├── edit_transaction.html # Página para editar transações
│   │   ├── charts/        # Páginas de gráficos
│   │       ├── bar_chart.html
│   │       ├── line_chart.html
│   │       ├── pie_chart.html
│   ├── static/            # Arquivos estáticos (CSS, JS, imagens)
├── tests/                 # Módulos de teste
│   ├── __init__.py
│   ├── test_routes.py     # Testes das rotas
│   ├── test_models.py     # Testes do modelo
├── dashboard.db           # Banco de dados SQLite
├── requirements.txt       # Dependências do projeto
├── run.py                 # Arquivo principal para rodar o app

Requisitos
Python: 3.10 ou superior
Bibliotecas Python:
Flask
Flask-SQLAlchemy
SQLAlchemy
Instale as dependências com:

pip install -r requirements.txt
Configuração e Execução
Clone o repositório:

git clone <link-do-repositorio>
cd project/
Configure o ambiente:

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

pip install -r requirements.txt
Execute a aplicação:

python run.py
Acesse no navegador:

http://127.0.0.1:5000
Funcionalidades
1. CRUD de Transações
Adicionar: Permite adicionar novas transações (Receita ou Despesa).
Editar: Atualizar informações de uma transação existente.
Excluir: Remover transações.
2. Visualização Gráfica
Gráfico de Barras: Comparação de receitas e despesas.
Gráfico de Linhas: Evolução temporal das transações.
Gráfico de Pizza: Proporção de receitas e despesas.
3. Exportação
Exporta os dados em formato CSV para análise externa.
Arquitetura do Sistema
Flask Blueprints:

main: Gerencia as rotas principais (CRUD).
charts: Gerencia as rotas de gráficos.
export: Gerencia a exportação de dados.
Banco de Dados:

Utiliza SQLite para armazenar as transações.
Modelo:
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # Receita ou Despesa
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    value = db.Column(db.Float, nullable=False)
Rotas e Endpoints
Rotas Principais
Método	Rota	Função	Descrição
GET	/	main.index	Página inicial
GET/POST	/add	main.add_transaction	Adiciona nova transação
GET/POST	/edit/<id>	main.edit_transaction	Edita transação existente
GET	/delete/<id>	main.delete_transaction	Exclui transação
Rotas de Gráficos
Método	Rota	Função	Descrição
GET	/charts/bar	charts.bar_chart	Gráfico de barras
GET	/charts/line	charts.line_chart	Gráfico de linhas
GET	/charts/pie	charts.pie_chart	Gráfico de pizza
Rotas de Exportação
Método	Rota	Função	Descrição
GET	/export/csv	export.export_csv	Exporta dados em formato CSV
Testes
Os testes automatizados verificam o funcionamento das rotas e do modelo.

Executar Testes:

python -m unittest discover -s tests
Cobertura de Testes:

Testes de rotas principais (adicionar, editar, excluir).
Testes do modelo Transaction.