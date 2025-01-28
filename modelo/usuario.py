from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    @abstractmethod
    def registrar(self):
        pass

class Estudiante(Usuario):
    def registrar(self):
        print(f"Estudiante {self.nombre} registrado.")

class Profesor(Usuario):
    def registrar(self):
        print(f"Profesor {self.nombre} registrado.")

class Administrador(Usuario):
    def registrar(self):
        print(f"Administrador {self.nombre} registrado.")

class UsuarioFactory:
    @staticmethod
    def crear_usuario(tipo, id, nombre, email):
        if tipo == "estudiante":
            return Estudiante(id, nombre, email)
        elif tipo == "profesor":
            return Profesor(id, nombre, email)
        elif tipo == "administrador":
            return Administrador(id, nombre, email)
        else:
            raise ValueError("Tipo de usuario no válido.")