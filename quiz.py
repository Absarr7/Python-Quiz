print("Welcome to my Quiz")

playing = input("Do you want to play the game?: ")

if playing.lower() != "yes":
    quit()
    
print("Okay!! Let's play :)")

score = 0

answer1 = input("What does RAM stands for?\n")
if answer1.lower() == "random access memory":
    print("Correct!")
    score +=1
else: print("Incorrect!")

answer2 = input("What does CPU stands for?\n")
if answer2.lower() == "central processing unit":
    print("Correct!")
    score +=1
else: print("Incorrect!")

answer3 = input("What does PSU stands for?\n")
if answer3.lower() == "power supply unit":
    print("Correct!")
    score +=1
else: print("Incorrect!")

answer4 = input("What does GPU stands for?\n")
if answer4.lower() == "graphics processing unit":
    print("Correct!")
    score +=1
else: print("Incorrect!")

answer5 = input("What invented bulb?\n")
if answer5.lower() == "thomas edison":
    print("Correct!")
    score +=1
else: print("Incorrect!")

answer6 = input("Who is the CEO of google?\n")
if answer6.lower() == "sundar pichai":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
print(f"You got {str(score)} questions correct!")
print(f"You got {str((score/6)*100)}% questions correct!")