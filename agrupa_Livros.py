# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:42:03 2023

@author: rian8
"""
import requests
import pandas as pd
import os

# =================== Agrupar os arquivos csv =================================

velhott = ['gn','ex','lv','nm','dt','js','jz','rt','1sm','2sm','1rs','2rs',
           '1cr','2cr','ed','ne','et','jó','sl','pv','ec','ct','is','jr',
           'lm','ez','dn','os','jl','am','ob','jn','mq','na','hc','sf','ag',
           'zc','ml']

novott = ['mt','mc','lc','jo','atos','rm','1co','2co','gl','ef',
          'fp','cl','1ts','2ts','1tm','2tm','tt','fm','hb','tg',
          '1pe','2pe','1jo','2jo','3jo','jd','ap']


def Nome_livros(nome_livro, Testamento):
    
    if Testamento == 'NOVO': 
        Dicionario_nome_ntt = {'mt':'Mateus','mc':'Marcos','lc':'Lucas','jo':'João',
                               'atos':'Atos','rm':'Romanos','1co':'1 Coríntios',
                               '2co':'2 Coríntios','gl':'Gálatas','ef':'Efésios',
                               'fp':'Filipenses','cl':'Colossenses','1ts':'1 Tessalonicenses',
                               '2ts':'2 Tessalonicenses','1tm':'1 Timóteo','2tm':'2 Timóteo',
                               'tt':'Tito','fm':'Filemom','hb':'Hebreus','tg':'Tiago',
                               '1pe':'1 Pedro','2pe':'2 Pedro','1jo':'1 João',
                               '2jo':'2 João','3jo':'3 João','jd':'Judas','ap':'Apocalipse'
                               }
        return Dicionario_nome_ntt[nome_livro]
    
    elif Testamento == 'VELHO': 
        Dicionario_nome_vtt= {'gn':'Gênesis','ex':'Êxodo','lv':'Levítico','nm':'Números',
                              'dt':'Deuteronômio','js':'Josué','jz':'Juízes','rt':'Rute',
                              '1sm':'1 Samuel','2sm':'2 Samuel','1rs':'1 Reis','2rs':'2 Reis',
                              '1cr':'1 Crônicas','2cr':'2 Crônicas','ed':'Esdras','ne':'Neemias',
                              'et':'Ester','jó':'Jó','sl':'Salmos','pv':'Provérbios',
                              'ec':'Eclesiastes','ct':'Cânticos','is':'Isaías','jr':'Jeremias',
                              'lm':'Lamentações','ez':'Ezequiel','dn':'Daniel','os':'Oséias',
                              'jl':'Joel','am':'Amós','ob':'Obadias','jn':'Jonas','mq':'Miquéias',
                              'na':'Naum','hc':'Habacuque','sf':'Sofonias','ag':'Ageu',
                              'zc':'Zacarias','ml':'Malaquias'
                              }
        return Dicionario_nome_vtt[nome_livro]


def Numero_capitulos(nome_livro, Testamento):

    if Testamento == 'NOVO': 
        Dicionario_cap_ntt = {'mt':28,'mc':16,'lc':24,'jo':21,'atos':28,'rm':16,
                              '1co':16,'2co':13,'gl':6,'ef':6,'fp':4,'cl':4,
                              '1ts':5,'2ts':3,'1tm':6,'2tm':4,'tt':3,'fm':1,
                              'hb':13,'tg':5,'1pe':5,'2pe':3,'1jo':5,'2jo':1,
                              '3jo':1,'jd':1,'ap':22
                               }
        return Dicionario_cap_ntt[nome_livro]
        
    elif Testamento == 'VELHO':
        Dicionario_cap_vtt = {'gn':50,'ex':40,'lv':27,'nm':36,'dt':34,'js':24,
                              'jz':21,'rt':4,'1sm':31,'2sm':24,'1rs':22,'2rs':25,
                              '1cr':29,'2cr':36,'ed':10,'ne':13,'et':10,'jó':42,
                              'sl':150,'pv':31,'ec':12,'ct':8,'is':66,'jr':52,
                              'lm':5,'ez':48,'dn':12,'os':14,'jl':3,'am':9,'ob':1,
                              'jn':4,'mq':7,'na':3,'hc':3,'sf':3,'ag':2,'zc':14,
                              'ml':4
                              }
        return Dicionario_cap_vtt[nome_livro]
 


def VerificaArquivosPasta(PastaPrimaria,versao):
    
    # Diretório que contém os arquivos ========================================
    diretorio = PastaPrimaria+'/'+versao
    
    # Lista para armazenar os nomes dos arquivos
    lista_arquivos = []
    
    # Iterar sobre os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        # Verificar se é um arquivo
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            # Adicionar o nome do arquivo à lista
            lista_arquivos.append(arquivo)

    return lista_arquivos


ListaLivros = VerificaArquivosPasta('Biblia','nvi')



caminho_pasta = 'Biblia/nvi'

# Lista para armazenar os caminhos dos arquivos CSV
lista_caminhos_arquivos = []

# Loop para listar os arquivos na pasta e adicionar os caminhos dos arquivos CSV na lista
for nome_arquivo in os.listdir(caminho_pasta):
    if nome_arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
        lista_caminhos_arquivos.append(caminho_arquivo)


# =============================================================================

# Lista para armazenar todos os DataFrames
lista_dataframes = []

# Leitura de cada arquivo CSV e adição ao DataFrame
for caminho_arquivo in lista_caminhos_arquivos:
    df = pd.read_csv(caminho_arquivo)
    lista_dataframes.append(df)

# Concatenação dos DataFrames em um único DataFrame
df_concatenado = pd.concat(lista_dataframes, ignore_index=True)

# Caminho para o novo arquivo CSV que será gerado com os 50 arquivos juntos
caminho_arquivo_concatenado = 'Biblia/Biblia_NVI_ArquivoUnico.csv'

# Salvando o DataFrame resultante em um novo arquivo CSV
df_concatenado.to_csv(caminho_arquivo_concatenado, index=False)

print("Arquivos concatenados com sucesso e salvo em:", caminho_arquivo_concatenado)

