import pandas as pd

url_mercado = "produtos_mercado.csv" #importamos o DF copiando o nome junto com o csv
df_produtos= pd.read_csv(url_mercado)

#Quatas linhas e colunas tem o df
print("Total de colunas")
print(f"\nO dataframe de produtos de mercado tem {df_produtos.shape[0]} linhas e {df_produtos.shape[1]} colunas")

#Os nomes das colunas são:
print("-"*80)
print("\nO nome de cada coluna:")
print(list(df_produtos.columns))

#Os tipos de dadode cada coluna
print("-"*80)
print("\nO tipo de dados de cada coluna: ")
print(df_produtos.dtypes)
formato_data = df_produtos['Data_Ultima_Reposicao'].dtype
print(f"\nA coluna Data_ultima_Reposicao esta no formato '{formato_data}'")
print("Não esta no formato tradicional dia/mes/ano")

#Pedindo as 7 primeiras linhas do DataFrama
print("-"*80)
print("\n Chamando as 7 primeiras linhas do DataFrame:")
print(df_produtos.head(7))

#Exibindo as ultimas 3 linhas
print("-"*80)
print("\n *Ultimas 3 linhas do DataFrame de Produtos de mercado:")
print(df_produtos.tail(3))

#Obtendo um resumo estatistico das colunas (preço e estoque)
print("-"*80)
print("\nO Resumo estatistico é:")
print(df_produtos.describe())