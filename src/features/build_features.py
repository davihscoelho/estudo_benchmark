
def get_returns(df): 
  
  dataset_returns = df.loc[:,["Data de Referência","Variação Diária (%)"]]
  
  return dataset_returns

def get_duration(df):
  
  dataset_duration = df.loc[:,["Data de Referência","Duration (d.u.)"]]
  
  return dataset_duration

def  get_janelas_rolantes(df):

  dataset_janelas_rolantes_1 = df.loc[:,["Data de Referência","Variação 12 Meses (%)"]]
  dataset_janelas_rolantes_2 = df.loc[:,["Data de Referência","Variação 24 Meses (%)"]]
  
  return dataset_janelas_rolantes_1,dataset_janelas_rolantes_2
  
def media_retorno(df):
  
  media = round(df.describe(),2)
  
  return media