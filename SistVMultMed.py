import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        try: 
            fecha_v= datetime.strptime(f,"%d /%m/%y")
            self.__fecha_ingreso=fecha_v.date()
        
        except ValueError:
            print("Error la fecha debe de estar de forma dd/mmm/yy. Intentelo nuevamente con este formato")

    def asignarLista_Medicamentos(self, lista_med):
     nombres = set()
     nueva_lista = []
     for med in lista_med:
        nombre = med.verNombre().lower()
        if nombre in nombres:
            print(f"El medicamento '{nombre}' ya está en la lista, se omite.")
        else:
            nombres.add(nombre)
            nueva_lista.append(med)
     self.__lista_medicamentos = nueva_lista

    def eliminarMedicamento(self, nombre_medicamento):
        for m in self.__lista_medicamentos:
            if m.verNombre().lower() == nombre_medicamento.lower():
                self.__lista_medicamentos.remove(m)
                print(f"Medicamento '{nombre_medicamento}' eliminado con éxito.")
                return True
        print(f"Medicamento '{nombre_medicamento}' no encontrado.")
        return False    
class sistemaV:
    def __init__(self):
        self.__mascotas = {
            "canino": {},
            "felino": {}
        }
        self.__lista_mascotas = []  # nueva lista de todas las mascotas en orden

    def verificarExiste(self, historia):
        for tipo in self.__mascotas:
            if historia in self.__mascotas[tipo]:
                return True
            
            return False
        
    def ingresarMascota(self, mascota):
        tipo = mascota.verTipo().lower()
        if tipo in self.__mascotas:
            self.__mascotas[tipo][mascota.verHistoria()] = mascota
            self.__lista_mascotas.append(mascota)  # se añade a la lista también
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas)

    def obtenerMascota(self, historia):
        for tipo in self.__mascotas:
            if historia in self.__mascotas[tipo]:
                return self.__mascotas[tipo][historia]
        return None

    def eliminarMascota(self, historia):
        for tipo in self.__mascotas:
            if historia in self.__mascotas[tipo]:
                mascota = self.__mascotas[tipo][historia]
                self.__lista_mascotas.remove(mascota)  # eliminar también de la lista
                del self.__mascotas[tipo][historia]    # eliminar del diccionario
                return True
        return False

    def verListaMascotas(self):
        return self.__lista_mascotas
def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento de una mascota 
                       \n7- Salir
                       \nUsted ingresó la opción: ''' ))
        if menu == 1:
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...")
                continue
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            if not servicio_hospitalario.verificarExiste(historia):
                nombre = input("Ingrese el nombre de la mascota: ")
                tipo = input("Ingrese el tipo de mascota (felino o canino): ")
                peso = int(input("Ingrese el peso de la mascota: "))
                fecha = input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm = int(input("Ingrese cantidad de medicamentos: "))
                lista_med = []

                for i in range(nm):
                    nombre_medicamento = input("Ingrese el nombre del medicamento: ")
                    dosis = int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamento)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
           
            else:
                 print("Ya existe la mascota con ese número de historia clínica.")
        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
       
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        elif menu==6: 
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            paciente= servicio_hospitalario.obtenerMascota(historia)
            if paciente:
                nombre_medicamento = input("Ingrese el nombre del medicamento a eliminar: ")
                paciente.eliminarMedicamento(nombre_medicamento)
            else:
                print("No se encontró la mascota.")

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()
