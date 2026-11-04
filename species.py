class Species:
    def __init__(self, name, pokedex_number, pokemon_type, evolution, evolution_level, base_stats):
        self.name = name
        self.pokedex_number = pokedex_number
        self.pokemon_type = pokemon_type
        self.evolution = evolution
        self.evolution_level = evolution_level
        self.base_stats = base_stats

    @property
    def total_base_stats(self):
        return sum(self.base_stats.values())