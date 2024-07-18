
import requests
import json
from tqdm.notebook import tqdm
from datetime import datetime
import pandas as pd

class CpiCrawler :
    def __init__(self) :
        self.__url = 'https://sbcharts.investing.com/events_charts/us/733.json'

    def crawl(self) :
        resp = requests.get(self.__url)
        dic = json.loads(resp.content)
        infos = dic["attr"]

        timestampList = []
        actualList = []
        forecastList = []
        revisedList = []

         
        for info in infos :
             timestampList.append(datetime.date(datetime.fromtimestamp(info["timestamp"]/1000)))
             actualList.append(info["actual"])
             forecastList.append(info["forecast"])
             revisedList.append(info["revised"])

        df = pd.DataFrame({"date":timestampList,"실제":actualList,"예측":forecastList,"이전":revisedList})

        df.to_csv("CPI 물가지수.csv", encoding='utf-8', index=False)

        return df

