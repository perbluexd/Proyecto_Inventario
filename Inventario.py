inventario = {}

def mostrarInventario(inventario):
    for key, values in inventario.items():
        print(f"Categoria: {key}")
        for elemento in values:
            print(f"Nombre: {elemento['nombre']}, Precio: {elemento['precio']}, Cantidad: {elemento['cantidad']}, Disponibilidad: {elemento['disponible']}")

def agregarProducto(inventario):
    while True:
        categoria = input("Ingresa la categoría donde deseas agregar el producto: ").lower()
        
        if categoria not in inventario:
            inventario[categoria] = []
        
        nombre = input("Ingresa el nombre del producto: ").lower()
        
        try:
            precio = float(input("Ingresa el precio del producto: "))
        except ValueError:
            print("El precio ingresado es incorrecto. Por favor vuelve a intentarlo.")
            continue
        
        try:
            cantidad = int(input("Ingresa la cantidad que agregarás: "))
        except ValueError:
            print("La cantidad ingresada es incorrecta. Por favor vuelve a intentarlo.")
            continue
        
        disponible = input("Ingresa 'true' o 'false' de acuerdo a la disponibilidad del producto: ").lower()
        if disponible not in {"true", "false"}:
            print("Disponibilidad no válida. Por favor ingresa 'true' o 'false'.")
            continue
        estado = disponible == "true"
        
        inventario[categoria].append({"nombre": nombre, "precio": precio, "cantidad": cantidad, "disponible": estado})
        
        opcion = input("Si deseas agregar otro producto presiona 's', de lo contrario presiona 'n': ").lower()
        if opcion != "s":
            print("Hasta pronto.")
            break

def eliminarProducto(inventario):
    categoria = input("De qué categoría es el producto que deseas eliminar: ").lower()
    if categoria in inventario:
        while True:
            nombre = input("Ingresa el nombre del producto que deseas eliminar: ").lower()
            for elemento in inventario[categoria]:
                if elemento["nombre"] == nombre:
                    inventario[categoria].remove(elemento)
                    print(f"El producto '{nombre}' ha sido eliminado.")
                    break
            else:
                print("El producto que deseas eliminar no se encuentra.")
            
            opcion = input("Si deseas eliminar otro producto presiona 's', de lo contrario presiona 'n': ").lower()
            if opcion != "s":
                print("Hasta pronto.")
                break
    else:
        print("La categoría no se encuentra.")

def editarProducto(inventario):
    categoria = input("Ingresa la categoría que quieres modificar: ").lower()
    if categoria in inventario:
        productos = inventario[categoria]
        if not productos:
            print("No hay productos en esta categoría.")
            return
        
        print("Productos disponibles: ")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}, Disponibilidad: {producto['disponible']}")
        
        try:
            seleccion = int(input("Selecciona el número del producto que deseas editar: "))
            if seleccion < 1 or seleccion > len(productos):
                print("Selección no válida.")
                return
        except ValueError:
            print("Ingresa un valor válido por favor.")
            return
        
        producto = productos[seleccion - 1]
        print("¿Qué deseas editar?")
        print("1. Nombre")
        print("2. Precio")
        print("3. Cantidad")
        print("4. Disponibilidad")
        opcion = input("Selecciona una opción (1/2/3/4): ").strip()
        
        if opcion == "1":
            nuevo_nombre = input("Escribe el nuevo nombre del producto: ").lower()
            producto["nombre"] = nuevo_nombre
        elif opcion == "2":
            try:
                nuevo_precio = float(input("Ingresa el nuevo precio del producto: "))
                producto["precio"] = nuevo_precio
            except ValueError:
                print("El precio ingresado no es válido.")
        elif opcion == "3":
            try:
                nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
                producto["cantidad"] = nueva_cantidad
            except ValueError:
                print("La cantidad ingresada no es válida.")
        elif opcion == "4":
            nueva_disponibilidad = input("Ingresa 'true' para disponible o 'false' para no disponible: ").lower()
            if nueva_disponibilidad in {"true", "false"}:
                producto["disponible"] = nueva_disponibilidad == "true"
            else:
                print("Estado no válido. No se realizarán cambios.")
        else:
            print("No marcaste ninguna opción válida. Vuelve a intentarlo.")
    else:
        print("La categoría no existe.")

def buscarProducto(inventario):
    while True:
        nombre = input("Ingresa el producto que deseas buscar (o escribe 'salir' para terminar): ").lower()
        if nombre == "salir":
            print("Búsqueda finalizada.")
            break

        for categoria, productos in inventario.items():
            for producto in productos:
                if producto["nombre"] == nombre:
                    print(f"Categoría: {categoria}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}, Disponibilidad: {producto['disponible']}")
                    break
            else:
                continue
            break
        else:
            print("El producto no se encontró.")

def actualizarStock(inventario):
    categoria = input("Ingresa la categoría donde deseas actualizar el stock: ").lower()
    if categoria in inventario:
        productos = inventario[categoria]
        if not productos:
            print("No hay productos en esta categoría.")
            return
        
        print("Productos disponibles: ")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}, Disponibilidad: {producto['disponible']}")
        
        try:
            seleccion = int(input("Selecciona el número del producto cuyo stock deseas actualizar: "))
            if seleccion < 1 or seleccion > len(productos):
                print("Selección no válida.")
                return
        except ValueError:
            print("Ingresa un valor válido por favor.")
            return
        
        producto = productos[seleccion - 1]
        try:
            nueva_cantidad = int(input("Ingresa la nueva cantidad para el producto: "))
            producto["cantidad"] = nueva_cantidad
            print(f"El stock del producto '{producto['nombre']}' ha sido actualizado a {nueva_cantidad}.")
        except ValueError:
            print("La cantidad ingresada no es válida.")
    else:
        print("La categoría no existe.")

def menu():
    while True:
        opcion = input(
            "Menú de Inventario:\n"
            "1. Mostrar Inventario\n"
            "2. Agregar Producto\n"
            "3. Eliminar Producto\n"
            "4. Editar Producto\n"
            "5. Buscar Producto\n"
            "6. Actualizar Stock\n"
            "7. Salir\n"
            "Selecciona una opción: "
        ).strip()
        if opcion == "1":
            mostrarInventario(inventario)
        elif opcion == "2":
            agregarProducto(inventario)
        elif opcion == "3":
            eliminarProducto(inventario)
        elif opcion == "4":
            editarProducto(inventario)
        elif opcion == "5":
            buscarProducto(inventario)
        elif opcion == "6":
            actualizarStock(inventario)
        elif opcion == "7":
            print("Gracias por usar el Inventario. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
