#quizz avec functions

from functions import quizz

quizz1 = quizz(5)
quizz1.begin()

while quizz1.remain() != 0:
    
    answer1 = input("What is the colour of the white horse of Napoléon ?")
    solution1 = "white"
    while answer1 != solution1 and quizz1.status() == "alive":
        quizz1.wrong()
        if quizz1.status() == "alive":
            answer1 = input("What is the colour of the white horse of Napoléon ?")
    if quizz1.status() == "dead":
        break
    
    print("Yep yep, time to reveal the next question !")
    answer2 = input("How many hair does Thanos have ?")
    solution2 = "0"
    while answer2 != solution2 and quizz1.status() == "alive":
        quizz1.wrong()
        if quizz1.status() == "alive":
            answer2 = input("How many hair does Thanos have ?")
    if quizz1.status() == "dead":
        break

    print("Okay big boy, let's see if you are a legend of this game !")
    answer3 = input("We are going to die before Luffy becomes the Pirates' King : yes (y) or no (n) ?")
    solution3 = "y"
    while answer3 != solution3 and quizz1.status() == "alive":
        quizz1.wrong()
        if quizz1.status() == "alive":
            answer3 = input("We are going to die before Luffy becomes the Pirates' King : yes (y) or no (n) ?")
    if quizz1.status() == "dead" or answer3 == solution3:
        break

quizz1.endgame()