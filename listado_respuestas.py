from respuesta import Respuesta

class ListadoRespuestas:
    def __init__(self):
        # Lista que almacena objetos de tipo Respuesta
        self.respuestas = []

    def agregar_respuesta(self, respuesta: Respuesta):
        self.respuestas.append(respuesta)

    def mostrar_respuestas(self):
        for r in self.respuestas:
            print(f"{r.pregunta.enunciado} -> {r.alternativa.texto}")