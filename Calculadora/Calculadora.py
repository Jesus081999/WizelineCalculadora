class Calculadora:

    def __init__(self):
        self.cifraPrincipal = 0.0
        self.cifraModificador = 0.0
        self.menu = ""
        self.crearMenu()
    pass

    def crearMenu(self):
        menu = "fz"
        +"\n************************************"
        +"\n " + str(self.cifraPrincipal) 
        +"\n************************************"
        +"\n* Ingrese su opcion de preferencia *"
        +"\n* 1. Sumar                         *"
        +"\n* 2. Restar                        *"
        +"\n* 3. Multiplicar                   *"
        +"\n* 4. Dividir                       *"
        +"\n* 5. Raiz n                        *"
        +"\n* 6. Exponente n                   *"
        +"\n* 7. Seno                          *"
        +"\n* 8. Coseno                        *"
        +"\n* 9. Tangente                      *"
        +"\n* 0. Salir                         *"
        +"\n* c. Reiniciar                     *"
        +"\n************************************"
    pass

    def getMenu(self):
        return self.menu
    pass

    def setCifraPrincipal(self, cifra):
        self.cifraPrincipal = cifra
    pass
pass