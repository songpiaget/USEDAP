import requests # 웹 상의 데이터를 가져올 때
from bs4 import BeautifulSoup # 가져온 데이터에서 필요한 정보를 골라낼(파싱할) 때
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

class SPXCrawler():


    def crawl(self): #  크롤링
        url = 'https://finance.yahoo.com/quote/%5EGSPC/history/?frequency=1d&period1=401932800&period2=1721027779'
        filename='SPXCrawler'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        }

        resp = requests.get(url,headers=headers)
        resp


        soup = BeautifulSoup(resp.content, 'lxml')

        ex = soup.select('tbody tr.svelte-ewueuo')
        result=[]


        result = []


        num_rows = len(ex)


        for i in range(num_rows):
            row = ex[i]

            tds = row.find_all('td')


            row_data = [td.text for td in tds]


            result.append(row_data)
        a1=[]
        b1=[]
        c1=[]
        d1=[]
        e1=[]
        f1=[]
        g1=[]


        for k in range(len(result)):
            a1.append(result[k][0])
            b1.append(result[k][1])
            c1.append(result[k][2])
            d1.append(result[k][3])
            e1.append(result[k][4])
            f1.append(result[k][5])
            g1.append(result[k][6])

        g1= [0 if x == '-' else x for x in g1]

    # csv 파일 저장
        answer=pd.DataFrame({'date':a1,
                'open':b1,
                'high':c1,
                'low':d1,
                'close':e1,
                'adjClose':f1,
                'volume':g1})

        answer.to_csv(f'{filename}.csv', index=False)


    # 형변환
        df_petition = pd.read_csv(f'{filename}.csv')
        df_petition['date'] = pd.to_datetime(df_petition['date'],errors='coerce')
        df_petition['open'] = df_petition.open.str.replace(',', '').astype('float')
        df_petition['high'] = df_petition.high.str.replace(',', '').astype('float')
        df_petition['low'] = df_petition.low.str.replace(',', '').astype('float')
        df_petition['close'] = df_petition.close.str.replace(',', '').astype('float')
        df_petition['volume'] = df_petition.volume.str.replace(',', '').astype('float')
        df_petition['adjClose'] = df_petition.adjClose.str.replace(',', '').astype('float')


        df_petition.to_csv(f'{filename}.csv', index=False)

        return df_petition
