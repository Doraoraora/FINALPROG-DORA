from gameplay import Map
from character import Character

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
    print()

if __name__ == '__main__':
    player = Character("", 0, "")
    print_dramatic_text('WHICH STORY WOULD YOU LIKE TO BEGIN YOUR GAMEPLY WITH?' ' LEON(1) OR CLAIRE(2)')
    print_dramatic_text('FOR COMBAT-HEAVY GAMEPLAY, LEON IS RECOMMENDED. FOR STORY-BASED GAMEPLAY, CLAIRE IS RECOMMENDED')
    player_input = input()
    if input == 'LEON' or '1' or 'Leon':
        player = Character("Leon", 3, "Pistol")
        print_dramatic_text ('On the night of September 30, 1998 two months after the events of Resident Evil, rookie police officer Leon S. Kennedy makes his way toward Raccoon City to start his first shift at the Raccoon City Police Department.')
    if input == 'CLAIRE' or '1' or 'Claire':
        player = Character("Claire", 3, "Pistol")
        print_dramatic_text('You never thought that a zombie outbreak ')

    if player.name == 'Leon':
        print_dramatic_text('Leon falls down the sewer!')

