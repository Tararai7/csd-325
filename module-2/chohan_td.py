# ============================================================
# Student Name: Tara Rai
# Assignment   : M3 (Module 3)
# Course       : CSD-325
# File         : chohan_td.py
# Date         : December 2025
# Description  : Modified Chō-Han dice game with:
#                - Initials prompt ("td: ")
#                - 12% house cut (was 10%)
#                - 10 mon bonus for rolling total 2 or 7
# ============================================================

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

NOTE: If you roll a total of 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print(f'You have {purse} mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('td: ').upper()  # ✅ Updated prompt: initials + colon
        if pot == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    # ✅ Bonus: 10 mon for rolling 2 or 7
    if total == 2 or total == 7:
        print(f'You rolled a {total}! Bonus: +10 mon!')
        purse += 10

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('td: ').upper()  # ✅ Also updated here
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[die1], '-', JAPANESE_NUMBERS[die2])
    print('    ', die1, '-', die2)

    # Determine if the player won:
    rollIsEven = (total % 2) == 0
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print(f'You won! You take {pot} mon.')
        purse += pot
        # ✅ Updated: 12% house fee (was 10%)
        house_fee = int(pot * 0.12)
        print(f'The house collects a {house_fee} mon fee (12%).')
        purse -= house_fee
    else:
        purse -= pot
        print('You lost!')

    # Check if the player has run out of money:
    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()