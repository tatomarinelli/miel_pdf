import os
import sys
import webbrowser

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

#---------- HEADERS ----------#
headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
#-*-*-*-*-* HEADERS *-*-*-*-*-#

currentVersion = "1.8"

def getCurrent():
    writeVersion(currentVersion)
    return currentVersion

def writeVersion(current):
    vers = (os.getcwd() + "\\modules\\")
    if not os.path.exists(vers):
        os.makedirs(vers)
    f = open(vers + "vers.txt", "wt")
    f.write(current)
    f.close()

def checkUpdate():
    session = requests.Session()
    url = 'https://raw.githubusercontent.com/tatomarinelli/miel_pdf/master/modules/vers.txt'
    read = session.get(url, headers=headers)
    soup = BeautifulSoup(read.content, 'html.parser')
    updatedVersion = str(soup).split("\n")[0] #Nos quedamos solo con el numero de version.
    

    if (updatedVersion == currentVersion):
        print("\nPosee la ultima version! - ", currentVersion, "\n")
    else: 
        print("\nHay una nueva actualizacion, version actual:v",currentVersion, "Nueva version:v",soup, "\n")
        print("Dirigase a: https://github.com/tatomarinelli/miel_pdf/releases para obtener la ultima version\n\n")
        os.system("pause")
        webbrowser.open("https://github.com/tatomarinelli/miel_pdf/releases")


