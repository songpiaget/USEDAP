# U.S.EDAP
United States Economy Data Analysis Program

<h2>개발 참고 사항</h2> datetime 형식 : %Y-%m

<h3>프로젝트 요약</h3>
미국의 1980년대부터 현재까지의 경제지표 데이터 및 기사를 크롤링하고 데이터를 시각화하여 분석한다. 경제 지표 간의 연관성과 특정한 기간 동안의 기사 키워드를 추출해 경제 지표와 경제 위기 및 경기와의 연관성을 분석 및 해설하고자 한다.  
  
<h3>크롤링 대상</h3>
<ol>
  <li>경제 지표 : Feds 결정금리, CPE 물가지수, 채권(13 week T-bill) 수익률, 주가지수(S%P500), 비트코인, 금 시세 총 6가지 항목  => 이하 각 금리, 물가, 채권, 주가, 비트코인, 금으로 서술한다.</li>
  <li>기사 : 2000-08-18 ~ 현재</li>
</ol>

<h3>크롤링 사이트</h3>
<ol>
  <li>Investing.com : 금리, 물가</li>
  <li>Yahoo finanace : 채권, 주가, 비트코인, 금</li>
  <li>News Archive : 기사 </li>
</ol>

<h3>개발환경</h3> 
<ol>
  <li>Colab</li>
  <li>언어 : Python</li>
  <li>크롤링 :</li>
  <li>데이터 시각화 :</li>
</ol>

<h3>프로젝트 설계도</h3>
StarUml class diagram으로 작성했다.  

![classDiagram_EDAP](https://github.com/user-attachments/assets/45408e6a-6bed-46ef-b322-6d9b732f1227)  

<h3>클래스 구조</h3>
<ol>
  <li>Crawler : 각 경제지표 데이터를 웹사이트에서 크롤링하고 Csv 파일로 저장, 전처리된 데이터를 pandas DataFrame으로 만들어 반환하는 클래스  
    <ol>
      <li>setDataFrame() : 전처리 필수!!(날짜 형식 등)</li>  
    </ol>
  </li>
  <li>News_wordCloud_maker : 뉴스 크롤러를 통해 크롤링 데이터를 가져오고 원하는 기간을 입력받아 해당하는 기간 동안의 기사 제목을 키워드로 만들어 word cloud 이미지로 만드는 클래스</li>  
  <li>Main : Crawler, wordCloud_maker 클래스의 객체들을 생성하여 작동시키는 메인 클래스    
    <ol>
      <li>make_mergedChart() : 원하는 종류의 경제지표의 DataFrame을 인자로 받아 차트로 시각화하는 함수. 가변인자로 받아 1개 이상의 경제지표를 시각화할 수 있게한다.</li>  
    </ol>
  </li>
</ol>
