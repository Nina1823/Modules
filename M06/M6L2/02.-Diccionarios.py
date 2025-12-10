# El diccionario original de superhéroes del Universo DC, y sus respectivos superpoderes
dc_heroes = {
    "Batman": "Inteligencia y habilidades de combate",
    "Superman": "Vuelo y super fuerza",
    "Flash": "Super velocidad",
    "Catwoman": "Agilidad",
    "Aquaman": "Control sobre el agua y criaturas marinas"
}

# Agregando al héroe Green Lantern con el superpoder Anillo de energía poderosa
dc_heroes["Green Lantern"] = "Anillo de energía poderosa"

# Eliminando al héroe Flash
removed_hero = dc_heroes.pop("Flash")

# Reemplazando el superpoder de Catwoman con Artes marciales
dc_heroes["Catwoman"] = "Artes marciales"

# Mostrando la lista final de héroes y sus superpoderes
print("La lista final de héroes y sus superpoderes:")
for hero, power in dc_heroes.items():
    print(hero + ': ' + power)