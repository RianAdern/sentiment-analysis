# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 17:00:11 2022

@author: rian8
"""

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import unidecode
import unicodedata
import json
palavras = pd.read_excel('sinonimos.xlsx',engine='openpyxl')
dic_pal_sin={}
for pal in palavras.values.tolist():
    print(pal[0])
    pal_clean = unidecode.unidecode(pal[0])
    print(pal_clean)
    url = 'https://www.sinonimos.com.br/'+pal_clean
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    results = soup.find_all("a", {"class": "sinonimo"})
    print(results)
    lista_pal=[]
    for i in range(len(results)):
        s = str(results[i])
        print(s)
        start = s.find('/">') + len('/">')
        end = s.find('</a>')
        substring = s[start:end]
        print(substring)
        lista_pal.append(substring)
    print(lista_pal)
    dic_pal_sin[pal[0]]=lista_pal
out_file = open("sinonimos.json", "w", encoding='utf8')
json.dump(dic_pal_sin, out_file, indent = 6, ensure_ascii=False)
out_file.close()
