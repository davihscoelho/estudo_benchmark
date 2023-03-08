
from pipeline.carga_inicial import carga_retornos_diario,carga_retornos_anual,carga_transformacoes

def main():
  
  carga_retornos_diario()
  carga_retornos_anual()
  carga_transformacoes()
  
if __name__ == "__main__":
  
  main()
  