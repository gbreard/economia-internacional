"""
Descarga los datasets base de S7:
1. Natural Earth (shapefile de países, escala 1:110m) para los mapas
2. ECI Atlas de Harvard (Economic Complexity Index, serie histórica)

Se ejecuta una sola vez. Los archivos quedan en datos/.
"""

import sys
import io
import os
import urllib.request
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DATOS = Path(__file__).parent.parent / 'datos'
DATOS.mkdir(exist_ok=True)

# 1) Natural Earth — countries 1:110m (versión GeoJSON, ~200 KB)
NE_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
NE_OUT = DATOS / 'ne_110m_admin_0_countries.geojson'

if not NE_OUT.exists():
    print(f"Descargando Natural Earth -> {NE_OUT.name}...")
    urllib.request.urlretrieve(NE_URL, NE_OUT)
    print(f"   {NE_OUT.stat().st_size // 1024} KB")
else:
    print(f"Natural Earth ya existe ({NE_OUT.stat().st_size // 1024} KB)")

print()
print("Hecho.")
