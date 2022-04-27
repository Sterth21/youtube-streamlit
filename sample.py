# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 15:17:18 2022

@author: naohi
"""

import streamlit as st
import time

st.title("streamlit　超入門")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration=st.empty()
bar=st.progress(0)

time.sleep(3)

for i in range(100):
    latest_iteration.text(f"iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done!!"


left_column,right_columns=st.columns(2)

button=left_column.button("右カラムに表示")
if button:
    right_columns.write("ここは右カラムです")
    
expander1=st.expander("問い合わせ1")
expander1.write("問い合わせ内容を書く")

expander2=st.expander("問い合わせ2")
expander2.write("問い合わせ内容を書く")

expander3=st.expander("問い合わせ3")
expander3.write("問い合わせ内容を書く")



#text=st.text_input("あなたの趣味を教えてください。")
#"あなたの趣味：",text

#condition=st.slider("あなたの今の調子は",0,100,50,10)
#"あなたのコンディション",condition

