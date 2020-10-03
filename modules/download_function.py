
import os
import sys

try:
    from modules.file_extension import Fext
except ImportError:
    print("Error al importar modulos de extensiones")
    os.system("pause")
    sys.exit(0)

## Este modulo se encarga de todas las funciones de descarga ##
#---------- DESCARGA FUNCTION ----------#
def descargaEnCarpetas(soup, session, download_path):

    ext = Fext().GetFileExt()
    
    moduloArray = 0 #Posicion del array para las carpetas
    modulos= []
    cant = 0

    #Buscamos el nombre del modulo.
    for modulo in soup.findAll("div", {"class" : "desplegarModulo"}, "span"):
        modulos.append(modulo.get_text())

    #Buscamos dentro del modulo si hay extensiones validas
    for moduloContainer in soup.findAll("div", {"class" : "w3-accordion-content"}):        
        moduloArray += 1 #Posicion del array para las carpetas
        for tag in moduloContainer('a', href=True):
            moduloPath = modulos[moduloArray-1].split("\n")[2] #Bastante horrible, si se debugea se entiende. Buscamos en el array obtenido para traernos el nombre de la carpeta correspondiente

            #Una vez en el href, buscamos que contenga las ext validas           
            for extension in ext:
                if extension in tag['href']:
                    current = session.get(tag['href'])
                    filename = tag['href'].split('/')[-3] # Se podría mejorar y evitar ese hardcode.
                    cant+=1 #Cantidad de descargas

                    moduloPath_norm = normalizarPath(moduloPath) #Mejor optimizacion, evitar que un mismo path vuelva a normalizarse

                    # Tenemos que crear el path correspondiente a la carpeta #
                    final_path = download_path + str(moduloArray) + "--" + moduloPath_norm + "\\"
                    #final_path = download_path + str(moduloArray) + "--" + moduloPath.replace(" ", "-") + "\\"
                    if not os.path.exists(final_path):
                        os.makedirs(final_path)

                    # -- Descargamos -- #
                    print ("\n Descargando: %s " %filename)
                    f = open(final_path + filename, "wb")
                    f.write(current.content)
                    f.close()
    return cant

def descargaSinCarpetas(soup, session, download_path):
    cant = 0
    ext = Fext().GetFileExt()

    #Ya dentro de la comisión, buscamos todos los href
    for tag in soup.findAll('a', href=True): 
    #Una vez en el href, buscamos que contenga ext validas
        for extension in ext:
                if extension in tag['href']:
                    current = session.get(tag['href'])
                    
                    filename = tag['href'].split('/')[-3] # Se podría mejorar y evitar ese hardcode.
                    print ("\n Descargando: %s " %filename)
                    cant+=1
                    
                    # -- Descargamos -- #
                    f = open(download_path + filename, "wb")
                    f.write(current.content)
                    f.close()
    return cant
#-*-*-*-*-* DESCARGA FUNCTION *-*-*-*-*-#


def normalizarPath(str):
    str_cpy = "" #Declaramos un string vacio

    for i in range(len(str)): # i is the current index
        char_compare = ord(str[i].lower()) #Guardamos el char a comparar

        #Validamos que sea letra o numero - Los acentos no pasan
        if ( (char_compare >= ord('a') and char_compare <= ord ('z')) or
             (char_compare >= ord('0') and char_compare <= ord('9')) ):

            str_cpy += str[i]
        else:
            str_cpy += "-" #Char no valido se reemplaza por "-""

    return str_cpy