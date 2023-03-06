# -*- coding: utf-8 -*-
import pandas as pd
import os
import glob

# #Path Name File
# path = r"wealth_study\data\raw\ANBIMA"
# filenames = glob.glob(path + "\*.xls")
# #print(filenames)

#### Getting the data from anbima source
def get_data(path):
  
  df = pd.read_excel(path)
  
  return df


  
