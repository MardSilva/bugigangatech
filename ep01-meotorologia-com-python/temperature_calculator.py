import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np
import pandas as pd

# loading the csv 
file_path = 'C:\\Users\\User\\Desktop\\Desktop\\tempcsv\\python\\Indoor use_log_from_20230521_to_20231215_.csv'
data = pd.read_csv(file_path)

# showing the first lines to a better understanding 
data.head()
# converting the 'time' column to an datetime
data['Time'] = pd.to_datetime(data['Time'])

# setting up some items
inicio_onda_calor = datetime(2023, 11, 14)
fim_onda_calor = inicio_onda_calor + pd.Timedelta(days=7)

# filtering
dados_onda_calor = data[(data['Time'] >= inicio_onda_calor) & (data['Time'] < fim_onda_calor)]

# grouping by month
data['Month'] = data['Time'].dt.to_period('M')
media_mensal = data.groupby('Month')['Temperature(℃)'].mean()

# creating the graph
plt.figure(figsize=(12, 6))
plt.plot(media_mensal.index.to_timestamp(), media_mensal, marker='o', linestyle='-', color='blue', label='Média Mensal')
plt.scatter(dados_onda_calor['Time'], dados_onda_calor['Temperature(℃)'], color='red', label='Semana de Onda de Calor')

# formatting
plt.title('Variação de Temperatura Mensal de Maio a Dezembro de 2023')
plt.xlabel('Mês')
plt.ylabel('Temperatura (℃)')
plt.xticks(media_mensal.index.to_timestamp(), media_mensal.index.strftime('%b %Y'))
plt.legend()
plt.grid(True)

# showing
plt.show()