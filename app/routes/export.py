"""
Rota para exportar dados em formato CSV.
"""

from flask import Blueprint, Response
from app.models import Transaction

# Define o blueprint
export = Blueprint('export', __name__)

@export.route("/csv")
def export_csv():
    """
    Exporta as transações para um arquivo CSV.
    """
    transactions = Transaction.query.all()

    def generate_csv():
        yield "ID,Tipo,Descrição,Data,Valor\n"
        for t in transactions:
            yield f"{t.id},{t.type},{t.description},{t.date},{t.value}\n"

    return Response(
        generate_csv(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=transacoes.csv"}
    )
