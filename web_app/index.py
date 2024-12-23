import os
import dash
from dash import html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
from application.revenue_service import RevenueService
from application.transaction_service import TransactionService

# Carregar os dados do arquivo CSV com o delimitador correto
base_path = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(base_path, 'dados.csv')
df = pd.read_csv(csv_path, delimiter=';')

# Renomear as colunas para corresponder aos nomes esperados
df.columns = ['Tipo', 'Descrição', 'Data', 'Valor']

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Controle Financeiro"),
    dcc.Graph(id='line-graph'),
    dcc.Graph(id='pie-graph'),
    html.Div([
        html.H2("Adicionar Transação"),
        dcc.Input(id='description', type='text', placeholder='Descrição'),
        dcc.Input(id='date', type='text', placeholder='Data (dd/mm/aaaa)'),
        dcc.Input(id='value', type='number', placeholder='Valor'),
        dcc.Dropdown(
            id='transaction-type',
            options=[
                {'label': 'Receita', 'value': 'r'},
                {'label': 'Despesa', 'value': 'd'}
            ],
            placeholder='Tipo de Transação'
        ),
        html.Button('Adicionar', id='add-button', n_clicks=0),
        html.Div(id='output-message')
    ])
])


@app.callback(
    Output('line-graph', 'figure'),
    Output('pie-graph', 'figure'),
    Output('output-message', 'children'),
    Input('add-button', 'n_clicks'),
    State('description', 'value'),
    State('date', 'value'),
    State('value', 'value'),
    State('transaction-type', 'value')
)
def update_output(n_clicks, description, date, value, transaction_type):
    global df
    if n_clicks > 0:
        if transaction_type == 'r':
            service = RevenueService(description, date, value)
        elif transaction_type == 'd':
            service = TransactionService(description, date, value)
        else:
            return px.line(df, x='Data', y='Valor', color='Tipo', title='Receitas e Despesas ao longo do tempo'), px.pie(df, names='Tipo', values='Valor', title='Receitas e Despesas'), "Erro: Tipo de transação inválido!"

        message = service.validate_and_save()
        if "sucesso" in message:
            # Atualizar o DataFrame com a nova transação
            new_row = pd.DataFrame([{'Data': date, 'Valor': value, 'Tipo': 'Receita' if transaction_type == 'r' else 'Despesa', 'Descrição': description}])
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(csv_path, index=False, sep=';')
            line_figure = px.line(df, x='Data', y='Valor', color='Tipo', title='Receitas e Despesas ao longo do tempo')
            pie_figure = px.pie(df, names='Tipo', values='Valor', title='Receitas e Despesas')
            return line_figure, pie_figure, message
        else:
            return px.line(df, x='Data', y='Valor', color='Tipo', title='Receitas e Despesas ao longo do tempo'), px.pie(df, names='Tipo', values='Valor', title='Receitas e Despesas'), message

    return px.line(df, x='Data', y='Valor', color='Tipo', title='Receitas e Despesas ao longo do tempo'), px.pie(df, names='Tipo', values='Valor', title='Receitas e Despesas'), ""


# Rodar o servidor web
if __name__ == '__main__':
    app.run_server(debug=True)