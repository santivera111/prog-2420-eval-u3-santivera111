 #TRABAJO 3

def VShore():
      pass


 #La idea principal del codigo es realizar una tienda web donde se puedan realizar varias compras de celulares, para eso estoy haciendo un directorio con descripcion de los celulares


Iphones = {
    "Nombre": "Iphone 13",
    "Precio": 2500000,
    "Envio": 5000,
    "Descripcion": "Destaca por su excelente rendimiento y la calidad de su camara, siendo muy completo en funciones. Ademas, es reconocido por su fluidez y eficiencia, cumpliendo con las expectativas de los usuarios",
    "Memoria": 128,
    "Color": ["Rosa", "Verde", "Negro"]
}

Samsumgs = {
    "Nombre": "Samsumg_Galaxy_S23",
    "Precio": 3800000,
    "Envio": 5000,
    "Descripcion": "Este magnífico dispositivo combina diseño y potencia, ideal para quienes buscan la mejor experiencia en cada momento. Con su fluidez y velocidad, podrás realizar tus tareas diarias sin interrupciones.",
    "Memoria": 512,
    "Color": ["Azul", "Rojo", "Negro"]
}

Xiaomi = {
    "Nombre": "Xiaomi_Pro",
    "Precio": 1500000,
    "Envio": 5000,
    "Descripcion": "La elección perfecta para los amantes de la tecnología. Con el Xiaomi Pro, tendrás un aliado confiable para tu día a día, ya sea para trabajar, jugar o disfrutar de contenido multimedia.",
    "Memoria": 128,
    "Color": ["Gris", "Blanco", "Negro"]
}

Xiaomi_X6_Pro = {
    "Nombre": "Xiaomi_X6_Pro",
    "Precio": 1500000,
    "Envio": 5000,
    "Descripcion": "Vive una experiencia premium con el Xiaomi X6 Pro. Ideal para quienes buscan un equilibrio entre rendimiento y estilo, este smartphone te permitirá disfrutar de todo tu contenido con una pantalla envolvente y colores vibrantes.",
    "Memoria": 512,
    "Color": ["Gris", "Blanco", "Negro"]
}

Moto = {
    "Nombre": "Moto_G24",
    "Precio": 1500000,
    "Envio": 5000,
    "Descripcion": "La opción perfecta para quienes buscan practicidad y buen rendimiento. El Moto G24 es el compañero ideal para mantenerte al día en tus redes sociales, realizar videollamadas o gestionar tus tareas sin complicaciones.",
    "Memoria": 128,
    "Color": ["Gris", "Blanco", "Negro"]
}


#Despues de realizar el diccionario de cada uno debo de realizar una matriz donde esten cada uno de estos, y en cualquier momento llamar cualquier descripcion de estos para compararlas

# Listas de atributos
precios = [(Iphones["Nombre"], Iphones["Precio"]), 
           (Samsumgs["Nombre"], Samsumgs["Precio"]), 
           (Xiaomi["Nombre"], Xiaomi["Precio"]), 
           (Xiaomi_X6_Pro["Nombre"], Xiaomi_X6_Pro["Precio"]), 
           (Moto["Nombre"], Moto["Precio"])]

memorias = [(Iphones["Nombre"], Iphones["Memoria"]), 
            (Samsumgs["Nombre"], Samsumgs["Memoria"]), 
            (Xiaomi["Nombre"], Xiaomi["Memoria"]), 
            (Xiaomi_X6_Pro["Nombre"], Xiaomi_X6_Pro["Memoria"]), 
            (Moto["Nombre"], Moto["Memoria"])]

envios = [(Iphones["Nombre"], Iphones["Envio"]), 
          (Samsumgs["Nombre"], Samsumgs["Envio"]), 
          (Xiaomi["Nombre"], Xiaomi["Envio"]), 
          (Xiaomi_X6_Pro["Nombre"], Xiaomi_X6_Pro["Envio"]), 
          (Moto["Nombre"], Moto["Envio"])]

dispositivos = [Iphones, Samsumgs, Xiaomi, Xiaomi_X6_Pro, Moto]

#Posterior a esto debo de poder comparar las descripciones de cada uno, por medio de una lista de descripciones



# Menú interactivo
#FInalmente realizar un menu con cada una de los celulares disponibles, para poder seleccionarlos, generando otra lista
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Ver lista de precios")
        print("2. Ver lista de memorias")
        print("3. Ver lista de costos de envío")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            print("\nLista de precios:")
            for nombre, precio in precios:
                print(f"{nombre}: {precio}")

            nombre_producto = input("\nIngresa el nombre del producto para ver detalles o 'volver' para regresar: ")
            if nombre_producto.lower() == "volver":
                continue
            for dispositivo in dispositivos:
                if dispositivo["Nombre"].lower() == nombre_producto.lower():
                    print("\nDetalles del producto:")
                    for key, value in dispositivo.items():
                        print(f"{key}: {value}")  #Use ayuda de la ia para poder generar el menu con key en dispositivos
                    break
            else:
                print("Producto no encontrado.")

        elif opcion == "2":
            print("\nLista de memorias:")
            for nombre, memoria in memorias:
                print(f"{nombre}: {memoria} GB")
           
            nombre_producto = input("\nIngresa el nombre del producto para ver detalles o 'volver' para regresar: ")
            if nombre_producto.lower() == "volver":
                continue
            for dispositivo in dispositivos:
                if dispositivo["Nombre"].lower() == nombre_producto.lower():
                    print("\nDetalles del producto:")
                    for key, value in dispositivo.items():
                        print(f"{key}: {value}") #Use ayuda de la ia para poder generar el menu con key en dispositivos, pero continua la idea inicial
                    break
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            print("\nLista de costos de envío:")
            for nombre, envio in envios:
                print(f"{nombre}: {envio}")
         
            nombre_producto = input("\nIngresa el nombre del producto para ver detalles o 'volver' para regresar: ")
            if nombre_producto.lower() == "volver":
                continue
            for dispositivo in dispositivos:
                if dispositivo["Nombre"].lower() == nombre_producto.lower():
                    print("\nDetalles del producto:")
                    for key, value in dispositivo.items():
                        print(f"{key}: {value}")
                    break
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            print("¡Gracias por usar nuestro sistema!")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el menú
menu()


#Otra opcion es realizar un carrito donde se use la funcion del sum, para sumar los productos del carrito



if __name__ == "__VShore__":
    VShore()
