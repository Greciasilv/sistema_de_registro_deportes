
from usuario import Usuario

class Torneo:
    def __init__(self, id_torneo, deporte, nombre, fecha, hora, lugar, precio, cupos, lista_inscritos=None):
        self.id = id_torneo
        self.deporte = deporte
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.precio = precio
        self.cupos_disponibles = cupos
        self._inscritos = lista_inscritos if lista_inscritos is not None else []

    def inscribir_atleta(self, objeto_usuario):
        if self.cupos_disponibles <= 0:
            print(f" No quedan cupos para {self.nombre}.")
            return False
            
        for atleta in self._inscritos:
            if atleta.cedula == objeto_usuario.cedula:
                print(f" El atleta {objeto_usuario.nombre} ya está inscrito.")
                return False
                
        self._inscritos.append(objeto_usuario)
        self.cupos_disponibles -= 1
        return True

    def to_dict(self):
        return {
            "id": self.id,
            "deporte": self.deporte,
            "nombre": self.nombre,
            "fecha": self.fecha,
            "hora": self.hora,
            "lugar": self.lugar,
            "precio": self.precio,
            "cupos_disponibles": self.cupos_disponibles,
            "inscritos": [atleta.to_dict() for atleta in self._inscritos]
        }