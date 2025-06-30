from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str):
        # Atributo que almacena el enunciado de la pregunta
        self.enunciado = enunciado
        # Lista de objetos Alternativa
        self.alternativas = []

    def agregar_alternativa(self, alt: dict):
        """
        Agrega una nueva alternativa a la pregunta.
        alt: debe ser un diccionario con clave 'texto'.
        """
        if 'texto' in alt:
            nueva = Alternativa(alt['texto'])
            self.alternativas.append(nueva)