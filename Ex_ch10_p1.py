# 아래에 코드를 작성해주세요.
import streamlit as st

def intro():
    st.markdown("# 나의 소개 페이지")
    st.markdown("## 자기소개")
    st.markdown("안녕하세요, 제 이름은 강태훈입니다.")
    st.markdown("저는 **식품 산업**에 관심이 있습니다.")
    st.markdown("## 좋아하는 것")
    st.markdown("저는 게임을 좋아합니다.")
    st.markdown("## 앞으로의 목표")
    st.markdown("배운 코딩을 바탕으로 다양하게 시도 해보고 싶습니다.")
    st.caption("제가 좋아하는 파이썬 코드")
    st.code("""
while True:
    continue
""",language = "python")

intro()
