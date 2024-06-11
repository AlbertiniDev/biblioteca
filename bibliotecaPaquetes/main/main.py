from bibliotecaPaquetes.agregar_libro.agregar import agregar_libro
from bibliotecaPaquetes.mostrar_libros.mostrar import mostrar_libros
from bibliotecaPaquetes.buscar_por_autor.buscar import buscar_por_autor
from bibliotecaPaquetes.eliminar_libro.eliminar import eliminar_libro

def main():
    '''Función principal que maneja el menú y la interacción con el usuario.'''
    biblioteca = []
    while True:
        print("\nOpciones:")
        print("1. Añadir un nuevo libro")
        print("2. Mostrar todos los libros")
        print("3. Buscar libros por autor")
        print("4. Eliminar un libro")
        print("5. Terminar el programa")
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            agregar_libro(biblioteca)
        elif opcion == "2":
            mostrar_libros(biblioteca)
        elif opcion == "3":
            autor_buscar = input("Introduce el nombre del autor: ")
            buscar_por_autor(biblioteca, autor_buscar)
        elif opcion == "4":
            titulo_eliminar = input("Introduce el título del libro a eliminar: ")
            eliminar_libro(biblioteca, titulo_eliminar)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
