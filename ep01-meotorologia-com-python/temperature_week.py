import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

# Carregando o arquivo CSV
file_path = 'C:\\Users\\User\\Desktop\\Desktop\\tempcsv\\python\\Indoor use_log_from_20230521_to_20231215_.csv'
data = pd.read_csv(file_path)

# Convertendo a coluna 'Time' para datetime
data['Time'] = pd.to_datetime(data['Time'])

# Filtrando os dados para a semana anterior à onda de calor (6/11 a 12/11) e a semana da onda de calor (13/11 a 19/11)
semana_anterior = data[(data['Time'] >= datetime(2023, 11, 6)) & (data['Time'] < datetime(2023, 11, 13))]
semana_onda_calor = data[(data['Time'] >= datetime(2023, 11, 13)) & (data['Time'] < datetime(2023, 11, 20))]

# Criando o gráfico
plt.figure(figsize=(15, 7))

# Plotando as temperaturas para a semana anterior
plt.plot(semana_anterior['Time'], semana_anterior['Temperature(℃)'], label='Semana Anterior (6/11 a 12/11)', color='blue')

# Plotando as temperaturas para a semana da onda de calor
plt.plot(semana_onda_calor['Time'], semana_onda_calor['Temperature(℃)'], label='Semana da Onda de Calor (13/11 a 19/11)', color='red')

# Adicionando detalhes ao gráfico
plt.title('Comparação de Temperaturas: Semana Anterior vs Semana da Onda de Calor (Novembro 2023)')
plt.xlabel('Data')
plt.ylabel('Temperatura (℃)')
plt.legend()
plt.grid(True)

# Formatando o eixo x para melhor visualização
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gcf().autofmt_xdate()  # Auto-ajuste para melhorar a legibilidade

# Mostrando o gráfico
plt.show()