import unittest
from app import create_app, db
from app.models import Transaction
from datetime import datetime

class TestRoutes(unittest.TestCase):
    def setUp(self):
        """
        Configura o ambiente para os testes.
        """
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco de dados em memória
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()  # Cria as tabelas no banco de dados

    def tearDown(self):
        """
        Limpa o ambiente após os testes.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_route(self):
        """
        Testa a rota da página inicial.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_add_transaction(self):
        """
        Testa a adição de uma nova transação.
        """
        response = self.client.post("/add", data={
            "type": "Receita",
            "description": "Teste de Receita",
            "date": "2024-12-11",
            "value": 100.50
        })
        self.assertEqual(response.status_code, 302)  # Redireciona após adicionar

        # Verifica se a transação foi adicionada
        with self.app.app_context():
            transaction = Transaction.query.first()
            self.assertIsNotNone(transaction)
            self.assertEqual(transaction.description, "Teste de Receita")

    def test_delete_transaction(self):
        """
        Testa a exclusão de uma transação.
        """
        with self.app.app_context():
            # Converte a data de string para datetime.date
            date = datetime.strptime("2024-12-11", "%Y-%m-%d").date()
            transaction = Transaction(type="Despesa", description="Teste de Despesa", date=date, value=50.0)
            db.session.add(transaction)
            db.session.commit()

            transaction_id = transaction.id

        response = self.client.get(f"/delete/{transaction_id}")
        self.assertEqual(response.status_code, 302)  # Redireciona após excluir

        # Verifica se a transação foi excluída
        with self.app.app_context():
            transaction = Transaction.query.get(transaction_id)
            self.assertIsNone(transaction)

if __name__ == "__main__":
    unittest.main()
