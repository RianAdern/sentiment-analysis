# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:56:42 2022

@author: rian8
"""
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

livros=['tt']
biblia = pd.DataFrame(columns=['livro','cap','versiculos','texto'])
for liv in livros:
    print(liv)
    for cap in range(3):
        cap = cap+1
        print(cap)
        url = 'https://www.bibliaonline.com.br/nvi/'+liv+'/'+str(cap)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        results = soup.find_all("p")
        for i in range(len(results)):
            versiculo = i+1
            print(versiculo)
            s = str(results[i])
            start = s.find("<!-- -->") + len("<!-- -->")
            end = s.find("</p>")
            substring = s[start:end]
            print(substring)
            biblia = pd.concat([biblia,pd.DataFrame([[liv,cap,versiculo,substring]],
                                                    columns=['livro','cap','versiculos','texto'])],axis=0)
            #with pd.ExcelWriter('biblia_nvi.xlsx') as writer:
            #    biblia.to_excel(writer,sheet_name='liv')