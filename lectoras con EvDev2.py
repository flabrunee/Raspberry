#https://programmerclick.com/article/3117956331/
################################################

#Unas pocas líneas de código simples para detectar dispositivos USB:
#-----------------------------------------------------
#!/usr/bin/python3

import asyncio
import evdev

# Lista de dispositivos usb
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

print('Descubrir dispositivo:')
for device in devices:
  print(device.path, device.name, device.phys)


#-------------------------------------------------------------------------------
#El siguiente paso es leer la entrada del escáner. Modificar el código anterior

#!/usr/bin/python3

 # Disparo cuando se detecta entrada


async def print_events(device):
  async for event in device.async_read_loop():
    print(device.path, evdev.categorize(event), sep=': ')

 # Lista de dispositivos usb
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

 print('Se encontraron los siguientes dispositivos:')
for device in devices:
  print(device.path, device.name, device.phys)

for device in devices:
     # Use asyncio para aceptar entradas de varios dispositivos al mismo tiempo
  asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()

#Se utiliza para ser compatible con la entrada de varios dispositivos.asyncio, Ejecución asincrónica
#El bucle de eventos de un solo dispositivo, de modo que el bloque de entrada de un dispositivo
# no bloqueará otros dispositivos.

#Se imprimen los eventos detallados de cada botón. Significa que la entrada se ha recibido correctamente.
#---------------------------------------------------------
#Un paso más es convertir el contenido del botón en una cadena. Continuar modificando el código:

#!/usr/bin/python3

 # La clave de la tabla de caracteres solo enumera los caracteres de uso común
keymap = {
    'KEY_0': u'0',
    'KEY_1': u'1',
    'KEY_2': u'2',
    'KEY_3': u'3',
    'KEY_4': u'4',
    'KEY_5': u'5',
    'KEY_6': u'6',
    'KEY_7': u'7',
    'KEY_8': u'8',
    'KEY_9': u'9',
    'KEY_A': u'A',
    'KEY_B': u'B',
    'KEY_C': u'C',
    'KEY_D': u'D',
    'KEY_E': u'E',
    'KEY_F': u'F',
    'KEY_G': u'G',
    'KEY_H': u'H',
    'KEY_I': u'I',
    'KEY_J': u'J',
    'KEY_K': u'K',
    'KEY_L': u'L',
    'KEY_M': u'M',
    'KEY_N': u'N',
    'KEY_O': u'O',
    'KEY_P': u'P',
    'KEY_Q': u'Q',
    'KEY_R': u'R',
    'KEY_S': u'S',
    'KEY_T': u'T',
    'KEY_U': u'U',
    'KEY_V': u'V',
    'KEY_W': u'W',
    'KEY_X': u'X',
    'KEY_Y': u'Y',
    'KEY_Z': u'Z',
    'KEY_TAB': u'\t',
    'KEY_SPACE': u' ',
    'KEY_COMMA': u',',
    'KEY_SEMICOLON': u';',
    'KEY_EQUAL': u'=',
    'KEY_LEFTBRACE': u'[',
    'KEY_RIGHTBRACE': u']',
    'KEY_MINUS': u'-',
    'KEY_APOSTROPHE': u'\'',
    'KEY_GRAVE': u'`',
    'KEY_DOT': u'.',
    'KEY_SLASH': u'/',
    'KEY_BACKSLASH': u'\\',
    'KEY_ENTER': u'\n',
}

 # Disparo cuando se detecta entrada


async def print_events(device):
    buf = ''
    async for event in device.async_read_loop():
        # key_up= 0 key_down= 1 key_hold= 2
        if event.type == evdev.ecodes.EV_KEY and event.value == 1:
            kv = evdev.events.KeyEvent(event)
                         # En esta modificación, mapee el evento a la tabla de caracteres
            if (kv.scancode == evdev.ecodes.KEY_ENTER):
                             print('Leer entrada:', buf)
                '''
                                 Lógica de negocios 
                '''
                                 # Borrar búfer
                buf = ''
            else:
                buf += keymap.get(kv.keycode)
 
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
 print ('Se encontraron los siguientes dispositivos:')
for device in devices:
print(device.path, device.name, device.phys)
 
for device in devices:
asyncio.ensure_future(print_events(device))
 
loop = asyncio.get_event_loop()
loop.run_forever()
