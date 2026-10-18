print("hi")
print("this is a quiz and i will make it extremely hard for you to solve.")
answer = input("are you ready to take the quiz? (yes/no):")
if answer.lower() == "no":
    print("too bad, you have to take the quiz anyway.💀💀💀")
else:
    print("great! let's get started.")

score = 0

answer = input("Question 1: 1 2 4 8 16 32 ? (type the next number in the sequence): ")
if answer.strip() == "64":
    print("correct!")
    score += 1
elif not answer.strip().isdigit():
    print("bro that's not even a number 😭")
else:
    print("incorrect. the correct answer is 64.")

print("i was going easy on you, but now it will get harder.")

answer = input("Question 2: 2, 3, 5, 9, 17, 33 (type the next number in the sequence): ")
if answer.strip() == "65":
    print("correct!")
    score += 1
elif not answer.strip().isdigit():
    print("-_-")
else:
    print("incorrect. the correct answer is 65.")

print("you are doing well, but now it will get even harder.")

answer = input("Question 3: 1, 1, 2, 6, 24, 120 (type the next number in the sequence): ")
if answer.strip() == "720":
    print("correct!")
    score += 1
elif not answer.strip().isdigit():
    print("nah how can you not even type a number💀💀💀?")
else:
    print("incorrect. the correct answer is 720.")  

print("Okay, no more boring sequences. Time for a real word puzzle!")

answer = input("Question 4: A farmer has both Chickens and Cows on his farm. "
               "Altogether, there are 10 heads and 28 legs. "
               "How many COWS does the farmer have?: ")

if answer.strip() == "4":
    print("correct!")
    print("how did you know that? you are a genius!")
    
    score += 1
elif not answer.strip().isdigit():
    print("level of ignorance is too high. you are not even trying to solve the puzzle.")
else:
    print("incorrect. the correct answer is 4.")

print("time for the ones i know you will lose on. this is the hardest question of all.")

answer = input("Question 5: name 4 digits of pi dont use decimal point: ")

if answer.strip() == "3141":
    print("correct!")
    score += 1
elif not answer.strip().isdigit():
    print("bro the answer isnt a banana. it is a number.")
else:
    print("incorrect. the correct answer is 3141.")

answer = input("Question 6: what is the square root of 144? ")
if answer.strip() == "12":
    print("correct!")
    score += 1 
elif not answer.strip().isdigit():
    print(f"bro the answer isnt ({answer}). it is a number.")
else:
    print("a third grade could answer this its 12.")

print(f"You got {score}/6 correct, which is {(score/6)*100}%!")

input("\nPress ENTER to close the game...") 
