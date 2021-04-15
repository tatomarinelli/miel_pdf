import os
try:
    from modules.header import headerInfo
except ImportError:
    print("url_function.py: importing header.py error")
    
def AskForUrl():
    url_mielhistorico = 'https://mielhistorico.unlam.edu.ar/'
    url_miel = 'https://miel.unlam.edu.ar/'

    print("\n Seleccione el sitio de MIeL a ingresar: \n")
    print("1 -- MIeL\n")
    print("2 -- MIeL Historico\n\n")
    while True:
        try:
            menu = int(input())
            while (menu > 2 or menu <= 0):
                print("Error, por favor ingrese un valor valido\n")
                menu = int(input())
        except  ValueError:
            print("Error, por favor ingrese un valor valido\n")
            continue
        else:
            break
        
    os.system('cls')
    headerInfo()

    if(menu == 1):
        print("Ha seleccionado: MIeL \n")
        return url_miel
    else:
        print ("Ha seleccionado: MIeL Historico \n")
        return url_mielhistorico