import time


class Ascensor:

    def __init__(self, piso_actual):
        self.piso_actual = piso_actual
        self.estado_actual = "parado"
        self.pisos = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def subir_pisos(self, piso_actual, piso_destino):
        if piso_destino > self.pisos[-1] or piso_destino < self.pisos[0]:
            print("🚨🚨🚨ERROR🚨🚨🚨")
            exit()
        for i in self.pisos:
            self.estado_actual = "Subiendo"
            time.sleep(2)
            print(
                f"{self.estado_actual}... actualmente se encuentra en el piso {piso_actual}")
            if piso_actual == piso_destino:
                self.estado_actual = "parado"
                print(
                    f"Ha llegado a su destino,piso {piso_destino}, el ascensor se ha {self.estado_actual}")
                self.set_piso_actual(piso_destino)
                break
            piso_actual += 1

        #self.piso_actual = piso_actual

    def cambiar_piso(self, ascensor, piso_destino):

        if piso_destino > ascensor.piso_actual:
            ascensor.subir_pisos(ascensor.piso_actual, piso_destino)
        else:
            ascensor.bajar_pisos(ascensor.piso_actual, piso_destino)

    def bajar_pisos(self, piso_actual, piso_destino):

        for i in self.pisos:
            self.estado_actual = "Bajando"
            time.sleep(2)
            print(
                f"{self.estado_actual}... actualmente se encuentra en el piso {piso_actual}")
            if piso_actual == piso_destino:
                self.estado_actual = "detenido"
                print(
                    f"Ha llegado a su destino,piso {piso_destino}, el ascensor se ha {self.estado_actual}")
                self.set_piso_actual(piso_destino)
                break
            piso_actual -= 1

    def get_piso_actual(self):
        return self.piso_actual

    def set_piso_actual(self, x):
        self.piso_actual = x

    def stop(self):
        self.estado_actual = "detenido"
        print(f"el ascensor se ha {self.estado_actual}")

    def emergency_call(self):
        print("llamando a emergencias 📞... Nadie contesta 🙃")


if __name__ == '__main__':
    ascensor1 = Ascensor(1)
    ascensor1.emergency_call()
    ascensor2 = Ascensor(7)
    ascensor2.bajar_pisos(ascensor2.piso_actual, 2)
