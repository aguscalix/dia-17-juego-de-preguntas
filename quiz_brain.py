class CerebroPrueba:
    def __init__(self, p_lista):
        self.pregunta_numero = 0
        self.puntuacion = 0
        self.pregunta_lista = p_lista

    def todavia_hay_preguntas(self):
        return self.pregunta_numero < len(self.pregunta_lista)

    def siguiente_pregunta(self):
        pregunta_actual = self.pregunta_lista[self.pregunta_numero]
        self.pregunta_numero += 1
        respuesta_usuario = input(f"P.{self.pregunta_numero}: {pregunta_actual.texto} (Verdadero(V) / Falso(F)): ")
        self.check_respuesta(respuesta_usuario, pregunta_actual.respuesta)

    def check_respuesta(self, respuesta_usuario, respuesta_correcta):
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            self.puntuacion += 1
            print("¡Estás en lo correcto!")
        else:
            print("Respuesta incorrecta.")
        print(f"La respuesta correcta es: {respuesta_correcta}")
        print(f"Tu puntuación actual es: {self.puntuacion} / {self.pregunta_numero} \n")




