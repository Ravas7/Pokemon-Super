

class MoveEffect:
    def __init__(self, who_gets="enemy"):
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
        print(f"{pokemon_user.nickname} deals damage to {pokemon_enemy.nickname}")

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
    def __init__(self, effect_chance, who_gets, condition):
        super().__init__(who_gets)
        self.effect_chance = effect_chance
        self.condition = condition

    def apply_effect(self, pokemon_user, pokemon_enemy):
        target = self._get_target(pokemon_user, pokemon_enemy)
        print(f"{target.nickname} was {self.condition}")
        