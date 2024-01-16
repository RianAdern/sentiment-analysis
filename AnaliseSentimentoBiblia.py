# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:22:23 2023

@author: rian8
"""


import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download the stopwords list (only need to run this once)
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


def carregar_DataFrame_livros(nome_arquivo):
    
    df_livros = pd.read_csv(nome_arquivo,index_col=None)
    #print(df_livros)
    return df_livros

nomelivro ='Provérbios'

Book = carregar_DataFrame_livros('Biblia/nvi/'+ nomelivro +'.csv')

usuario = 'feliz'

user_path = 'usuario_input/'+usuario+'_text.txt'

# Abre o input do usuario
with open(user_path, 'r',encoding='utf8') as file:
    document = file.read()
#print(document)
document = [document]


data = {
    'texto': [
    'A depressão é uma doença séria que afeta milhões de pessoas ao redor do mundo.',
    'Sentir-se constantemente triste e sem motivação são sintomas comuns da depressão.',
    'É mportante buscar ajuda profissional ao lidar com a depressão, como um psicólogo ou psiquiatra.',
    'Apoio emocional e compreensão por parte dos amigos e familiares são essenciais para quem enfrenta a depressão.'
    ]
}

corpus = pd.DataFrame(data)["texto"].tolist()


document = ['A depressão é uma doença séria que afeta milhões de pessoas ao redor do mundo.']


# livro
corpus = Book["texto"].tolist()



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
    tf_df = pd.DataFrame(tf_matrix.toarray(), columns=vectorizer.get_feature_names())
    
    
    # Print the list of words
    word_list = vectorizer.get_feature_names()
    #print(word_list)
    
    
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
    feature_names = tfidf_vectorizer.get_feature_names()
    # .get_feature_names() python 3.7
    
    # Create a new dataframe using feature_names and tfidf_matrix_dense
    df_tfidf = pd.DataFrame(tfidf_matrix_dense, columns=feature_names)
    
    # Print the new dataframe
    #print(df_tfidf)
    
    
    return tf_df, df_tfidf, vectorizer, tfidf_vectorizer
    
    #---- Arquivos de Saida ------------------------------------------------------
    
    file_path = 'palavras_matriz_'+nomelivro+'_tf.txt'
    
    # Open file in write mode
    with open(file_path, "w") as f:
        # Write each element of the list to the file
        for item in word_list:
            f.write("%s\n" % item)
    
    # exportar a matriz dt_df
    tf_df.to_csv('biblia_'+nomelivro+'_tf.csv',sep =';',encoding ='latin1',index=False)
    df_tfidf.to_csv('biblia_'+nomelivro+'_tf_idf.csv',sep =';',encoding ='latin1',index=False)
    

# Livro Biblia
tf_livro, tfidf_livro, vectorizer, tfidf_vectorizer = AnaliseTexto(corpus)    
    
# input usuario
tf_User, tfidf_User, vectorizer, tfidf_vectorizer  = AnaliseTexto(document,objeto1 = vectorizer, objeto2 = tfidf_vectorizer)



#columns1 = list(tfidf_livro.columns)
#columns2 = list(tfidf_User.columns)

#all_feature_names = set(columns1).union(columns2)


#tfidf_livro = pd.DataFrame(tfidf_livro.values, columns=all_feature_names)
#tfidf_User = pd.DataFrame(tfidf_User.values, columns=all_feature_names)

similarity1 = pd.DataFrame(cosine_similarity(tfidf_livro, tfidf_User)).reset_index().rename(columns={0:'score'}).sort_values(['score'])

similarity2 = pd.DataFrame(1 - cosine_similarity(tfidf_livro, tfidf_User)).reset_index().rename(columns={0:'score'}).sort_values(['score'])


Book = Book.reset_index()

df2 = Book.merge(similarity2, how='inner', on='index')

Resultado_df = df2.drop(df2.columns[:2], axis=1)

print(Resultado_df.sort_values(['score']).head(8))


# stemming, lematization, knn

