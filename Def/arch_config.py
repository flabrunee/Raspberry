import json


class LectEst1:
    Nombre
    NSerie


def GuardarConfigEstacion(estacion):
    data = {"id": estacion.lect_id, "path": estacion.lect_path, "nombre": estacion.lect_nombre,
            "phys": estacion.lect_phys, "serie": estacion.lect_nserie, "ip_impresora": estacion.ip_imp}
    #Guardar
    with open("config.json", "w") as file:
        json.dump(data, file, indent=4)


def LeerConfigEstacion(Estacion):


    #Leer
with open("config.json", "r") as file:
    mdata = json.load(file)
    print(mdata)
    print(mdata["NSerieLectEst1"])
