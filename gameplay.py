class Map:
      def __init__(self):
            self.locations = {
                  'sewers': ['herbs', 'ammo'], 
                  'police_station' : ['pouch'],
                  'back_streets' : ['herbs', 'ammo', 'first aid spray']
            }

      def add_item_to_location(self, location: str, item: str):
            self.locations[location].append(item)

      def item_is_in_location(self, location: str, target: str) -> bool: 
            items = self.locations[location]
            for item in items: 
                  if item == target: 
                        return True 
            return False


            
