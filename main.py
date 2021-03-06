from ColeccionPersonal import ColeccionPersonal
from ObjectEncoder import ObjectEncoder
from Menu import Menu

if __name__=="__main__":
    unObjectEncoder = ObjectEncoder()

    try:
        diccionario = unObjectEncoder.leerArchivojson("personal.json")
    except FileNotFoundError:
        unaColeccionPersonal = ColeccionPersonal()
    else:
        unaColeccionPersonal = unObjectEncoder.decodificarDiccionario(diccionario)
    
    unMenu = Menu()
    unMenu.ejecutarMenu(unaColeccionPersonal)
    diccionario = unaColeccionPersonal.toJSON()
    unObjectEncoder.guardarArchivojson(diccionario, "personal.json")