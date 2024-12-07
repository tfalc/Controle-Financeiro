import datetime
import re  # Importa o módulo de expressões regulares
from data_persistence import data_manager

class Transaction:
    def __init__(self, type, description, date, value):
        self.type = type
        self.description = description
        self.date = date
        self.value = value

    def validate_description(self):
        """Valida a descrição para garantir que a string esteja correta"""
        # Verifica se a descrição é uma string e se não está vazia
        if not isinstance(self.description, str) or len(self.description.strip()) == 0:
          return "A descrição não pode ser vazia"
    
        # Verifica se a descrição excede o limite de 50 caracteres
        if len(self.description) > 50:
          return "A descrição é muito longa! Deve ter no máximo 50 caracteres"
    
        # Verifica se a descrição contém caracteres especiais usando regex
        if not re.match(r'^[a-zA-Z0-9\s,.!?-]*$', self.description):
          return "A descrição contém caracteres inválidos! Use apenas letras, números, espaços, e pontuação básica (.,!?-)"
    
        return None

    def validate_date(self, date_str):
        """ Valida a data para garantir que esteja no formato correto (dd/mm/aaaa)"""
        try:
            self.date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            if self.date.year < 1950 or self.date.year > 3000:
                return "Digite um ano válido!"
            self.date = self.date.strftime("%d/%m/%Y")
            return None
        except ValueError:
            return "Data inválida! Use o formato dd/mm/aaaa."

    def validate_value(self):
        """Valida o valor, se é um número e se é um numéro positivo"""
        if not isinstance(self.value, (int, float)):
            return "O valor deve ser um número!"
        if self.value <= 0:
            return "O valor deve ser positivo!"
        return None

    def save(self):
        """Salve os dados usando o gerenciador de dados."""
        data_manager.save([self.type, self.description, self.date, self.value])

class Revenue(Transaction):
    def __init__(self, description, date, value):
        super().__init__("Receita", description, date, value)

class Expense(Transaction):
    def __init__(self, description, date, value):
        super().__init__("Despesa", description, date, value)