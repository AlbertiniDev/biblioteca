from setuptools import setup

setup(
    name = 'biblioteca',
    version = '1.0',
    description = 'biblioteca',
    author= 'Albert Ortiz Munté',
    author_email='aomunte@gmail.com',
    url='www.google.com',
    packages=['bibliotecaPaquetes','bibliotecaPaquetes.agregar_libro','bibliotecaPaquetes.mostrar_libros',
    'bibliotecaPaquetes.buscar_por_autor','bibliotecaPaquetes.eliminar_libro','bibliotecaPaquetes.main',],
    scripts=['script_principal.py']
)