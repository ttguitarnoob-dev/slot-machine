import random

print("Slot Machine!\n", "=" * 50, "\nHello, welcome to slot machine.  Enter credits to begin.  With each roll, your bet will be subtracted from your credits.  Your bet will be applied to your earnings only if you receive a bonus from your roll.  Otherwise, bet is lost. Scoring is as follows: ", "\n3 in a row: +10", "\n2 in a row: bet added", "\n🍒 = +1", "\n⭐ = +2", "\n🤖 = -1", "\n🌻 = 0", "\n🍄 = -3", "\n❄️ = -1", "\n3 in a row 🍄 = Earnings reset to 0\n", "=" * 50)


def play(starting_amount, starting_earnings):

    slide = ['🍒', '⭐', '🤖', '🌻', '🍄', '❄️']
    credits = starting_amount
    earnings = starting_earnings
    score = 0
    roll = int(bet())

    if roll > credits + earnings:

        print("Not enough credits, please add more.")
        credits = int(add_credits())

        if roll > credits:
            earnings -= roll - credits
            credits = 0
    else:   
        credits -= roll

    if credits < 0:
        credits = 0
        
    sl1 = slide[random.randint(0, 5)]
    sl2 = slide[random.randint(0, 5)]
    sl3 = slide[random.randint(0, 5)]
    roll_score = [sl1, sl2, sl3]
    print(roll_score)
    score = scoring(roll_score, roll)

    if score < -900:
        score = 0

    earnings += score

    if earnings < 0:
        earnings = 0

    print("Credits: ", credits)
    print('Earnings: ', earnings)
    play_again(credits, earnings)




def play_again(credits, earnings):
    play_again_ask = input("Roll again? (enter y or n) ")
    if play_again_ask == "y" or play_again_ask == "Y":
        play(credits, earnings)
    elif play_again_ask == "n":
        print("Thanks for playing, your total earning was", earnings)
        quit()
    else:
        print("Please say y or n")
        play_again(credits, earnings)


#Scoring
def scoring(roll, bet):
    score = 0
    for i in roll:
        if i == '🍒':
            score += 1
        elif i == '⭐':
            score += 2
        elif i == '🤖':
            score -= 1
        elif i == '🌻':
            score += 0
        elif i == '🍄':
            score -= 3
        elif i == '❄️':
            score -= 1
    if roll[0] == roll[1] and roll[0] == roll[2]:
        score += 10
        score += bet
        print("3 IN A ROW BONUS! +10 and bet will be added to score for this round")
    if roll[0] == roll[1] or roll[1] == roll[2]:
        score += bet
        print("2 IN A ROW BONUS!  Bet amount will be added to score for this round")
    
    if roll[0] == '🍄' and roll[1] == '🍄' and roll[2] == '🍄':
        score = -999
        print("Oh no!  You ate deadly mushrooms.  Earnings reset to 0")
    
    print("You scored a total of", score)
    return score

def bet():
    roll = input("How much would you like to bet? ")
    if roll.isdigit():
        return roll
    else:
        print("Please enter a number!")
        bet()

def add_credits():
    credits = input("How many credits would you like to add? ")
    if credits.isdigit():
        return credits
    else:
        print('Please enter a number!')
        add_credits()


credits = int(add_credits())
earnings = 0

play(credits, earnings)