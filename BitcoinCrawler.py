
import pandas as pd
from tqdm.notebook import tqdm

import requests # 웹 상의 데이터를 가져올 때
from bs4 import BeautifulSoup # 가져온 데이터에서 필요한 정보를 골라낼(파싱할) 때


class BitcoinCrawler():
    def __init__(self):
        self.url = "https://finance.yahoo.com/quote/BTC-USD/history/?frequency=1mo&period1=1410912000&period2=1721010174"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }
        self.data = None

    def crawl(self):
        dates = []
        open_prices = []
        high_prices = []
        low_prices = []
        close_prices = []
        adj_close_prices = []
        volumes = []

        # request 요청
        resp = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(resp.content, 'lxml')

        # 히스토리 데이터 html 위치 반환
        cells = soup.select("td.svelte-ewueuo")

        # 데이터 추출
        for i in tqdm(range(0, len(cells), 7)):
            if i + 6 >= len(cells):
                continue  # 불완전한 열 건너뛰기

            dates.append(cells[i].text)
            open_prices.append(cells[i+1].text.replace(',', ''))
            high_prices.append(cells[i+2].text.replace(',', ''))
            low_prices.append(cells[i+3].text.replace(',', ''))
            close_prices.append(cells[i+4].text.replace(',', ''))
            adj_close_prices.append(cells[i+5].text.replace(',', ''))
            volumes.append(cells[i+6].text.replace(',', ''))

        # 데이터프레임 생성
        self.data = pd.DataFrame({
            'date': dates,
            'open': open_prices,
            'high': high_prices,
            'low': low_prices,
            'close': close_prices,
            'adj close': adj_close_prices,
            'volume': volumes
        })

        # 데이터 변환
        self.data['date'] = pd.to_datetime(self.data['date'], format='%b %d, %Y')
        cols_to_convert = ['open', 'high', 'low', 'close', 'adj close', 'volume']
        for col in cols_to_convert:
            self.data[col] = self.data[col].astype(float)

        # CSV 파일로 저장
        csv_file = 'bitcoin_monthly.csv'
        self.data.to_csv(csv_file, encoding='utf-8', index=False)

        return csv_file
