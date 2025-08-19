ingreso_mensual = 100000
gasto_mensual = 80000

# if anidados y else if (elif)
if ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("bien, estas bien")
    else:
        print("estas gastando mucho, hay que ver si te alcanza")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("estas bien en argentina")
elif ingreso_mensual > 200:
    print("estas bien en venezuela")
else:
    print("No tenes dinero ")


print(ingreso_mensual)