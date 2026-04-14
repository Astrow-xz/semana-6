#codigo calcula fecha de nacimiento 
edad = int(input("¿Cuál es tu edad? "))
año_actual = 2025
año_nacimiento = año_actual - edad
print("Naciste en el año " + str(año_nacimiento) + ".")

#segun año de nacimiento ya calculado calcular descuentos
if año_nacimiento <= 2000:
    print("Tienes un descuento del 20% en tu compra.")
elif año_nacimiento > 2000 and año_nacimiento <= 2010:
    print("Tienes un descuento del 10% en tu compra.")
else:
    print("No tienes descuento en tu compra.")
    