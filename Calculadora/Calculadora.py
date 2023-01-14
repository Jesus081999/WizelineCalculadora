import math

class Calculadora:

    def __init__(self):
        self.cifraPrincipal = 0.0
        self.menu = ""
        self.operation = ""
    pass

    def crearMenu(self):
        self.menu = "\n************************************\n " + str(self.cifraPrincipal) + "\n************************************\n* Ingrese su opcion de preferencia *\n* 1. Sumar                         *\n* 2. Restar                        *\n* 3. Multiplicar                   *\n* 4. Dividir                       *\n* 5. Raiz n                        *\n* 6. Exponente n                   *\n* 7. Seno                          *\n* 8. Coseno                        *\n* 9. Tangente                      *\n* 0. Salir                         *\n* c. Reiniciar                     *\n************************************"
    pass

    def getMenu(self):
        return self.menu
    pass

    def setCifraPrincipal(self, cifra):
        self.cifraPrincipal = cifra
    pass

    def sumar(self, cifra):
        self.cifraPrincipal = self.cifraPrincipal + cifra
        self.crearMenu()
    pass

    def restar(self, cifra):
        self.cifraPrincipal = self.cifraPrincipal - cifra
        self.crearMenu()
    pass

    def multiplicar(self, cifra):
        self.cifraPrincipal = self.cifraPrincipal * cifra
        self.crearMenu()
    pass

    def dividir(self, cifra):
        self.cifraPrincipal = self.cifraPrincipal / cifra
        self.crearMenu()
    pass

    def exponente(self, cifra):
        self.cifraPrincipal = math.pow(self.cifraPrincipal, cifra)
        self.crearMenu()
    pass

    def raiz(self, cifra):
        self.cifraPrincipal = math.pow(self.cifraPrincipal, 1/cifra)
        self.crearMenu()
    pass

    def sin(self):
        self.cifraPrincipal = math.sin(self.cifraPrincipal)
        self.crearMenu()
    pass

    def cos(self):
        self.cifraPrincipal = math.cos(self.cifraPrincipal)
        self.crearMenu()
    pass

    def tan(self):
        self.cifraPrincipal = math.tan(self.cifraPrincipal)
        self.crearMenu()
    pass
pass