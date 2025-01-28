from modelo.libro import Libro
from modelo.usuario import UsuarioFactory
from vista.consola import Consola

class ControladorBiblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def iniciar(self):
        while True:
            opcion = Consola.mostrar_menu_principal()
            if opcion == "1":
                Consola.mostrar_libros(self.libros)
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                self.prestar_libro()
            elif opcion == "4":
                self.devolver_libro()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    def registrar_usuario(self):
        tipo = input("Tipo de usuario (estudiante/profesor/administrador): ").lower()
        nombre = input("Nombre: ")
        email = input("Email: ")
        usuario = UsuarioFactory.crear_usuario(tipo, len(self.usuarios) + 1, nombre, email)
        usuario.registrar()
        self.usuarios.append(usuario)

    def prestar_libro(self):
        Consola.mostrar_libros(self.libros)
        id_libro = int(input("ID del libro a prestar: "))
        libro = next((l for l in self.libros if l.id == id_libro), None)
        if libro:
            libro.prestar()
        else:
            print("Libro no encontrado.")

    def devolver_libro(self):
        Consola.mostrar_libros(self.libros)
        id_libro = int(input("ID del libro a devolver: "))
        libro = next((l for l in self.libros if l.id == id_libro), None)
        if libro:
            libro.devolver()
        else:
            print("Libro no encontrado.")