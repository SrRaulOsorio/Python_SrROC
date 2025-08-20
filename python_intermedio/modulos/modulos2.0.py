#si el modulo esta en la misma carpeta
#import modulos_enrutamiento.saludar as m_saludar

#print(m_saludar.saludar("Raul"))


import sys
sys.path.append("C:\\xampp\\htdocs\\RaulOsorioSrROC\\Python_SrROC\\modulos_enrutamiento")

import saludar as modulo_saludo

#print(sys.builtin_module_names)
#print(sys.path)

print(modulo_saludo.saludar("Raul"))