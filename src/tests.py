from api_handler import BMEApiHandler

ah = BMEApiHandler()

maestro = ah.get_ticker_master(market='IBEX')
print(maestro.ticker.to_list())
maestro = ah.get_ticker_master(market='DAX')
print(maestro.ticker.to_list())
maestro = ah.get_ticker_master(market='EUROSTOXX')
print(maestro.ticker.to_list())