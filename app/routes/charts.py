"""
Rotas para exibição de gráficos: barras, linhas e pizza.
"""

from flask import Blueprint, render_template
from app.models import Transaction

# Define o blueprint
charts = Blueprint('charts', __name__)

@charts.route("/bar")
def bar_chart():
    """
    Exibe o gráfico de barras.
    """
    transactions = Transaction.query.all()
    total_revenues = sum(t.value for t in transactions if t.type == "Receita")
    total_expenses = sum(t.value for t in transactions if t.type == "Despesa")
    return render_template("bar_chart.html", total_revenues=total_revenues, total_expenses=total_expenses)

@charts.route("/line")
def line_chart():
    """
    Exibe o gráfico de linha.
    """
    transactions = Transaction.query.all()
    evolution_data = {"dates": [], "revenues": [], "expenses": []}

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

@charts.route("/pie")
def pie_chart():
    """
    Exibe o gráfico de pizza.
    """
    transactions = Transaction.query.all()
    total_revenues = sum(t.value for t in transactions if t.type == "Receita")
    total_expenses = sum(t.value for t in transactions if t.type == "Despesa")
    return render_template("pie_chart.html", total_revenues=total_revenues, total_expenses=total_expenses)
