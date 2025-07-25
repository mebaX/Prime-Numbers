from time import sleep

number = 2

while True:
    isItPrime = True
    for i in range(2, number):
        if number % i == 0:
            isItPrime = False
            break

    if isItPrime:
        print(number)
    sleep(0.01)
    number += 1

#asal