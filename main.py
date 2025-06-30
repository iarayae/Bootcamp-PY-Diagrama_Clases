from encuesta import EncuestaLimitadaRegion
from usuario import Usuario

# Crear encuesta
encuesta = EncuestaLimitadaRegion(
    "Encuesta de satisfacción de clientes",
    regiones_validas=["Ñuble", "Biobío"]
)

# Agregar preguntas a la encuesta
encuesta.agregar_pregunta({
    "enunciado": "¿Qué te pareció el servicio?",
    "alternativas": [
        {"texto": "Excelente"},
        {"texto": "Bueno"},
        {"texto": "Regular"},
        {"texto": "Malo"}
    ]
})

encuesta.agregar_pregunta({
    "enunciado": "¿Recomendarías este lugar?",
    "alternativas": [
        {"texto": "Sí"},
        {"texto": "No"}
    ]
})

# Crear usuario válido
usuario = Usuario("Ignacio", 39, "Biobío")

# Validar región (en caso de ser EncuestaLimitadaRegion)
if hasattr(encuesta, "validar_usuario"):
    if not encuesta.validar_usuario(usuario):
        print("Usuario no autorizado para responder esta encuesta por región.")
        exit()

# Mostrar encuesta general
encuesta.mostrar_encuesta()

# Separador para claridad
print("\nAhora responde la encuesta:\n")

# Registrar respuestas del usuario
usuario.responder_encuesta(encuesta)

# Mostrar respuestas guardadas
print("\nRespuestas registradas:")
usuario.respuestas.mostrar_respuestas()
