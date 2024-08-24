# Ejercicios
# Proceder a la creacion de una tienda
# Crear un sistema de inventario

my_stock = {
}
def add_pro():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    my_stock[nombre] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    print(f"Producto '{nombre}' agregado al inventario.")
    
def delete_pro():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in my_stock:
        del my_stock[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")

# Función para realizar una compra
def realizar_compra():
    total = 0
    productos_comprados = []
    while True:
        nombre = input("Ingrese el nombre del producto a comprar (o 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break
        if nombre in my_stock:
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            if cantidad <= my_stock[nombre]["cantidad"]:
                total += my_stock[nombre]["precio"] * cantidad
                productos_comprados.append((nombre, cantidad))
                my_stock[nombre]["cantidad"] -= cantidad
            else:
                print(f"No hay suficiente cantidad de '{nombre}' en el inventario.")
        else:
            print(f"Producto '{nombre}' no encontrado en el inventario.")
    print("\nResumen de la compra:")
    for producto, cantidad in productos_comprados:
        print(f"{producto}: {cantidad} x {my_stock[producto]['precio']} = {my_stock[producto]['precio'] * cantidad}")
    print(f"Total: {total}")
    cash = float(input("Ingrese el efectivo: "))
    if cash >= total:
        cambio = cash - total
        print(f"Cambio: {cambio}")
    else:
        print("No hay suficiente efectivo.")
        
# Menú principal
while True:
    print("\nMenú:")
    print("1. Agregar producto al inventario")
    print("2. Eliminar producto del inventario")
    print("3. Realizar una compra")
    print("4. Salir")
    op = input("Ingrese una opción: ")
    if op == "1":
        add_pro()
    elif op == "2":
        delete_pro()
    elif op == "3":
        realizar_compra()
    elif op == "4":
        break
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")