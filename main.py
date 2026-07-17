from gestor import GestorDeportes
from usuario import Usuario

if __name__ == "__main__":
    gestor = GestorDeportes()

    while True:
        print("\n--- PLATAFORMA DEPORTIVA (MODULAR) ---")
        print("1. Ver torneos disponibles")
        print("2. Registrarse e Inscribirse")
        print("3. Salir y Guardar")
        
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            print("\n--- PRÓXIMOS EVENTOS ---")
            for torneo in gestor.lista_objetos_torneos:
                print(f"[{torneo.id}] {torneo.nombre} ({torneo.deporte})")
                print(f" Cupos libres: {torneo.cupos_disponibles}")
                print("-" * 50)

        elif opcion == "2":
            print("\n--- FORMULARIO DE INSCRIPCIÓN ---")
            try:
                id_elegido = int(input("ID del torneo: "))
                
                torneo_encontrado = None
                for t in gestor.lista_objetos_torneos:
                    if int(t.id) == id_elegido:
                        torneo_encontrado = t
                        break
                        
                if torneo_encontrado:
                    cedula = input("Cédula: ")
                    nombre = input("Nombre completo: ")
                    email = input("Correo: ")
                    
                    nuevo_atleta = Usuario(cedula, nombre, email)
                    
                    if torneo_encontrado.inscribir_atleta(nuevo_atleta):
                        print(f"¡{nombre} inscrito con éxito!")
                    else:
                        print("No se pudo realizar la inscripción (quizás no hay cupos).")
                else:
                    print(" Torneo no encontrado. Verifica el ID en la lista.")
                    
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número entero para el ID.")

        elif opcion == "3":
            gestor.guardar_datos()
            print(" ¡Datos guardados! Cerrando sistema modular.")
            break