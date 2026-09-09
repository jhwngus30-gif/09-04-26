import streamlit as st
import random
from datetime import datetime
import zoneinfo  # 한국 표준시(KST) 적용용

st.title('🤑 로또 번호 자동 생성기 🤑')
st.caption('버튼을 누르면 1~45 사이의 중복 없는 번호 6개짜리 세트를 5개 만들어줍니다.')

def lotto_one_set() -> list:
    """1~45에서 중복없이 번호 6개 뽑아 정렬된 리스트로 반환"""
    number = set()
    while len(number) < 6:
        number.add(random.randint(1, 45))
    return sorted(number)

st.markdown('---')

# 버튼 클릭 시에만 생성
if st.button('5개 세트 번호 생성하기', key='lotto_btn'):
    # 1. 한국 표준시(Asia/Seoul) 기준 현재 시간 가져오기
    try:
        kst = zoneinfo.ZoneInfo("Asia/Seoul")
        now = datetime.now(kst)
    except Exception:
        now = datetime.now()

    # 2. 안전한 날짜/시간 포맷팅 (f-string으로 직접 조립하여 %d 인식 오류 원천 차단)
    # 2026-09-09 14:01:15 형식
    now_str = f"{now.year:04d}-{now.month:02d}-{now.day:02d} {now.hour:02d}:{now.minute:02d}:{now.second:02d}"

    st.write(f'생성시간: **{now_str}**')

    # 5세트 생성 및 출력
    for set_index in range(1, 6):
        lotto_num = lotto_one_set()
        st.write(f'**{set_index}세트:** {lotto_num}')