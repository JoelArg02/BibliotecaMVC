class Libro:
    def __init__(self, id, titulo, autor, genero, disponibilidad=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponibilidad = disponibilidad

    def prestar(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponibilidad = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")