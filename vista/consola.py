from modelo.observador import Observador

class Consola:
    @staticmethod
    def mostrar_menu_sin_sesion():
        print("\n--- Menú ---")
        print("1. Ver libros disponibles")
        print("2. Iniciar sesión")
        print("3. Salir")
        return input("Selecciona una opción: ")

    @staticmethod
    def mostrar_menu_admin():
        print("\n--- Menú Administrador ---")
        print("1. Ver libros disponibles")
        print("2. Registrar usuario")
        print("3. Cerrar sesión")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Ver usuarios registrados")
        print("7. Ver libros prestados")
        print("8. Salir")
        return input("Selecciona una opción: ")

    @staticmethod
    def mostrar_menu_profesor():
        print("\n--- Menú Profesor ---")
        print("1. Ver libros disponibles")
        print("2. Cerrar sesión")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")
        return input("Selecciona una opción: ")

    @staticmethod
    def mostrar_menu_estudiante():
        print("\n--- Menú Estudiante ---")
        print("1. Ver libros disponibles")
        print("2. Cerrar sesión")
        print("3. Salir")
        return input("Selecciona una opción: ")


    @staticmethod
    def mostrar_libros(libros):
        if not libros:
            print("\nNo hay libros disponibles.")
            return

        print("\n--- Libros Disponibles ---")
        for libro in libros:
            if libro.disponibilidad:
                estado = "Disponible"
            else:
                estado = f"Prestado" if libro.prestado_a else "No disponible"  

            print(f"{libro.id}. {libro.titulo} - {libro.autor} ({estado})")  



class ObservadorConsola(Observador):
    def actualizar(self, evento, datos):
        if evento == "usuarios_cargados":
            print("\n📢 Notificación: Usuarios cargados en el sistema.")
        elif evento == "libro_prestado":
            print(f"\n📢 Notificación: El libro '{datos['libro'].titulo}' fue prestado a {datos['usuario'].nombre}.")
        elif evento == "libro_devuelto":
            print(f"\n📢 Notificación: El libro '{datos['libro'].titulo}' ha sido devuelto.")

