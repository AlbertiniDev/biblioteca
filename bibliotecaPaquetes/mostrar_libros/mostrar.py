def mostrar_libros(biblioteca):
    '''Declaramos la funcion mostrar libros listados:'''
    print("Libros en la colección:")
    for libro in biblioteca:
        print(f"Título: {libro['Titulo']}, Autor: {libro['Autor']}, Año: {libro['Año']}")