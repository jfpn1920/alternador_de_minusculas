import random
ids = []
titulos = []
textos_originales = []
textos_alternados = []
fechas = []
estados = []
observaciones = []
#---------------------------------------------#
#--|menu_principal_alternador_de_minúsculas|--#
#---------------------------------------------#
while True:
    print("menu principal alternador de minúsculas")
    print("1) crear texto")
    print("2) editar texto")
    print("3) eliminar texto")
    print("4) buscar texto")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------#
    #--|crear_texto|--#
    #-----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_texto = 1
        else:
            id_texto = ids[-1] + 1
        titulo = input("título: ")
        texto_original = input("texto original: ")
        texto_alternado = ""
        mayuscula = False
        for letra in texto_original:
            if letra.isalpha():
                if mayuscula:
                    texto_alternado += letra.upper()
                else:
                    texto_alternado += letra.lower()
                mayuscula = not mayuscula
            else:
                texto_alternado += letra
        fecha = input("fecha: ")
        estado = input("estado (procesado o pendiente): ")
        observacion = input("observación: ")
        ids.append(id_texto)
        titulos.append(titulo)
        textos_originales.append(texto_original)
        textos_alternados.append(texto_alternado)
        fechas.append(fecha)
        estados.append(estado)
        observaciones.append(observacion)
        print("texto registrado correctamente.")
        print("id:", id_texto)
    #------------------#
    #--|editar_texto|--#
    #------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar texto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {textos_originales[i]} | {textos_alternados[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {textos_originales[posicion]} | {textos_alternados[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                titulos[posicion] = input("nuevo título: ")
                texto_original = input("nuevo texto original: ")
                texto_alternado = ""
                mayuscula = False
                for letra in texto_original:
                    if letra.isalpha():
                        if mayuscula:
                            texto_alternado += letra.upper()
                        else:
                            texto_alternado += letra.lower()
                        mayuscula = not mayuscula
                    else:
                        texto_alternado += letra
                textos_originales[posicion] = texto_original
                textos_alternados[posicion] = texto_alternado
                fechas[posicion] = input("nueva fecha: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|eliminar_texto|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar texto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {textos_originales[i]} | {textos_alternados[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {textos_originales[posicion]} | {textos_alternados[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    textos_originales.pop(posicion)
                    textos_alternados.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------#
    #--|buscar_texto|--#
    #------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar texto")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {textos_originales[posicion]} | {textos_alternados[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            procesados = 0
            pendientes = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {textos_originales[i]} | {textos_alternados[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
                if estados[i].lower() == "procesado":
                    procesados += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
            print("estadísticas alternador de minúsculas")
            print("cantidad de textos:", len(ids))
            print("textos procesados:", procesados)
            print("textos pendientes:", pendientes)
            print("primer texto:", titulos[0])
            print("último texto:", titulos[-1])
            posicion = random.randint(0, len(ids) - 1)
            print("demostración")
            print("texto original:")
            print(textos_originales[posicion])
            print("texto alternado:")
            print(textos_alternados[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el alternador de minúsculas.")
        break
    else:
        print("opción no válida.")