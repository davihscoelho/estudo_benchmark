import sys
sys.path.append('/')
import pandas as pd
import numpy as np

from src.data.get_data import get_data

def get_anual_returns_indices_imab():
  
  path = "data/raw/ANBIMA/IMAB-HISTORICO.xls"
  load_path = r"data/processed/"
  nome_arquivo = "10_anual_returns_imab.csv"
  df = get_data(path)
  
  df = df.loc[:,["Data de Referência","Variação 12 Meses (%)"]].round(4) 
  df.columns= ["data","Variação_12_Meses_(%)"]
  df.to_csv(load_path+nome_arquivo,index=False)
  
def get_anual_returns_indices_ihfa():
  
  path = "data/raw/ANBIMA/IMAB-HISTORICO.xls"
  load_path = r"data/processed/"
  nome_arquivo = "11_anual_returns_ihfa.csv"
  df = get_data(path)
  
  df = df.loc[:,["Data de Referência","Variação 12 Meses (%)"]].round(4)
  df.columns= ["data","Variação_12_Meses_(%)"]
  df.to_csv(load_path+nome_arquivo,index=False)

def get_anual_returns_indices_imab5():
  
  
  path = "data/raw/ANBIMA/IMAB5-HISTORICO.xls"
  load_path = r"data/processed/"
  nome_arquivo = "12_anual_returns_imab5.csv"
  df = get_data(path)
  
  df = df.loc[:,["Data de Referência","Variação 12 Meses (%)"]].round(4)
  df.columns= ["data","Variação_12_Meses_(%)"]
  df.to_csv(load_path+nome_arquivo,index=False)
  
def get_anual_returns_portfolios():
  #Get Data
  path1 = r"data/processed/05_daily_returns_port1.csv"
  path2 = r"data/processed/06_daily_returns_port4.csv"
  path3 = r"data/processed/07_daily_returns_port8.csv"
  
  load_path = r"data/processed/"
  
  df1 = pd.read_csv(path1)
  df2 = pd.read_csv(path2)
  df3 = pd.read_csv(path3)
  date = df1["data"]
  
  #Create dataframes
  df_p1 = pd.DataFrame({
                        "Variação_12_Meses_(%)":df1["Variação_Diária_(%)"].rolling(window=252).sum(),
                        "data":date
                        }).round(4)
  df_p2 = pd.DataFrame({
                      "Variação_12_Meses_(%)":df2["Variação_Diária_(%)"].rolling(window=252).sum(),
                      "data":date
                      }).round(4)
  df_p3 = pd.DataFrame({
                    "Variação_12_Meses_(%)":df3["Variação_Diária_(%)"].rolling(window=252).sum(),
                    "data":date
                    }).round(4)
  #Load Data
  df_p1.to_csv(load_path+"13_anual_returns_port1.csv",index=False)
  df_p2.to_csv(load_path+"13_anual_returns_port4.csv",index=False)
  df_p3.to_csv(load_path+"13_anual_returns_port8.csv",index=False)
  
def get_anual_returns_cdi():
  path = "data/processed/08_daily_returns_cdi.csv"
  load_path = r"data/processed/"
  nome_arquivo = "14_anual_returns_cdi.csv"
  
  df = pd.read_csv(path)
  df["Variação_12_Meses_(%)"] = df["Variação_Diária_(%)"].rolling(window=252).sum()
  df.drop(columns="Variação_Diária_(%)",inplace=True)
  df["Variação_12_Meses_(%)"] = df["Variação_12_Meses_(%)"].round(4)
  
  df.to_csv(load_path+nome_arquivo,index=False)
  #print(df.head())

##### EXECUTION #####
get_anual_returns_indices_imab()
get_anual_returns_indices_ihfa()
get_anual_returns_indices_imab5()
get_anual_returns_portfolios()
get_anual_returns_cdi()