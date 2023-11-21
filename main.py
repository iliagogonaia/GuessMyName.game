import random
import time


computer = random.randint(1,100)
attempts = True
lives = 10
print("Lets Play Guess My Number Game!")
time.sleep(1)
print("You Have 10 Lives To Guess My Number!")
time.sleep(0.5)
print("Im Thinking Of Number From 1-100,Try To Guess It!")
while attempts:
    ricxvi = int(input("Enter Number:"))
    if ricxvi > 100:
        time.sleep(0.5)
        print("Choose Number From 1-100")
    elif ricxvi < computer:
        time.sleep(0.5)
        print("Try Higher Number")
        lives -=1
        time.sleep(0.5)
        print(f"You Have {lives} Lives Left!")
        time.sleep(0.5)
    elif ricxvi > computer and ricxvi < 100:
        time.sleep(0.5)
        print("Try Lower Number")
        time.sleep(0.5)
        lives-=1
        print(f"You Have {lives} Lives Left!")
    elif ricxvi == computer:
        time.sleep(0.5)
        print("You Won!")
        print(f"{computer} Is The Number I Was Thinking About!")
        attempts = False

    if lives == 0:
        print("You're out of Lives!")
        time.sleep(0.5)
        print("Game Over!")
        break




