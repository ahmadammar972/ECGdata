# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 12:27:47 2023

@author: 100840150
"""
import json
from kafka import KafkaConsumer
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

import pandas as pd 
disease=pd.read_csv('single_disease_leads.csv')
i=pd.read_csv('I.csv')
ii=pd.read_csv('II.csv')
iii=pd.read_csv('III.csv')
avf=pd.read_csv('AVF.csv')
avl=pd.read_csv('AVL.csv')
avr=pd.read_csv('AVR.csv')
v1=pd.read_csv('V1.csv')
v2=pd.read_csv('V2.csv')
v3=pd.read_csv('V3.csv')
v4=pd.read_csv('V4.csv')
v5=pd.read_csv('V5.csv')
v6=pd.read_csv('V6.csv')
mc=pd.read_csv('main_class.csv')

@app.route('/id/<itr>')
def ecg(itr=1):
    itr=int(itr)
    dis=disease.iloc[itr,0]
    if dis=='NORM':
        m='Normal'
    elif dis in mc.iloc[0,:]:
        m='Hypertrophy'
    elif dis in mc.iloc[1,:]:
        m="Myocardial Infarction"
    elif dis in mc.iloc[2,:]:
        m='ST-T wave abnormality'
    else:
        m='CardioDiverse Datasets'
    res={'I':list(i.iloc[itr,:]),'II':list(ii.iloc[itr,:]),'III':list(iii.iloc[itr,:]),'AVF':list(avf.iloc[itr,:]),\
         'AVR':list(avr.iloc[itr,:]),'AVL':list(avl.iloc[itr,:]),'V1':list(v1.iloc[itr,:]),'V2':list(v2.iloc[itr,:]),'V3':list(v3.iloc[itr,:])\
             ,'V4':list(v4.iloc[itr,:]),'V5':list(v5.iloc[itr,:]),'V6':list(v6.iloc[itr,:]),'dis':dis,'main':m}
        
    return json.dumps(res)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False) 

