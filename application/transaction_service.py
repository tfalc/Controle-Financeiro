class TransactionService:
    def __init__(self, description, date, value):
        self.description = description
        self.date = date
        self.value = value

    def validate_and_save(self):
        # Implement the validation and save logic here
        return "Transação salva com sucesso!"