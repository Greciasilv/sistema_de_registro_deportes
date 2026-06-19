
class Usuario:
    def __init__(self, cedula, nombre, email):
        self.cedula = cedula
        self.nombre = nombre
        self.email = email

    def to_dict(self):
        return {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "email": self.email
        }