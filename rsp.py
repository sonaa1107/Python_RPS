import random


def get_choices():
    
    player_choice=input("Enter a choice (rock, paper, scissors:)")
    options=["rock","paper","scissors"]
    computer_choice= random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer,player_score,computer_score):
    print(f"You chose {player}, computer chose {computer}")
    if player==computer:
        result={"mssg":"It's a tie!","score":{"computer":computer_score+1,"you":player_score+1}}
        return result
    elif player=="rock":
        if computer=="scissors":
            result={"mssg":"Rock smashes scissors! You win!","score":{"computer":computer_score,"you":player_score+1}}
            return result
        else:
            result={"mssg":"Paper covers rock! You lose. ","score":{"computer":computer_score+1,"you":player_score}}
            return result
    elif player=="paper":
        if computer=='rock':
            result={"mssg":"Paper covers rock! You win! ","score":{"computer":computer_score,"you":player_score+1}}
            return result
        else:
            result={"mssg":"Scissor cuts paper! You lose.","score":{"computer":computer_score+1,"you":player_score}}
            return result
    else:
        if computer=='paper':
            result={"mssg": "Scissor cuts paper! You win!","score":{"computer":computer_score,"you":player_score+1}}
            return result
        else:
            result={"mssg":"Rock smashes scissors! You lose.","score":{"computer":computer_score+1,"you":player_score}}
            return result

comp_score=0
player_score=0
print("5 chances are there to win the game")
for i in range (5):
    choices=get_choices()
    result=check_win(choices["player"],choices["computer"],player_score,comp_score)
    player_score=result["score"]["you"]
    comp_score=result["score"]["computer"]
    print(result["mssg"])
    print(f"Score -> you: {player_score},computer: {comp_score}")

print("Thank you")
