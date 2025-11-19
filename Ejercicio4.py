import csv
from collections import defaultdict

fichero = "la-liga-2025-UTC.csv"

# ---------------------------------------------------------
# (1) Cargar resultados (tu código, completado)
# ---------------------------------------------------------
def cargar_Resultados(ruta_csv: str) -> list:
    partidos = []
    print("Carga el fichero:", ruta_csv)

    with open(ruta_csv, newline='', encoding="utf-8") as f:
        lector = csv.DictReader(f)
        i = 0
        for fila in lector:
            i += 1
            partidos.append(fila)

    print("Partidos cargados:", i)
    return partidos
