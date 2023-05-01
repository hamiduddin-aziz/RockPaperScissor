# project 3 Rock paper scissor
import random
userScore = 0
comScore = 0
rounds = 0
go = ["r","p","s"]
while userScore < 3 and comScore < 3:
    user_input = input("type R for Rock, P for Paper, S for Scissors and Q to quit. ").lower()
    comPick = random.randint(0,2)
    if user_input == "q":
        print( "Your score is ",userScore," and computer score is ", comScore," out of ", rounds," rounds.")
        break

    elif user_input == "r" and go[comPick] == "s":
        print("User pick:", user_input, ". Computer pick:", go[comPick], "User win.")
        userScore +=1
        rounds += 1

    elif user_input == "p" and go[comPick] == "r":
        print("User pick:", user_input, ". Computer pick:", go[comPick], "User win.")
        userScore += 1
        rounds += 1

    elif user_input == "s" and go[comPick] == "p":
        print("User pick:", user_input, ". Computer pick:", go[comPick], "User win.")
        userScore +=1
        rounds += 1

    elif user_input == "r" and go[comPick] == "p":
        print("User pick:", user_input, ". Computer pick:", go[comPick], "Computer win.")
        comScore +=1
        rounds += 1

    elif user_input == "p" and go[comPick] == "s":
        print("User pick:", user_input, ". Computer pick:", go[comPick], "Computer win.")
        comScore +=1
        rounds += 1

    elif user_input == "s" and go[comPick] == "r":
        print("User pick:", user_input, ". Computer pick:", go[comPick], "Computer win.")
        comScore +=1
        rounds += 1

    elif user_input == go[comPick]:
        print("User pick:",user_input,". Computer pick:",go[comPick],"its a tie")
        rounds +=1

    else:
        print("Try again")

print("User: ", userScore, ", Computer: ",comScore, " out of ", rounds, " rounds.")
if userScore > comScore:
    print("User Win")
elif userScore > comScore:
    print("Computer Win")
else:
    print("Goodbye")
