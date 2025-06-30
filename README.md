# Bootcamp-PY-Diagrama_Clases
Desafio Bootcamp - Python - Diagrama de Clases

Este proyecto consiste en la implementación de un modelo orientado a objetos basado en un diagrama de clases UML. El sistema permite crear encuestas, definir preguntas con alternativas, registrar usuarios y guardar sus respuestas.

## Archivos y Clases ##

### alternativa.py ##
Contiene la clase 'Alternativa', que representa una opción de respuesta:
- Atributo: 'texto: str'

### pregunta.py ## 
Contiene la clase 'Pregunta', que incluye:
- Atributos:
  - 'enunciado: str'
  - 'alternativas: list[Alternativa]'
- Método:
  - 'agregar_alternativa(alt: dict)'

### encuesta.py ##
Contiene:
- Clase 'Encuesta'
- Clase 'EncuestaLimitadaEdad' (hereda de 'Encuesta')
- Clase 'EncuestaLimitadaRegion' (hereda de 'Encuesta')

'Encuesta' permite agregar preguntas a través de diccionarios y mostrarlas por pantalla.
'EncuestaLimitadaRegion' implementa un método para validar usuarios por región.

### respuesta.py ##
Contiene la clase 'Respuesta', que relaciona una pregunta con la alternativa elegida:
- Atributos:
  - 'pregunta: Pregunta'
  - 'alternativa: Alternativa'

### listado_respuestas.py ##
Contiene la clase 'ListadoRespuestas', que almacena respuestas de un usuario:
- Atributo: 'respuestas: list[Respuesta]'
- Métodos:
  - 'agregar_respuesta(respuesta: Respuesta)'
  - 'mostrar_respuestas()'

### usuario.py ##
Contiene la clase 'Usuario', que representa a una persona que responde encuestas:
- Atributos:
  - 'nombre: str'
  - 'edad: int'
  - 'region: str'
  - 'respuestas: ListadoRespuestas'
- Método:
  - 'responder_encuesta(encuesta)'

### main.py ##
Ejecuta una prueba funcional completa:
- Crea una encuesta limitada por región
- Agrega preguntas con alternativas
- Crea un usuario válido
- Verifica si puede responder la encuesta
- Registra respuestas
- Muestra las respuestas guardadas

## Observaciones ##
- Las preguntas y alternativas se agregan como diccionarios.
- Las restricciones de edad y región son aplicables si se usa 'EncuestaLimitadaEdad' o 'EncuestaLimitadaRegion'.