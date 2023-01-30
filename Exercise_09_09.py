import random


def main():
    # Create a deck of cards
    deck = create_deck()

    # Get the number of cards to deal
    num_cards = int(input('How many cards to deal? '))

    # Play game
    play_game(deck, num_cards)


def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs
    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
            '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
            '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
            '10 of Diamonds': 10, 'Jack of Diamonds': 10,
            'Queen of Diamonds': 10, 'King of Diamonds': 10}

    return deck


def play_game(deck, number):
    # Initialize accumulator variables
    player1_pts, player1_cards = deal_cards(deck, number)
    player2_pts, player2_cards = deal_cards(deck, number)

    if player1_pts >= 21 and player2_pts >= 21:
        display(player1_pts, player1_cards, player2_pts, player2_cards)
        print('Result: No Winner')
    elif player1_pts >= 21:
        display(player1_pts, player1_cards, player2_pts, player2_cards)
        print('Result: Player 2 Wins!')
    elif player2_pts >= 21:
        display(player1_pts, player1_cards, player2_pts, player2_cards)
        print('Result: Player 1 Wins!')
    else:
        display(player1_pts, player1_cards, player2_pts, player2_cards)
        print(f'Player 1 was dealt with:\n{player1_cards}\nPlayer 2 was dealt with:\n{player2_cards}')


def deal_cards(deck, number):
    # Initialize accumulator for the hand values
    hand_value = 0
    cards = ''
    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck
    if number > len(deck):
        number = len(deck)

    # Deal the cards and accumulate their values
    for count in range(number):
        card = random.choice(list(deck))
        cards += card + '\n'
        if card[:3] == 'Ace':
            if (hand_value + 11) > 21:
                hand_value += deck[card]
            else:
                hand_value += 11
        else:
            hand_value += deck[card]

    # Return hand value
    return hand_value, cards


def display(player1_pts, player1_cards, player2_pts, player2_cards):
    print(f'\nPlayer 1 - Hand Value: {player1_pts}')
    print(f'-------------------------\n{player1_cards}')
    print(f'Player 2 - Hand Value: {player2_pts}')
    print(f'-------------------------\n{player2_cards}')


# Call the main function
if __name__ == '__main__':
    main()
