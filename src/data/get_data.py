import sys
sys.path.append('/')
import pandas as pd
import numpy as np

from src.data.get_bacen import consulta_bc
#from get_bacen import consulta_bc
# #Path Name File
# path = r"wealth_study\data\raw\ANBIMA"
# filenames = glob.glob(path + "\*.xls")
# #print(filenames)

#### Getting the data from anbima source
def get_data(path):
  
  df = pd.read_excel(path)
  
  return df

def get_daily_returns_cdi():
  
  #get the cdi dataframe
  df_cdi = consulta_bc(12)
  
  # #Define new Feature Column df_cdi
  df_cdi["data"] = df_cdi.index

  #Drop index df_cdi 
  df_cdi.reset_index(drop=True,inplace=True)

  df_cdi = df_cdi.loc[df_cdi["data"]>="2000-01-01"]
  
  load_path = r"data/processed/"
  nome_arquivo = "08_daily_returns_cdi.csv"
  df_cdi.columns = ["Variação_Diária_(%)","data"]
  df_cdi["Variação_Diária_(%)"] = df_cdi["Variação_Diária_(%)"]/100
  df_cdi.to_csv(load_path+nome_arquivo,index=False)
  
def get_daily_returns_indice_imab():
  
  path = "data/raw/ANBIMA/IMAB-HISTORICO.xls"
  load_path = r"data/processed/"
  nome_arquivo = "01_daily_returns_imab.csv"
  df = get_data(path)
  
  df = df.iloc[:,[1,2]]
  df.iloc[:,1]= np.log(df.iloc[:,1]/df.iloc[:,1].shift(1))
  df.columns = ["data","Variação_Diária_(%)"]
  df.to_csv(load_path+nome_arquivo,index=False)
  #print(df.head())
def get_daily_returns_indice_imag():
  
  path = "data/raw/ANBIMA/IMAGERAL-HISTORICO.xls"
  load_path = r"data/processed/"
  nome_arquivo = "01_daily_returns_imag.csv"
  df = get_data(path)
  
  df = df.iloc[:,[1,2]]
  df.iloc[:,1]= np.log(df.iloc[:,1]/df.iloc[:,1].shift(1))
  df.columns = ["data","Variação_Diária_(%)"]
  df.to_csv(load_path+nome_arquivo,index=False)

def get_daily_returns_indice_ihfa():
  
  path = "data/raw/ANBIMA/IHFA-HISTORICO.xls"
  load_path = r"data/processed/"
  nome_arquivo = "02_daily_returns_ihfa.csv"
  df = get_data(path)
  
  df = df.iloc[:,[1,2]]
  df.iloc[:,1]= np.log(df.iloc[:,1]/df.iloc[:,1].shift(1))
  df.columns = ["data","Variação_Diária_(%)"]
  df.to_csv(load_path+nome_arquivo,index=False)
  #print(df.head())
def get_daily_returns_indice_imab5():
  
  path = "data/raw/ANBIMA/IMAB5-HISTORICO.xls"
  load_path = r"data/processed/"
  nome_arquivo = "03_daily_returns_imab5.csv"
  df = get_data(path)
  
  df = df.iloc[:,[1,2]]
  df.iloc[:,1]= np.log(df.iloc[:,1]/df.iloc[:,1].shift(1))
  df.columns = ["data","Variação_Diária_(%)"]
  df.to_csv(load_path+nome_arquivo,index=False)

def get_daily_returns_indices():
  
  #Get Data
  path = "data/raw/economatica.xlsx"
  load_path = r"data/processed/"
  nome_arquivo = "04_daily_returns_indices.csv"
  df = get_data(path)
  
  #Exclude IPCA column
  df = df.iloc[:,0:8].replace("-",np.nan).dropna()
  date = df["Data"]
  
  #Calculate the daily returns
  df = np.log(df.iloc[:,1:]/df.iloc[:,1:].shift(1))
  df["data"] = date
  
  #Load dataset
  df.to_csv(load_path+nome_arquivo,index=False)

def get_daily_returns_portfolios():
  
  path = r"data/processed/04_daily_returns_indices.csv"
  load_path = r"data/processed/"
  df_returns = pd.read_csv(path)
  date = df_returns["data"]
  
  w1 = np.array([51,5,15,23,2.5,2.5,1]) #Porfolio Perfil 1
  w2 = np.array([17.5,10,15,10,10,30,5]) #Portfolio Perfil 4
  w3 = np.array([0,0,0,0,30,50,20]) #Porfolio Perfil 8
  w1 = w1/100
  w2 = w2/100
  w3 = w3/100
  #Create a df for portfolio 1 daily returns
  df_p1= pd.DataFrame({
          "Variação_Diária_(%)":np.sum(w1*df_returns.iloc[:,0:7],axis=1),
          "data":date
  }).round(4)
  
  #Create a df for portfolio 4 daily returns
  df_p2= pd.DataFrame({
          "Variação_Diária_(%)":np.sum(w2*df_returns.iloc[:,0:7],axis=1),
          "data":date
  }).round(4)
  
  #Create a df for portfolio 8 daily returns
  df_p3= pd.DataFrame({
          "Variação_Diária_(%)":np.sum(w3*df_returns.iloc[:,0:7],axis=1),
          "data":date
  }).round(4)
  
  #Load dataset
  df_p1.to_csv(load_path+"05_daily_returns_port1.csv",index=False)
  df_p2.to_csv(load_path+"06_daily_returns_port4.csv",index=False)
  df_p3.to_csv(load_path+"07_daily_returns_port8.csv",index=False)
  #print(df_p1.head())

############################## EXECUTION ###############################
# get_daily_returns_indice_imab()
# get_daily_returns_indice_ihfa()
# get_daily_returns_indice_imab5()
# get_daily_returns_indices()
# get_daily_returns_portfolios()
# get_daily_returns_cdi()
