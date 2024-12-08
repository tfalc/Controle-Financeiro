from transaction.transaction import Expense
from data_persistence import data_manager

def calc():
    new_transaction = Expense("", "", 0)
    try:
        # Validação da descrição
        while True:
          new_transaction.description = input("Qual o nome/descrição da despesa?")
          msg_error = new_transaction.validate_description()
          if msg_error:
              print(f"Erro: {msg_error}")
          else:
              break
        # Validação da data
        while True:
          date_str = input("Qual a data da transação (dd/mm/aaaa)?")
          msg_error = new_transaction.validate_date(date_str)
          if msg_error:
              print(f"Erro: {msg_error}")
          else:
              break
        # Validação do valor
        while True:
          new_transaction.value = float(input("Qual o valor da transação?"))
          msg_error = new_transaction.validate_value()
          if msg_error:
              print(f"Erro: {msg_error}")
          else:
              break
    except ValueError as e:
        print(f"Erro {e}")

    new_transaction.save()
    print("Despesa salva com sucesso")

def get_total_value():
    """
    Retorna a soma dos valores de despesas.
    """
    expense_df = data_manager.get_data("Despesa", "Valor")
    if expense_df is not None:
        return expense_df.sum()
    return 0.0
