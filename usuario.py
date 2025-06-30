from listado_respuestas import ListadoRespuestas
from respuesta import Respuesta

class Usuario:
    def __init__(self, nombre: str, edad: int, region: str):
        self.nombre = nombre
        self.edad = edad
        self.region = region
        self.respuestas = ListadoRespuestas()

    def responder_encuesta(self, encuesta):
        """
        Muestra preguntas y permite seleccionar una alternativa para cada una.
        Guarda las respuestas en el ListadoRespuestas del usuario.
        """
        for pregunta in encuesta.preguntas:
            print(f"{pregunta.enunciado}")
            for i, alt in enumerate(pregunta.alternativas):
                print(f"  {i + 1}. {alt.texto}")
            opcion = int(input("Selecciona una alternativa: ")) - 1
            seleccion = pregunta.alternativas[opcion]
            respuesta = Respuesta(pregunta, seleccion)
            self.respuestas.agregar_respuesta(respuesta)