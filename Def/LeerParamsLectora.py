import hid
for d in hid.enumerate(0x0483, 0x5710):
    print('\nPath:',d['path'],'\nVendor_id: ',d['vendor_id'],'\nProduct_id: ',str(d['product_id']),'\nNumero interface: ',d['interface_number'],'\nNumero de serie: ',d['serial_number'],'\nRelease Number: ',d['release_number'],'\nFabricante: ',d['manufacturer_string'],'\nProducto: ',d['product_string'],'\nUsage Page¿?: ',d['usage_page'],'\nUsage¿?: ',d['usage'],'\n')