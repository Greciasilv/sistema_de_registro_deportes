
import json

def cargar_eventos():
    try:
        with open("eventos.json", "r", encoding="utf-8") as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        print("Error: El archivo eventos.json no existe en esta carpeta.")
        return []


lista_de_eventos = cargar_eventos()

print("--- LISTA DE EVENTOS CARGADOS ---")
print(lista_de_eventos)

def filtrar_por_deporte(lista_eventos, deporte_buscado):
    eventos_filtrados = []
    for evento in lista_eventos:
        
        if evento["deporte"].lower() == deporte_buscado.lower():
            eventos_filtrados.append(evento)
    return eventos_filtrados

def mostrar_eventos(lista_eventos):
    if not lista_eventos:
        print("No se encontraron eventos para este deporte.")
        return
    
    for evento in lista_eventos:
        print("========================================")
        print(f" {evento['nombre'].upper()}")
        print(f" Lugar: {evento['lugar']}")
        print(f" Fecha: {evento['fecha']} |  Hora: {evento['hora']}")
        print(f" Precio: {evento['precio']}")
        print(f" Cupos disponibles: {evento['cupos_disponibles']}")
    print("========================================\n")


todos_los_eventos = cargar_eventos()