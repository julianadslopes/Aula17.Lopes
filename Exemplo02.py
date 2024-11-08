import os
import pandas as pd
import numpy as np

# Obter dados:
try: 
    print ("Obtendo dados...")
    ENDERECO_DADOS = "https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv"

# Encodings: utf-8, iso 8859, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep= ";", encoding="iso-8859-1")

# Delimitando somente as variáveis do Exemplo01: munic e roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[["munic", "roubo_veiculo"]]

# Totalizar roubo_veiculos por munic
    df_roubo_veiculo = df_roubo_veiculo.groupby(["munic"]).sum(["roubo_veiculo"]).reset_index()
    print(df_roubo_veiculo.head())
    print("\nDados obtidos com sucesso!")

except Exception as e:
    print (f'Erro ao obter dados: {e}')
    exit()

print("*****************************************************************************************************")
# Gerando novos dados:
try: 
    print ("\n Calculando informações sobre padrão de roubo de veículos...")
#Array NumPy
    array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])
# Média de roubo_veiculo
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
# Mediana de roubo_veiculo - Divide a distribuição em duas partes iguais
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)
# Distância entre média e mediana para ver se o valor da média é aceitável
    distancia_media_mediana = abs(media_roubo_veiculo-mediana_roubo_veiculo)/mediana_roubo_veiculo

# PRINTS    
    print(f' Média: {media_roubo_veiculo}')
    print(f' Mediana: {mediana_roubo_veiculo}')
    print(f' Distância: {distancia_media_mediana}')
except Exception as e:
    print (f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()     