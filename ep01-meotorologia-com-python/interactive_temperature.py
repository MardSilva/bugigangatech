import pandas as pd
import plotly.express as px

# Carregando o arquivo CSV
file_path = 'C:\\Users\\User\\Desktop\\Desktop\\tempcsv\\python\\Indoor use_log_from_20230521_to_20231215_.csv'
data = pd.read_csv(file_path)

# Convertendo a coluna 'Time' para datetime
data['Time'] = pd.to_datetime(data['Time'])

# Filtrando os dados para o período de outubro a dezembro de 2023
periodo_foco = data[(data['Time'].dt.month >= 10) & (data['Time'].dt.year == 2023)]

# Criando o gráfico interativo com Plotly
fig = px.line(periodo_foco, x='Time', y='Temperature(℃)', title='Comparação de Temperaturas: Outubro a Dezembro de 2023')

# Adicionando o mês de novembro com uma cor diferente
novembro = periodo_foco[(periodo_foco['Time'].dt.month == 11) & (periodo_foco['Time'].dt.year == 2023)]
fig.add_scatter(x=novembro['Time'], y=novembro['Temperature(℃)'], mode='lines', name='Novembro (com Onda de Calor)', line=dict(color='orange'))

# Mostrando o gráfico
fig.show()