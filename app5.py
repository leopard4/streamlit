# 웹 대시보드에 이미지파일, 동영상 파일 넣는방법

import streamlit as st
import pandas as pd


# 이미지 처리를 위한 라이브러리 
from PIL import Image

def main():
    img = Image.open('streamlit_data/image_03.jpg')

    print(img)

    st.image(img)
    
    st.image(img, use_column_width= True)

    image_url = 'https://www.motorgraph.com/news/photo/202212/31176_98030_5735.jpg'

    st.image(image_url)

    # 동영상 
    
    video_file = open('streamlit_data/secret_of_success.mp4','rb')

    st.video(video_file)





if __name__ == '__main__' : 
    main()