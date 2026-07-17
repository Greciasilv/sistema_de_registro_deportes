import json
from torneo import Torneo
from usuario import Usuario

class GestorDeportes:
    # Se actualizó el nombre por defecto a 'eventos.json'
    def __init__(self, ruta_archivo="eventos.json"):
        self.ruta_archivo = ruta_archivo
        self.lista_objetos_torneos = []
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                datos_json = json.load(archivo)
                
                for t in datos_json:
                    usuarios_guardados = []
                    for u in t.get("inscritos", []):
                        usuarios_guardados.append(Usuario(u["cedula"], u["nombre"], u["email"]))
                        
                    objeto_torneo = Torneo(
                        id_torneo=t["id"],
                        deporte=t["deporte"],
                        nombre=t["nombre"],
                        fecha=t["fecha"],
                        hora=t["hora"],
                        lugar=t["lugar"],
                        precio=t["precio"],
                        cupos=t["cupos_disponibles"],
                        lista_inscritos=usuarios_guardados
                    )
                    self.lista_objetos_torneos.append(objeto_torneo)
                    
            print(f"Módulos cargados. {len(self.lista_objetos_torneos)} torneos listos.\n")
            
        except FileNotFoundError:
            print(f" Archivo {self.ruta_archivo} no encontrado.")

    def guardar_datos(self):
        lista_diccionarios = [torneo.to_dict() for torneo in self.lista_objetos_torneos]
        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
        print("\n ¡Base de datos JSON actualizada por el Gestor!")