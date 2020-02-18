import random


answer = random.randint(1, 100)
username = input("Hi there, What's your name?")


while True: # 무한반복
    print(username)
    guess = eval(input("Hi, "+ username + "guess the number: "))
    # eval 함수는 사용자가 입력한 형태 그대로, type을 평가하여 저장한다.

    if guess == answer:
        print("Correct! The answer was ", str(answer))
        break #함수 종료
    else:
        print("That's not what I wanted!!, Try again")