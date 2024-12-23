# application/revenue_service.py
from application.transaction_service import TransactionService

class RevenueService(TransactionService):
    def __init__(self, description, date, value):
        super().__init__(description, date, value)