# random 모듈을 이용해서 1~45 중 중복에 없는 번호 6개 뽑고
# 자료 구조 set , 버튼을 나오면 5세트를 한 번에 생성
# datetime으로 생성 시간도 함께 보여준다.

# lotto v1

import streamlit as st
import random
from datetime import datetime
# datetime(앞) 안에 들어있는 datetime(뒤)만 가져올거야.

st.title('🤑로또 번호 자동 생성기🤑')
st.caption('버튼을 누르면 1~45 사이의 중복 없는 번호 6개짜리 세트를 5개 만들어줍니다.')

# while 조건식 :
#     참 -> 처리문
# return 값

def lotto_one_set() -> list :
    """1~45에서 중복없이 번호 6개 뽑아 정렬된 리스트로 반환"""
    # -> 함수를 약축해서 사용하겠다. """""" => 함수 정의 부가설명
    # int = 정수, any = 아무거나, str =문자
    number = set[int]()
    while len(number) < 6 :
        number.add(random.randint(1,45)) # 1이상 45이하 정수 하나 뽑기
    # set자리에 하나씩 더해서 추가
    return sorted(number)

# set(중복없이 뽑기), len(개수), sort(정렬)
# 들여쓰기 tap, 내어쓰기 shift + tap
st.markdown('---')

st.button('5개 세트 번호 생성하기', key='lotto_btn')
now_str = datetime.now().strftime('%y-%m-%%d %H:%M:%S')
st.write(f'생성시간: **{now_str}**')

for set_index in range(1,6):
    lotto_num = lotto_one_set()
    st.write(f'{set_index}세트: {lotto_num}')