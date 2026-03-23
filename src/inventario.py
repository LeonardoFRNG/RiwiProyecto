print("===== Inventario Riwi =====")

nombre = input("Ingrese el nombre del producto: ")

#esta es la entrada de datos, usamos while para verificar hasta que sea True el valor que ingresemos
while True:
    try: #con try intentamos hasta que ingresemos un valor true
        precio = float(input("Ingrese el precio del producto: "))
        break
    except: #aca lo que hacemos es que si ponemos un valor incorrcto el muestra este mensaje.
        print("El precio es invalido, Ingrese un valor correcto.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except:
        print("La cantidad es invalida, Ingrese un valor correcto.")

costo_total = precio * cantidad #operacion matematica

print(f"Nombre del producto: {nombre}")
print(f"Precio unitario: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Costo total calculado: {costo_total}")
        