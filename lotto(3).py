import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="로또 번호 자동 생성기", layout="centered")

st.title("🤑 로또 번호 자동 생성기 🤑")
st.caption("버튼을 누르면 1~45 사이의 중복 없는 번호 6개짜리 세트를 총 5개 생성합니다.")

def get_ball_color(num: int) -> str:
    """번호 범위에 맞춰 공 배경색 반환"""
    if 1 <= num <= 10:
        return "#fbc400"  # 노란색 (1~10)
    elif 11 <= num <= 20:
        return "#69c8f2"  # 파란색 (11~20)
    elif 21 <= num <= 30:
        return "#ff7272"  # 빨간색 (21~30)
    elif 31 <= num <= 40:
        return "#aaaaaa"  # 회색 (31~40)
    else:
        return "#b0d840"  # 녹색 (41~45)

def lotto_one_set() -> list:
    """1~45에서 중복 없이 번호 6개를 뽑아 오름차순 정렬 후 반환"""
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(1, 45))
    return sorted(numbers)

def render_lotto_balls(numbers: list) -> str:
    """번호 리스트를 가로로 나열된 동그란 공 HTML로 변환"""
    balls_html = ""
    for num in numbers:
        color = get_ball_color(num)
        balls_html += (
            f'<span style="display:inline-flex; justify-content:center; align-items:center; '
            f'width:38px; height:38px; border-radius:50%; background-color:{color}; '
            f'color:#ffffff; font-weight:700; font-size:15px; margin-right:8px; '
            f'box-shadow:1px 2px 4px rgba(0,0,0,0.2);">{num}</span>'
        )
    return balls_html

st.markdown("---")

if st.button("🎲 번호 5세트 생성하기", key="lotto_btn", use_container_width=True):
    # 날짜와 시간을 f-string으로 안전하게 포맷팅
    now = datetime.now()
    now_str = f"{now.year:04d}-{now.month:02d}-{now.day:02d} {now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    st.write(f"생성 시간: **{now_str}**")
    st.write("")

    for set_index in range(1, 6):
        selected_numbers = lotto_one_set()
        balls_html = render_lotto_balls(selected_numbers)

        # 마크다운 코드블록 오작동(공백 4칸 인식)을 방지하기 위해 태그 앞 들여쓰기를 제거한 한 줄 문자열로 출력
        row_html = (
            f'<div style="display:flex; align-items:center; margin-bottom:12px;">'
            f'<span style="font-weight:700; font-size:16px; min-width:65px;">{set_index}세트:</span>'
            f'<div>{balls_html}</div>'
            f'</div>'
        )
        st.markdown(row_html, unsafe_allow_html=True)