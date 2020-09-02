try:
    from bs4 import BeautifulSoup
except ImportError:
    print ("Por favor, primero descargue BeautifulSoup (pip install bs4).")
    os.system("pause")
    sys.exit(0)

#---------- HEADERS ----------#
headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
#-*-*-*-*-* HEADERS *-*-*-*-*-#

currentVersion = "1.3"

def getCurrent()
    return currentVersion

def writeVersion(current):
    vers = (os.getcwd() + "\\modules\\" + "\\")
    f = open(vers + "vers.txt", "wt")
    f.write(current)
    f.close()

def checkUpdate()
    session = requests.Session()
    url = 'https://github.com/tatomarinelli/miel_pdf/blob/master/README.md
    read = session.get(url, headers=headers)
    soup = BeautifulSoup(read.content, 'html.parser')
    print(soup)


