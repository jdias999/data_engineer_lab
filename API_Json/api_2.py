import requests
import pandas as pd

url = "https://api.exchangerate-api.com/v4/latest/USD"

response = requests.get(url)
data = response.json() #aqui, ja transforma em dictionarie

dicionario_taxas = data['rates']
df_moedas = pd.DataFrame(dicionario_taxas.items(), columns=['Moedas', 'Cotacao'])
print(df_moedas.head())