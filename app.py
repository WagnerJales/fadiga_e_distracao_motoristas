import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

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
"olhando para baixo N2" tem características similares a "Sonolência N1" em relação a distribuição de eventos ao longo do dia, e em relação a velocidade, concentra suas ocorrências em baixas velocidades e vai decaindo a medida que a velocidade aumenta.
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

"""# Conclusões e considerações

**Em relação a forma de captação da informação de fadiga**

O corpo manifesta de diversas a condição da fadiga/distraçãoo mas, apesar da experiência humana ser algo complexo, a tecnologia se esforça na busca de captar manifestações faciais que possam ser correlacionadas com a incapacidade do motorista de exercer a sua função, não capta necessariamente o que acontece "por dentro" pois nem toda expressão facial considerada na tecnologia é expressão da incapacidade do motorista em excercer a sua atividade. Mas esse fato não invalida o uso da tecnologia.

O sistema de detecção de fadiga/distração pode ser considerado a "última barreira" para prevenção de acidentes mas uma barreira eficaz é aquela que sequer permitirá que o motorista incapaz inicie a jornada de trabalho.



**Sobre o dado 'Olhar para baixo N1'**

Este evento é captado quando o motorista desvia o olhar da frente em 1,5seg e esse tipo de comportamento não caracteriza necessariamente o comportamento de fadiga/distração pois esse desvio é necessário para que o motorista olha o retrovisor em cruzamentos, conversões e paradas em semáforos. 



**Sobre a 'Oclusão'**

A Oclusão também não é necessiariamente o comportamento de fadiga/distração pois é uma ação voluntária do motorista em inibir o funcionamento da câmera sugerindo ações adiministrativas com a identificação dos motoristas. A oclusão também pode ser falha no equipamento.


**Em relação aos dias da semana**

A chamada "lei do motorista" (13.103/2015) prevê tempo descanço no interjornada para os motoristas mas é necessário expandir o conceito pois qualquer esforço prolongado que o motorista execute no final-de-semana que não seja necessariamente digirir, está sujeito a ter o mesmo efeito no que diz repeito a coloca-lo numa condição de fadiga. 

É necessário observar se de fato os motoristas do regime administrativo (que operam de segunda a sexta) estão cumprindo o repouso necessário no final de semana para que não começem a jornada na segunda-feita já fadigados. Para isso pode-se associar testes de atenção antes do inicio da jornada, especialmente para estes casos.


**Em relação ao local das ocorrências**

A concentração das ocorrências em "baixa velocidade" na área industrial sugere que de fato os motoristas obedecem as retrições de velocidade impostas devido ao próprio risco operacional do lugar. O fato de haver uma quantidade significativa de ocorrência nessa região citada não significa necessamente que os motoristas são mais fadigados ou distraídos em tais locais, o que de fato ocorre é que se tem mais quilômetro rodado por m² nessa região do que no restante da cidade, então a possibilidade de ocorrência dos eventos dentro da área industrial é significativamente superior. Para testes futuros, pode-se agregar à analise um indicador de "densidade de circulação" para que fututos modelos preditivos captem tal condição.

Em relação as ocorrências no Araçagy, precisaria observa o inicio da jornada de trabalho dos motoristas pois, operacionalmente, o mesmo precisa ir até a gararem pegar o veiculos para depois se dirigir até o ponto inicial da rota. Se considerar as rotas mais longas e de ponto inicial distante da garagem como no caso destas, o motorista precisa acordar até 3h antes que o primeiro empregado chegue na área industrial.

**Recomendações para trabalhos futuros**

Recomenda-se a realização de testes estatísticos que permitam verificar a hipotese de haver uma relação "hierarquia" entre os tipos de ocorrências como uma espécie de "pirâmide de Bird" da qual possa se prever um caso mais grave (no caso, sonolência N2) a partir do acumulo de ocorrências menos graves. Por exemplo, quantas ocorrências de "Sonolência N1" acontecem antes de uma "N2"?

Para isso é necessário que os dados sejam estruturados de forma a vincular as ocorrências ao motorista realizando numa mesma viagem. Esse tipo de estruturação de dados facilitará até na identificação da fadiga/distração como causas durante a investigação de acidentes.
"""
