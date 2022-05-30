import sys
import evdev
import asyncio
from constantes import *
from evdev import ecodes, list_devices, AbsInfo, InputDevice

#def Set_lectoras(device):
Lect1 = evdev.InputDevice('/dev/input/event5')
Lect2 = evdev.InputDevice('/dev/input/event7')

####################################################################################################
#Lectura


async def leer_eventos(device):
    buf = ''
    async for event in device.async_read_loop():
        # Si el evento es de una tecla y se apretó la tecla.  0=key up 1=key down 2=key hold
        if event.type == evdev.ecodes.EV_KEY and event.value == 1:
            kv = evdev.events.KeyEvent(event)
            print(device.path[16] == Lect1.)
            if (kv.scancode == evdev.ecodes.KEY_ENTER):  # Fin de la lectura
                if buf != '':
                    print(buf)
                buf = ''
            else:  # Mientras no termine de leer, agregar a la lectura
                #buf += KEYMAP.get(kv.keycode)
                print(KEYMAP.get(kv.keycode))


def main():
    #Lect1.grab()   #Deshabilitar echo lectoras
    #Lect2.grab()
    '''    path=evdev.list_devices()
    print(path)
    print(evdev.InputDevice(path[0]).uniq)'''

    for device in Lect1, Lect2:
        print(device.path[16])
        asyncio.ensure_future(leer_eventos(device))
    loop = asyncio.get_event_loop()
    loop.run_forever()

    ''' devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print ('Se encontraron los siguientes dispositivos:')
    for device in devices:
        print(device.path, device.name, device.phys, device.uniq) '''
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
