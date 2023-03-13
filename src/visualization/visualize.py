import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import sys
sys.path.append('../')

path_load = "../reports/figures/"

def gerar_grafico_retorno_portfolio(benchmark,final_df,path_load):
  
  fig,([ax0,ax1,ax2]) = plt.subplots(nrows=1,ncols=3,figsize=(20,5))
  
  final_df.plot(kind="line",
                x="Variação_12_Meses_(%)_data",
                y=[f'Variação_12_Meses_(%)_{benchmark}','Variação_12_Meses_(%)_port1'],
                xlabel="Periodo",
                ylabel="Retorno (%)",
                title=f'Analise Retorno Anual {benchmark} e Port1',
                ax=ax0)

  final_df.plot(kind="line",
                x="Variação_12_Meses_(%)_data",
                y=[f'Variação_12_Meses_(%)_{benchmark}','Variação_12_Meses_(%)_port4'],
                xlabel="Periodo",
                ylabel="Retorno (%)",
                title=f'Analise Retorno Anual {benchmark} e Port4',
                ax=ax1)

  final_df.plot(kind="line",
                x="Variação_12_Meses_(%)_data",
                y=[f'Variação_12_Meses_(%)_{benchmark}','Variação_12_Meses_(%)_port8'],
                xlabel="Periodo",
                ylabel="Retorno (%)",
                title=f'Analise Retorno Anual {benchmark} e Port8',
                ax=ax2)
  ax0.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  plt.tight_layout();
  fig.savefig(path_load+f'Retorno_Port_{benchmark}.png')
  


  

def gerar_grafico_vol_portfolio(benchmark,final_df,path_load):
  
  fig,([ax0,ax1,ax2]) = plt.subplots(nrows=1,ncols=3,figsize=(20,5))
  final_df.plot(kind="line",
                x="Volatilidade_data",
                y=[f'Volatilidade_{benchmark}','Volatilidade_port1'],
                xlabel="Periodo",
                ylabel="Volatilidade (%)",
                title=f'Analise Volatilidade Anualizada {benchmark} e Port1',
                ax=ax0)

  final_df.plot(kind="line",
                x="Volatilidade_data",
                y=[f'Volatilidade_{benchmark}','Volatilidade_port4'],
                xlabel="Periodo",
                ylabel="Volatilidade (%)",
                title=f'Analise Volatilidade Anualizada {benchmark} e Port4',
                ax=ax1)

  final_df.plot(kind="line",
                x="Volatilidade_data",
                y=[f'Volatilidade_{benchmark}','Volatilidade_port8'],
                xlabel="Periodo",
                ylabel="Volatilidade (%)",
                title=f'Analise Volatilidade Anualizada {benchmark} e Port8',
                ax=ax2)
  
  ax0.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  plt.tight_layout();
  fig.savefig(path_load+f'Volatilidade_Port_{benchmark}.png')
  
def gerar_grafico_retorno_portfolio_cdi(benchmark,final_df,path_load):
  
  fig,([ax0,ax1,ax2]) = plt.subplots(nrows=1,ncols=3,figsize=(20,5))
  
  final_df.plot(kind="line",
                x="Variação_12_Meses_(%)_data",
                y=[f'Variação_12_Meses_(%)_{benchmark}','Variação_12_Meses_(%)_port1'],
                xlabel="Periodo",
                ylabel="Retorno (%) do CDI",
                title=f'Analise Retorno Anual {benchmark} e Port1',
                ax=ax0)

  final_df.plot(kind="line",
                x="Variação_12_Meses_(%)_data",
                y=[f'Variação_12_Meses_(%)_{benchmark}','Variação_12_Meses_(%)_port4'],
                xlabel="Periodo",
                ylabel="Retorno (%) do CDI",
                title=f'Analise Retorno Anual {benchmark} e Port4',
                ax=ax1)

  final_df.plot(kind="line",
                x="Variação_12_Meses_(%)_data",
                y=[f'Variação_12_Meses_(%)_{benchmark}','Variação_12_Meses_(%)_port8'],
                xlabel="Periodo",
                ylabel="Retorno (%) do CDI",
                title=f'Analise Retorno Anual {benchmark} e Port8',
                ax=ax2)
  ax0.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  plt.tight_layout();
  fig.savefig(path_load+f'Retorno_Port_{benchmark}_CDI.png')

def gerar_grafico_sharpe_portfolio(benchmark,final_df,path_load):
  
  fig,([ax0,ax1,ax2]) = plt.subplots(nrows=1,ncols=3,figsize=(20,5))
  
  final_df.plot(kind="line",
                x="data",
                y=[f'sharpe_{benchmark}','sharpe_port1'],
                xlabel="Periodo",
                ylabel="Sharpe",
                title=f'Analise Sharpe Anual {benchmark} e Port1',
                ax=ax0)

  final_df.plot(kind="line",
                x="data",
                y=[f'sharpe_{benchmark}','sharpe_port4'],
                xlabel="Periodo",
                ylabel="Sharpe",
                title=f'Analise Sharpe Anual {benchmark} e Port4',
                ax=ax1)

  final_df.plot(kind="line",
                x="data",
                y=[f'sharpe_{benchmark}','sharpe_port8'],
                xlabel="Periodo",
                ylabel="Sharpe",
                title=f'Analise Sharpe Anual {benchmark} e Port8',
                ax=ax2)
  plt.tight_layout();
  fig.savefig(path_load+f'Sharpe_Port_{benchmark}.png')
  
  
def gerar_grafico_retorno_total_portfolios(dataframes,benchmarks,path_load,nome):
  
  fig,axes =plt.subplots(2,4,sharex=True,figsize=(30,10))
  plt.style.use('ggplot')
  # benchmark1 = "IBOV"
  # benchmark2 = "Port1"
  # benchmark3 = "Port4"
  # benchmark4 = "Port8"

  ax1=dataframes[0].plot(
                kind="line",
                x="data",
                y="acumulado",
                xlabel="Periodo",
                ylabel="Retorno Acumulado (%)",
                ax=axes[0][0],
                label=f"{benchmarks[0]}",
                legend=True
    );

  ax2=dataframes[0].plot(
                kind="line",
                x="data",
                y="drawdown",
                xlabel="Periodo",
                ylabel="Drawdown",
                ax=axes[1][0],
                legend=False
                
  )

  ax3=dataframes[1].plot(
                kind="line",
                x="data",
                y="acumulado",
                xlabel="Periodo",
                ylabel="Retorno Acumulado (%)",
                ax=axes[0][1],
                label=f"{benchmarks[1]}",
                legend=True
    );

  ax4=dataframes[1].plot(
                kind="line",
                x="data",
                y="drawdown",
                xlabel="Periodo",
                ylabel="Drawdown",
                ax=axes[1][1],
                legend=False
                
  )

  ax5=dataframes[2].plot(
                kind="line",
                x="data",
                y="acumulado",
                xlabel="Periodo",
                ylabel="Retorno Acumulado (%)",
                ax=axes[0][2],
                label=f"{benchmarks[2]}",
                legend=True
    );

  ax6=dataframes[2].plot(
                kind="line",
                x="data",
                y="drawdown",
                xlabel="Periodo",
                ylabel="Drawdown",
                ax=axes[1][2],
                legend=False
                
  )

  ax7=dataframes[3].plot(
                kind="line",
                x="data",
                y="acumulado",
                xlabel="Periodo",
                ylabel="Retorno Acumulado (%)",
                ax=axes[0][3],
                label=f"{benchmarks[3]}",
                legend=True
    );

  ax8=dataframes[3].plot(
                kind="line",
                x="data",
                y="drawdown",
                xlabel="Periodo",
                ylabel="Drawdown",
                ax=axes[1][3],
                legend=False
                
  )


  ax1.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax2.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax3.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax4.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax5.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax6.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax7.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  ax8.yaxis.set_major_formatter(StrMethodFormatter('{x:.0%}'))
  plt.tight_layout();
  fig.savefig(path_load+nome)
  
  
  