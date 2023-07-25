import pandas as pd 
from data.platos import platosPopulares
from data.proveedor import Proveedores
from data.reservas import Reservas
from data.creartabla import crearTabla

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
crearTabla(tablaPlatos,"Tabla platos Populares")

tablaProveedor=pd.DataFrame(Proveedores)
print(tablaProveedor)
crearTabla(tablaProveedor," Tabla Proveedores")

tablaReservas=pd.DataFrame(Reservas)
print(tablaReservas)
crearTabla(tablaReservas,"Tabla Reservas")

