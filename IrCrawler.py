
import requests
import json
from tqdm.notebook import tqdm
from datetime import datetime
import pandas as pd



class IrCrawler():
    def __init__(self) :
        self.__url = 'https://sbcharts.investing.com/events_charts/us/168.json'

    def crawl(self) :
        timestampList = []
        actualStateList = []
        actualList = []
        forecastList = []
        revisedList = []
        changeList = [0]

        resp = requests.get(self.__url)
        dic = json.loads(resp.content)
        infos = dic["attr"] 


        for info in infos :
            timestampList.append(datetime.date(datetime.fromtimestamp(info["timestamp"]/1000)))
            actualStateList.append(info["actual_state"])
            actualList.append(info["actual"])
            forecastList.append(info["forecast"])

        
        for idx in range(1,len(actualList)) :
            changeList.append(actualList[idx]-actualList[idx-1])

        df = pd.DataFrame({'date' : timestampList,'실제' : actualList, '예상' : forecastList, '변동' : changeList, 'Actual State' : actualStateList})

        df.to_csv("Feds 기준금리 변동.csv", encoding ='utf-8', index=False)

        return df



        
