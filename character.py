

class Character():
    def __init__(self, name: str, health: int, weapon: str):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.alive = True
        self.inventory = []

    def take_damage(self) -> str:
        self.health -= 1
        if self.health <= 0:
            self.alive = False
            return 'you died!'
        if self.health == 1:
            return 'hazard'
        if self.health == 2:
            return 'critical'
        if self.health == 3:
            return 'safe'

    def add_to_inventory(self, item: str) -> None:
        self.inventory.append(item)

      
