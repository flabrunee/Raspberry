import sys
import evdev


def obt_numserie_metodo1():

    devenum = hid.enumerate(0x0483, 0x5710)

    for dev in devenum:
        if dev['vendor_id'] == 0x0483 and dev['product_id'] == 0x5710:
            print('\nSerial: ', (dev['serial_number']))
            print('\n', dev)


def obt_numserie_metodo2():

    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print('Se encontraron los siguientes dispositivos:')
    for device in devices:
        print('Device: Path: ', device.path, ' Name: ', device.name,
              ' Phys: ', device.phys, ' Uniq: ', device.uniq)


def obt_numserie_metodo3():
    path = evdev.list_devices()
    print(path)
    print(evdev.InputDevice(path[0]).uniq)


def main():

    print('\nMetodo 1: ')
    obt_numserie_metodo1()

    print('\nMetodo 2: ')
    obt_numserie_metodo2()

    print('\nMetodo 3: ')
    obt_numserie_metodo3()


if __name__ == '__main__':
    import hid

    try:
        ret = main()
    except (KeyboardInterrupt, EOFError):
        ret = 0
    sys.exit(ret)
