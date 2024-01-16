# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 19:23:16 2022

@author: rian8
"""

import glob
import pandas as pd

# ===== Construtor de livros ===================
'''
lista = []
print('Named explicitly ?:')

for name in glob.glob('C:/DATA SCIENCE/programas em python/Projeto_biblia/NV_TT/*.xlsx'):
    lista.append(name[57:])
    print(name)    
    
print(lista)'''



# ===== Ordenar a lista =======================

Dicionario_nome_ntt = ['Mateus','Marcos','Lucas','João',
                      'Atos','Romanos','1 Coríntios',
                      '2 Coríntios','Gálatas','Efésios',
                      'Filipenses','Colossenses','1 Tessalonicenses',
                      '2 Tessalonicenses','1 Timóteo','2 Timóteo',
                      'Tito','Filemom','Hebreus','Tiago',
                      '1 Pedro','2 Pedro','1 João',
                      '2 João','3 João','Judas','Apocalipse'
                      ]
 
Dicionario_nome_vtt= ['Gênesis','Êxodo','Levítico','Números',
                      'Deuteronômio','Josué','Juízes','Rute',
                      '1 Samuel','2 Samuel','1 Reis','2 Reis',
                      '1 Crônicas','2 Crônicas','Esdras','Neemias',
                      'Ester','Jó','Salmos','Provérbios',
                      'Eclesiastes','Cânticos','Isaías','Jeremias',
                      'Lamentações','Ezequiel','Daniel','Oséias',
                      'Joel','Amós','Obadias','Jonas','Miquéias',
                      'Naum','Habacuque','Sofonias','Ageu',
                      'Zacarias','Malaquias'
                      ]






# ===== Chamar função de captura ===============


df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]],
                   columns=['letter', 'number'])

def juntion_dataframe(data1,data2):
    juntiondf3 = pd.concat([data1, data2])
    
    return juntiondf3


resultado = juntion_dataframe(df1, df2)

i =0
for i in range(3):
    i+=1
    print(i)
    df1 = juntion_dataframe(df1, df2)
    
    
print (df1)


# ===== junção dos dataframes ==================





    