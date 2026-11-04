from species import Species
from pokemon import Pokemon

charmander = Species(
    name="Charmander", 
    pokedex_number=4, 
    pokemon_type=["Fire"], 
    evolution="Charmeleon", 
    evolution_level=16, base_stats={
    "HP": 39,
    "Attack": 52,
    "Defense": 43,
    "Sp. Atk": 60,
    "Sp. Def": 50,
    "Speed": 65,
}
)
firestorm = Pokemon(level=5, nickname="firestorm", moves=["Scratch", "Growl"], species=charmander)

print(f"{firestorm.nickname} is a {firestorm.species.name} at level {firestorm.level}")
print(charmander.total_base_stats)