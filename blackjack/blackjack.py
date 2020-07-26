# ==============================================================================================================
# svg-cards.sourceforge.net created by David Bellot
# .png files are added into tkinter 8.6 if you are using the earlier version on tkinter then you need to use ppm files.
# the aim is for players to get a high score or higher total than dealer without going above the score of 21
# if the total value of the cards in a hand comes to more than 21 then the player is said to have bust or have busted and
# that is game over

#
# ==============================================================================================================

import random
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for eah suit retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = 'cards_png/cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # next the face cards
        for card in face_cards:
            name = 'cards_png/cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def dealer_frame():
    global dealer_card_frame
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)


def player_frame():
    global player_card_frame
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)


# =================================================
# till now we have placed all the widgets using the grid manager
# when it comes to adding the card images a pack manager is a much
# simpler one to use as you add new ones to the left
# its a very bad idea to mix grid and pack in the same window and Python 3
# compiler will give an error if you try but it is ok to use the pack manager in its own window
# now as every widget is a window packing the images into this frame is fine as long as
# we don't try to add anything else to the frame using grid now
# =================================================
def _deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)  # 0 here means that we want to pop the card from the top of the deck
    # add the image to a Label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list
    # Only one ace can have the value 11, and this will be reduce to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract: 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


# ==========================================================
# if you see player_hand is not complaining about the shadowing even though it is part of main program.
# that is because variable is defined as list and we can add items or remove items from the list but the list variable is not changing.
# ==========================================================
def deal_dealer():
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins")
    else:
        result_text.set("Draw!")


# ===================================================
# if you see player_hand is not complaining about the shadowing even though it is part of main program.
# that is because variable is defined as list and we can add items or remove items from the list but the list variable is not changing.


# THIS WHOLE SECTION IS FOR THE COMMENTED CODE

# when a global variable is used inside a function, Python is going to use the global variable as long as you don't
# assign a new value to it, but as soon as you add code that tries to change the value the variable itself becomes local
# and shadows the global variable with the same name. so in this case it assigns the value 0 to player_score variable.

# so if we are using the global variable's value and then trying to change the value of
# it will give error saying that unresolved reference variable.
# so here after removing the variable definition of player_score and using it in augmented assignment will also result into unresolved reference variable as
# the variable has to be initialised before using it in augmented assignment.

# so to tell Python that you want to use the global variable without shadowing and not making the variables local to that function anymore
# we use the global keyword with the global variable inside the function.
# ===================================================
def deal_player():
    # player_score = 0
    # global player_score
    # global player_ace
    #
    # card_value = deal_card(player_card_frame)[0]  # to return the face value of the card we are mentioning the element 0
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there is an ace and subtract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer Wins")
    # print(locals())  # locals() function can be used to find which variables are local in your function
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)

    if player_score > 21:
        result_text.set("Dealer Wins")


def initial_deal():
    deal_player()
    deal_dealer()


def reset_game():
    global deck

    dealer_hand.clear()
    player_hand.clear()
    player_score_label.set(0)
    dealer_score_label.set(0)
    result_text.set('')
    dealer_card_frame.destroy()
    player_card_frame.destroy()
    dealer_frame()
    player_frame()
    deck.clear()
    deck = list(cards)
    random.shuffle(deck)
    initial_deal()


def play():
    initial_deal()
    mainwindow.mainloop()


# __name__ = '__main__'

mainwindow = tkinter.Tk()

# set up the screen and frames for the dealer and player
mainwindow.title("Black Jack")
mainwindow.geometry("640x480")
mainwindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainwindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white', ).grid(row=1, column=0)

# ========================================================================
# embedded frame hold the card images
# grid and pack cannot work together if you uncomment the next line and comment out the other two
# you will get error.
# ========================================================================d
# dealer_card_frame = tkinter.Frame(card_frame, background='green').grid(row=0, column=1, sticky="ew", rowspan=2)
# dealer_card_frame = tkinter.Frame(card_frame, background='green')
# dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_frame()

player_score_label = tkinter.IntVar()
# =========================================
# variables defined in the main part of the program
# rather than in a function are called global variables
# variables that only exist inside a function are called local variables
# below variables are defined as global variable.
# refer the deal_player function's comment section

# we will not be using the below variables anymore as it may create conflict
# when they are used in some other functions.
# =========================================
# player_score = 0
# player_ace = False

tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

# embedded frame to hold the card images
# player_card_frame = tkinter.Frame(card_frame, background='green')
# player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
player_card_frame = tkinter.Frame(card_frame, background='green')
player_frame()

button_Frame = tkinter.Frame(mainwindow)
button_Frame.grid(row=3, column=0, columnspan=3, sticky='w')

# the function name has been assigned to the command parameter so that when the button is clicked the function is called
dealer_button = tkinter.Button(button_Frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)
# the function name has been assigned to the command parameter so that when the button is clicked the function is called
player_button = tkinter.Button(button_Frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)
# Reset game
reset_button = tkinter.Button(button_Frame, text='Reset Game', command=reset_game)
reset_button.grid(row=0, column=2)

# load cards
cards = []
load_images(cards)
print(cards)
# Create a new deck of cards and shuffle them
deck = list(cards)
# so if you want to use 3 packs of card then you need to append same list of cards
# deck = list(cards) + list(cards) + list(cards)

random.shuffle(deck)

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()


