print("Departamante de confección")
print("1. Ingresar producto a fabrica")
print("2. Mostrar inventario en fabrica")
print("0. SALIR")
opcion=100

listaProductos=[]
while opcion!=0:
  
    opcion=int(input("digita una opcion: "))
    if opcion==1:
       producto=input("Digita el producto que ingresa a fabricación: ")
       #agregar un producto a la lista de productos  
       listaProductos.append(producto)
    elif opcion==2:
        print("mostrando el inventario: ")
        print(listaProductos)
    elif opcion==0:
        print("gracias, hasta pronto")
    else:
        print("opcion invalida..")
print("adios, fin del programa")