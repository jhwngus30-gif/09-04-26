import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="로또 번호 자동 생성기", layout="centered")

st.title("🤑 로또 번호 자동 생성기 🤑")
st.caption("버튼을 누르면 번호 5개로 구성된 세트를 총 5개 생성합니다.")

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
    """1~45에서 중복 없이 번호 5개를 뽑아 오름차순 정렬 후 반환"""
    numbers = set()
    while len(numbers) < 5:
        numbers.add(random.randint(1, 45))
    return sorted(numbers)

def render_lotto_balls(numbers: list) -> str:
    """번호 리스트를 한 줄(가로)로 나열된 공 HTML로 렌더링"""
    balls_html = "".join([
        f"""
        <span style="
            display: inline-flex;
            justify-content: center;
            align-items: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: {get_ball_color(num)};
            color: #ffffff;
            font-weight: 700;
            font-size: 15px;
            margin-right: 8px;
            box-shadow: 1px 2px 4px rgba(0, 0, 0, 0.2);
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
            flex-shrink: 0;
        ">{num}</span>
        """
        for num in numbers
    ])
    return balls_html

st.markdown("---")

if st.button("🎲 5개 번호 5세트 생성하기", key="lotto_btn", use_container_width=True):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"생성 시간: **{now_str}**")
    st.write("")

    for set_index in range(1, 6):
        selected_numbers = lotto_one_set()
        balls_html = render_lotto_balls(selected_numbers)

        # 세트 텍스트와 5개의 공이 모두 한 줄에 가로로 나열
        st.markdown(
            f"""
            <div style="
                display: flex;
                flex-direction: row;
                align-items: center;
                margin-bottom: 14px;
                white-space: nowrap;
            ">
                <span style="font-weight: 600; font-size: 16px; min-width: 65px;">{set_index}세트:</span>
                <div style="display: flex; flex-direction: row; align-items: center;">
                    {balls_html}
            """,
            unsafe_allow_html=True
        )