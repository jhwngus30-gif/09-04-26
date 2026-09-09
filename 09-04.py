import streamlit as st
import pandas as pd
import os  #외부자료를 가지고 들어오겠다.

csv_path = os.path.join(os.path.dirname(__file__), "..", 'csv_file', 'raw_trade_data.csv')
# csv_path = os.path.join(os.path.dirname(__file__), 'raw_trade_data.csv')  : 같은 경로에 있을 경우

# 환율 샘플 데이터:
# 딕셔너리로 만들기
exchange_data = {
    "통화" : ['USD','EUR','JPY(100엔)','CNY'],
    "환율(KRW)" : [1390.5000,1503.2000,930.8000,191.3000],
    "전일대비" : [+5.2000,-3.1000,+1.0000,-0.4000],
}
df_exchange = pd.DataFrame(exchange_data)

st.title('💱오늘의 환율 대시보드')
st.caption('아래 데이터는 실제 환율이 아닌 실습용 샘플 데이터입니다.')


st.header('1) 주요 환율 카드 (st.metric)')
# st.metric(라벨, 현재값, 증량값) 

col1, col2, col3 = st.columns(3)
with col1 : 
    st.metric(label='USD/KRW', value='1,450.5',delta='+5.2')
with col2 : 
    st.metric(label='EUR/KRW', value='1,450.5',delta='-3.1')
with col3 : 
    st.metric(label='JPY(100엔)/KRW', value='930.5',delta='+1.0')

st.markdown('---')

st.header('2) 환율 표 보기')

st.write('▶ st.dataframe (상호작용 가능한 표)')
st.dataframe(df_exchange, use_container_width=True)

st.write('▶ st.table (정적인 표)')
st.table(df_exchange)



st.markdown('---')

st.header('3) 보너스: 무역 원본 데이터 미리보기')
st.caption('공용 데이터 파일 raw_trade_data.csv를 읽어온 상위 5행입니다.')

df_trade = pd.read_csv(csv_path, encoding='UTF-8')
st.dataframe(df_trade.head(5),use_container_width=True)