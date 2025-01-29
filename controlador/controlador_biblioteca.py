from modelo.comando import Comando
from modelo.libro import Libro
from modelo.usuario import UsuarioFactory, Estudiante, Profesor, Administrador
from vista.consola import Consola, ObservadorConsola
import json

from modelo.comando import (
    ComandoMostrarLibros, ComandoIniciarSesion, ComandoCerrarSesion, 
    ComandoRegistrarUsuario, ComandoPrestarLibro, ComandoDevolverLibro, 
    ComandoMostrarUsuarios, ComandoMostrarLibrosPrestados, ComandoSalir
)

class ControladorBiblioteca:
    def __init__(self):
        self.observadores = []
        self.usuarios = self.cargar_usuarios()  
        self.libros = self.cargar_libros()
        self.usuario_actual = None

        self.agregar_observador(ObservadorConsola())


    def actualizar(self, evento, datos):
        if evento == "usuarios_cargados":
            print("\n📢 Notificación: Usuarios cargados en el sistema.")
        elif evento == "libro_prestado":
            print(f"\n📢 Notificación: El libro '{datos['libro'].titulo}' fue prestado a {datos['usuario'].nombre}.")
        elif evento == "libro_devuelto":
            print(f"\n📢 Notificación: El libro '{datos['libro'].titulo}' ha sido devuelto.")

                                                        
    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, evento, datos):
        for observador in self.observadores:
            observador.actualizar(evento, datos)

    def iniciar(self):
        while True:
            if not self.usuario_actual: 
                opcion = Consola.mostrar_menu_sin_sesion()
                comandos = {
                    "1": ComandoMostrarLibros(),
                    "2": ComandoIniciarSesion(),
                    "3": ComandoSalir()
                }

            elif isinstance(self.usuario_actual, Administrador): 
                opcion = Consola.mostrar_menu_admin()
                comandos = {
                    "1": ComandoMostrarLibros(),
                    "2": ComandoRegistrarUsuario(),
                    "3": ComandoCerrarSesion(),
                    "4": ComandoPrestarLibro(),
                    "5": ComandoDevolverLibro(),
                    "6": ComandoMostrarUsuarios(),
                    "7": ComandoMostrarLibrosPrestados(),
                    "8": ComandoSalir()
                }

            elif isinstance(self.usuario_actual, Profesor): 
                opcion = Consola.mostrar_menu_profesor()
                comandos = {
                    "1": ComandoMostrarLibros(),
                    "2": ComandoCerrarSesion(),
                    "3": ComandoPrestarLibro(),
                    "4": ComandoDevolverLibro(),
                    "5": ComandoSalir()
                }

            else: 
                opcion = Consola.mostrar_menu_estudiante()
                comandos = {
                    "1": ComandoMostrarLibros(),
                    "2": ComandoCerrarSesion(),
                    "3": ComandoSalir()
                }

            if opcion in comandos:
                comandos[opcion].ejecutar(self)
            else:
                print("Opción no válida.")


    def guardar_usuarios(self):
        with open("usuarios.json", "w") as file:
            json.dump([
                {"id": u.id, "nombre": u.nombre, "email": u.email, "tipo": type(u).__name__.lower()}
                for u in self.usuarios
            ], file)

    def cargar_usuarios(self):
        try:
            with open("usuarios.json", "r") as file:
                usuarios_data = json.load(file)
                usuarios = []
                for u in usuarios_data:
                    if u["tipo"] == "estudiante":
                        usuario = Estudiante(u["id"], u["nombre"], u["email"])
                    elif u["tipo"] == "profesor":
                        usuario = Profesor(u["id"], u["nombre"], u["email"])
                    elif u["tipo"] == "administrador":
                        usuario = Administrador(u["id"], u["nombre"], u["email"])
                    else:
                        continue
                    
                    usuarios.append(usuario)

                self.notificar_observadores("usuarios_cargados", usuarios) 
                return usuarios

        except FileNotFoundError:
            print("\n❌ ERROR: El archivo usuarios.json no existe. Se creará uno nuevo al registrar usuarios.\n")
            return []
        except json.JSONDecodeError:
            print("\n❌ ERROR: El archivo usuarios.json está corrupto o vacío. Verifica su contenido.\n")
            return []


    def guardar_libros(self):
        with open("libros.json", "w") as file:
            json.dump([
                {
                    "id": l.id,
                    "titulo": l.titulo,
                    "autor": l.autor,
                    "genero": l.genero,
                    "disponibilidad": l.disponibilidad,
                    "prestado_a": l.prestado_a.email if l.prestado_a else None  
                }
                for l in self.libros
            ], file, indent=4)  

    def cargar_libros(self):
        try:
            with open("libros.json", "r") as file:
                libros_data = json.load(file)
                libros = []
                for l in libros_data:
                    libro = Libro(l["id"], l["titulo"], l["autor"], l["genero"], l["disponibilidad"])

                    if l["prestado_a"]:
                        usuario_prestado = next((u for u in self.usuarios if u.email == l["prestado_a"]), None)
                        libro.prestado_a = usuario_prestado
                    
                    libros.append(libro)
                return libros
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def mostrar_usuarios(self):
        if not isinstance(self.usuario_actual, Administrador):
            print("No tienes permisos para ver la lista de usuarios.")
            return

        if not self.usuarios:
            print("\nNo hay usuarios registrados.")
        else:
            print("\n--- Usuarios Registrados ---")
            for usuario in self.usuarios:
                print(f"{usuario.id}. {usuario.nombre} - {usuario.email} ({usuario.__class__.__name__})")


    def iniciar_sesion(self):
        email = input("Ingrese su email: ")
        usuario = next((u for u in self.usuarios if u.email == email), None)

        if usuario:
            self.usuario_actual = usuario
            print(f"Inicio de sesión exitoso. Bienvenido, {usuario.nombre} ({usuario.__class__.__name__}).")
        else:
            print("Correo no registrado. Regístrese primero.")

    def cerrar_sesion(self):
        self.usuario_actual = None
        print("Sesión cerrada.")

    def registrar_usuario(self):
        if not isinstance(self.usuario_actual, Administrador):
            print("No tienes permisos para registrar usuarios.")
            return

        tipo = input("Tipo de usuario (estudiante/profesor): ").lower()
        nombre = input("Nombre: ")
        email = input("Email: ")
        usuario = UsuarioFactory.crear_usuario(tipo, len(self.usuarios) + 1, nombre, email)
        usuario.registrar()
        self.usuarios.append(usuario)
        self.guardar_usuarios()
        print(f"Usuario {nombre} registrado con éxito.")

    def mostrar_libros(self):
        Consola.mostrar_libros(self.libros)


    def prestar_libro(self):
        if not isinstance(self.usuario_actual, (Profesor, Administrador)):
            print("No tienes permisos para prestar libros.")
            return

        Consola.mostrar_libros(self.libros)
        id_libro = int(input("ID del libro a prestar: "))
        libro = next((l for l in self.libros if l.id == id_libro and l.disponibilidad), None)

        if libro:
            libro.disponibilidad = False
            libro.prestado_a = self.usuario_actual
            self.guardar_libros()
            print(f"El libro '{libro.titulo}' ha sido prestado a {self.usuario_actual.nombre}.")

            self.notificar_observadores("libro_prestado", {"libro": libro, "usuario": self.usuario_actual})
        else:
            print("El libro no está disponible o no existe.")

    def devolver_libro(self):
        if not self.libros:
            print("No hay libros registrados.")
            return

        libros_prestados = [libro for libro in self.libros if not libro.disponibilidad]
        
        if not libros_prestados:
            print("No hay libros prestados.")
            return

        print("\n--- Libros Prestados ---")
        for libro in libros_prestados:
            print(f"{libro.id}. {libro.titulo} (Prestado a: {libro.prestado_a.nombre})")

        id_libro = int(input("ID del libro a devolver: "))
        libro = next((l for l in libros_prestados if l.id == id_libro), None)

        if libro:
            libro.disponibilidad = True
            print(f"El libro '{libro.titulo}' ha sido devuelto por {libro.prestado_a.nombre}.")
            libro.prestado_a = None
            self.guardar_libros()

            self.notificar_observadores("libro_devuelto", {"libro": libro})  # 🔥 Notificamos la devolución
        else:
            print("ID de libro no válido.")

    def mostrar_libros_prestados(self):
        if not isinstance(self.usuario_actual, Administrador):
            print("No tienes permisos para ver los libros prestados.")
            return

        libros_prestados = [libro for libro in self.libros if not libro.disponibilidad]

        if not libros_prestados:
            print("\nNo hay libros prestados actualmente.")
            return

        print("\n--- Libros Prestados ---")
        for libro in libros_prestados:
            print(f"{libro.id}. {libro.titulo} - {libro.autor} (Prestado a: {libro.prestado_a.nombre})")
