import random
print("Choose a number")
print("rock=1\n"+"scissor=2\n"+"Paper=3")
print("Close the game=30")
while True:
    choice_player=int(input())
    #choice2_pc=random.randint(1,3)
    choice2_pc =3
    if choice_player==30:
        break

    rock=1
    scissor=2
    Paper=3
    x=["rock","scissor","Paper"]

    def win():
        results()
        print("you won")
    def tie():
        results()
        print("it is a tie")
    def lose():
        results()
        print("you lost")
    def results():
        print(x[choice_player-1]+" "+"vs"+" "+x[choice2_pc-1])

    outcome=choice_player-choice2_pc
    if outcome ==-1 or outcome==2:
        win()
    elif outcome==0:
        tie()
    else:lose()
