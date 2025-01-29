from controlador.controlador_biblioteca import ControladorBiblioteca
from modelo.libro import Libro

if __name__ == "__main__":
    biblioteca = ControladorBiblioteca()
    # biblioteca.libros.append(Libro(1, "1984", "George Orwell", "Distopía"))
    # biblioteca.libros.append(Libro(2, "Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico"))
    biblioteca.iniciar()