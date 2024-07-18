from pytrends.request import TrendReq
import numpy as np 
from wordcloud import WordCloud
import cv2
from google.colab.patches import cv2_imshow

class TrendsCrawler():
    def crawl(self, year) :
        pytrends = TrendReq()
        df = pytrends.top_charts(year,  hl = 'en-US', tz=300, geo ='US')
        randoms = np.random.randint(100, size = 10)
        randoms = np.sort(randoms)[::-1]
        df["count"] = randoms
        dic = {}
        for idx in range(len(df)) :
            dic[df["title"].values[idx]] = df["count"].values[idx]
        wc=WordCloud(width=500, height=500, max_words=10, max_font_size=1000)
        wc.generate_from_frequencies(dic)
        wc.to_file("wc_title.png")
        img = cv2.imread('wc_title.png', cv2.IMREAD_UNCHANGED)
        cv2_imshow(img)
