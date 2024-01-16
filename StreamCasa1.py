# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:30:10 2023

@author: rian8
"""


 # Streamlit Casa 1 python 3.10 AmbientePy310


import streamlit as st
import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download the stopwords list (only need to run this once)
#nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import os


@st.cache_data

def AnaliseTexto(corpo,objeto1=None, objeto2=None):
       
    
    # Preprocess the sentences
    stop_words = set(stopwords.words('portuguese'))
    translator = str.maketrans('', '', string.punctuation)
    
    # =======================================================================
    def preprocess_text(sentence):
        # Convert to lowercase
        sentence = sentence.lower()
        
        # Remove punctuation
        sentence = sentence.translate(translator)
        
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        
        # Remove stopwords
        words = [word for word in words if word not in stop_words]
        
        # Join the words back into a sentence
        preprocessed_sentence = ' '.join(words)
        
        return preprocessed_sentence
    # =======================================================================
    
    corpo = [preprocess_text(sentence) for sentence in corpo]
    #print(corpo)
    
    # =======================================================================
    # Create a CountVectorizer to calculate term frequency
    if objeto1 == None: 
        vectorizer = CountVectorizer()
        tf_matrix = vectorizer.fit(corpo)
    else:
        vectorizer = objeto1
    # =======================================================================
    
    tf_matrix = vectorizer.transform(corpo)
    
    # Convert the TF matrix to a DataFrame
    tf_df = pd.DataFrame(tf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    # get_feature_names_out() python3.10

    
    
    # =======================================================================
    # Initialize the TfidfVectorizer
    if objeto2 == None: 
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit(corpo)
    else:
        tfidf_vectorizer = objeto2
    
        
    # =======================================================================
    
    # Fit and transform the documents into the TF-IDF matrix
     
    tfidf_matrix = tfidf_vectorizer.transform(corpo)
    
    # Convert the TF-IDF matrix to a dense numpy array (if needed)
    tfidf_matrix_dense = tfidf_matrix.toarray()
    
    # Get the feature names (words) from the TfidfVectorizer
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    
    # Create a new dataframe using feature_names and tfidf_matrix_dense
    df_tfidf = pd.DataFrame(tfidf_matrix_dense, columns=feature_names)
    
    # Print the new dataframe
    #print(df_tfidf)
    
    
    return tf_df, df_tfidf, vectorizer, tfidf_vectorizer

# Configuração do layout
st.set_page_config(layout="wide")
st.header("Analise Sentimento Tf-idf")

st.write('Escolha qual será o input do usuario')
colEsquerda, colCentral, colDireita= st.columns([2,7,6])

with colEsquerda:
    
    userInput = st.radio("Como está se sentido hoje?",('feliz', 'apaixonado','depressão','inseguro','com medo'))
    
    if userInput == 'feliz':
        #st.write('You selected feliz.')
        usuario = 'feliz'
        
    elif userInput =='apaixonado':
        #st.write('You selected apaixonado.')
        usuario = 'apaixonado'
        
    elif userInput =='depressão':
        #st.write('You selected depressão.') 
        usuario = 'depressao'
        
    elif userInput =='inseguro':
        #st.write('You selected inseguro.')
        usuario = 'inseguro'

    elif userInput =='com medo':
        #st.write('You selected com medo.')
        usuario = 'medo'
        
    user_path = 'usuario_input/'+usuario+'_text.txt'
    #st.write(user_path) 
    
    stop_button = st.button("Stop")
    if stop_button:
        st.write("Stopping the execution...")
        print("Stopping the execution...")
        st.stop()
        os._exit(0)
    
with colDireita:
    
    LivroBiblia = st.selectbox(
    'Qual livro da biblia deseja comparar?',
    ('Selecionar','Gênesis','Êxodo','Levítico','Números','Deuteronômio','Josué','Juízes','Rute','1 Samuel',
     '2 Samuel','1 Reis','2 Reis','1 Crônicas','2 Crônicas','Esdras','Neemias','Ester','Jó','Salmos',
     'Provérbios','Eclesiastes','Cânticos','Isaías','Jeremias','Lamentações','Ezequiel','Daniel',
     'Oséias','Joel','Amós','Obadias','Jonas','Miquéias','Naum','Habacuque','Sofonias','Ageu','Zacarias','Malaquias',
     'Mateus','Marcos','Lucas','João','Atos','Romanos','1 Coríntios','2 Coríntios','Gálatas',
     'Efésios','Filipenses','Colossenses','1 Tessalonicenses','2 Tessalonicenses','1 Timóteo',
     '2 Timóteo','Tito','Filemom','Hebreus','Tiago','1 Pedro','2 Pedro','1 João','2 João',
     '3 João','Judas','Apocalipse'
     ))

    st.write('Você selecionou:', LivroBiblia)
    
    
    def carregar_DataFrame_livros(nome_arquivo):
    
        df_livros = pd.read_csv(nome_arquivo,index_col=None)
        #print(df_livros)
        return df_livros

    if LivroBiblia != 'Selecionar':
        Book = carregar_DataFrame_livros('Biblia/nvi/'+ LivroBiblia +'.csv')
        st.dataframe(Book['texto'])
        
        
with colCentral:
    
    with open(user_path, 'r',encoding='utf8') as file:
        document = file.read()
    document = [document]
    #st.write(document[0]) 
    st.text_area('Texto Input usuário:', document[0],height=200)
    
    if LivroBiblia != 'Selecionar':
        corpus = Book["texto"].tolist()
    
        # Livro Biblia
        tf_livro, tfidf_livro, vectorizer, tfidf_vectorizer = AnaliseTexto(corpus)    
            
        # input usuario
        tf_User, tfidf_User, vectorizer, tfidf_vectorizer  = AnaliseTexto(document,objeto1 = vectorizer, objeto2 = tfidf_vectorizer)
        
                
        #similarity1 = pd.DataFrame(cosine_similarity(tfidf_livro, tfidf_User)).reset_index().rename(columns={0:'score'}).sort_values(['score'])

        similarity2 = pd.DataFrame(1 - cosine_similarity(tfidf_livro, tfidf_User)).reset_index().rename(columns={0:'score'}).sort_values(['score'])
            
        Book = Book.reset_index()
    
        df2 = Book.merge(similarity2, how='inner', on='index')
        
        Resultado_df = df2.drop(df2.columns[:3], axis=1)
        
        st.dataframe(Resultado_df.sort_values(['score']).head(8))
        