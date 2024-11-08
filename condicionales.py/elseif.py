ingreso_mensual = 60000     
gasto_mensual = 4000

if ingreso_mensual >= 50000:
    if ingreso_mensual - gasto_mensual < 0:
       print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 15000:
        print("estas bien")
    else:
        print("tas gastando mucho pibe")

elif ingreso_mensual > 5000:
    print("podes salir una vez al mes")
    
else:
   print("sos un seco de mierda")