import random
import move_effect

class Move:
    def __init__(self, name, move_type, accuracy, pp, effects):
        self.name = name
        self.move_type = move_type
        self.accuracy = accuracy
        self.pp = pp
        self.effects = effects

    def use_attack(self, pokemon_user, pokemon_enemy):
        print(f"{pokemon_user.nickname} used {self.name}!")

        roll = random.randint(1,100) 

        if roll > self.accuracy:
            print(f"{pokemon_user.nickname}'s attack missed!")
            return
        
        for effect in self.effects:
            effect_roll = random.randint(1,100)
            if effect_roll <= effect.effect_chance:
                effect.apply_effect(pokemon_user, pokemon_enemy)    

