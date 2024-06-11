def buscar_por_autor(biblioteca, autor_buscar):
    '''Declaramos la funcion buscar por el nombre de autor:'''
    print(f"Libros escritos por {autor_buscar}:")
    for libro in biblioteca:
        if libro['Autor'] == autor_buscar:
            print(f"Título: {libro['Titulo']}, Año: {libro['Año']}")