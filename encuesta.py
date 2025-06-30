from pregunta import Pregunta

class Encuesta:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.preguntas = []

    def agregar_pregunta(self, pregunta_dict: dict):
        """
        Recibe un diccionario con el enunciado y lista de alternativas.
        { 'enunciado': str, 'alternativas': [ { 'texto': str }, ... ] }
        """
        nueva = Pregunta(pregunta_dict['enunciado'])
        for alt in pregunta_dict.get('alternativas', []):
            nueva.agregar_alternativa(alt)
        self.preguntas.append(nueva)

    def mostrar_encuesta(self):
        print(f"Encuesta: {self.titulo}")
        for i, p in enumerate(self.preguntas):
            print(f"{i + 1}. {p.enunciado}")
            for j, alt in enumerate(p.alternativas):
                print(f"   {j + 1}. {alt.texto}")


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, titulo: str, edad_minima: int, edad_maxima: int):
        super().__init__(titulo)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, titulo: str, regiones_validas: list):
        super().__init__(titulo)
        self.regiones_validas = regiones_validas

    def validar_usuario(self, usuario):
        return usuario.region in self.regiones_validas