try:
    from modules.version import getCurrent
except ImportError:
    print("header.py: importing version.py error")

def headerInfo():
 print("##################################################################")
 print("Vers: ", getCurrent())
 print("Actualizaciones en:\t https://github.com/tatomarinelli/miel_pdf")
 print("##################################################################\n\n")