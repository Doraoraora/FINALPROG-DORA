import random
from gameplay import Map
from character import Character

pfs = ['pistol', 'fist', 'shiv']

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
    print()

def generate_zombie() -> str:
    result = pfs[random.randint(0, 2)]
    return result

def pistol_fists_shiv(player: str, zombie: str) -> str:
    if player == 'pistol' and zombie == 'shiv':
        return 'win'
    if player == 'pistol' and zombie == 'fist':
        return 'lose'
    if player == 'shiv' and zombie == 'fist':
        return 'win'
    if player == 'shiv' and zombie == 'pistol':
        return 'lose'
    if player == 'fist' and zombie == 'pistol':
        return 'win'
    if player == 'fist' and zombie == 'shiv':
        return 'lose'
    if player == zombie:
        return 'tie'
    return 'invalid'

if __name__ == '__main__':
    level = Map()
    player = Character("", 3, "")

    print_dramatic_text('Enter your character name. Leon is recommended for combat-heavy gameplay. \n Claire is reccommended for story-based gameplay')
    name = input()
    player.name = name

    print_dramatic_text ('On the night of September 30, 1998 two months after the events of Resident Evil, rookie police officer Leon S. Kennedy makes his way toward Raccoon City to start his first shift at the Raccoon City Police Department. /n Meanwhile, Claire Refield is navigating through the back streets')

    wins = 0
    while(wins < 3 and player.alive):
        level.current_location = random.choice(list(level.locations))
        print_dramatic_text('You enter the ' + level.current_location + ' ...')

        if level.item_is_in_location(level.current_location, 'first aid spray'):
            print('first aid spray is in this location!')

        print_dramatic_text('A zombie appears!')
        zombie = generate_zombie()

        player_input = input('Enter pistol, fist, or shiv: ')
        result = pistol_fists_shiv(player_input, zombie)

        while result == 'invalid':
            player_input = input('Try again (pistol, fist, shiv): ')
            result = pistol_fists_shiv(player_input, zombie)

        while result == 'tie':
            player_input = input('You tied, try again (pistol, fist, shiv): ')
            zombie = generate_zombie()
            result = pistol_fists_shiv(player_input, zombie)
            while result == 'invalid':
                player_input = input('Try again (pistol, fist, shiv): ')
                result = pistol_fists_shiv(player_input, zombie)
            
        if result == 'win':
            print_dramatic_text('You won this round!')
            item = level.get_random_item_from_current_location()
            print_dramatic_text(player.name + ' receives ' + item + ' from ' + level.current_location + '!')
            wins += 1
        if result == 'lose':
            health = player.take_damage()
            print_dramatic_text('You lost this round ... ' + player.name + '\'s health is ' + health)

    if wins == 3 and player.alive:
        print_dramatic_text(' Y O U   S U R V I V E D !')
    else:
        print_dramatic_text('Y O U   D I E D!')

