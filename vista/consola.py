class Consola:
    @staticmethod
    def mostrar_menu_principal():
        print("\n--- Menú Principal ---")
        print("1. Mostrar libros disponibles")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")
        return input("Selecciona una opción: ")

    @staticmethod
    def mostrar_libros(libros):
        print("\n--- Libros Disponibles ---")
        for libro in libros:
            estado = "Disponible" if libro.disponibilidad else "No Disponible"
            print(f"{libro.id}. {libro.titulo} - {libro.autor} ({estado})")