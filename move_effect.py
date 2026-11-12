class MoveEffect:

    VALID_TARGETS = ("user", "enemy")

    def __init__(self, who_gets="enemy"):
        if who_gets not in self.VALID_TARGETS:
            raise ValueError(f"who_gets must be one of {self.VALID_TARGETS}, got '{who_gets}'")
        self.who_gets = who_gets

    def apply_effect(self, pokemon_user, pokemon_enemy):
        raise NotImplementedError("Subclasses must implement apply_effect")
    def _get_target(self, pokemon_user, pokemon_enemy):
        if self.who_gets =="user":
            return pokemon_user
        return pokemon_enemy

class Damage(MoveEffect):
    def __init__(self, power, who_gets="enemy"):
        super().__init__(who_gets)
        self.power = power

       
    def apply_effect(self, pokemon_user, pokemon_enemy):
        target = self._get_target(pokemon_user, pokemon_enemy)
        print(f"{pokemon_user.nickname} deals damage to {target.nickname}")

class StatsChange(MoveEffect):
    def __init__(self, which_stats, stages, who_gets):
        super().__init__(who_gets)
        self.which_stats = which_stats
        self.stages = stages
        
    def apply_effect(self, pokemon_user, pokemon_enemy):

        target = self._get_target(pokemon_user, pokemon_enemy)
        if self.stages > 0:
            direction = "rose"
        else:
           direction = "fell"

        print(f"{target.nickname}'s {self.which_stats} {direction}")


class StatsCondition(MoveEffect):
    STATUS_CONDITIONS = {
        "burn": {"tag": "BRN", "phrase": "was burned"},
        "paralysis": {"tag": "PAR", "phrase": "was paralyzed"},
        "sleep": {"tag": "SLP", "phrase": "fell asleep"},
        "poison": {"tag": "PSN", "phrase": "was poisoned"},
        "freeze": {"tag": "FRZ", "phrase": "was frozen"},
    }

    def __init__(self, effect_chance, who_gets, condition):
        super().__init__(who_gets)
        if condition not in self.STATUS_CONDITIONS:
            raise ValueError(f"Unknown condition '{condition}'. Valid: {list(self.STATUS_CONDITIONS)}")
        if not 0 <= effect_chance <= 100:
            raise ValueError(f"effect_chance must be between 0 and 100, got {effect_chance}")
        self.effect_chance = effect_chance
        self.condition = condition

    def apply_effect(self, pokemon_user, pokemon_enemy):
        target = self._get_target(pokemon_user, pokemon_enemy)
        info = self.STATUS_CONDITIONS[self.condition]
        print(f"{target.nickname} {info['phrase']}")