import sys
import json

def GuardarConfig(puestos):
    #Guardar
    try:
        with open("config.json","w") as file:
            json.dump(puestos, file, indent=4)
    except OSError:
        return -1
    return 0

def LeerConfig():
    #Leer
    try:
        with open("config.json", "r") as file:
            data = json.load(file)
    except:   #No lo pudo abrir
        return -1
    return data

def CrearConfig():   #Crea estructura archivo configuracion (con verdura)
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
    if (GuardarConfigPuestos(puestos) == -1):   #No pudo crear archivo
        return -1
    else:
        return puestos

def main():
    #GuardarConfigPuestos(data)
    LeerConfigPuestos()

if __name__ == '__main__':
    try:
        ret = main()
    except (KeyboardInterrupt, EOFError):
        ret = 0
    sys.exit(ret)
