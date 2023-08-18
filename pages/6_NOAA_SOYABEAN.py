import pandas as pd 



import pandas as pd 
import streamlit as st 
import pickle


import plotly.graph_objects as go
from plotly.subplots import make_subplots



df = pd.read_csv("NOAA_temp_data.csv")






stations = st.sidebar.radio('Stations',(['Chicago', 'Indiana', 'Iowa', 'Minnesota', 'Ohio']))
period = st.sidebar.radio('Period',(['Weekly','Monthly','Season']))
attributes = st.sidebar.radio('Attributes',(["Rainfall","Temperature"]))

per = {"Weekly":"week","Monthly":"month"}
attr = {"Rainfall":"PRCP","Temperature":"TMAX"}


st.title("NOAA Weather")


df  = df[df["Region"] == stations ]


def pivot_generation_rain(df,p):
    return df.pivot_table(columns="year",values ='PRCP',index = p,aggfunc="sum", margins=True)

 

def pivot_generation_temp(df,p):
    

    return df.pivot_table(columns="year",values ='TAVG',index = p,aggfunc="mean", margins=True)
















    year_start, year_end = st.slider('Select year range', min_value=2017, max_value=2023, value=(2018, 2023))
    month_start, month_end = st.slider('Select week range', min_value=1, max_value=12, value=(1, 12))


    filtered_df = df[(df['year'] >= year_start) & (df['year'] <= year_end)]
    filtered_df = filtered_df[(filtered_df['month'] >= month_start) & (filtered_df['month'] <= month_end)]
    filtered_df = filtered_df[filtered_df["Region"] == padd]



    st.subheader("Piviots Tables for {}".format(padd))
    for i in ['TMAX', 'TAVG', 'TMIN']:
    	st.subheader(i)
    	st.dataframe(pivot_generation(filtered_df,i).round(2),width = 700)





