"""
Rotas principais: index, adicionar, editar e excluir transações.
"""

from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Transaction  # Importe Transaction diretamente do models
from app import db  # Importa o db de app/__init__.py
from datetime import datetime

# Define o blueprint
main = Blueprint('main', __name__)

@main.route("/")
def index():
    """
    Página inicial: exibe as transações com filtros opcionais.
    """
    t_type = request.args.get("type")  # Tipo de transação
    start_date = request.args.get("start_date")  # Data inicial
    end_date = request.args.get("end_date")  # Data final

    transactions = Transaction.query
    if t_type:
        transactions = transactions.filter_by(type=t_type)
    if start_date:
        transactions = transactions.filter(Transaction.date >= start_date)
    if end_date:
        transactions = transactions.filter(Transaction.date <= end_date)

    return render_template("index.html", transactions=transactions.all())

@main.route("/add", methods=["GET", "POST"])
def add_transaction():
    """
    Adiciona uma nova transação.
    """
    if request.method == "POST":
        t_type = request.form["type"]
        description = request.form["description"]
        date = datetime.strptime(request.form["date"], "%Y-%m-%d")
        value = float(request.form["value"])

        transaction = Transaction(type=t_type, description=description, date=date, value=value)
        db.session.add(transaction)
        db.session.commit()
        return redirect(url_for("main.index"))

    return render_template("add_transaction.html")

@main.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    """
    Edita uma transação existente.
    """
    transaction = Transaction.query.get_or_404(transaction_id)

    if request.method == "POST":
        transaction.type = request.form["type"]
        transaction.description = request.form["description"]
        transaction.date = datetime.strptime(request.form["date"], "%Y-%m-%d")
        transaction.value = float(request.form["value"])
        db.session.commit()
        return redirect(url_for("main.index"))

    return render_template("edit_transaction.html", transaction=transaction)

@main.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    """
    Exclui uma transação.
    """
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for("main.index"))
