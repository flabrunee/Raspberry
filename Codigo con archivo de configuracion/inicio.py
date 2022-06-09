import re
import os
import sys
import evdev
import asyncio
from constantes import *
from evdev import ecodes, list_devices, AbsInfo, InputDevice
from config import *

Lect1 = evdev.InputDevice('/dev/input/event5')   #TODO Al inicio buscar las lectoras por el serial y engancharlas con el path
                                                 #Esta asignacion tira una falla si no existe el /event_
try:
    Lect2 = evdev.InputDevice('/dev/input/event7')
except:
    print('Fallo')

TerminarApp = False
CancelarLecturaEtiqueta = False
CteEstacion = SET_ESTACION1[0:-1]
'''
puestos = [{"event_id":"5",
            "puesto_id":"1",
            "path":"/dev/input/event5",
            "nombre":"Lectora Elect",
            "phys":"phys",
            "serie":"serie",
            "ip_impresora":"192.168.1.5"},
           {"event_id":"7",
            "puesto_id":"2",
            "path":"/dev/input/event7",
            "nombre":"Lectora Elect2",
            "phys":"phys2",
            "serie":"serie2",
            "ip_impresora":"192.168.1.7"
          }]
'''
def GuardarConfiguracion(estacion, lectora):

    puestos = LeerConfig()
    print('lectora :',lectora)
    if (puestos != -1):
        puestos[estacion-1] = {
            "event_id":lectora.path[16],   #Obtener el id del event de esa lectora   "5"
            "puesto_id":estacion,                                                   #"2"
            "path":lectora.path,                                                    #"/dev/input/event5"
            "nombre":lectora.name,                                                  #"Electronics ...."
            "phys":lectora.phys,                                                    #""
            "serie":lectora.uniq,                                                   #"$%·%·&RT%&"
            "ip_impresora":"192.168.1.5"   #TODO agregar la impresora
           }
        if (GuardarConfig(puestos) == 0):   #Guarda en archivo de configuracion
            return puestos
        else:
            return -1   #No pudo guardar datos
    else:   #No pudo leer archivo
        return -1

def CambioConfiguracion(p):
    id_puesto = None
    for puesto in p:
        strpath = '/dev/input/event' + '8' #puesto.get('event_id')   #Ver q pasa cuando  pide otra ruta => genera excepcion
        lectora = evdev.InputDevice(strpath)
        if (puesto.get('serie') != lectora.uniq):   #Si el numero de serie es distinto...
            id_puesto = puesto.get('puesto_id')
            print(lectora)
    return id_puesto
    '''USO:
    hubo_cambio= CambioConfiguracion(puestos)
    if (hubo_cambio is not None):
        print('Cambió configuracion lectora ', hubo_cambio)'''

def leer_etiqueta():
    '''
       Lo que hace esta funcion es leer de todos los dispositivos que hay enchufados HASTA que encuentre la etiqueta
          de configuracion de estacion o puesto (SET_ESTACION1 Y 2) o hasta que el operario cancele la lectura
          desde la interfaz grafica.
       Cuando encuentra una lectura correcta, corta el ciclo de lectura y devuelve la posicion leída en la etiqueta
          para guardar la configuracion en la ubicacion (/dev/input/event...) que corresponda. Si sale sin encontrar nada devuelve null.
    '''
    global CancelarLecturaEtiqueta
    CancelarLecturaEtiqueta = False
    from select import select   #TODO Llenar la lista de devices
    devices = map(InputDevice, ('/dev/input/event5', '/dev/input/event7', '/dev/input/event3', '/dev/input/event2', '/dev/input/event1', '/dev/input/event4', '/dev/input/event6', '/dev/input/event0'))
    devices = {dev.fd: dev for dev in devices}
    '''    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for dev in devices:
        print(dev)'''
    buf = ''
    find = False
       #Cargar constante de etiqueta para usar de filtro
    CteEstacion = SET_ESTACION1[0:-1]   #Sacarle el 1 para evaluar en re.match(...  (Falta Verificar que funcione)
    print(CteEstacion)
    while ((not find) and (CancelarLecturaEtiqueta == False)):
        r, w, x = select(devices, [], [])
        for fd in r:
            for event in devices[fd].read():
                if event.type == 1 and event.value == 1:   #Si el evento es de una tecla y se apretó la tecla.  evdev.ecodes.EV_KEY=1, value 0=key up 1=key down 2=key hold
                    kv = evdev.events.KeyEvent(event)   #El evento tiene tipo, codigo y valor. Tipo: 01->tecla Codigo: codigo de la tecla. Valor: 0,1,2  soltada,apretada,sostenida
                    if (kv.scancode == 28):   #Fin de la lectura   evdev.ecodes.KEY_ENTER=28
                            #Si la etiqueta leída es la de reconfiguracion de lectora... (CteEstacion => SET_ESTACION -1)
                        #find = re.match("^"+CteEstacion+"?[12]$", buf)   # <- Deberia quedar este codigo
                        find = re.match("^0000000000$", buf)      #o if (buf[0:-1] == CteEstacion):
                        if (find):
                            break
                        buf = ''
                    else:   #Mientras no termine de leer, agregar a la lectura
                        buf += KEYMAP[kv.keycode]
                    if (CancelarLecturaEtiqueta): break   #Van 2 break??
    if (find):   #Sacar el numero de estacion de la etiqueta
        #numeroestacion = re.findall("[12]",buf)   #Extrae numero de Estacion de la etiqueta
        numeroestacion = 1
        print('devices[fd]: ',devices[fd])   #Y le manda el dispositivo
        return [{"puesto_id":numeroestacion,"lectora":devices[fd]}]   #Devuelve esto para que se pueda hacer la modificacion al config afuera de esta función
    else:
        return False


def RegistrarLectora():
    #Hacer el registro de una lectora
    res = leer_etiqueta()
    print('res: ',res)
    if (res != False):   #Si leyó la etiqueta    res = [{"puesto_id":2,"event_id":5,"lectora":device}]
        if (GuardarConfiguracion(res['puesto_id'],res['lectora']) != -1):
            return puestos
        else:
            return -1
    else:   #Cancelaron la lectura
        return -1

####################################################################################################
#Lectura
cnt1, cnt2 = 0
TerminarLectura = False
async def leer_eventos(device):
    buf = ''
    global cnt1,cnt2
    global TerminarLectura
    async for event in device.async_read_loop():
        if event.type == 1 and event.value == 1:   #Si el evento es de una tecla y se apretó la tecla.  evdev.ecodes.EV_KEY=1, value 0=key up 1=key down 2=key hold
            kv = evdev.events.KeyEvent(event)   #El evento tiene tipo, codigo y valor. Tipo: 01->tecla. Codigo: codigo de la tecla. Valor: 0,1,2  soltada,apretada,sostenida
            if (kv.scancode == 28):   #Fin de la lectura   evdev.ecodes.KEY_ENTER => 28
                if (device.path[16] == Lect1.path[16]):   #Si es la lectora 1
                    cnt1+=1
                    print('Lectora 5 ', cnt1, ' Serie: ', Lect1.uniq)
                else:   #Si es la lectora 2
                    cnt2+=1
                    print('Lectora 7 ', cnt2, ' Serie: ', Lect2.uniq)
                print(buf)
                buf = ''
            else:   #Mientras no termine de leer, agregar a la lectura
                buf += KEYMAP[kv.keycode]
            if (TerminarLectura == True):
                break

def VerificarLectoras(puestos):
    #Por cada puesto/lectora verificar que la lectora fisica sea la misma que la cargada en el archivo de configuración
    for (dev in puestos):
        
   #TODO Hacer la parte que falta

def Terminar(mensaje):   #TODO Algun dia hacer
    global TerminarApp
    TerminarApp = True

def main():
    #Lect1.grab()   #Deshabilitar echo lectoras
    #Lect2.grab()
    if (os.path.isfile("./config.json") == False):   #Si no existe archivo de configuración
        if (CrearConfig() == -1):   #Crea el archivo de configuracion
            Terminar('ERR_CREARARCHCONFIG')   #Error
        else:   #Ok
            puestos = RegistrarLectora()   #No salir hasta que no se registre al menos una lectora
    if (not TerminarApp):
        puestos = LeerConfig()
        if (puestos == -1):
            Terminar('ERR_LEERARCHCONFIG')   #Error
        else:   #Ok
            #RegistrarLectora()
            VerificarLectoras(puestos)

#TODO Seguir por aca

'''    for device in Lect1, Lect2:
        asyncio.ensure_future(leer_eventos(device))
    loop = asyncio.get_event_loop()
    loop.run_forever() '''
    #Lect1.ungrab()   #Habilitar echo lectoras
    #Lect2.ungrab()
####################################################################################################

if __name__ == '__main__':
    import hid

    try:
        ret = main()
    except (KeyboardInterrupt, EOFError):
        ret = 0
    sys.exit(ret)
