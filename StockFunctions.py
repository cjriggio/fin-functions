def StockData(ticker, start_date, end_date):
    '''requires pandas datareader and date time'''
    import pandas as pd
    import pandas_datareader.data as web
    import datetime
    df = web.DataReader(ticker, 'yahoo', start_date, end_date)
    return df

def set_index(df):
    '''use to set date as index when importing
    a stock CSV into jupyter'''
    import pandas as pd
    import datetime
    df.set_index(df['Date'], inplace=True)
    df.drop(['Date'], axis=1, inplace=True)
    pd.to_datetime(df.index)

def DailyReturns(df, column_name):
    '''Calculate daily returns '''
    import pandas as pd
    return df[column_name].diff(1) / df[column_name].shift(1)
