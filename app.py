import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np


# função para selecionar a quantidade de linhas do dataframe
def mostra_qntd_linhas(dataframe):
    
    qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value = 1, max_value = len(dataframe), step = 1)

    st.write(dataframe.head(qntd_linhas).style.format(subset = ['Eventos'], formatter="{:.2f}"))


# importando os dados
dados = pd.read_csv('df2.csv')

st.title('Análise de ocorrências de Fadiga e Distração\n')
st.write('É possível prever quando um motorista manifestará sintomas de fadiga ao dirigir? A fadiga tem causas diversas e seus sintomas se manifestam por um bocejo ou até mesmo passando curtos espaços de tempo de olhos fechados ao volante? Uma das tecnologias desenvolvidas para identificar tais sintomas é através do reconhecimento deles na expressão facial dos motoristas. A partir dos dados históricos de uma operação de transporte de passageiros sob regime de fretamento, realizou-se uma análise exploratória dos dados e das relações entre as ocorrências (Variável explicada) e dados de tempo e espaço referente a tais ocorrências buscando identificar algum insght que possibilite modificar a operação para reduzir a exposição dos motoristas e, por consequencia, dos passeiros transportados.')


df = pd.dados(
     np.random.randn(1000, 2),
     columns=['Latitude', 'Longitude'])
st.map(df)

