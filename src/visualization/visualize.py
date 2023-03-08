import matplotlib.pyplot as plt

def grafico_janelas_rolantes(df,coluna1,coluna2,ativo,frequencia):
    
    #Define Estilo Graph Sheet
    plt.style.use("ggplot")
    #Define o texto Base
    texto = f"Retorno {ativo} {frequencia}"
    #Cria o subplot
    fig,ax = plt.subplots()
    df.plot(kind="line",x=coluna1,y=coluna2,ax=ax)
    ax.set(title=texto,xlabel="Periodo",ylabel="Retorno (%)")
    #Adiciona uma reta da Media
    #ax.axhline(y=df[coluna2].mean(),color="black",linestyle="--")
    
    return fig
  
  
def grafico_janelas_rolantes_vol(df,coluna1,coluna2,ativo,frequencia):
    
    #Define Estilo Graph Sheet
    plt.style.use("ggplot")
    #Define o texto Base
    texto = f"Volatilidade {ativo} {frequencia}"
    #Cria o subplot
    fig,ax = plt.subplots()
    df.plot(kind="line",x=coluna1,y=coluna2,ax=ax)
    ax.set(title=texto,xlabel="Periodo",ylabel="Volatilidade (%)")
    #Adiciona uma reta da Media
    ax.axhline(y=df[coluna2].mean(),color="black",linestyle="--")
    
    return fig
  
  