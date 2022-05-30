class prueba:
    nombre = ''
    serie = ''
    event = 0

    def __init__(self, name, nserie):
        self.nombre = name
        self.serie = nserie
        #self


d = prueba('uno', 'h987y-KMhg87g')
e = prueba('dos', '76r7JBNNf75/-f87')

print(d.nombre)

print(e.nombre)

registro = {'Nombre':'','IdVendor':'', 'IdProd':'', 'NSerie':'', 'Event':''}

#REGISTRAR LECTORA
#Avisar por grafica q se va a registrar una lectora
#Leer dispositivos
#Ver cual envia ESTACION_
#Asignar la lectora al lugar q corresponda con sus datos (Nombre, Fabricante, Producto, NSerie, Event)
