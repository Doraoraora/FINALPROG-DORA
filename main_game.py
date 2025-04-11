import random
from gameplay import Map
from character import Character

rps = ['rock', 'paper', 'scissors']

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
    print()

def generate_zombie() -> str:
    result = rps[random.randint(0, 2)]
    return result

def rock_paper_scissors(player: str, zombie: str) -> str:
    if player == 'rock' and zombie == 'scissors':
        return 'win'
    if player == 'rock' and zombie == 'paper':
        return 'lose'
    if player == 'scissors' and zombie == 'paper':
        return 'win'
    if player == 'scissors' and zombie == 'rock':
        return 'lose'
    if player == 'paper' and zombie == 'rock':
        return 'win'
    if player == 'paper' and zombie == 'scissors':
        return 'lose'
    if player == zombie:
        return 'tie'
    return 'invalid'

if __name__ == '__main__':
    level = Map()
    player = Character("", 0, "")

    print_dramatic_text('Enter your character name. Leon is recommended for combat-heavy gameplay.')
    name = input()
    player.name = name

    print_dramatic_text ('On the night of September 30, 1998 two months after the events of Resident Evil, rookie police officer Leon S. Kennedy makes his way toward Raccoon City to start his first shift at the Raccoon City Police Department.')

    wins = 0
    while(wins < 3 and player.alive):
        level.current_location = random.choice(list(level.locations))
        print_dramatic_text('You enter the ' + level.current_location + ' ...')

        print_dramatic_text('A zombie appears!')
        zombie = generate_zombie()

        player_input = input('Enter rock, paper, or scissors: ')
        result = rock_paper_scissors(player_input, zombie)

        while result == 'invalid':
            player_input = input('Try again (rock, paper, scissors): ')
            result = rock_paper_scissors(player_input, zombie)

        while result == 'tie':
            player_input = input('You tied, try again (rock, paper, scissors): ')
            zombie = generate_zombie()
            result = rock_paper_scissors(player_input, zombie)
            while result == 'invalid':
                player_input = input('Try again (rock, paper, scissors): ')
                result = rock_paper_scissors(player_input, zombie)
            
        if result == 'win':
            print_dramatic_text('You won this round!')
            item = level.get_random_item_from_current_location()
            print_dramatic_text(player.name + ' receives ' + item + ' from ' + level.current_location + '!')
            wins += 1
        if result == 'lose':
            health = player.take_damage()
            print_dramatic_text('You lost this round ... ' + player.name + '\'s health is ' + health)

    if wins == 3 and player.alive:
        print_dramatic_text('congratulations, you survived!')
    else:
        print_dramatic_text('you died!')

