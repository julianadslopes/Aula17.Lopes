# pip install pandas sqlalchemy pymysql
import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pandas as pd

os.system("cls")

def pular_linha ():
    print('*' * 70)

host = "localhost"
user = "root"
password = "root"
database = "bd_loja"
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


#leitura dos dados da tabela de produtos
df_estoque = pd.read_sql ("tb_produtos", engine)
pular_linha()

# # printando os 5 primeiros
print(df_estoque.head())
pular_linha()

# Calcula o valor do estoque por linha
df_estoque["TotalEstoque"] = df_estoque["QuantidadedeEstoque"] * df_estoque["Valor"]
print (df_estoque[["NomeProduto", "TotalEstoque"]])
pular_linha()

# Calcula o valor do total do estoque
print (f'Total geral em estoque: R${df_estoque["TotalEstoque"].sum():.2f}')
pular_linha()

# Calcula valor médio dos produtos
valor_medio = np.mean(df_estoque["Valor"])
print (f'O valor médio por produto é: R$ {valor_medio:.2f}')
pular_linha()

# Calcula mediana do valor dos produtos
mediana_valor = np.median(df_estoque["Valor"])
print (f'A mediana dos produtos é de: R$ {mediana_valor:.2f}')
pular_linha()

# Transformando o campo TOTALESTOQUE em um array numpy
array_total_estoque = np.array(df_estoque["TotalEstoque"])

# Print (array_total_estoque)
media = np.mean(array_total_estoque)
mediana = np.median (array_total_estoque)
pular_linha()

# Distância entre média e mediana (em valor absoluto "abs")
distancia_media_mediana = abs((media-mediana)/mediana)
print(distancia_media_mediana)
pular_linha()

print (f'A média do Total de Estoque é: R$ {media:.2f}')
print (f'A mediana é igual a: R$ {mediana:.2f}')
print (f'Distância entre a média e a mediana: {distancia_media_mediana:.2f}')
pular_linha()

# Agrupando os produtos com o mesmo nome e somando as quantidades e valores
df_agrupado = df_estoque.groupby("NomeProduto").agg({"QuantidadedeEstoque": "sum", "TotalEstoque": "sum"}).reset_index()
print(df_agrupado)
pular_linha()

# Ordenando os produtos pelo total de estoque
df_ordenado = df_agrupado.sort_values(by="TotalEstoque", ascending=False)
print (df_ordenado[["NomeProduto","TotalEstoque"]])
pular_linha()

# Calculando o total geral do estoque
print (f'\n Total geral em estoque: R$ {df_ordenado["TotalEstoque"].sum():.2f}')