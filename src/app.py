import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from api_handler import BMEApiHandler


app = dash.Dash(__name__)

ah = BMEApiHandler()



app.layout = html.Div(children=[
    html.H1(children='MIAX DATA EXPLORER'),
    html.Div(children='mIAx API'),
    dcc.Dropdown(
        id='menu-index',
        options=[
            {'label': 'IBEX', 'value': 'IBEX'},
            {'label': 'DAX', 'value': 'DAX'},
            {'label': 'EUROSTOXX', 'value': 'EUROSTOXX'},
        ],
        value='IBEX'
    ),
    dcc.Dropdown(
        id='menu-ticker'
    ),
    dcc.Graph(
        id='example-graph',
    )
])


@app.callback(
    Output("menu-ticker", 'options'),
    Input('menu-index', 'value')
)
def market_changed(market):
    maestro = ah.get_ticker_master(market=market)
    tcks = maestro.ticker.to_list()
    options = [{'value': tck, 'label': tck} for tck in tcks]
    return options


@app.callback(
    Output("menu-ticker", 'value'),
    Input('menu-ticker', 'options'),
)
def select_first_tck(options):
    return options[0]['value']


@app.callback(
    Output("example-graph", 'figure'),
    State('menu-index', 'value'),
    Input('menu-ticker', 'value'),
)
def plot_data(market, tck):
    print(market, tck)
    # df_close = ah.get_close_data(market=market, tck=tck)
    # fig = px.line(df_close)
    data_to_plot = ah.get_ohlc_data(market=market, tck=tck)
    fig = go.Figure(
        go.Candlestick(
            x=data_to_plot.index,
            open=data_to_plot['open'],
            high=data_to_plot['high'],
            low=data_to_plot['low'],
            close=data_to_plot['close']
        )
    )
    return fig



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
