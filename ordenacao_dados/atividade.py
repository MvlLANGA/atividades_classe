import pandas as pd

url_mercado = "produtos_mercado.csv" #importamos o DF copiando o nome junto com o csv
df_produtos= pd.read_csv(url_mercado)

#Selecionando e exibindo a coluna "Produto"
coluna_produtos = df_produtos['Produto']
print("Produtos:")
print(coluna_produtos)

#Selecionando e exibindo as colunas "Produtos", "Categorias" e "Preços_Kg"
colunas_df = df_produtos[['Produto','Categoria','Preco_Kg']]
print("-"*80)
print("Produtos:")
print(colunas_df)

#Exibindo os dados de produto com ID_produto igual a 110(Limao Tahiti)
produto_filtrado = df_produtos[df_produtos['ID_Produto']>=110]
print("-"*80)
print(produto_filtrado)

#Quais são os produtos da categoria verdura?
categoria_verduras = df_produtos[df_produtos['ID_Produto'] =='Verdura']
print("-"*80)
print("\nOs produtos que tem a categoria verdura: ")
print(categoria_verduras.head())

#Quais frutas tem um preço superior a 10Reais
df_frutas_preco= df_produtos[df_produtos['Preco_Kg'] > 10.0]
print("-"*80)
print("n\As frutas com preco maior que 10Reais são: ")
print(df_frutas_preco)

#Os produtos repostos no dia "2024-0601"
df_produtos['Data_Ultima_Reposicao'] = pd.to_datetime(df_produtos['Data_Ultima_Reposicao'], errors='coerce')
print("-"*80)
produtos_repostos = df_produtos[df_produtos['Data_Ultima_Reposicao']== '2024-06-01']
print(produtos_repostos)

#OS Produtos fornecidos pela fazenda sol nascente e da categoria frutas
produtos_fazenda = df_produtos[df_produtos['Categoria'] == 'Fruta']
print("-"*80)
print("\nOs produtos da Fazendo Sol nascente do genero frutas são: ")
print(produtos_fazenda['Produto'].head())

#Produtos 'Frutas' ou tem Estoque_kg maior que 150kg
frutas_kg = df_produtos[(df_produtos['Categoria'] == 'Fruta') & (df_produtos['Estoque_Kg']>150)]
print("-"*80)
print("\n Os produtos que tem mais de 150Kg em estoque são: ")
print(frutas_kg['Produto'].head(10))
