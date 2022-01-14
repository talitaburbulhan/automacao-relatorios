#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import gspread
import json
import os
import pandas as pd

def escreve_planilha(dataframe, worksheet):
    worksheet.append_row(["Reporte de alcance por  publicaciones y red  JSB"])
    worksheet.append_row(["Facebok; Twitter; Instagram; YouTube por Buffer y analítica"])
    worksheet.append_row(["Fecha", "Impressiones", "Alcance", "Likes, Comentarios, Shares e Clics", "Etiqueta", "Enlace"])

    time.sleep(5)
    worksheet.append_row(["Campaña Defensa de Defensores y Defensoras"])
    dados = dataframe[(dataframe["item da planilha"] == "campaña_defesa")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Campaña La Vida Antes que la Deuda"])
    dados = dataframe[(dataframe["item da planilha"] == "vida_antes_deuda")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Acción Protagonismo"])
    dados = dataframe[(dataframe["item da planilha"] == "protagonismo")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])
    
    time.sleep(5)
    worksheet.append_row(["Campaña Justicia Socio ecológica"])
    dados = dataframe[(dataframe["item da planilha"] == "justicia_socioecologica")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Megaproyectos,Militarización, TLC"])
    dados = dataframe[(dataframe["item da planilha"] == "megaproyectos")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Militarización; Ocupación; Cuba Salva No al Bloqueo; Palestina Libre"])
    dados = dataframe[(dataframe["item da planilha"] == "militarizacion")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Notas/Comunicados"])
    dados = dataframe[(dataframe["item da planilha"] == "notas_comunicados")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Estudios,  Boletines, Investigaciones"])
    dados = dataframe[(dataframe["item da planilha"] == "estudios")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Eventos Públicos, Foros, Seminarios - por favor en referencia ubicar a que sub actividad pertenece cada evento"])
    dados = dataframe[(dataframe["item da planilha"] == "eventos")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Publicaciones de Aliades; Efemérides Relevantes y Trabajos con Red de Comunicadores"])
    dados = dataframe[(dataframe["item da planilha"] == "publicaciones_aliade")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Ayudas a Terceros/ Fortalecimiento territorial"])
    dados = dataframe[(dataframe["item da planilha"] == "ayudas_terceros")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["Inserciones mensuales de la Red JSB en medios de comunicación  de nivel nacional o regional"])
    dados = dataframe[(dataframe["item da planilha"] == "inserciones")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    worksheet.append_row(['*'])
    worksheet.append_row(['*'])

    time.sleep(5)
    worksheet.append_row(["CHECAR"])
    dados = dataframe[(dataframe["item da planilha"] == "CHECAR")]
    linhas = []
    for linha in dados.itertuples():
        linhas.append(linha[2:8])
    worksheet.append_rows(linhas)
    soma1 = int(dados['impressions'].sum()) 
    soma2 = int(dados['reach'].sum())
    soma3 = int(dados['engagement'].sum())
    soma4 = f'{len(dados)} postagens'
    worksheet.append_row(["Subtotal", soma1, soma2, soma3, soma4])
    
    print("Atualização concluída")

