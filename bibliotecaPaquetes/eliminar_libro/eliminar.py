def eliminar_libro(biblioteca, titulo_eliminar):
    '''Función para eliminar un libro de la colección por su título.'''
    encontrado = False
    for libro in biblioteca:
        if libro['Titulo'] == titulo_eliminar:
            biblioteca.remove(libro)
            print(f"El libro '{titulo_eliminar}' ha sido eliminado de la colección.")
            encontrado = True
            break  # Salimos del bucle una vez que encontramos y eliminamos el libro
    if not encontrado==False:
        print(f"No se encontró ningún libro con el título '{titulo_eliminar}'.")
