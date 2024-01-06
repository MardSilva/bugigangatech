import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import pandas as pd

# Carregando o arquivo CSV para verificar seu conteúdo
file_path = 'C:\\Users\\User\\Desktop\\Desktop\\tempcsv\\python\\Indoor use_log_from_20230521_to_20231215_.csv'
data = pd.read_csv(file_path)

# Convertendo a coluna 'Time' para datetime
data['Time'] = pd.to_datetime(data['Time'])

# Filtrando os dados para o período de outubro a dezembro de 2023
periodo_foco = data[(data['Time'].dt.month >= 10) & (data['Time'].dt.year == 2023)]

# Criando um gráfico de linha para mostrar a variação diária de temperatura
plt.figure(figsize=(15, 7))

# Plotando as temperaturas para o período selecionado
plt.plot(periodo_foco['Time'], periodo_foco['Temperature(℃)'], label='Temperatura Diária', color='gray')

# Destacando o mês de novembro
novembro = periodo_foco[(periodo_foco['Time'].dt.month == 11) & (periodo_foco['Time'].dt.year == 2023)]
plt.plot(novembro['Time'], novembro['Temperature(℃)'], label='Novembro (com Onda de Calor)', color='orange')

# Adicionando detalhes ao gráfico
plt.title('Comparação de Temperaturas: Outubro a Dezembro de 2023')
plt.xlabel('Data')
plt.ylabel('Temperatura (℃)')
plt.legend()
plt.grid(True)

# Formatando o eixo x para melhor visualização
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.gcf().autofmt_xdate()  # Auto-ajuste para melhorar a legibilidade

# Mostrando o gráfico
plt.show()
