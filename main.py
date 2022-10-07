from ascensor import *

def print_menu(ascensor):
    
    print(f"=========== Piso {ascensor.piso_actual} ============")
    print("1. Subir/bajar de piso")
    print("2. Detener Ascensor")
    print("3. Llamada de emergencia")
    print("4. Salir")

   
    
def run():
    ascensor1 = Ascensor(0)
    print_menu(ascensor1)
    user_input = input("Seleccione una opcion: ")
    
    if user_input == "1":
        piso_destino = int(input("Hasta que piso quiere ir? (0-8)")) 
        ascensor1.cambiar_piso(ascensor1,piso_destino)
        option = input("Desea seguir subiendo o bajando pisos? (Y/N)")
    if user_input == "2":
        ascensor1.stop()
    if user_input == "3":
        ascensor1.emergency_call()
    if user_input == "4":
        exit()

if __name__ == '__main__':
    run()
