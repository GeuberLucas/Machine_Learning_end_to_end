#libs de dados
import pandas as pd
import numpy as np

#libs graficas
import matplotlib.pyplot as plt
import seaborn as sn

#avisos
import warnings
warnings.filterwarnings('ignore')

#config Pandas
pd.set_option('display.max_rows',200)
pd.set_option('display.max_columns',100)

#config Matplot
plt.rcParams['figure.figsize'] = (15,6)
plt.style.use('seaborn-darkgrid')


baseData= pd.read_csv('./house_data.csv')

print('dimensão da base= '+ str(baseData.shape))
#vendo dados
print(baseData.head())
print("----")
#Removendo colunas e dados vazios
baseData.drop(columns=['fire insurance (R$)','total (R$)'],inplace=True)
print(baseData.isnull().sum().sort_values(ascending=False))
print("----")

#campos Unicos
print(baseData.nunique())
print("----")


##EDA
categoryColumns= baseData.columns[baseData.dtypes == object]  
numbersColumns= baseData.columns[baseData.dtypes != object]  

#analise dos categoricos
print(str(categoryColumns))
print("----")
for column in categoryColumns:
    print(column)
    print(baseData[column].value_counts(normalize=True)*100)
    print("----")



#consertando dados
print(baseData.loc[baseData['floor']== '301'])
baseData.iloc[2562,5] = 30

#substituindo o - por 0
baseData['floor'] = baseData['floor'].apply(lambda r : 0 if r == '-' else r)

#substituindo tipos de dados
baseData['floor'] = pd.to_numeric(baseData['floor'])

#GRID - GRAFICOS

#tamanho
Figura,eixo = plt.subplots(figsize=(20,30))


#cor de fundo
cor_fundo = '#f5f5f5'
Figura.set_facecolor(cor_fundo)

#Paleta de Cores
paletteOfColors=sn.color_palette('flare', len(numbersColumns) * 2)

#Titulo
plt.suptitle('Análise das Variaveis')