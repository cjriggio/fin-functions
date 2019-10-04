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

def AdjustedClose(df, identifier, start_time, end_time):
    '''Takes a dataframe with a column of stock tickers and returns a
    dataframe of adjusted close prices columns are named afer each stock
    ticker, also uses the StockData function'''
    import pandas as pd
    import pandas_datareader.data as web
    import datetime
    stock_list = []
    adj_close_list = []
    for i in range(0, len(df)):
        stock_list.append(StockData(df.identifier[i], start_time, end_time))
        adj_close_list.append(stock_list[i]['Adj Close'])

    temp1 = pd.DataFrame(adj_close_list)
    temp2 = temp1.transpose()

    cols = []
    count = 0
    for column in temp2.columns:
        if column == 'Adj Close':
            cols.append(f'Adj Close_{count}')
            count+=1
            continue
        cols.append(column)
    temp2.columns = cols

    for i in range(0, len(df)):
        temp2.rename(columns={temp2.columns[i]:df.identifier[i]}, inplace=True)

    return temp2
