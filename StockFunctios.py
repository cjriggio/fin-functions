def StockData(ticker, start_date, end_date):
    '''requires pandas datareader and date time'''
    import pandas as pd
    import pandas_datareader.data as web
    import datetime
    df = web.DataReader(ticker, 'yahoo', start_date, end_date)
    return df
