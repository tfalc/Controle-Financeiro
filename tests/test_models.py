import unittest
from app import create_app, db
from app.models import Transaction
from datetime import datetime

class TestModels(unittest.TestCase):
    def setUp(self):
        """
        Configura o ambiente para os testes.
        """
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco de dados em memória

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Limpa o ambiente após os testes.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_transaction_model(self):
        """
        Testa o modelo Transaction.
        """
        with self.app.app_context():
            # Converte a data de string para datetime.date
            date = datetime.strptime("2024-12-11", "%Y-%m-%d").date()
            transaction = Transaction(type="Receita", description="Teste de Receita", date=date, value=200.0)
            db.session.add(transaction)
            db.session.commit()

            # Verifica se a transação foi salva corretamente
            saved_transaction = Transaction.query.first()
            self.assertEqual(saved_transaction.type, "Receita")
            self.assertEqual(saved_transaction.description, "Teste de Receita")
            self.assertEqual(saved_transaction.value, 200.0)

if __name__ == "__main__":
    unittest.main()
