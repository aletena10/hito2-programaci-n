# Diccionarios iniciales
# Almacenamos los datos de clientes, productos y pedidos en estructuras de tipo diccionario.
clientes = {}  # Diccionario para almacenar clientes: {id_cliente: datos_cliente}
productos = {  # Diccionario con productos cargados previamente
    "P001": {"nombre": "Producto 1", "precio": 10.0},
    "P002": {"nombre": "Producto 2", "precio": 20.0},
    "P003": {"nombre": "Producto 3", "precio": 15.0},
}
pedidos = {}  # Diccionario para almacenar pedidos: {número_pedido: datos_pedido}

# Funciones principales
def registrar_cliente():
    """Registra un nuevo cliente en el sistema."""
    print("Registro de cliente")
    id_cliente = input("Introduzca un ID único: ")  # Solicita un ID único para el cliente
    if id_cliente in clientes:  # Verifica si el ID ya existe
        print("El ID ya está registrado. Intente con otro.")
        return
    # Solicita los datos personales del cliente
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    # Almacena los datos en el diccionario de clientes
    clientes[id_cliente] = {
        "nombre": nombre,
        "email": email,
        "telefono": telefono,
        "direccion": direccion,
    }
    print("Cliente registrado con éxito.")

def mostrar_clientes():
    """Muestra todos los clientes registrados."""
    print("Clientes registrados:")
    for id_cliente, datos in clientes.items():  # Itera sobre los clientes registrados
        print(f"{id_cliente}: {datos}")  # Muestra ID y datos del cliente

def realizar_compra():
    """Permite a un cliente realizar una compra seleccionando productos."""
    print("Realizar una compra")
    id_cliente = input("Introduzca su ID de cliente: ")  # Solicita el ID del cliente
    if id_cliente not in clientes:  # Verifica si el cliente está registrado
        print("Cliente no registrado.")
        return
    # Muestra los productos disponibles en el sistema
    print("Productos disponibles:")
    for codigo, info in productos.items():
        print(f"{codigo}: {info['nombre']} - {info['precio']}€")
    
    carrito = []  # Lista para almacenar los productos seleccionados
    while True:
        codigo = input("Seleccione un producto (o 'fin' para terminar): ")  # Solicita un producto
        if codigo == "fin":  # Finaliza la selección si el usuario escribe "fin"
            break
        if codigo not in productos:  # Verifica que el código sea válido
            print("Producto no válido.")
            continue
        cantidad = int(input("Cantidad: "))  # Solicita la cantidad del producto
        carrito.append({"codigo": codigo, "cantidad": cantidad})  # Agrega el producto al carrito
    
    # Calcula el total de la compra
    total = sum(productos[item["codigo"]]["precio"] * item["cantidad"] for item in carrito)
    # Genera un número único de pedido
    numero_pedido = len(pedidos) + 1
    # Almacena el pedido en el diccionario
    pedidos[numero_pedido] = {"cliente": id_cliente, "carrito": carrito, "total": total}
    # Muestra el número de pedido y el total
    print(f"Compra finalizada. Número de pedido: {numero_pedido}")
    print(f"Total a pagar: {total}€")

def seguimiento_pedido():
    """Permite al usuario consultar los detalles de un pedido existente."""
    print("Seguimiento de pedido")
    numero_pedido = int(input("Introduzca el número de pedido: "))  # Solicita el número de pedido
    if numero_pedido not in pedidos:  # Verifica si el pedido existe
        print("Pedido no encontrado.")
        return
    pedido = pedidos[numero_pedido]  # Obtiene los datos del pedido
    cliente = clientes[pedido["cliente"]]  # Obtiene los datos del cliente asociado
    # Muestra la información del cliente
    print(f"Datos del cliente: {cliente}")
    print("Detalle del pedido:")
    # Muestra los productos del pedido
    for item in pedido["carrito"]:
        producto = productos[item["codigo"]]
        print(f"{producto['nombre']}: {item['cantidad']} unidades")
    # Muestra el total de la compra
    print(f"Total: {pedido['total']}€")

# Menú principal
def menu():
    """Muestra el menú principal y permite seleccionar funcionalidades."""
    while True:
        print("\n--- Menú ---")
        print("1. Registrar cliente")
        print("2. Mostrar clientes")
        print("3. Realizar compra")
        print("4. Seguimiento de pedido")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")  # Solicita una opción del menú
        if opcion == "1":
            registrar_cliente()  # Llama a la función de registro de cliente
        elif opcion == "2":
            mostrar_clientes()  # Llama a la función para mostrar clientes
        elif opcion == "3":
            realizar_compra()  # Llama a la función para realizar una compra
        elif opcion == "4":
            seguimiento_pedido()  # Llama a la función de seguimiento de pedido
        elif opcion == "5":  # Sale del programa
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")  # Maneja opciones inválidas

# Ejecutar la aplicación
menu()
