class Comando:
    def ejecutar(self, biblioteca):
        pass  

class ComandoMostrarLibros(Comando):
    def ejecutar(self, biblioteca):
        biblioteca.mostrar_libros()

class ComandoIniciarSesion(Comando):
    def ejecutar(self, biblioteca):
        biblioteca.iniciar_sesion()

class ComandoCerrarSesion(Comando):
    def ejecutar(self, biblioteca):
        biblioteca.cerrar_sesion()

class ComandoRegistrarUsuario(Comando):
    def ejecutar(self, biblioteca):
        biblioteca.registrar_usuario()

class ComandoPrestarLibro(Comando):
    def ejecutar(self, biblioteca):
        biblioteca.prestar_libro()

class ComandoDevolverLibro(Comando):
    def ejecutar(self, biblioteca):
        biblioteca.devolver_libro()

class ComandoMostrarUsuarios(Comando):
    def ejecutar(self, biblioteca):
        biblioteca.mostrar_usuarios()

class ComandoMostrarLibrosPrestados(Comando):
    def ejecutar(self, biblioteca):
        biblioteca.mostrar_libros_prestados()

class ComandoSalir(Comando):
    def ejecutar(self, biblioteca):
        print("¡Hasta luego!")
        exit()
