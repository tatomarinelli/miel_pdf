import os
import sys

try:
    from modules.download_function import descargaEnCarpetas
    from modules.download_function import descargaSinCarpetas
    from modules.login_function import loginForm
    from modules import version
except ImportError:
    print("Error al importar modulos de funciones")
    os.system("pause")
    sys.exit(0)

try:
    import requests
except ImportError:
    print ("Por favor, primero descargue el modulo requests (pip install requests).")
    os.system("pause")
    sys.exit(0)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print ("Por favor, primero descargue BeautifulSoup (pip install bs4).")
    os.system("pause")
    sys.exit(0)


# UPDATES #
currentVersion = version.getCurrent()
version.checkUpdate()
######################################

def headerInfo():
 print("##################################################################")
 print("Vers: ", currentVersion)
 print("Actualizaciones en:\t https://github.com/tatomarinelli/miel_pdf")
 print("##################################################################\n\n")
    
headerInfo()


#---------- HEADERS ----------#
headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
#-*-*-*-*-* HEADERS *-*-*-*-*-#

#---------- LOGIN REQUEST ----------#
class _errorLogin(Exception) : pass 
while True:
    try:
        login_data = loginForm()
        print("\nConectando...")
        session = requests.Session()
        url = 'https://miel.unlam.edu.ar/principal/event/login/'
        read = session.get(url, headers=headers)
        read = session.post(url, headers = headers, data = login_data)
        soup = BeautifulSoup(read.content, 'html.parser')
    
        loginState = soup.find("a", attrs = {'href': "https://miel.unlam.edu.ar/data2/ayuda/recuperar_clave_intraconsulta.pdf"})
        if loginState != None:
            print("Usuario o Contrasena incorrectos\n")
            raise _errorLogin()
            
    except _errorLogin:
        continue
    else:
        os.system('cls')
        break
    
#-*-*-*-*-* LOGIN REQUEST *-*-*-*-*-#

headerInfo()

#######################################################################################
## Se podria guardar todo en una clase Materia que incluya nombre y link de comision ##
#######################################################################################
#---------- MOSTRAMOS Y GUARDAMOS MATERIAS DISPONIBLES ----------#
try:    
    
    url = 'https://miel.unlam.edu.ar/principal/interno/'
    read = session.get(url)
    soup = BeautifulSoup(read.content, 'html.parser')
    
    materias = []
    print("Materias disponibles:\n")
    for materia in soup.findAll("div", {"class" : "materia-titulo"}):
        materias.append(materia.get_text())
    
    for i, materia in enumerate(materias, start = 1):
        print(i, "--", materia)
    
    linkMaterias = []
    for comisiones in soup.findAll("a", href = True):
        if comisiones['href'].find('https://miel.unlam.edu.ar/contenido/archivos/comision/') == 0:
            linkMaterias.append(comisiones['href'])
#-*-*-*-*-* MOSTRAMOS Y GUARDAMOS MATERIAS DISPONIBLES *-*-*-*-*-#

#---------- SELECCION MATERIA ----------#
    print("\n Seleccione la materia que desea descargar:  ")
    while True:
        try:
            menu = int(input())
            while (menu > len(materias) or menu <= 0):
                print("Error, por favor ingrese un valor valido\n")
                menu = int(input())
        except  ValueError:
            print("Error, por favor ingrese un valor valido\n")
            continue
        else:
            break
        
    os.system('cls')
    headerInfo()
    
    print("Ha seleccionado: ", materias[menu - 1],"\n")
#-*-*-*-*-* SELECCION MATERIA *-*-*-*-*-#

#---------- PATH DESCARGA ----------#
    download_path = (os.getcwd() + "\\Materias\\" + materias[menu - 1] + "\\")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
#-*-*-*-*-* PATH DESCARGA *-*-*-*-*-#

#---------- NAVEGAMOS A LA COMISION ----------#
    url = linkMaterias[menu - 1]        
    read = session.get(url)
    soup = BeautifulSoup(read.content, 'html.parser')
#-*-*-*-*-* NAVEGAMOS A LA COMISION *-*-*-*-*-#

#---------- SELECCION CARPETAS ----------#
    seleccionMaterias = 0
    print("Desea guardar los PDF's en las carpetas especificas?\n")
    print("1 -- Si\n")
    print("2 -- No\n")
    while True:
        try:
            menu = int(input())
            while (menu != 1 and menu != 2):
                print("Error, por favor ingrese un valor valido\n")
                menu = int(input())
        except  ValueError:
            print("Error, por favor ingrese un valor valido\n")
            continue
        else:
            seleccionMaterias = menu
            break

    if (seleccionMaterias == 1):
        enCarpetas = True
        print("Los PDF's se descargan en carpetas")
    else:
        enCarpetas = False
        print ("Los PDF's se descargan todos juntos")

    os.system("pause")
    os.system("cls")
#-*-*-*-*-* SELECCION CARPETAS *-*-*-*-*-#


#---------- DESCARGA ----------#
    print("Comenzando la descarga...\n")
    cant = 0 #Cantidad de descargas

    if (enCarpetas):
        cant = descargaEnCarpetas(soup, session, download_path)
    else:
        cant = descargaSinCarpetas(soup, session, download_path)
    
    print("\n Se descargaron %d archivos" %(cant))
    os.system("pause")               
#-*-*-*-*-* DESCARGA *-*-*-*-*-#

#---------- Exceptions ----------#
except KeyboardInterrupt:
    print("\n[Descarga interrumpida, saliendo...]")
    