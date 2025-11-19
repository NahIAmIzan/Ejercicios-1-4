import csv
from collections import defaultdict

fichero = "la-liga-2025-UTC.csv"

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
def procesar_estadisticas(partidos):
    equipos = defaultdict(lambda: {
        "GF": 0, "GC": 0,
        "Puntos": 0,
        "DG": 0,
        "FairPlay": 0,
        "Directos": defaultdict(lambda: {"GF": 0, "GC": 0})
    })

    for p in partidos:

        # --- COLUMNAS ADAPTADAS A TU CSV ---
        home = p["Home Team"]
        away = p["Away Team"]

        resultado = p["Result"].strip()     # Ej: "2 - 1"
        if "-" not in resultado or resultado.strip() == "" or resultado.count("-") != 1:
            print("Resultado no válido encontrado:", resultado)
            continue  # saltamos este partido

        gh, ga = map(int, resultado.split('-'))

        # ---- Goles ----
        equipos[home]["GF"] += gh
        equipos[home]["GC"] += ga
        equipos[away]["GF"] += ga
        equipos[away]["GC"] += gh

        equipos[home]["DG"] = equipos[home]["GF"] - equipos[home]["GC"]
        equipos[away]["DG"] = equipos[away]["GF"] - equipos[away]["GC"]

        # ---- Puntos ----
        if gh > ga:
            equipos[home]["Puntos"] += 3
        elif ga > gh:
            equipos[away]["Puntos"] += 3
        else:
            equipos[home]["Puntos"] += 1
            equipos[away]["Puntos"] += 1

        # ⚠️ SIN TARJETAS → Fair Play queda en 0

        # ---- Enfrentamientos directos ----
        equipos[home]["Directos"][away]["GF"] += gh
        equipos[home]["Directos"][away]["GC"] += ga

        equipos[away]["Directos"][home]["GF"] += ga
        equipos[away]["Directos"][home]["GC"] += gh

    return equipos
