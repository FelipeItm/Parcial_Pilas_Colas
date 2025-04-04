from Inventario_Pc import Inventario
from InventarioTablet import Inventario_T

d1 = Inventario()
d2 = Inventario_T()
bandera = True
while bandera:
    while True:
        try:
            d1.menu()
            opc = int(input("Digite una opcion: "))
            if opc < 1 or opc > 3:
                print("Rango de opciones invalido")
            elif opc == 1:
                    while True:
                        try:
                            d1.Menu_Pc()
                            opc_pc = int(input("Digite una opcion: "))
                            if opc_pc < 1 or opc_pc > 5:
                                print("Opcione invalida")
                            else:
                                if opc_pc == 1:
                                    d1.Ingresar()
                                    print(d1.mostrar())
                                elif opc_pc == 2:
                                    d1.prestar()
                                    #print(d1.mostrar())
                                elif opc_pc == 3:
                                    d1.modificar()
                                    #print(d1.mostrar())
                                elif opc_pc == 4:
                                    d1.devolver()
                                    #print(d1.mostrar())
                                else:
                                    print("Regrsando a menu anterior")
                                    break
                        except ValueError:
                            print("Opcion invalida")
            elif opc == 2:
                    while True:
                        try:
                            d1.Menu_Tablet()
                            opc_t = int(input("Digite una opcion: "))
                            if opc_t < 1 or opc_t > 5:
                                print("Opcion invalida")
                            else:
                                if opc_t == 1:
                                    d2.Ingresar()
                                    print(d2.mostrar())
                                elif opc_t == 2:
                                    d2.prestar()
                                elif opc_t == 3:
                                    d2.modificar()
                                elif opc == 4:
                                    d2.devolver()
                                else:
                                    print("Regresando a menu anterior")
                                    break
                        except ValueError:
                            print("Opcion invalida")  
            else:
                print("Chao")
                bandera = False
                break
        except ValueError:
            print("Error, dato invalido")