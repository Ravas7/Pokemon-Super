

class MoveEffect:
    def __init__(self):
        pass
    def apply_effect(self, pokemon_user, pokemon_enemy):
        raise NotImplementedError("Subclasses must implement apply_effect")

class Damage(MoveEffect):
    def __init__(self, power):
        self.power = power
       
    def apply_effect(self, pokemon_user, pokemon_enemy):
        print(f"{pokemon_user.nickname} deals damage to {pokemon_enemy.nickname}")

class StatsChange(MoveEffect):
    def __init__(self, which_stats, stages, who_gets):
        self.which_stats = which_stats
        self.stages = stages
        self.who_gets = who_gets
        
    def apply_effect(self, pokemon_user, pokemon_enemy):

        if self.who_gets =="user":
            target = pokemon_user
        else:
            target = pokemon_enemy
        if self.stages > 0:
            direction = "rose"
        else:
           direction = "fell"

        print(f"{target.nickname}'s {self.which_stats} {direction}")


class StatsCondition(MoveEffect):
    def __init__(self, effect_chance, who_gets, condition):
        self.effect_chance = effect_chance
        self.who_gets = who_gets
        self.condition = condition

    def apply_effect(self, pokemon_user, pokemon_enemy):
        if self.who_gets == "user":
            target = pokemon_user
        else:
            target = pokemon_enemy
        print(f"{target.nickname} was {self.condition}")
        