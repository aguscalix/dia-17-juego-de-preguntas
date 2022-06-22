from question_model import Pregunta
from data import question_data
from quiz_brain import CerebroPrueba

question_bank = []

for pregunta in question_data:
    texto_pregunta = pregunta["text"]
    texto_respuesta = pregunta["answer"]
    nueva_pregunta = Pregunta(texto_pregunta, texto_respuesta)
    question_bank.append(nueva_pregunta)


quiz = CerebroPrueba(question_bank)

while quiz.todavia_hay_preguntas():
    quiz.siguiente_pregunta()

print("Has completado la prueba.")
print(f"Tu puntuación final es: {quiz.puntuacion} / {quiz.pregunta_numero}")


