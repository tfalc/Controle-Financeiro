from .transaction import Transaction

class Expense(Transaction):
    def __init__(self, description, date, value):
        super().__init__("Despesa", description, date, value)