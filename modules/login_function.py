## Funcion simple de pedido de datos, los datos se validan en el main ya que requiere de parseo ##
#---------- LOGIN FUNCTION ----------#
def loginForm():
    print("Ingrese usuario: ")
    _user = str(input())
    print("\nIngrese contraseña: ")
    _pass = str(input())
    _data = {'usuario' : _user , 'clave' : _pass}
    return _data
#-*-*-*-*-* LOGIN FUNCTION *-*-*-*-*-#