# -*- coding: utf-8 -*-

#from urllib.request import Request, urlopen
#import urllib.parse as urlparse
import os
import sys

try:
    import requests
except ImportError:
    print ("Por favor, primero descargue el modulo requests (pip install requests).")
    sys.exit(0)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print ("Por favor, primero descargue BeautifulSoup (pip install bs4).")
    sys.exit(0)
 
    
#---------- HEADERS ----------#
headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
#-*-*-*-*-* HEADERS *-*-*-*-*-#
print("Vers: 1.1")
print("Actualizaciones en:\t https://github.com/tatomarinelli/miel_pdf")
#---------- LOGIN DATA ----------#
print("Ingrese usuario: ")
_user = str(input())
print("Ingrese contraseña: ")
_pass = str(input())
login_data = {'usuario' : _user , 'clave' : _pass}
#-*-*-*-*-* LOGIN DATA *-*-*-*-*-#

# #---------- PATH DESCARGA ----------#
# download_path = (os.getcwd()+"\\Materias\\")
# if not os.path.exists(download_path):
#     os.makedirs(download_path)
# #-*-*-*-*-* PATH DESCARGA *-*-*-*-*-#

#---------- LOGIN REQUEST ----------#
print("Conectando...")
s = requests.Session()
url = 'https://miel.unlam.edu.ar/principal/event/login/'
read = s.get(url, headers=headers)
read = s.post(url, headers = headers, data = login_data)
soup = BeautifulSoup(read.content, 'html.parser')
#-*-*-*-*-* LOGIN REQUEST *-*-*-*-*-#

os.system('cls')
print("Vers: 1.1")
print("Actualizaciones en:\t https://github.com/tatomarinelli/miel_pdf")
#######################################################################################
## Se podria guardar todo en una clase Materia que incluya nombre y link de comision ##
#######################################################################################
#---------- MOSTRAMOS Y GUARDAMOS MATERIAS DISPONIBLES ----------#
try:    
    
    url = 'https://miel.unlam.edu.ar/principal/interno/'
    read = s.get(url)
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

#---------- VALIDACION ----------#
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
    print("Vers: 1.1")
    print("Proximas actualizaciones en: https://github.com/tatomarinelli/miel_pdf \n\n")    
    print("Ha seleccionado: ", materias[menu - 1], "\n")
#-*-*-*-*-* VALIDACION *-*-*-*-*-#

#---------- NAVEGAMOS A LA COMISION ----------#
    url = linkMaterias[menu - 1]        
    read = s.get(url)
    soup = BeautifulSoup(read.content, 'html.parser')
#-*-*-*-*-* NAVEGAMOS A LA COMISION *-*-*-*-*-#
    
#---------- PATH DESCARGA ----------#
    download_path = (os.getcwd() + "\\Materias\\" + materias[menu - 1] + "\\")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
#-*-*-*-*-* PATH DESCARGA *-*-*-*-*-#

#---------- DESCARGA ----------#
    print("Comenzando la descarga...\n")    
    i = 0
    #Ya dentro de la comisión, buscamos todos los href
    for tag in soup.findAll('a', href=True): 
    #Una vez en el href, buscamos que contenga .pdf
      if '.pdf' in tag['href']:
        current = s.get(tag['href'])
        
        filename = tag['href'].split('/')[-3] # Se podría mejorar y evitar ese hardcode.
        print ("\n Descargando: %s " %filename)
        i+=1
        
        # -- Descargamos -- #
        f = open(download_path + filename, "wb")
        f.write(current.content)
        f.close()
    
    print("\n Se descargaron %d archivos" %(i))
    os.system("pause")               
#-*-*-*-*-* DESCARGA *-*-*-*-*-#
    
    
#---------- Exceptions ----------#
except KeyboardInterrupt:
    print("\n[Descarga interrumpida, saliendo...]")
