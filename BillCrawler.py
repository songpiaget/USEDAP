import requests
from bs4 import BeautifulSoup
import datetime
from datetime import datetime
import pandas as pd
import numpy as np

class BillCrawler():


    def __init__(self) :
        self.__url = 'https://finance.yahoo.com/quote/%5EIRX/history/?period1=-315312000&period2=1720747437&frequency=1mo'



    def crawl(self):
        # url='https://finance.yahoo.com/quote/%5EIRX/history/?period1=-315312000&period2=1720747437&frequency=1mo'

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'Referer':'https://finance.yahoo.com/'}

        resp = requests.get(self.__url, headers=headers)
        resp

        soup = BeautifulSoup(resp.content, 'lxml')
        tnx = soup.select('div.table-container.svelte-ewueuo  table  tbody  tr')

        data={'date':[],'Open':[],'High':[],'Low':[],'Close':[],'Adj_Close':[],'Volume':[]}


        for i in tnx:
            j=i.text
            tnxs=(j.split(' '))
            date_str = str((f'{tnxs[2]}-{tnxs[0]}-{tnxs[1]}').replace(',', ''))
            data['date'].append(pd.to_datetime(date_str,format='%Y-%b-%d'))
            data['Open'].append(tnxs[3])
            data['High'].append(tnxs[4])
            data['Low'].append(tnxs[5])
            data['Close'].append(tnxs[6])
            data['Adj_Close'].append(tnxs[7])
            data['Volume'].append(tnxs[8])


        df = pd.DataFrame(data)
        df = df.sort_values(by='date',ascending=True)

        df.replace('-',np.nan,inplace=True)
        columns_to_convert = ['Open', 'High', 'Low', 'Close', 'Adj_Close']
        for column in columns_to_convert:
            df[column] = df[column].str.replace(',', '').astype('float')

        df.to_csv('채권.csv',encoding = 'utf-8-sig',index=False)

        return df
