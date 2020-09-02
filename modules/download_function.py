
## Este modulo se encarga de todas las funciones de descarga ##
import os
#---------- DESCARGA FUNCTION ----------#
def descargaEnCarpetas(soup, session, download_path):
    moduloArray = 0 #Posicion del array para las carpetas
    modulos= []
    cant = 0

    #Buscamos el nombre del modulo.
    for modulo in soup.findAll("div", {"class" : "desplegarModulo"}, "span"):
        modulos.append(modulo.get_text())

    #Buscamos dentro del modulo si hay PDF's
    for moduloContainer in soup.findAll("div", {"class" : "w3-accordion-content"}):        
        moduloArray += 1 #Posicion del array para las carpetas
        for tag in moduloContainer('a', href=True):
            moduloPath = modulos[moduloArray-1].split("\n")[2] #Bastante horrible, si se debugea se entiende. Buscamos en el array obtenido para traernos el nombre de la carpeta correspondiente

            #Una vez en el href, buscamos que contenga .pdf
            if '.pdf' in tag['href']:
                current = session.get(tag['href'])
                filename = tag['href'].split('/')[-3] # Se podría mejorar y evitar ese hardcode.
                cant+=1 #Cantidad de descargas

                # Tenemos que crear el path correspondiente a la carpeta #
                final_path = download_path + str(moduloArray) + "--" + moduloPath + "\\"
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
    #Ya dentro de la comisión, buscamos todos los href
    for tag in soup.findAll('a', href=True): 
    #Una vez en el href, buscamos que contenga .pdf
        if '.pdf' in tag['href']:
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