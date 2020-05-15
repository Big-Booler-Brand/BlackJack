import random

class Player():
    def __init__(self, cash=0, name='', hand=[], bet=0, blackjack=False):
        self.cash = 0
        self.name = ''
        self.originalname = ''
        self.hand = []
        self.isasplit = False
        self.bet = 0
        self.blackjack = False
class Card():
    def __init__(self):
        self.suit = ''
        self.rank = ''
        self.value_hard = 0
        self.value_soft = 0
    def getCard(self):
        return self.rank + " of " + self.suit
class Deck():
    def __init__(self):
        self.stack = []
        self.created_size = 0
        self.standard_size = 52
    def size(self):
        return len(self.stack)
class Table():
    def __init__(self):
        self.players = []
        self.deck = 0
        self.dealprogression = 0

table = Table()

def setup():
    global table

    print('Welcome to the Blackjack table')
    dealer = Player()
    dealer.name = 'Dealer'
    table.players.append(dealer)

    print('How many players?')
    playernum = 0
    while playernum == 0:
        playernum = int(input())
        if playernum < 1:
            print('You need at least 1 player.')
            playernum = 0
    i = 0
    while i < playernum:
        print('Please input name for player', i + 1)
        new_player = Player()
        new_player.name = str(input())
        table.players.append(new_player)
        i += 1
    print("Thanks")
    print("Please select how many decks (ACR uses 6, some casinos use 8 or 4)")
    deck_num = int(input())
    table.deck = newdeck(deck_num)

    print('How much money will players start with?')
    startcash = int(input())
    print('You will have $' + startcash + ' to begin, good luck')
    i = 0
    for player in table.players:
        if player.name != 'Dealer':
            player.cash = startcash

def newdeck(n = 1):

    suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
    ranks = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    hard_values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soft_values = [1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    std_deck = Deck()
    finaldeck = Deck()

    card_data = zip(ranks, hard_values, soft_values)

    for i in suits:
        for j in card_data:
            newCard = Card()
            newCard.suit = i
            newCard.rank = j[0]
            newCard.value_hard = j[1]
            newCard.calue_soft = j[2]
            std_deck.stack.append(newCard)

    std_deck.size = len(std_deck.stack)

    finaldeck.stack = std_deck.stack * n
    finaldeck.created_size = len(finaldeck.stack)
    random.shuffle(finaldeck.stack)
    return finaldeck

def deal():
    global table

    if table.dealprogression != 0 and table.deck.size() < 26:
        print('Deck needs to be reshuffled')
        table.deck = newdeck(deck.created_size / deck.standard_size)

    playerCount = len(table.players)
    i = 0
    for player in table.players:
        player.hand.append(table.deck.stack.pop(i))
        table.dealprogression += 1
        player.hand.append(table.deck.stack.pop(i + playerCount - table.dealprogression))
        if value(player.hand) == 21:
            player.blackjack = True

    def hit(cards):
        global table
        cards.append(table.deck.stack.pop(0))
        print('Hit results in ', cards[-1].getCard())

    def doubledown(player):
        player.cash = player.cash - player.bet
        player.bet = player.bet * 2
        print('You have doubled down, your bet is now $', player.bet)
        hit(player.hand)
        print('Your cards are:')
        for item in player.hand:
            print(item.getCard())
        print('The value is now', value(player.hand))
        if value(player.hand) > 21:
            print("You lose by bust!")

    def surrender(player):
        print('You have surrendered... Pussy')
        player.cash += player.bet / 2
        print('you sacrificed $', player.bet/2, 'to withdraw')

    def resolve():
        global table
        def win(player, con = ''):
            if con == 'bust':
                print('Dealer busts! You win!')
                print('You win $', str(player.bet))
                player.cash += 2 * player.bet
            elif con == 'BJ':
                print('Blackjack! You lucky bastard!')
                print('Payout is 1.5, you win $', str((3. / 2) * player.bet))
                player.cash += (5. / 2) * player.bet
            else:
                print('You won!')
                print('You win $', str(player.bet))
                player.cash += 2 * player.bet
        def lose(player):
            print('You lost! You forfeit your bet of $', str(player.bet))
        def push(player):
            print('Push! Nobody wins or loses money')
            player.cash += player.bet

        dealer = table.player[0]
        player_list = []
        for player in table.players:
            if player.name != 'Dealer':
                player_list.append(player)

        print('To continue, type [ok]')
        check = ''
        while check != 'ok':
            check = raw_input()
            if check != 'ok'
                print('You MUST type in [ok] to continue')

        print('--------------------------------------------------------')

        allbust = True
        for player in player_list:
            if value(player.hand) <= 21
                allbust = False
        if allbust == True:
            print('All players busted, Dealer takes cheeks!')
        else:
            print('Dealer reveals his other card:')
            print(dealer.hand[0].getcard(),"\n")
            print('The value of his hand is', value(dealer.hand), '\n')
            if dealer.blackjack == True:
                print('Dealer has blackjack, get fucked kid')
            while value(dealer.hand) <17:
                print('Dealer hits until reaching or exceeding 17')
                hit(dealer.hand)
                print('Dealer is now at', value(dealer.hand))


            for player in player_list:
                print('\nResults for' + player.name)
                if value(player.hand) > 21:
                    print(player.name + ' busted')
                    lose(player)
                elif value(dealer.hand) > 21:
                    win(player, 'bust')
                elif dealer.blackjack:
                    if player.blackjack:
                        push(player)
                    else: lose(player)
                else:
                    if player.blackjack:
                        win(player, 'BJ')
                    elif value(player.hand) > value(dealer.hand):
                        win(player)
                    elif value(player.hand) < value(dealer.hand):
                        lose(player)
                    else:
                        push(player)

        done_list = []
        for player in player_list:
            if player.isasplit:
                done_list.append(player)
                for player_obj in player_list:
                    if player.originalname == player_obj.originalname
                        player_obj.cash += player.cash
            elif player.originalname:
                player.name = player.originalname
        for item in done_list:
            table.players.remove(item)

    def split(player):
        global table
        print('\n\n\nSplit: you now play as if you had two hands, and your bet is doubled to cover.')
        player.cash -= player.bet

        split_ghost = Player()
        split_ghost.name = player.name + """'s 2nd split hand"""
        split_ghost.originalname = player.name
        split_ghost.isasplit = True
        split_ghost.bet = player.bet
        split_ghost.hand.append(player.hand.pop(1))

        print('You will now play your first hand')
        hit(player.hand)
        player_action(player)

        print('You will now play your second hand')
        hit(split_ghost.hand)
        player_action(split_ghost)

        i = table.players.index(player) + 1
        table.players.insert(i, split_ghost)
        player.originalname = player.name
        player.name = player.name + """'s 1st split hand"""

    def main():
        global table
        setup()
        xyzzy = 0
        while xyzzy == 0:
            print('You must bet before the deal.\n')
            for player in table.players:
                if player.name == 'Dealer':
                    continue
                print(player.name, ": You must bet. What is your wager?")
                while player.bet == 0:
                    player.bet = int(input('Enter your bet: $'))
                    if player.bet > player.cash:
                        print('You bet too much, cannot bet this amount')
                        player.bet = 0
                player.cash -= player.bet

            deal()

            print('\nThe Dealer shows', table.players[0].hand[1].getCard(),'\n')

            for player in table.players:
                if player.name == 'Dealer'
                    continue
                if player.isasplit == True
                    continue
                print('Action is to the player')
                print('Player must check by typing [ok]')
                check = ''
                while check != 'ok':
                    check = input()
                    if check != 'ok':
                        print('You MUST type in [ok] to continue')
                player_action(player)
            resolve()
            xyzzy = playagain()
        print('Thanks for playing nerd!')
        return 0
    def playagain():
        global table
        done_list = []
        for i in range(1, len(table.players)):
            yn = ''
            while yn == '':
                player = table.players[i]
                print('Player has $', player.cash, ' available to bet')
                print('Would you like to play again? [y/n]')
                yn = raw_input()
                if yn == 'y':
                    player.bet = 0
                    player.hand = []
                    player.blackjack = False
                    player.splitbet = 0
                    player.splithand = []
                elif yn == 'n':
                    print('Thank you for playing')
                    done_list.append(table.players[i])
                else:
                    print('Please input [y] or [n] only.')
                    yn = ''

        table.players[0].hand = []
        table.players[0].blackjack = False
        table.dealprogression = 0
        for item in done_list:
            table.players.remove(item)
        if len(table.players) == 1:
            return 1
        else:
            return 0
    def int(input(n='', input_message = '(Enter a whole number): ', error_message = 'Use numbers only fuckwad: ')):
        import string
        n = input(input_message)
        while n.isdigit() == False:
            n = input(error_message)
        return int(n)

    def value(cards):

        total = [0]
        for card in cards:
            if card.value_hard == card.value_soft:
                total = [i + card.value_hard for i in total]
            else:
                soft_totals = [i + card.value_soft for i in total]
                hard_totals = [i + card.value_hard for i in total]
                total = soft_totals + hard_totals
        if min(total) > 21:
            return min(total)
        else:
            total = filter(lambda x: x <= 21, total)
            return max(total)

    def player_action():
        global table
        cardslist = ''
        for item in player.hand:
            while len(cardslist) != 0:
                cardslist += ', '
                break
            cardslist += item.getCard()

        print('\nyour cards are:', cardslist)
        print('Your hand value is', value(player.hand))

        if player.hand[0].rank == player.hand[1].rank:
            splitCheck = True
        else:
            splitCheck = False

        decision = 0
        while decision = 0:
            decision = decisiontree(player, split = splitCheck)
            if decision == 1:
                hit(player.hand)
                cardslist = ''
                for item in player.hand:
                    while len(cardslist) != 0:
                        cardslist += ', '
                        break
                    cardslist += item.getCard()
                print('Your cards are now:', cardslist)
                print('Your hand value is', value(player.hand))
                if value(player.hand) == 21:
                    print('You should stand.')
                    decision = 0
                elif value(player.hand) > 21:
                    print('You busted! Loser!')
                    break
                else:
                    decision = 0

            elif decision == 2:
                print('Player has elected to stand')
                if player != table.players[-1]:
                    print('Play now passes to next player')
                break
            elif decision == 3:
                if player.bet > player.cash - player.bet:
                    print('You cannot double down you broke fuck.')
                    decision = 0
                else:
                    doubledown(player)
                    break
            elif decision == 4:
                yn = ''
                while yn == '':
                    print("""Surrender: Gives up half your bet and retires the hand.""")
                    print('Are you sure?')
                    yn = input()
                    if yn == 'y':
                        surrender(player)
                        break
                    elif yn == 'n':
                        decision =0
                    else:
                        print('Please input [y] or [n] only.')
                        yn = ''
            elif decision == 5 and splitCheck == True:
                split(player)
            else:
                decision = 6

    def decisiontree(player, decision = 0, split = False):
        def option_text(n = 2):
            option_list = ['1 to hit', '2 to stand', '3 to double down', '4 to surrender', '5 to split']
            str = ''
            for i in range(len(option_list)):
                while i < n:
                    str = str + option_list[i]
                    break
            print('Press ' + str + '.')

        firstpass = False
        if len(player.hand) == 2:
            firstpass = True

        decision = 0
        while decision == 0:
            if split == True:
                option_text(n = 5)
                decision = int(input('z', input_message = 'Please enter 1 thru 5: '))
                if decision > 5:
                    print('1 thru 5 only.')
            elif firstpass == True:
                    option_text(n = 4)
                    decision = int(input('z', input_message = 'Please enter 1 thru 4: '))
                    if decision > 4:
                        print('1 thru 4 only, learn to read dick.')
            else:
                option_text(n = 2)
                decision = int(input('z', input_message = 'Please enter 1 or 2: '))
                if decision > 2:
                    print('Illiterate fuck. 1 or 2!')

        return decision

main()
