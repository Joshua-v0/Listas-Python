#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

lista = []
guardar = ""
saved = 0 
nom = 0 
loop = 0

while loop == 0:
    print("que desea hacer")
    print("\n1. guardar materias")
    print("2. ver materias guardadas materias")
    print("3. ver cantidad de materias guardadas.")
    opc = input("\nesocga un opcion: ")  

    if opc == "1":
        cant = 0
        contador = 0
        nom = ""

        cant = int(input("\ningrese la cantidad de materias que desea guardar: "))
        for i in range(cant):
            contador = contador +1
            print("\nmateria #", str(contador))
            lista.append

            nom = input(f"ingrese el nombre de la materia: ")  
            print("nombre #",nom)
            lista.append

    elif opc == "2":
        print(nom)    
         

    elif opc == "3":
        print("\nCantidad de materias guardadas: ",cant) 
        break 

    



