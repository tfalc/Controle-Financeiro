# app/models.py

from app import db

class Transaction(db.Model):
    """
    Modelo para representar uma transação no banco de dados.
    """
    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    type = db.Column(db.String(10), nullable=False)  # Tipo: Receita ou Despesa
    description = db.Column(db.String(100), nullable=False)  # Descrição
    date = db.Column(db.Date, nullable=False)  # Data
    value = db.Column(db.Float, nullable=False)  # Valor
