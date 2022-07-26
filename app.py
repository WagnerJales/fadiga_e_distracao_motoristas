import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline


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


# filtro para o gráfico
st.sidebar.markdown('## Filtro para o gráfico')

categoria_grafico = st.sidebar.selectbox('Selecione a categoria para apresentar no gráfico', options = dados['Eventos'].unique())
figura = plot_df2(df2, Eventos_grafico)
st.pyplot(figura)



figgeo = px.scatter_mapbox(df2, lat="Latitude", lon="Longitude", color="Velocidade", size="Eventos", width = 1500, height = 900, 
                       size_max=20, zoom=10,
                  mapbox_style="carto-positron")
figgeo.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
figgeo.show()
# uma escala de cor espcial pode ser adicionada utilizando - color_continuous_scale=px.colors.cyclical.IceFire,

"""**Observando os tipos de ocorrências pela velocidade ao longo do dia**

Considerando o eixo "x" como as horas ao longo dia "normalizada" (ou seja, variando de 0 a 1) observa-se o pico da manhã e o pico da tarde. 
Entre os tipos de ocorrência, apenas o "bocejo" possui eventos no pico da tarde sendo este superior ao primeiro, sua maior frequência são em baixas velocidades com tendência de redução a medida que se aumenta esta variável.
"Sonolência N1" contrabalanceia as ocorrências de "bocejo" concentrando as suas no pico da manhã quase não existindo no pico da tarde mas em contra-partida, em termos de velocidade, concetra 2 "picos"; em 32km/h e em 52km/h.
A "oclusão" possui eventos no "entre picos", não obedecendo ao padrão dos demais.
"olhando para baixo N2" tem características similares a "Sonolência N1" em relação a distribuição de eventos ao longo do dia, e em relação a velocidade, 
concentra suas ocorrências em baixas velocidades e vai decaindo a medida que a velocidade aumenta.
O caso de "Sonolência N2", unico registro do período, ocorre no pico da manhã e com velocidade acima da média.

"""

#Convertendo os dados da coluna "Eventos" de um tipo "inteiro" para "string"
df2.Eventos = df2.Eventos.astype(str)

df2['Eventos'] = df2['Eventos'].map({
    '1' : 'Bocejo', 
    '2' : 'Oclusão', 
    '4' : 'Olhando pra Baixo N2', 
    '5' : 'Sonolência N1', 
    '6' : 'Solonência N2'})

#rodando o gráfico de dispersão com histogramas 
px.scatter(df2, x="hora", y="Velocidade", color = "Eventos", size = "Velocidade", marginal_x="histogram", marginal_y="histogram", width = 1500, height = 700)


st.title('Conclusões e considerações\n')
st.title('Em relação a forma de captação da informação de fadiga\n')

st.write('O corpo manifesta de diversas a condição da fadiga/distraçãoo mas, apesar da experiência humana ser algo complexo, a tecnologia se esforça na busca de captar manifestações faciais que possam ser correlacionadas com a incapacidade do motorista de exercer a sua função, não capta necessariamente o que acontece por dentro pois nem toda expressão facial considerada na tecnologia é expressão da incapacidade do motorista em excercer a sua atividade. Mas esse fato não invalida o uso da tecnologia.')


st.write('O sistema de detecção de fadiga/distração pode ser considerado a última barreira para prevenção de acidentes mas uma barreira eficaz é aquela que sequer permitirá que o motorista incapaz inicie a jornada de trabalho.')
