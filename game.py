import random
guess=int(input("guess the number"))
num=random.randint(1,10)
if(num==guess):
        print("congratulation! u guessed the right answer")
else:
        print("try again! u guessed the wrong answer")