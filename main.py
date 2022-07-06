
import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def blackjack():
    print(logo)
    answered=input("Respond with 'y' to start or 'n' to quit")
    if answered=="y":
        user_cards = []
        computer_cards = []
        
        is_done=False
        for _ in range(2):
            user_cards.append(random.choice(deal_card()))
            computer_cards.append(random.choice(deal_card()))
            
        
        #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
        #and returns the score. 
        def calculate_score(cards):
            score=sum(cards)
            if 11 in cards and score==21:
                return 0
            else:
                if score>21 and 11 in cards:
                    cards.remove(11)
                    cards.append(1)
                    score=sum(cards)
                return score
        #Look up the sum() function to help you do this.
        
        #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        while not is_done:        
            print(f"{user_cards}, {computer_cards}")
            computer_score=calculate_score(computer_cards)
            user_score=calculate_score(user_cards)
            #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
            if user_score>21 or computer_score==0:
                print(f"Your cards are{user_cards} an score is {user_score}.\n Computer cards are{computer_cards} and score is {computer_score}.\n You lose")
                blackjack()
                is_done=True
            elif user_score<21 and computer_score<21:
                answer=input("respond with a 'y' to pick a card: ").lower()
                if answer=='y':
                    user_cards.append(random.choice(deal_card()))
                    user_score=calculate_score(user_cards)
                    if user_score==21 or user_score==0:
                        print(f"Your cards are{user_cards} an score is {user_score}.\n Computer cards are{computer_cards} and score is {computer_score}.\n You win")
                    elif user_score==computer_score:
                        print("You draw")
                    elif user_score>computer_score and user_score<21:
                        print(f"Your cards are{user_cards} an score is {user_score}.\n Computer cards are{computer_cards} and score is {computer_score}.")
                        answer=input("respond with a 'y' to tell the deler to pick a card: ").lower()
                        if answer=='y':
                            computer_cards.append(random.choice(deal_card()))
                            computer_score=calculate_score(computer_cards)
                            if computer_score>21:
                                print(f"Your cards are{user_cards} an score is {user_score}.\n Computer cards are{computer_cards} and score is {computer_score}.\n You win")
                            else:
                                print(f"Your cards are{user_cards} an score is {user_score}.\n Computer cards are{computer_cards} and score is {computer_score}.")
                                
                            
                        
                    else:
                        print(f"Your cards are{user_cards} an score is {user_score}.\n Computer cards are{computer_cards} and score is {computer_score}.\n You lose")
                        is_done=True
                        blackjack()
                    
                    
            






    else:
        print("Thank you for trying out the game")
blackjack()

