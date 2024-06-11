def agregar_libro(biblioteca):
    '''Declaramos la funcion agregar libro, del modulo Libroteca'''
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    anio = input("Introduce el año de publicación del libro: ")
    libro = {
        'Titulo' : titulo,
        'Autor' : autor,
        'Año' : anio
    }
    biblioteca.append(libro)
    print(f"El libro '{titulo}' ha sido añadido a la colección.")