# ИМПОРТ БИБЛИОТЕК
import streamlit as st
from streamlit_lottie import st_lottie
import json

# КОНФИГУРАЦИЯ ПРИЛОЖЕНИЯ
st.set_page_config(
    page_title="Happy Birthday Card",
    page_icon=":material/featured_seasonal_and_gifts:",
    layout="wide",
    menu_items=None
)

# ОФОРМЛЕНИЕ
st.markdown(
    """
    <style>    
    /* НАСТРОЙКИ ШРИФТА */
    /* Изменение цвета текста и шрифта в label */
    [data-testid="stWidgetLabel"] {
        font-size: 14px;                        /* Размер текста */
        font-family: 'Helvetica', sans-serif;   /* Шрифт текста */
    }

    /* Изменение шрифта */
    bodybody, h1, h2, h3, h4, h5, h6, p, div, span, li, a, blockquote, pre, code {
        font-family: 'Helvetica', sans-serif;
    }
    .st-emotion-cache-16tyu1 h1, 
    .st-emotion-cache-16tyu1 h2, 
    .st-emotion-cache-16tyu1 h3, 
    .st-emotion-cache-16tyu1 h4, 
    .st-emotion-cache-16tyu1 h5, 
    .st-emotion-cache-16tyu1 h6, 
    .st-emotion-cache-102y9h7 h1, 
    .st-emotion-cache-102y9h7 h2, 
    .st-emotion-cache-102y9h7 h3, 
    .st-emotion-cache-102y9h7 h4, 
    .st-emotion-cache-102y9h7 h5, 
    .st-emotion-cache-102y9h7 h6,
    .st-emotion-cache-16tyu1 td {
        font-family: 'Helvetica', sans-serif;
    }   

    /* Скрыть кнопку увеличение изображения */
    .st-emotion-cache-z56u96 {
        display: none;
    }
    
    /* Скрыть якорь заголовка */
    .st-emotion-cache-gi0tri {
        display: none !important;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# ФУНКЦИИ
# Загрузка Lottie-анимации из локального файла
def load_lottie_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


#ФРОНТ
# Заголовок
st.markdown("""
<h1 style="text-align: center; 
           margin: -81px 0 15px 0;   /* top, right, bottom, left */
           color: #2e2e2e; 
           font-family: 'Helvetica', sans-serif; 
           font-size: 4rem;
           font-weight: bold;">
    С Днём Рождения! 🎉
</h1>
""", unsafe_allow_html=True)

lottie_animation = load_lottie_file("files/congratulation.json")
st_lottie(lottie_animation, height=300, key="birthday")

tab1, tab2, tab3 = st.tabs(["1", "2", "3"])

text0 = "Руслан, пусть твоя жизнь будет наполнена яркими впечатлениями и бесконечным любопытством к миру!"
text1 = "Руслан, пусть рядом всегда будут верные друзья, которые ценят тебя и поддерживают любую твою идею!"
text2 = "Руслан, мы все гордимся тобой и любим тебя. Пусть в жизни будет много радости и удачи!"

with tab1:
    #st.header("Путешествия")
    col1, col2 = st.columns([1,1])
    with col1:
        st.image("files/hb_1.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""
                            <div 
                                style="background-color: #FFFAFA; 
                                padding: 20px; 
                                border-radius: 8px; 
                                text-align: left; 
                                font-style: italic; 
                                color: #2E2E2E;
                                white-space: pre-line;
                                margin: 0;">
                                {text0}
                            """, unsafe_allow_html=True)

with tab2:
    #st.header("Друзья")
    col1, col2 = st.columns([1,1])
    with col1:
        st.image("files/hb_2.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""
                            <div 
                                style="background-color: #FFFAFA; 
                                padding: 20px; 
                                border-radius: 8px; 
                                text-align: left; 
                                font-style: italic; 
                                color: #2E2E2E;
                                white-space: pre-line;
                                margin: 0;">
                                {text1}
                            """, unsafe_allow_html=True)
with tab3:
    #st.header("Любовь")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("files/hb_3.jpg", use_container_width=True)
    with col2:
        st.markdown(f"""
                    <div 
                        style="background-color: #FFFAFA; 
                        padding: 20px; 
                        border-radius: 8px; 
                        text-align: left; 
                        font-style: italic; 
                        color: #2E2E2E;
                        white-space: pre-line;
                        margin: 0;">
                        {text2}
                    """, unsafe_allow_html=True)







