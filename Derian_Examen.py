

productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
    
} 




stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
    
}


def validar_texto(texto):
    return texto.strip() != ""

def validar_peso(peso_kg):
    return peso_kg > 0

def validar_S_n(sn):
    return sn in ["s", "n"]

def validar_valor(precio):
    return precio > 0

def validar_unidad(unidades):

    return unidades > 0

def unidades_categorias(categorias):
    total_unidades=0
    cat=categorias.lower()

    for cat in productos:
        if productos[codigo[1]]== cat.lower():
            if codigo in stock

           

    return categorias

def busqueda_precio(p_min, p_max):
    r = []
    for codigo in stock:
        precio=stock[codigo][0]
        stock=stock[codigo][1]

        if precio >= p_min and precio <= p_max  and stock > 0:
            for codigo in productos:
                nombre=productos[codigo][0]
                form =print(f"{nombre}--------{codigo}")
        r.remove(form)
    
    

def actualizar_precio(codigo, nuevoprecio):
    codigoo= codigo.upper()
    if codigo in stock:
        stock[codigo][0]== nuevoprecio
        return True
    return False

def eliminar_producto(codigo):
    codi= codigo.upper()

    if codigo in productos and codi in stock:
        productos.pop(codi)
        stock.pop(codi)
        return True
    return False


def agregar_producto(nombre, categoria, precio, unidades, marca, peso_kg, es_importado, es_para_cachoros):
        codigoo = codigo.upper()

        if codigo in productos:

            return False
    es_importado=True if es_importado == "s" else False
    es_para_cachoro=True if es_para_cachoro == "s" else False



while True:
    print("===========Menu Princiapl===========")
    print("1. unidades por categoria")
    print("2.busqueda e productos por rango de precio")
    print("3.actualiar el precio de producto")
    print("4.agregar producto")
    print("5.eliminar producto")
    print("6.salir")
    print("============================================")
    try:
        opcion=int(input("ingrese una opcion: "))
    except ValueError:
        print("debe ingresar un numero entero valido")
        if opcion==1:
            cat=int(input("ingrese una categoria a consultar"))
            unidades_categorias(cat)
        elif opcion==2:
            try:
                p_max=int(input("ingrese el precio maximo"))
                p_min=int(input("ingrese el precio minimo"))
                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    busqueda_precio(p_min,p_max)
                    break
                else:
                    print("No hay recorridos encontrados")
            except ValueError:
                print("Error: Debe ingresar un dato valido")
        elif opcion==3:
            while True:
                codigo = input("Ingrese codigo: ")
                try:
                    nuevoprecio= int(input("Ingrese nuevo precio: "))
                    if nuevoprecio > 0:
                        if actualizar_precio(codigo,nuevoprecio):
                            print("Precio actualizado")
                        else:
                            print("El codigo no existe")
                    else:
                        print("El nuevo precio debe ser mayor a 0")
                except ValueError:
                    print("Error: Debe ingresar un dato valido")
                otro = input("¿Desea actualizar otro precio (s/n)?: ")
                if otro == "n":
                    break
        elif opcion==4:
            codigoo=input("ingrese codigo del producto:")
            nombre=input("ingrese nombre:")
            categoria=input("ingrese la categoria:")
            marca=input("ingrese marca:")
            try:
                peso=float(input("inrese peso (kg):"))
            except:
                print("error debe ingresar numero decimal valido")
            es_importado=input("es importado? (s/n): ")
            es_para_cachoro=input("es para cachorros? (s/n) ")
            try:
                
                precio=int(input("ingrese precio:"))
                unidades=int(input("ingrese unidades"))
            except ValueError:
                print("debe ingresar un numero entero valido")

            agregar_producto(nombre, codigo, categoria, marca, peso, es_importado, es_para_cachoro, precio,unidades)
        elif opcion==5:
            
            codi=int(input("ingrese el codigo para eliminar el producto"))
            if eliminar_producto(codigo):

                print("se ah eliminado correctamente")
            else:
                print("no existe el producto")

        elif opcion==6:
            print("programa finalizado")
            break


                


