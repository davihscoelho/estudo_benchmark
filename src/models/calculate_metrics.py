import numpy as np

def calculate_total_return(daily_returns):
  
  cum_ret = daily_returns.cumsum().apply(np.exp)-1
  
  return cum_ret

#def calcul

def calculate_drawdown(daily_returns):
  
  index = 1000*daily_returns.cumsum().apply(np.exp)
  picos = index.cummax()
  drawdown = ((index-picos)/picos)
  
  return picos,drawdown
  

# def calculateMaxDD(cumret)