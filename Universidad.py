class Universidad:
    def __init__(self):
        self.facultades = {}
        self.programas = {}
        self.estudiantes = {}

   
    def registrar_facultad(self, facultad):
        self.facultades[facultad.nombre] = facultad

   
    def registrar_programa(self, programa, facultad_nombre):
        if facultad_nombre in self.facultades:
            self.programas[programa.nombre] = {"programa": programa, "facultad": facultad_nombre}
        else:
            raise ValueError(f"La facultad '{facultad_nombre}' no está registrada.")

    # Registrar un estudiante en un programa
    def registrar_estudiante(self, estudiante, programa_nombre):
        if programa_nombre in self.programas:
            self.estudiantes[estudiante["id"]] = {
                "estudiante": estudiante,
                "programa": programa_nombre
            }
        else:
            raise ValueError(f"El programa '{programa_nombre}' no está registrado.")


    def buscar_estudiante(self, id):
        return self.estudiantes.get(id)

    
    def registrar_datos_examen(self, id, datos_examen):
        estudiante_info = self.buscar_estudiante(id)
        if estudiante_info:
            estudiante_info.setdefault("datos_examen", []).append(datos_examen)
        else:
            raise ValueError(f"El estudiante con ID '{id}' no existe.")

    # Obtener datos completos de un estudiante
    def obtener_datos_estudiante(self, id):
        estudiante_info = self.buscar_estudiante(id)
        if estudiante_info:
            programa_nombre = estudiante_info["programa"]
            facultad_nombre = self.programas[programa_nombre]["facultad"]
            return {
                "facultad": facultad_nombre,
                "programa": programa_nombre,
                "estudiante": estudiante_info["estudiante"],
                "datos_examen": estudiante_info.get("datos_examen", [])
            }
        else:
            raise ValueError(f"El estudiante con ID '{id}' no existe.")