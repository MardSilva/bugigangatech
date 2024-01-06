import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

# Carregando o arquivo CSV
file_path = 'C:\\Users\\User\\Desktop\\Desktop\\tempcsv\\python\\Indoor use_log_from_20230521_to_20231215_.csv'
data = pd.read_csv(file_path)

# Convertendo a coluna 'Time' para datetime
data['Time'] = pd.to_datetime(data['Time'])

# Filtrando os dados para o mês anterior (outubro) e a semana da onda de calor (13/11 a 19/11)
mes_anterior = data[(data['Time'] >= datetime(2023, 10, 1)) & (data['Time'] < datetime(2023, 11, 1))]
semana_onda_calor = data[(data['Time'] >= datetime(2023, 11, 13)) & (data['Time'] < datetime(2023, 11, 20))]

# Criando o gráfico
plt.figure(figsize=(15, 7))

# Plotando as temperaturas para o mês anterior
plt.plot(mes_anterior['Time'], mes_anterior['Temperature(℃)'], label='Outubro 2023', color='green')

# Plotando as temperaturas para a semana da onda de calor
plt.plot(semana_onda_calor['Time'], semana_onda_calor['Temperature(℃)'], label='Semana da Onda de Calor (13/11 a 19/11)', color='red')

# Adicionando detalhes ao gráfico
plt.title('Comparação de Temperaturas: Outubro 2023 vs Semana da Onda de Calor (13/11 a 19/11)')
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
