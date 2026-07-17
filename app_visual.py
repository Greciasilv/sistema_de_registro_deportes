import tkinter as tk
from tkinter import messagebox, ttk
from gestor import GestorDeportes
from usuario import Usuario


class AppDeportesVisual:

    def __init__(self, root):
        self.root = root
        self.root.title("Plataforma Deportiva Caracas 2026 🇻🇪")
        self.root.geometry("900x550")
        self.root.configure(bg="#f4f6f9")

        self.gestor = GestorDeportes()

        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure(
            "Treeview.Heading", font=("Arial", 10, "bold"), background="#2c3e50", foreground="white"
        )
        self.estilo.configure("TButton", font=("Arial", 10, "bold"), padding=6)

        self.crear_componentes()
        self.cargar_torneos_en_tabla()

    def crear_componentes(self):
        lbl_titulo = tk.Label(
            self.root,
            text="SISTEMA DE REGISTRO DEPORTIVO - CARACAS",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=12,
        )
        lbl_titulo.pack(fill=tk.X, pady=(0, 15))

        panel_principal = tk.Frame(self.root, bg="#f4f6f9")
        panel_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        frame_tabla = tk.LabelFrame(
            panel_principal,
            text=" Torneos Disponibles en la Ciudad ",
            font=("Arial", 11, "bold"),
            bg="white",
            padx=10,
            pady=10,
        )
        frame_tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        columnas = ("id", "deporte", "nombre", "lugar", "cupos")
        self.tabla = ttk.Treeview(
            frame_tabla, columns=columnas, show="headings", selectmode="browse"
        )

        self.tabla.heading("id", text="ID")
        self.tabla.heading("deporte", text="Deporte")
        self.tabla.heading("nombre", text="Torneo")
        self.tabla.heading("lugar", text="Ubicación")
        self.tabla.heading("cupos", text="Cupos")

        self.tabla.column("id", width=40, anchor=tk.CENTER)
        self.tabla.column("deporte", width=100, anchor=tk.W)
        self.tabla.column("nombre", width=180, anchor=tk.W)
        self.tabla.column("lugar", width=180, anchor=tk.W)
        self.tabla.column("cupos", width=60, anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(
            frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview
        )
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tabla.bind("<<TreeviewSelect>>", self.al_seleccionar_torneo)

        frame_registro = tk.LabelFrame(
            panel_principal,
            text=" Formulario de Inscripción ",
            font=("Arial", 11, "bold"),
            bg="white",
            padx=15,
            pady=15,
        )
        frame_registro.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))

        self.lbl_torneo_seleccionado = tk.Label(
            frame_registro,
            text="Selecciona un torneo de la lista",
            font=("Arial", 10, "italic", "bold"),
            fg="#2980b9",
            bg="white",
            wraplength=220,
            justify=tk.LEFT,
        )
        self.lbl_torneo_seleccionado.pack(anchor=tk.W, pady=(0, 20))

        tk.Label(
            frame_registro, text="Cédula de Identidad:", bg="white", font=("Arial", 9, "bold")
        ).pack(anchor=tk.W)
        self.txt_cedula = ttk.Entry(frame_registro, width=30)
        self.txt_cedula.pack(fill=tk.X, pady=(2, 10))

        tk.Label(
            frame_registro, text="Nombre Completo:", bg="white", font=("Arial", 9, "bold")
        ).pack(anchor=tk.W)
        self.txt_nombre = ttk.Entry(frame_registro, width=30)
        self.txt_nombre.pack(fill=tk.X, pady=(2, 10))

        tk.Label(
            frame_registro, text="Correo Electrónico:", bg="white", font=("Arial", 9, "bold")
        ).pack(anchor=tk.W)
        self.txt_email = ttk.Entry(frame_registro, width=30)
        self.txt_email.pack(fill=tk.X, pady=(2, 20))

        btn_inscribir = ttk.Button(
            frame_registro, text="Inscribir Atleta", command=self.procesar_inscripcion
        )
        btn_inscribir.pack(fill=tk.X, pady=5)

        frame_inferior = tk.Frame(self.root, bg="#f4f6f9")
        frame_inferior.pack(fill=tk.X, side=tk.BOTTOM, padx=20, pady=15)

        btn_guardar = ttk.Button(
            frame_inferior,
            text="Guardar Cambios en JSON",
            command=self.guardar_datos,
        )
        btn_guardar.pack(side=tk.RIGHT)

        lbl_info = tk.Label(
            frame_inferior,
            text="Nota: Los cambios se guardarán permanentemente al presionar 'Guardar'.",
            font=("Arial", 8, "italic"),
            bg="#f4f6f9",
            fg="#7f8c8d",
        )
        lbl_info.pack(side=tk.LEFT, pady=5)

    def cargar_torneos_en_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for torneo in self.gestor.lista_objetos_torneos:
            self.tabla.insert(
                "",
                tk.END,
                values=(
                    torneo.id,
                    torneo.deporte,
                    torneo.nombre,
                    torneo.lugar,
                    torneo.cupos_disponibles,
                ),
            )

    def al_seleccionar_torneo(self, event):
        seleccion = self.tabla.selection()
        if not seleccion:
            return

        valores = self.tabla.item(seleccion[0], "values")
        self.id_seleccionado = int(valores[0])
        nombre_torneo = valores[2]

        self.lbl_torneo_seleccionado.config(
            text=f"Torneo: {nombre_torneo}\n(ID: {self.id_seleccionado})",
            fg="#27ae60",
        )

    def procesar_inscripcion(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning(
                "Atención", "Por favor, selecciona un torneo de la lista izquierda primero."
            )
            return

        cedula = self.txt_cedula.get().strip()
        nombre = self.txt_nombre.get().strip()
        email = self.txt_email.get().strip()

        if not cedula or not nombre or not email:
            messagebox.showerror("Campos vacíos", "Todos los campos del atleta son obligatorios.")
            return

        torneo_encontrado = None
        for t in self.gestor.lista_objetos_torneos:
            if t.id == self.id_seleccionado:
                torneo_encontrado = t
                break

        if torneo_encontrado:
            nuevo_atleta = Usuario(cedula, nombre, email)

            if torneo_encontrado.inscribir_atleta(nuevo_atleta):
                messagebox.showinfo(
                    "¡Éxito!",
                    f"Atleta '{nombre}' inscrito con éxito en:\n{torneo_encontrado.nombre}",
                )

                self.txt_cedula.delete(0, tk.END)
                self.txt_nombre.delete(0, tk.END)
                self.txt_email.delete(0, tk.END)
                self.lbl_torneo_seleccionado.config(
                    text="Selecciona un torneo de la lista", fg="#2980b9"
                )

                self.cargar_torneos_en_tabla()
            else:
                messagebox.showerror(
                    "Error de Inscripción",
                    f"No se pudo inscribir al atleta. Puede que ya esté registrado o no queden cupos.",
                )
        else:
            messagebox.showerror("Error", "No se encontró el torneo seleccionado.")

    def guardar_datos(self):
        self.gestor.guardar_datos()
        messagebox.showinfo(
            "Guardado exitoso", "Los datos se han guardado correctamente en eventos.json"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = AppDeportesVisual(root)
    root.mainloop()