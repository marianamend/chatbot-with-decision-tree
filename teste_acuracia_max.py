import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/rapha/Documents/1_MariLinda/Projetos Python/arvore_pe/teste_auto_avaliacao/kc_house_data_teste.csv') #DataFrame das informações dos imóveis 
df_backup = df.copy() #DataFrame de backup das informações dos imóveis 

histogram_build = 'sqft_living'   #Variável selecionada para a análise, metro quadrado do imóvel 

sns.histplot(data = df, x = histogram_build)

df_zipcode = df[df['zipcode'] == 98001]

sns.histplot(data = df_zipcode, x = histogram_build)

#Definindo preço por metro quadrado 
price_sqft = df['price']/df['sqft_living']
df_backup['price_sqft'] = price_sqft

def class_output(x):  #criando uma função para agregar os valores do output
    if(x<-0.5):
        return 0
    elif(x<0.5):
        return 1
    else:
        return 2

df_zipcode = 98001
df_backup_zipcode = df_backup[df_backup['zipcode']==98001] #Novo DataFrame com o recorte do zipcode

media_price_sqft = df_backup_zipcode['price_sqft'].mean()  #Calculando a média por metro quadrado 

std_price_sqft = df_backup_zipcode['price_sqft'].std()  #Calculando o desvio padrão para calcular o Zscore

zscore = (df_backup_zipcode['price_sqft']-media_price_sqft) / std_price_sqft   #Calculando o zscore
df_backup_zipcode['zscore']  = zscore #Incluindo zscore no DF backup

df_backup_zipcode['class'] = df_backup_zipcode['zscore'].apply(class_output) #Armazenamos os parâmetros do output numa função 'class' e automatizamos o processo com a função apply

df_backup_zipcode

#df_backup_zipcode = df_backup_zipcode.drop(362,361,360,359,358,357,356,355,354,353)

df_backup_zipcode = df_backup_zipcode.reset_index(drop=True)
filter_ten = range(0,352)
#df_backup_zipcode_filter = df_backup_zipcode.iloc[[filtro], :]
#df_backup_zipcode_filter

df_backup_zipcode_filter_ten = df_backup_zipcode.loc[filter_ten]

df_backup_zipcode_filter_ten

from sklearn.cluster import KMeans
import numpy as np
pricesT=[]
prices= df_backup_zipcode_filter_ten['price'].values
for price in prices:
      pricesT.append([price])
kmeans_price = KMeans(n_clusters=3, random_state=0).fit(pricesT) #Clusters=3 nos garantiu um melhor resultado

prices_disc=[]
for price in prices:
  price_disc=kmeans_price.predict([[price]])
  prices_disc.append(price_disc[0])

df_backup_zipcode_filter_ten['price_discretized']=prices_disc
df_backup_zipcode_filter_ten.head()


from sklearn import tree 
import graphviz 


X=df_backup_zipcode_filter_ten[['bedrooms', 'yr_built', 'bathrooms', 'floors']]  
Y=df_backup_zipcode_filter_ten[['class']]

clf = tree.DecisionTreeClassifier(min_samples_leaf=20, min_impurity_decrease=0.001, min_samples_split=20)
clf = clf.fit(X, Y)
#min_samples_leaf=20, min_impurity_decrease=0.001, min_samples_split=20, modificar a nosso gosto
cn=['Abaixo da média ', 'Dentro da Média', 'Acima da média']

dot_data=tree.export_graphviz(clf,out_file=None,feature_names=X.columns, filled=True, rounded=True,class_names = cn, special_characters=True)
graph = graphviz.Source(dot_data)

print("\n\n\nSeja bem-vinda(o) ao Mig! \nNosso chatbot que irá lhe fornecer um orçamento sobre imóveis!\n ")

while True: 
    print("Caso queira encerrar, digite: '-1'\n ")
    while True:
        p1 = int(input('Digite a quantidade de quartos: '))
        if p1 == -1:
            print("\n--------fim--------")
            break
            
        p2 = int(input('Digite o ano de construção da casa: '))
        if p2 == -1:
            ("\n--------fim--------")
            break
            
        p3 = float(input('Digite a quantidade de banheiros: '))
        if p3 == -1:
            ("\n--------fim--------")
            break
            
        p4 = int(input('Digite a quantidade de pisos: '))
        if p4 == -1:
            ("\n--------fim--------")
            break
   
        
        model_answer = clf.predict([[p1,p2,p3,p4]])

        answer = 'teste'

        ternary_result = int(model_answer)
        if ternary_result == 1:
            answer = 'Preço por m² está dentro da média!\n'
        elif ternary_result == 2:
            answer = 'Preço está acima da média!\n'
        else:
            answer = 'Preço está abaixo da média!\n'

        print(answer)
        
    if p1 == -1 or p2 == -1 or p3 == -1 or p4 == -1:
        break
           


