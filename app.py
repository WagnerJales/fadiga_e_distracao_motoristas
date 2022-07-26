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

    
    
# função que cria o gráfico
def plot_estoque(dataframe, categoria):

    dados_plot = dataframe.query('Eventos == @Eventos')

    fig, ax = plt.subplots(figsize=(8,6))
    ax = sns.barplot(x = 'Produto', y = 'Quantidade', data = dados_plot)
    ax.set_title(f'Quantidade em estoque dos produtos de {categoria}', fontsize = 16)
    ax.set_xlabel('Produtos', fontsize = 12)
    ax.tick_params(rotation = 20, axis = 'x')
    ax.set_ylabel('Quantidade', fontsize = 12)
  
    return fig



# importando os dados
dados = pd.read_csv('df2.csv')

st.title('Análise de ocorrências de Fadiga e Distração\n')
st.write('É possível prever quando um motorista manifestará sintomas de fadiga ao dirigir? A fadiga tem causas diversas e seus sintomas se manifestam por um bocejo ou até mesmo passando curtos espaços de tempo de olhos fechados ao volante? Uma das tecnologias desenvolvidas para identificar tais sintomas é através do reconhecimento deles na expressão facial dos motoristas. A partir dos dados históricos de uma operação de transporte de passageiros sob regime de fretamento, realizou-se uma análise exploratória dos dados e das relações entre as ocorrências (Variável explicada) e dados de tempo e espaço referente a tais ocorrências buscando identificar algum insght que possibilite modificar a operação para reduzir a exposição dos motoristas e, por consequencia, dos passeiros transportados.')




# filtros para a tabela
opcao_1 = st.sidebar.checkbox('Mostrar tabela')
if opcao_1:

    st.sidebar.markdown('## Filtro para a tabela')

    categorias = list(dados['Eventos'].unique())
    categorias.append('Todas')

    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = categorias)

    if categoria != 'Todas':
        df_categoria = dados.query('Eventos == @Eventos')
        mostra_qntd_linhas(df_categoria)      
    else:
        mostra_qntd_linhas(dados)



df3 = pd.dados(
     np.random.randn(1000, 2),
     columns=['Latitude', 'Longitude'])
st.map(df3)

