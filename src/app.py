import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

from api_handler import BMEApiHandler


app = dash.Dash(__name__)

ah = BMEApiHandler()

df_close = ah.get_close_data(tck='SAN')
fig = px.line(df_close)

app.layout = html.Div(children=[
        html.H1(children='MIAX DATA EXPLORER'),
        html.Div(children='mIAx API'),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ]
)


# # 1 Dropdown que tenga las siguietes opciones:
#                 {'label': 'IBEX', 'value': 'IBEX'},
#                 {'label': 'DAX', 'value': 'DAX'},
#                 {'label': 'EUROSTOXX', 'value': 'EUROSTOXX'},
# ah.get_ticker_master(market='IBEX')
# ah.get_ticker_master(market='DAX')
# ah.get_ticker_master(market='EUROSTOXX')






if __name__ == '__main__':
    app.run(debug=True)
