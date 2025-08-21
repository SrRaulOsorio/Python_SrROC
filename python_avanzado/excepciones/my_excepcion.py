#creando nuestra propia excepcion personaloizada
class MiException(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
        
      
      
#lanzando mi propia excepcion
#raise MiException("jajajajajaja persona poco culta")  

#manejandola
try:
    raise MiException("jajajaja, persona poco culta")
except:
    print("Como vas a cometer ese ERROR")