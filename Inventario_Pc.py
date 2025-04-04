class Inventario:
    def __init__(self, serial="", RAM=0, disco=0, nombre="", marca="", precio=0):
        self._serial = serial
        self._RAM = RAM
        self._disco = disco
        self._nombre = nombre
        self._marca = marca
        self._precio = precio
        self._disponibilidad = True
        self._cantidades = []


    def get_serial(self):
        return self._serial
    
    def get_RAM(self):
        return self._RAM
    
    def get_disco(self):
        return self._disco
    
    def get_nombre(self):
        return self._nombre
    
    def get_marca(self):
        return self._marca
    
    def get_precio(self):
        return self._precio
    
    def get_disponibilidad(self):
        return self._disponibilidad
    
    def set_serial(self, serial):
        self._serial = serial
    
    def set_RAM(self, RAM):
        self._RAM = RAM
    
    def set_disco(self, disco):
        self._disco = disco
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_marca(self, marca):
        self._marca = marca
    
    def set_precio(self, precio):
        self._precio = precio
    
    def set_disponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad

    def Ingresar(self):
        self.set_serial(input("Digita el serial del computador: "))
        while True:
            try:
                self.set_RAM(int(input("Digita la capacidad de la memoria ram en GB: ")))
                break
            except ValueError:
                print("Error, El valor debe ser numerico")
        while True:
            try:
                self.set_disco(int(input("Digite el espacio del disco en GB: ")))
                break
            except ValueError:
                print("Error, El valor debe ser numerico")
        self.set_marca(input("Digite la marca del computador: "))
        while True:
            try:
                precio = int(input("Digite el precio del pc: "))
                if precio > 0:
                    self.set_precio(precio)
                    break
                else:
                    print("El precio debe ser mayor a cero")
            except ValueError:
                print("El valor debe ser numerico")

        self._disponibilidad = True
        
        computador = {"Serial":self.get_serial(), "RAM":self.get_RAM(), "Disco duro":self.get_disco(), "Marca":self.get_marca(), "Precio":self.get_precio(), "Disponibilidad":self._disponibilidad}
        self._cantidades.append(computador)

    def prestar(self):
        if not self._cantidades:
            print("No hay dispositivos para mostrar")
            return
    
        buscar_serial = input("Digite el serial del computador a prestar: ")
        buscar = False
        for pc in self._cantidades:
            if pc["Serial"] == buscar_serial:
                buscar = True
                if pc["Disponibilidad"]:
                    print("Computador disponible")
                    nombre_persona = input("Digite el nombre de la persona a prestar: ")
                    pc["Disponibilidad"] = False
                    self.set_nombre(nombre_persona)
                    print(f"Compuador prestado a: {self.get_nombre()}")
                    break
                else:
                    print("Computador prestado")
                break
        if not buscar:
            print("No se encontro pc con ese serial")

    def modificar(self):
        if not self._cantidades:
            print("Lista vacia")
            return
        buscar_serial = input("Digite el serial del computador a modificar el dato: ")
        buscar = False
        for pc in self._cantidades:
            if pc["Serial"] == buscar_serial:
                buscar = True
                ram_nueva = int(input("Digite la nueva cantidad de espacio de memoria ram en GB: "))
                pc["RAM"] = ram_nueva
                self.set_RAM(ram_nueva)
                print("Actualizacion exitosa")
                break
        if not buscar:
            print("No existe el serial")

    def devolver(self):
        if not self._cantidades:
            print("Sin datos")
            return
        buscar_serial = input("Digite el serial del computador a devolver: ")
        buscar = False
        for pc in self._cantidades:
            if pc["Serial"] == buscar_serial:
                buscar = True
                if pc["Disponibilidad"] == True:
                    print("El computador no esta prestado")
                else:
                    pc["Disponibilidad"] = True
                    self.set_disponibilidad(True)
                    print("Computador disponible de nuevo")
                break
        if not buscar:
            print("No existe el serial")

    def mostrar(self):
        return self._cantidades
    
    def menu(self):
        print("1. para pc")
        print("2. para tablet")
        print("salir")
    
    def Menu_Pc(self):
        print("1. para ingresar")
        print("2. para prestar")
        print("3. para modificar")
        print("4. para devolver")

    def Menu_Tablet(self):
        print("1. para ingresar")
        print("2. para prestar")
        print("3. para modificar")
        print("4. para devolver")