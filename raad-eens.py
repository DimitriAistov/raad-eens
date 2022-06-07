import random
print("Raad het getal tussen 1 en 1000") 
guess = -1 
ronde = 1 
score = 0 
while ronde <= 20: 
    print("Ronde " + str(ronde))
    nummer = random.randint(1,1000)
    kans = 1  
    while nummer != guess:
        guess = int(input(str(kans) + ": "))
        if guess < nummer:
            print("Hoger")
            if (nummer - guess) <= 20:
                print("Je bent heel warm")
            elif (nummer - guess) <= 50:
                print("Je bent warm")
        elif guess > nummer:
            print("Lager")
            if (guess - nummer) <= 20: 
                print("Je bent heel warm")
            elif (guess - nummer) <= 50:
                print("Je bent warm")
        else: 
            print("Correct")
            score = score + 1
        kans = kans + 1
        if kans > 10:
            break
    print("Het getal was " + str(nummer))
    if ronde >= 20:
        break  
    print("Score: " + str(score))
    print("Nog een getal raden? Ja/Nee")
    antwoord = input("")
    if not (antwoord == "Ja" or antwoord == "ja"):
        break
    ronde = ronde + 1
print("Einde!")
print("Uw eindscore is " + str(score))