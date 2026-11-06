class Move:
    def __init__(self, name, move_type, accuracy, pp, effects):
        self.name = name
        self.move_type = move_type
        self.accuracy = accuracy
        self.pp = pp
        self.effects = effects

    def use_attack(self, pokemon_user, pokemon_enemy):
        print(f"{pokemon_user.nickname} used {self.name}")
