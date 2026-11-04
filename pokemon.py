class Pokemon:
    def __init__(self, level, nickname, moves, species):
        self.level = level
        self.nickname = nickname
        self.moves = moves
        self.species = species
        self.xp = 0
        self.health_points = self.max_hp

    @property
    def max_hp(self):
        base_hp = self.species.base_stats["HP"]
        return (2 * base_hp * self.level // 100) + self.level + 10