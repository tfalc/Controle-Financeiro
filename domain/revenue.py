from .transaction import Transaction

class Revenue(Transaction):
    def __init__(self, description, date, value):
        super().__init__("Receita", description, date, value)