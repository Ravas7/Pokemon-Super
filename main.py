from species import Species
from pokemon import Pokemon
from move_effect import Damage, StatsChange, StatsCondition
from move import Move


def section(title):
    print()
    print("=" * 40)
    print(title)
    print("=" * 40)


# --- Espécies ---
charmander = Species(
    name="Charmander",
    pokedex_number=4,
    pokemon_type=["Fire"],
    evolution="Charmeleon",
    evolution_level=16,
    base_stats={
        "HP": 39,
        "Attack": 52,
        "Defense": 43,
        "Sp. Atk": 60,
        "Sp. Def": 50,
        "Speed": 65,
    },
)

dragonite = Species(
    name="Dragonite",
    pokedex_number=149,
    pokemon_type=["Dragon", "Flying"],
    evolution=None,
    evolution_level=None,
    base_stats={
        "HP": 91,
        "Attack": 134,
        "Defense": 95,
        "Sp. Atk": 100,
        "Sp. Def": 100,
        "Speed": 80,
    },
)

# --- Golpes ---
ember = Move(
    name="Ember",
    move_type="Fire",
    accuracy=100,
    pp=25,
    effects=[
        Damage(40),
        StatsCondition(condition="burn", effect_chance=10, who_gets="enemy"),
    ],
)

growl = Move(
    name="Growl",
    move_type="Normal",
    accuracy=100,
    pp=40,
    effects=[StatsChange("Attack", -1, "enemy")],
)

# --- Pokémon ---
firestorm = Pokemon(level=5, nickname="firestorm", moves=["Scratch", "Growl"], species=charmander)
veterano = Pokemon(level=50, nickname="veterano", moves=["Hyper Beam", "Outrage"], species=dragonite)

# --- Saída ---
section("POKÉMON")
for pokemon in (firestorm, veterano):
    print(f"{pokemon.nickname} - {pokemon.species.name} (Lv {pokemon.level}) - HP {pokemon.health_points}/{pokemon.max_hp}")
print(f"Total de stats base do {charmander.name}: {charmander.total_base_stats}")

section("EFEITOS (teste do polimorfismo)")
test_effects = [
    Damage(40),
    StatsChange("Attack", -1, "enemy"),
    StatsCondition(condition="burn", effect_chance=10, who_gets="enemy"),
]
for effect in test_effects:
    effect.apply_effect(firestorm, veterano)

section("GOLPES")
ember.use_attack(firestorm, veterano)
growl.use_attack(veterano, firestorm)

section("THUNDER WAVE (o alvo depende de quem usa)")
thunder_wave = StatsCondition(condition="paralysis", effect_chance=100, who_gets="enemy")
thunder_wave.apply_effect(firestorm, veterano)
thunder_wave.apply_effect(veterano, firestorm)

for i in range(20):
    ember.use_attack(firestorm, veterano)

never_hits = Move("Test", "Normal", 0, 10, [Damage(40)])
never_hits.use_attack(firestorm, veterano)