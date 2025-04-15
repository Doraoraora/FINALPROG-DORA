import random

class Map:
      def __init__(self):
            self.current_location = 'police station'
            self.locations = {
                  'sewers': ['herbs', 'ammo'], 
                  'police station' : ['pouch', 'first aid spray'],
                  'back streets' : ['herbs', 'ammo', 'first aid spray']
            }

      def add_item_to_location(self, location: str, item: str):
            self.locations[location].append(item)

      def item_is_in_location(self, location: str, target: str) -> bool: 
            items = self.locations[location]
            for item in items: 
                  if item == target: 
                        return True 
            return False
      
      def get_random_item_from_current_location(self) -> str:
            items = self.locations[self.current_location]
            return items[random.randint(0, len(items) - 1)]