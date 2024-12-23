import datetime
import re

class Transaction:
    def __init__(self, type, description, date, value):
        self.type = type
        self.description = description
        self.date = date
        self.value = value

    def validate_description(self):
        if not isinstance(self.description, str) or len(self.description.strip()) == 0:
            return "A descrição não pode ser vazia"
        if len(self.description) > 50:
            return "A descrição é muito longa! Deve ter no máximo 50 caracteres"
        if not re.match(r'^[a-zA-Z0-9\s,.!?-]*$', self.description):
            return "A descrição contém caracteres inválidos! Use apenas letras, números, espaços, e pontuação básica (.,!?-)"
        return None

    def validate_date(self, date_str):
        try:
            self.date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            if self.date.year < 1950 or self.date.year > 3000:
                return "Digite um ano válido!"
            self.date = self.date.strftime("%d/%m/%Y")
            return None
        except ValueError:
            return "Data inválida! Use o formato dd/mm/aaaa."

    def validate_value(self):
        if not isinstance(self.value, (int, float)):
            return "O valor deve ser um número!"
        if self.value <= 0:
            return "O valor deve ser positivo!"
        return None