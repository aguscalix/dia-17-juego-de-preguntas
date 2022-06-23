from question_model import Pregunta
from data import pregunta_datos
from quiz_brain import CerebroPrueba

question_bank = []

for pregunta in pregunta_datos:
    texto_pregunta = pregunta["pregunta"]
    texto_respuesta = pregunta["respuesta_correcta"]
    nueva_pregunta = Pregunta(texto_pregunta, texto_respuesta)
    question_bank.append(nueva_pregunta)


quiz = CerebroPrueba(question_bank)

while quiz.todavia_hay_preguntas():
    quiz.siguiente_pregunta()

print("Has completado la prueba.")
print(f"Tu puntuación final es: {quiz.puntuacion} / {quiz.pregunta_numero}")


