from species import Species
from pokemon import Pokemon
from move_effect import *

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

dragonite = Species(
    name="Dragonite",
    pokedex_number=149,
    pokemon_type=["Dragon", "Flying"],
    evolution=None,
    evolution_level=None,
    base_stats = {
    "HP": 91,
    "Attack": 134,
    "Defense": 95,
    "Sp. Atk": 100,
    "Sp. Def": 100,
    "Speed": 80
}
)

firestorm = Pokemon(level=5, nickname="firestorm", moves=["Scratch", "Growl"], species=charmander)
veterano = Pokemon(level=50, nickname="veterano", moves=["Hyper Beam", "Outrage"], species=dragonite)


effects = [
    Damage(40),
    StatsChange("Attack", -1, "enemy"),
    StatsCondition(condition="burned", effect_chance=10, who_gets="enemy")
]

for effect in effects:
    effect.apply_effect(firestorm, veterano)

thunder_wave = StatsCondition(condition="paralyzed", effect_chance=100, who_gets="enemy")
thunder_wave.apply_effect(firestorm, veterano)   # quem fica paralisado?
thunder_wave.apply_effect(veterano, firestorm)   # e agora?