import pandas as pd
import akshare as ak


class StockZhData():
    
    
    def query_data_daily(self, code: str, start_date: str, end_date: str) -> pd.DataFrame:
        daily_data_pd = ak.stock_zh_a_hist(symbol=code, period='daily', start_date=start_date, end_date=end_date, adjust='hfq')
        if daily_data_pd is None:
            return
        return daily_data_pd
    
    def query_data_weekly(self, code: str, start_date: str, end_date: str):
        weekly_data_pd = ak.stock_zh_a_hist(symbol=code, period='weekly', start_date=start_date, end_date=end_date, adjust='hfq')
        if weekly_data_pd is None:
            return
        return weekly_data_pd
    
    
    

if __name__ == '__main__':
    stock_zh_data = StockZhData()
    data_pd = stock_zh_data.query_data_daily("688981", "20230421", "20230421")
    print(data_pd)