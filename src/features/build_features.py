import sys
sys.path.append('../../')
import numpy as np
import pandas as pd
from functools import reduce

def rolling_vol_12M(df):
  df_vol = df.copy()
  
  df_vol["Volatilidade"] = (df_vol["Variação_Diária_(%)"].rolling(window=252).std())*np.sqrt(252)  
  df_vol.drop(columns="Variação_Diária_(%)",inplace=True)
  
  return df_vol
  
def rolling_vol_3M(df):
  df_vol = df.copy()
  
  df_vol["Volatilidade"] = (df_vol["Variação_Diária_(%)"].rolling(window=66).std())*np.sqrt(252)  
  df_vol.drop(columns="Variação_Diária_(%)",inplace=True)
  
  return df_vol

def merge_vol_12M_benchmarks():
  
    #Get the Data
    df1 = pd.read_csv("data/processed/01_daily_returns_imab.csv")
    df2 = pd.read_csv("data/processed/02_daily_returns_ihfa.csv")
    df3 = pd.read_csv("data/processed/03_daily_returns_imab5.csv")
    df4 = pd.read_csv("data/processed/08_daily_returns_cdi.csv")
    lista_dfs = [df1,df2,df3,df4]
    lista_dfs_vols = []
    
    #Calculate Vol on rolling window anual
    for df in lista_dfs:
      lista_dfs_vols.append(rolling_vol_12M(df))
    
    colunas = ["data","IMAB","IHFA","IMAB5","CDI"]
    
    final_df = reduce(lambda left,right: pd.merge(left,right,on="data",how='inner'),lista_dfs_vols).round(4).dropna()
    final_df.columns = colunas
    final_df = final_df.add_prefix("Volatilidade_")
    
    load_path = r"data/final/"
    nome_arquivo = "01_vol_benchmarks_rw_12M.csv"
    final_df.to_csv(load_path+nome_arquivo,index=False)
    
def merge_vol_3M_benchmarks():
  
    #Get the Data
    df1 = pd.read_csv("data/processed/01_daily_returns_imab.csv")
    df2 = pd.read_csv("data/processed/02_daily_returns_ihfa.csv")
    df3 = pd.read_csv("data/processed/03_daily_returns_imab5.csv")
    df4 = pd.read_csv("data/processed/08_daily_returns_cdi.csv")
    lista_dfs = [df1,df2,df3,df4]
    lista_dfs_vols = []
    
    #Calculate Vol on rolling window anual
    for df in lista_dfs:
      lista_dfs_vols.append(rolling_vol_3M(df))
      
    colunas = ["data","IMAB","IHFA","IMAB5","CDI"]
    
    final_df = reduce(lambda left,right: pd.merge(left,right,on="data",how='inner'),lista_dfs_vols).round(4).dropna()
    final_df.columns = colunas
    final_df = final_df.add_prefix("Volatilidade_")

    load_path = r"data/final/"
    nome_arquivo = "01_vol_benchmarks_rw_3M.csv"
    final_df.to_csv(load_path+nome_arquivo,index=False) 

def merge_vol_12M_portfolios():

    #Get the Data
    df1 = pd.read_csv("data/processed/05_daily_returns_port1.csv")
    df2 = pd.read_csv("data/processed/06_daily_returns_port4.csv")
    df3 = pd.read_csv("data/processed/07_daily_returns_port8.csv")
    
    lista_dfs = [df1,df2,df3]
    lista_dfs_vols = []
    
    #Calculate Vol on rolling window anual
    for df in lista_dfs:
      lista_dfs_vols.append(rolling_vol_12M(df))    
    
    colunas = ["data","port1","port4","port8"]
    final_df = reduce(lambda left,right: pd.merge(left,right,on="data",how='inner'),lista_dfs_vols).round(4).dropna()
    final_df.columns = colunas
    final_df = final_df.add_prefix("Volatilidade_")
    
    load_path = r"data/final/"
    nome_arquivo = "02_vol_portfolios_rw_12M.csv"
    final_df.to_csv(load_path+nome_arquivo,index=False) 

def merge_vol_3M_portfolios():

    #Get the Data
    df1 = pd.read_csv("data/processed/05_daily_returns_port1.csv")
    df2 = pd.read_csv("data/processed/06_daily_returns_port4.csv")
    df3 = pd.read_csv("data/processed/07_daily_returns_port8.csv")
    
    lista_dfs = [df1,df2,df3]
    lista_dfs_vols = []
    
    #Calculate Vol on rolling window anual
    for df in lista_dfs:
      lista_dfs_vols.append(rolling_vol_3M(df))    
    
    colunas = ["data","port1","port4","port8"]
    final_df = reduce(lambda left,right: pd.merge(left,right,on="data",how='inner'),lista_dfs_vols).round(4).dropna()
    final_df.columns = colunas
    final_df = final_df.add_prefix("Volatilidade_")
    
    load_path = r"data/final/"
    nome_arquivo = "02_vol_portfolios_rw_3M.csv"
    final_df.to_csv(load_path+nome_arquivo,index=False) 
    
def merge_returns_anual_benchmarks():
  #Get the Data
  df1 = pd.read_csv("data/processed/10_anual_returns_imab.csv")
  df2 = pd.read_csv("data/processed/11_anual_returns_ihfa.csv")
  df3 = pd.read_csv("data/processed/12_anual_returns_imab5.csv")
  df4 = pd.read_csv("data/processed/14_anual_returns_cdi.csv")
  lista_dfs = [df1,df2,df3,df4]
  
  
  #Merge All tada
  final_df = reduce(lambda left,right: pd.merge(left,right,on="data",how='inner'),lista_dfs).round(4).dropna()
  colunas = ["data","IMAB","IHFA","IMAB5","CDI"]
  final_df.columns = colunas
  final_df = final_df.add_prefix("Variação_12_Meses_(%)_")
  
  load_path = r"data/final/"
  nome_arquivo = "03_returns_benchmarks_rw_12M.csv"
  final_df.to_csv(load_path+nome_arquivo,index=False)
  #print(final_df.head())
  
def merge_returns_anual_portfolios():
  #Get the data
  df1 = pd.read_csv("data/processed/13_anual_returns_port1.csv")
  df2 = pd.read_csv("data/processed/13_anual_returns_port4.csv")
  df3 = pd.read_csv("data/processed/13_anual_returns_port8.csv")
  
  lista_dfs = [df1,df2,df3]
  
  #Merge All tada
  final_df = reduce(lambda left,right: pd.merge(left,right,on="data",how='inner'),lista_dfs).round(4).dropna()
  
  colunas = ["port1","data","port4","port8"]
  final_df.columns = colunas
  final_df = final_df[["data","port1","port4","port8"]]
  final_df = final_df.add_prefix("Variação_12_Meses_(%)_")
  
  load_path = r"data/final/"
  nome_arquivo = "03_returns_portfolios_rw_12M.csv"
  final_df.to_csv(load_path+nome_arquivo,index=False)
  
def sharpe_analysis(df_merge,df_cdi): #Recebe df_imab com Vol
  
  #Define new columns to merge_data_new_df
  df_merge.columns = ["data",'Variação 12 Meses (%)','Vol 12 Meses','Vol 3 Meses']
  
  #merge data
  merge_imab_di = df_merge.merge(df_cdi,on="data",how='inner',suffixes=["_IMAB","_CDI"])

  #Drop specific column
  merge_imab_di.drop(columns='valor',inplace=True)
  sharpe_ratio = (merge_imab_di["Variação 12 Meses (%)_IMAB"]-merge_imab_di["Variação 12 Meses (%)_CDI"])/merge_imab_di["Vol 12 Meses"]

  df_sr = pd.DataFrame({"Sharpe Ratio":sharpe_ratio
                      ,"data":merge_imab_di["data"]}).round(2)
  return df_sr
  
################### EXECUTION #######################
# merge_vol_12M_benchmarks()
# merge_vol_3M_benchmarks()
# merge_vol_12M_portfolios()
# merge_vol_3M_portfolios()
# merge_returns_anual_benchmarks()
# merge_returns_anual_portfolios()