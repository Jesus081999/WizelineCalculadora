from Calculadora import Calculadora

class Controlador():
    def __init__(self):
        self.option = ""
        self.cifra = ""
        self.encender()
    pass

    def encender(self):
        while self.option != "0":
            self.calculadora = Calculadora()
            self.setCifra()
            self.calculadora.setCifraPrincipal(cifra = float(self.cifra))
            self.calculadora.crearMenu()
            self.option = ""
            while self.option != "0" and self.option != "c":
                print(self.calculadora.getMenu())
                self.setOption()
            pass
        pass
    pass

    def setOption(self):
        self.option = input()
        self.selecOperation(self.option)
    pass

    def selecOperation(self, option):
        if option == "1":
            self.setCifra()
            self.calculadora.sumar(cifra = float(self.cifra))
        elif option == "2":
            self.setCifra()
            self.calculadora.restar(cifra = float(self.cifra))
        elif option == "3":
            self.setCifra()
            self.calculadora.multiplicar(cifra = float(self.cifra))
        elif option == "4":
            self.setCifra()
            self.calculadora.dividir(cifra = float(self.cifra))
        elif option == "5":
            self.setCifra()
            self.calculadora.raiz(cifra = float(self.cifra))
        elif option == "6":
            self.setCifra()
            self.calculadora.exponente(cifra = float(self.cifra))
        elif option == "7":
            self.calculadora.sin()
        elif option == "8":
            self.calculadora.cos()
        elif option == "9":
            self.calculadora.tan()
        elif option == "0":
            print("***   Adios   ***")
        elif option == "c":
            print("*     ***     *")
        else:
            print("*** La seleccion no es valida ***")
    pass

    def setCifra(self):
        isNumber = False
        while(not isNumber):
            try:
                self.cifra = input("Ingrese el número: ")
                float(self.cifra)
                isNumber = True
            except ValueError:
                print("------ EROR >>> Dato no válido ------")
        pass
    pass
pass