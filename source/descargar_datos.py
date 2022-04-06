#programa para que descargue los datos
import requests

# 
url = 'https://ukraine.bellingcat.com/ukraine-server/api/ukraine/export_events/deeprows'

import requests
import shutil

folder = 'data'
nombre_archivo = 'datos_geolocalizador'

def descargar(url):
    """
    La funcion descarga los datos del url en un nuevo archivo .csv
    
    Parametros:
    ------------
    url: str 
        link de donde se extrae la informacion.
    
    """
    r = requests.get(url, verify=False, stream=True)
    # verifica que este en servicio
    if r.status_code != 200:
        print("Fallo")
        exit()
    else:
        r.raw.decode_content = True
        with open(f"{folder}/{nombre_archivo}.csv", 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print("Datos descargados! :) ")

descargar(url)

