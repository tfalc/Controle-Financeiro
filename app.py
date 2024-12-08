# Importa as bibliotecas necessárias
import csv
from flask import Flask, Response, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dashboard.db'  # Define o caminho do banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa notificações de modificações desnecessárias
db = SQLAlchemy(app)  # Inicializa o SQLAlchemy para gerenciar o banco de dados

# Define o modelo para a tabela de transações
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Chave primária única
    type = db.Column(db.String(10), nullable=False)  # Tipo da transação: "Receita" ou "Despesa"
    description = db.Column(db.String(100), nullable=False)  # Descrição detalhada da transação
    date = db.Column(db.Date, nullable=False)  # Data da transação
    value = db.Column(db.Float, nullable=False)  # Valor da transação

# Cria as tabelas no banco de dados (se ainda não existirem)
with app.app_context():
    db.create_all()

# Rota para a página inicial
@app.route("/")
def index():
    """
    Página inicial: exibe as transações e links para os gráficos.
    """
    # Filtros opcionais
    t_type = request.args.get("type")  # Tipo de transação filtrada (Receita ou Despesa)
    start_date = request.args.get("start_date")  # Data inicial para o filtro
    end_date = request.args.get("end_date")  # Data final para o filtro

    # Consulta básica
    transactions = Transaction.query

    # Aplica filtros se fornecidos
    if t_type:
        transactions = transactions.filter_by(type=t_type)
    if start_date:
        transactions = transactions.filter(Transaction.date >= start_date)
    if end_date:
        transactions = transactions.filter(Transaction.date <= end_date)

    # Finaliza a consulta
    transactions = transactions.all()

    return render_template("index.html", transactions=transactions)

# Rota para adicionar uma nova transação
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    """
    Formulário para adicionar uma nova transação.
    """
    if request.method == "POST":
        # Coleta os dados do formulário enviado
        t_type = request.form["type"]  # Tipo da transação (Receita ou Despesa)
        description = request.form["description"]  # Descrição da transação
        date = datetime.strptime(request.form["date"], "%Y-%m-%d")  # Converte a data
        value = float(request.form["value"])  # Converte o valor para float

        # Cria uma nova transação
        new_transaction = Transaction(type=t_type, description=description, date=date, value=value)

        # Salva no banco de dados
        db.session.add(new_transaction)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("add_transaction.html")

# Rota para editar uma transação existente
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    """
    Formulário para editar uma transação existente.
    """
    transaction = Transaction.query.get_or_404(transaction_id)

    if request.method == "POST":
        # Atualiza os dados da transação
        transaction.type = request.form["type"]
        transaction.description = request.form["description"]
        transaction.date = datetime.strptime(request.form["date"], "%Y-%m-%d")
        transaction.value = float(request.form["value"])

        db.session.commit()  # Salva as alterações no banco
        return redirect(url_for("index"))

    return render_template("edit_transaction.html", transaction=transaction)

# Rota para excluir uma transação
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    """
    Exclui uma transação com base no ID fornecido.
    """
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for("index"))

# Rota para exibir o gráfico de barras (Receitas vs. Despesas)
@app.route("/chart/bar")
def bar_chart():
    """
    Página do gráfico de barras: compara receitas e despesas.
    """
    transactions = Transaction.query.all()
    total_revenues = sum(t.value for t in transactions if t.type == "Receita")
    total_expenses = sum(t.value for t in transactions if t.type == "Despesa")
    return render_template("bar_chart.html", total_revenues=total_revenues, total_expenses=total_expenses)

# Rota para exibir o gráfico de linha (Evolução Temporal)
@app.route("/chart/line")
def line_chart():
    """
    Página do gráfico de linha: evolução das transações ao longo do tempo.
    """
    transactions = Transaction.query.all()
    evolution_data = {"dates": [], "revenues": [], "expenses": []}

    # Ordena as transações por data
    sorted_transactions = sorted(transactions, key=lambda x: x.date)
    for transaction in sorted_transactions:
        date_str = transaction.date.strftime("%Y-%m-%d")
        if date_str not in evolution_data["dates"]:
            evolution_data["dates"].append(date_str)
            evolution_data["revenues"].append(0)
            evolution_data["expenses"].append(0)

        idx = evolution_data["dates"].index(date_str)
        if transaction.type == "Receita":
            evolution_data["revenues"][idx] += transaction.value
        else:
            evolution_data["expenses"][idx] += transaction.value

    return render_template("line_chart.html", evolution_data=evolution_data)

# Rota para exibir o gráfico de pizza (Proporção de Receitas e Despesas)
@app.route("/chart/pie")
def pie_chart():
    """
    Página do gráfico de pizza: proporção de receitas e despesas.
    """
    transactions = Transaction.query.all()
    total_revenues = sum(t.value for t in transactions if t.type == "Receita")
    total_expenses = sum(t.value for t in transactions if t.type == "Despesa")
    return render_template("pie_chart.html", total_revenues=total_revenues, total_expenses=total_expenses)

@app.route("/export/csv")
def export_csv():
    """
    Exporta todas as transações para um arquivo CSV.
    """
    # Consulta todas as transações do banco de dados
    transactions = Transaction.query.all()

    # Cria o CSV em memória usando um generator para eficiência
    def generate_csv():
        # Cabeçalho do CSV
        yield "ID,Tipo,Descrição,Data,Valor\n"
        # Adiciona cada transação como uma linha
        for t in transactions:
            yield f"{t.id},{t.type},{t.description},{t.date},{t.value}\n"

    # Configura a resposta HTTP com o CSV
    return Response(
        generate_csv(),  # Gera o conteúdo do CSV
        mimetype="text/csv",  # Define o tipo de conteúdo como CSV
        headers={"Content-Disposition": "attachment;filename=transacoes.csv"}  # Define o nome do arquivo para download
    )
# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
