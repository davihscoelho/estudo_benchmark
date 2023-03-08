import sys
sys.path.append('../')

import warnings
warnings.simplefilter("ignore")

from src.data.get_data import get_daily_returns_indice_imab,get_daily_returns_indice_imab5,get_daily_returns_cdi,get_daily_returns_indice_ihfa,get_daily_returns_indices,get_daily_returns_portfolios
from src.data.get_data2 import get_anual_returns_cdi,get_anual_returns_indices_ihfa,get_anual_returns_indices_imab,get_anual_returns_indices_imab5,get_anual_returns_portfolios
from src.features.build_features import merge_vol_12M_benchmarks,merge_vol_3M_benchmarks,merge_vol_12M_portfolios,merge_vol_3M_portfolios,merge_returns_anual_portfolios,merge_returns_anual_benchmarks

def carga_retornos_diario():
  
  get_daily_returns_indice_imab()
  get_daily_returns_indice_ihfa()
  get_daily_returns_indice_imab5()
  get_daily_returns_cdi()
  get_daily_returns_indices()
  get_daily_returns_portfolios()

def carga_retornos_anual():
  
  get_anual_returns_cdi()
  get_anual_returns_indices_imab()  
  get_anual_returns_indices_imab5()
  get_anual_returns_indices_ihfa()
  get_anual_returns_portfolios()


def carga_transformacoes():
  
  merge_vol_12M_benchmarks()
  merge_vol_3M_benchmarks()
  merge_vol_12M_portfolios()
  merge_vol_3M_portfolios()
  merge_returns_anual_benchmarks()
  merge_returns_anual_portfolios()
  

