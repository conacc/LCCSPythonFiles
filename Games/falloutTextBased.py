import random
import csv


choice = int(input("Do you want to play Singleplay(1), Simulation(2) or Multiplayer(3)?: "))
if choice == 1:
    print("Welcome to Fallout New Vegas, the text based version. In this game your goal is to explore the different areas and get revenge on the man who shot you, Benn! Good luck!")
    enter = input("Press enter to start")
    name = input("What's your name? ")
    print("Nice to meet you! Go on and explore the house if you want or go on and get out there")

    items = 0
    outside = 0
    enemys_killed = 0
    caps = 0
    flee = 0
    
    while outside == 0:
        action = input("What do you wanna do? Search or leave? ")
        if action == "search" or  action == "Search":
            if items == 0:
                print("You search the house for anything you can use. You find a stimpack and a gun")
                items = 1
                inventory = ["Stimpack","Gun"]
            elif items == 1:
                print("You already searched everything")
                
        elif action == "leave" or action == "Leave":
            print("You go to the outside world")
            outside = 1
            
        else:
            print("I didn't understand that")
            
    explore = 0
    print("You stand outside the docs house")
    while explore == 0:
        action = input("To the south stands the Saloon, beside it is the shop or you can leave the town to explore. Go to Saloon, Go to shop or leave the town?: ")
        
        if action == "saloon" or  action == "Saloon":
            print("You go inside the saloon")          
        elif action == "shop" or action == "Shop":
            print("You go to the shop")
        elif action == "leave" or action == "Leave":
            explore = 1
        else:
            print("I didn't understand that")

    def goodsprings():
        explore = 0
        
        while explore == 0:
            action = input("To the south stands the Saloon, beside it is the shop or you can leave the town to explore. Go to Saloon, Go to shop or leave the town?: ")
        
        
            if action == "saloon" or  action == "Saloon":
                print("You go inside the saloon")
                saloon = input("Look around or leave?: ")
                
               
            elif action == "shop" or action == "Shop":
                print("You go to the shop")
                

            
            elif action == "leave" or action == "Leave":
                explore = 1
        
            else:
                print("I didn't understand that")

    print("You stand outside the town of Goodsprings.")


    while explore == 1:
        action = input("Explore the wasteland or go back to Goodsprings?: ")

        if action == "goodsprings" or action == "Goodsprings":
            goodsprings()
        
        def choice():
            print("You encouter an enemy")
            choice = input("What do you wanna do? Attack or flee?: ")
            if choice == "attack" or choice == "Attack":
                print("You attack and kill the enemy!")
                global enemys_killed
                enemys_killed = enemys_killed + 1
                caps_gained = random.randint(1,50)
                print("You got",caps_gained,"caps")
                global caps
                caps = caps + caps_gained
            elif choice == "flee" or choice == "Flee":
                print("You run away from the enemy!")
                global flee
                flee = flee + 1
        
        if action == "explore" or action == "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Primm")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found a good item")
            elif success % 5 == 0:
                print("You found a junk item")
            elif success % 10 == 0:
                print("You found a junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        print("You stand in Primm")
        action = input("Leave and explore the wastes?: ")
        if action == "leave" or action == "Leave":
            explore = 1
            
        else:
            print("I didn't understand that")

    def primm():
        explore = 0
        while explore == 0:
            print("You stand in Primm")
            action = input("Leave and explore the wastes?: ")
            if action == "leave" or action == "Leave":
                explore = 1
            
            
            else:
                print("I didn't understand that")
                
    while explore == 1:
        action = input("Explore the wasteland, go back to Goodsprings or go back to Primm?: ")
        action.upper

        if action == "GOODSPRINGS":
                goodsprings()
            
        elif action == "PRIMM":
                primm()
        
        elif action == "EXPLORE":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Novac")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
        else:
            print("I didn't understand that")

    while explore == 0:
        action = input("Leave to the wastes?: ")
        if action == "leave" or action == "Leave":
            explore = 1
            
    def novac():
        explore = 0       
        while explore == 0:
            action = input("Leave to the wastes?: ")
            if action == "leave" or action == "Leave":
                explore = 1 
            
    while explore == 1:
        action = input("Explore the wasteland, go back to Goodsprings, go back to Primm or go back to Novac?: ")

        if action == "goodsprings" or action == "Goodsprings":
                goodsprings()
            
        elif action == "primm" or action == "Primm":
                primm()
                
        elif action == "novac" or action == "Novac":
                novac()
        
        elif action == "explore" or "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Boulder City")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        action = input("Go to the inside the ruined city or leave to the wastes?: ")
        if action == "leave" or action == "Leave":
            explore = 1
                
    def boulderCity():
        explore = 0       
        while explore == 0:
            action = input("Go to the funny dinosaur or leave to the wastes?: ")
            if action == "leave" or "Leave":
                explore = 1
                    
    while explore == 1:
        action = input("Explore the wasteland, go back to Goodsprings, go back to Primm, back to Novac or Boulder City?: ")

        if action == "goodsprings" or action == "Goodsprings":
                goodsprings()
            
        elif action == "primm" or action == "Primm":
                primm()
                
        elif action == "novac" or action == "Novac":
                novac()
                
        elif action == "boulder city" or action == "Boulder City":
                boulderCity()
        
        elif action == "explore" or "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found New Vegas")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")
            
    while explore == 0:
        action = input("Enter New Vegas or leave back to the wastes: ")
        if action == "leave" or action == "Leave":
            explore = 1
        elif action == "enter" or action == "Enter":
            print("You enter the New Vegas strip")
            action = input("Enter the Tops Casino or leave the strip?: ")
            if action == "enter" or action == "Enter":
                benny = 1
                while benny == 1:
                    print("At the back of the casino stands Benny")
                    action = input("Kill Benny, talk to Benny or leave: ")
                    if action == "kill" or action == "Kill":
                        print("You kill him dead")
                        benny = 0
                        end = 1
                        explore = 1

    def newvegas():
        explore = 0
        while explore == 0:
            action = input("Enter New Vegas or leave back to the wastes: ")
            if action == "leave" or action == "Leave":
                explore = 1
            
            elif action == "enter" or action == "Enter":
                print("You enter the New Vegas strip")
                action = input("Enter the Tops Casino or leave the strip?: ")
                if action == "enter" or action == "Enter":
                    while benny == 1:
                        print("At the back of the casino stands Benny")
                        action = input("Kill Benny, talk to Benny or leave: ")
                        if action == "kill" or action == "Kill":
                            print("You kill him dead")
                            benny = 0
                            explore = 1
                                 
    if end == 1:
        print("Congrats you did it!")
        print("In the end you killed", enemys_killed,"enemies, fled",flee,"times and got",caps," caps")
        record = [enemys_killed,caps,flee]
        file = open("results.csv","a",newline="")
        r = csv.writer(file)
        r.writerow(record)
        file.close()
        print("New Record added to CSV")


elif choice == 2:
    print("Intro stuff")
    print("Npc talk placeholder")

    items = 0
    outside = 0
    enemys_killed = 0
    flee = 0
    caps = 0
    benny = 1

    while outside == 0:
        print("What do you wanna do? Search or leave? ")
        action = random.randint(1,2)
        if action == 1:
            if items == 0:
                print("You search the house for anything you can use. You find a stimpack and a gun")
                items = 1
                inventory = ["Stimpack","Gun"]
            elif items == 1:
                print("You already searched everything")
                
        elif action == 2:
            print("You go to the outside world")
            outside = 1
            
        else:
            print("I didn't understand that")
            
            
    explore = 0
    print("You stand outside the docs house")
    while explore == 0:
        print("To the south stands the Saloon, beside it is the shop or you can leave the town to explore. Go to Saloon, Go to shop or leave the town?: ")
        
        action = random.randint(1,3)
        if action == 1:
            print("You go inside the saloon")          
        elif action == 2:
            print("You go inside the shop")                
        elif action == 3:
            print("You leave and the town")
            explore = 1
        else:
            print("I didn't understand that")

    def goodsprings():
        explore = 0
        
        while explore == 0:
            print("To the south stands the Saloon, beside it is the shop or you can leave the town to explore. Go to Saloon, Go to shop or leave the town?: ")
            action = random.randint(1,3)
            if action == 1:
                print("You go inside the saloon")          
            elif action == 2:
                print("You go inside the shop")                
            elif action == 3:
                print("You leave and the town")
                explore = 1
            else:
                print("I didn't understand that")

    print("You stand outside the town of Goodsprings.")

    def choice():
            print("You encouter an enemy")
            ("What do you wanna do? Attack or flee?: ")
            choice = random.randint(1,2)
            if choice == 2:
                print("You attack and kill the enemy!")
                global enemys_killed
                enemys_killed = enemys_killed + 1
                caps_gained = random.randint(1,50)
                print("You got",caps_gained,"caps")
                global caps
                caps = caps + caps_gained
            elif choice == 1:
                print("You run away from the enemy!")
                global flee
                flee = flee + 1

    while explore == 1:
        print("Explore the wasteland or go back to Goodsprings?: ")

        action = random.randint(1,2)
        
        if action == 1:
            goodsprings()
        
        elif action == 2:
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Primm")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        print("You stand in Primm")
        print("Go to the Vikki and Vance Casino(1)? Or leave and explore the wastes(2)?: ")
        action = random.randint(1,2)
        if action == 2:
            explore = 1
        
        elif action == 1:
            print("You stand in Vikki and Vance Casino")
            
        else:
            print("I didn't understand that")

    def primm():
        explore = 0
        while explore == 0:
            print("You stand in Primm")
            print("Go to the Vikki and Vance Casino(1)? Or leave and explore the wastes(2)?: ")
            action = random.randint(1,2)
            if action == 2:
                explore = 1
        
            elif action == 1:
                print("You stand in Vikki and Vance Casino")
            
            else:
                print("I didn't understand that")

                
    while explore == 1:
        print("Explore the wasteland, go back to Goodsprings or go back to Primm?: ")
        action = random.randint(1,3)

        if action == 2:
                goodsprings()
            
        elif action == 3:
                primm()
        
        elif action == 1:
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Novac")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        print("Go to the funny dinosaur or leave to the wastes?: ")
        action = random.randint(1,2)
        if action == 2:
            explore = 1
        elif action == 1:
            print("You stand in the dinosaur statue")
            
    def novac():
        explore = 0       
        while explore == 0:
            print("Go to the funny dinosaur or leave to the wastes?: ")
            action = random.randint(1,2)
            if action == 2:
                explore = 1
            elif action == 1:
                print("You stand in the dinosaur statue")
            
    while explore == 1:
        print("Explore the wasteland, go back to Goodsprings, go back to Primm or go back to Novac?: ")
        action = random.randint(1,4)
        if action == 2:
                goodsprings()
            
        elif action == 3:
                primm()
                
        elif action == 4:
                novac()
        
        elif action == 1:
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Boulder City")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        print("Go to the inside the ruined city or leave to the wastes?: ")
        action = random.randint(1,2)
        if action == 2:
            explore = 1
        elif action == 1:
            print("You stand in the ruins of boulder city")
                
    def boulderCity():
        explore = 0       
        while explore == 0:
            print("Go to the inside the ruined city or leave to the wastes?: ")
            action = random.randint(1,2)
            if action == 2:
                explore = 1
            elif action == 1:
                print("You stand in the ruins of boulder city")
            
    while explore == 1:
        print("Explore the wasteland, go back to Goodsprings, go back to Primm, back to Novac or Boulder City?: ")
        action = random.randint(1,5)
        if action == 2:
                goodsprings()
            
        elif action == 3:
                primm()
                
        elif action == 4:
                novac()
                
        elif action == 5:
                boulderCity()
        
        elif action == 1:
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found New Vegas")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")
            
    while explore == 0:
        print("You enter the New Veas strip")
        print("At the back of the casino stands Benny")
        print("You kill him dead")
        end = 1
        explore = 1

    
    if end == 1:
        print("Congrats you did it!")
        print("In the end you killed", enemys_killed,"enemies, fled",flee,"times and got",caps," caps")
        #header = ["Enemies killed", "Caps", "Times fled"]
        record = [enemys_killed,caps,flee]
        file = open("results.csv","a",newline="")
        #table = csv.writer(file)
        #table.writerow(header)
        r = csv.writer(file)
        r.writerow(record)
        file.close()
        print("New Record added to CSV")
        
        
elif choice == 3:
    print("Welcome to Fallout New Vegas, the text based version. In this game your goal is to explore the different areas and get revenge on the man who shot you, Benn! Good luck!")
    enter = input("Press enter to start")
    name = input("What's your name? ")
    print("Nice to meet you! Go on and explore the house if you want or go on and get out there")

    items = 0
    outside = 0
    enemys_killed = 0
    caps = 0
    flee = 0
    
    while outside == 0:
        action = input("What do you wanna do? Search or leave? ")
        if action == "search" or  action == "Search":
            if items == 0:
                print("You search the house for anything you can use. You find a stimpack and a gun")
                items = 1
                inventory = ["Stimpack","Gun"]
            elif items == 1:
                print("You already searched everything")
                
        elif action == "leave" or action == "Leave":
            print("You go to the outside world")
            outside = 1
            
        else:
            print("I didn't understand that")
            
    explore = 0
    print("You stand outside the docs house")
    while explore == 0:
        action = input("To the south stands the Saloon, beside it is the shop or you can leave the town to explore. Go to Saloon, Go to shop or leave the town?: ")
        
        if action == "saloon" or  action == "Saloon":
            print("You go inside the saloon")          
        elif action == "shop" or action == "Shop":
            print("You go to the shop")
        elif action == "leave" or action == "Leave":
            explore = 1
        else:
            print("I didn't understand that")

    def goodsprings():
        explore = 0
        
        while explore == 0:
            action = input("To the south stands the Saloon, beside it is the shop or you can leave the town to explore. Go to Saloon, Go to shop or leave the town?: ")
        
        
            if action == "saloon" or  action == "Saloon":
                print("You go inside the saloon")
                saloon = input("Look around or leave?: ")
                
               
            elif action == "shop" or action == "Shop":
                print("You go to the shop")
                

            
            elif action == "leave" or action == "Leave":
                explore = 1
        
            else:
                print("I didn't understand that")

    print("You stand outside the town of Goodsprings.")


    while explore == 1:
        action = input("Explore the wasteland or go back to Goodsprings?: ")

        if action == "goodsprings" or action == "Goodsprings":
            goodsprings()
        
        def choice():
            print("You encouter an enemy")
            choice = input("What do you wanna do? Attack or flee?: ")
            if choice == "attack" or choice == "Attack":
                print("You attack and kill the enemy!")
                global enemys_killed
                enemys_killed = enemys_killed + 1
                caps_gained = random.randint(1,50)
                print("You got",caps_gained,"caps")
                global caps
                caps = caps + caps_gained
            elif choice == "flee" or choice == "Flee":
                print("You run away from the enemy!")
                global flee
                flee = flee + 1
        
        if action == "explore" or action == "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Primm")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found a good item")
            elif success % 5 == 0:
                print("You found a junk item")
            elif success % 10 == 0:
                print("You found a junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        print("You stand in Primm")
        action = input("Go to the Vikki and Vance Casino? Or leave and explore the wastes?: ")
        if action == "leave" or action == "Leave":
            explore = 1
            
        else:
            print("I didn't understand that")

    def primm():
        explore = 0
        while explore == 0:
            print("You stand in Primm")
            action = input("Go to the Vikki and Vance Casino? Or leave and explore the wastes?: ")
            if action == "leave" or action == "Leave":
                explore = 1
            
            
            else:
                print("I didn't understand that")
                
    while explore == 1:
        action = input("Explore the wasteland, go back to Goodsprings or go back to Primm?: ")

        if action == "goodsprings" or action == "Goodsprings":
                goodsprings()
            
        elif action == "primm" or action == "Primm":
                primm()
        
        elif action == "explore" or "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Novac")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                print("You encouter an enemy")
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        action = input("Go to the funny dinosaur or leave to the wastes?: ")
        if action == "leave" or action == "Leave":
            explore = 1
            
    def novac():
        explore = 0       
        while explore == 0:
            action = input("Go to the funny dinosaur or leave to the wastes?: ")
            if action == "leave" or action == "Leave":
                explore = 1 
            
    while explore == 1:
        action = input("Explore the wasteland, go back to Goodsprings, go back to Primm or go back to Novac?: ")

        if action == "goodsprings" or action == "Goodsprings":
                goodsprings()
            
        elif action == "primm" or action == "Primm":
                primm()
                
        elif action == "novac" or action == "Novac":
                novac()
        
        elif action == "explore" or "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Boulder City")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        action = input("Go to the inside the ruined city or leave to the wastes?: ")
        if action == "leave" or action == "Leave":
            explore = 1
                
    def boulderCity():
        explore = 0       
        while explore == 0:
            action = input("Go to the funny dinosaur or leave to the wastes?: ")
            if action == "leave" or "Leave":
                explore = 1
                    
    while explore == 1:
        action = input("Explore the wasteland, go back to Goodsprings, go back to Primm, back to Novac or Boulder City?: ")

        if action == "goodsprings" or action == "Goodsprings":
                goodsprings()
            
        elif action == "primm" or action == "Primm":
                primm()
                
        elif action == "novac" or action == "Novac":
                novac()
                
        elif action == "boulder city" or action == "Boulder City":
                boulderCity()
        
        elif action == "explore" or "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found New Vegas")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")
            
    while explore == 0:
        action = input("Enter New Vegas or leave back to the wastes: ")
        if action == "leave" or action == "Leave":
            explore = 1
        elif action == "enter" or action == "Enter":
            print("You enter the New Vegas strip")
            action = input("Enter the Tops Casino or leave the strip?: ")
            if action == "enter" or action == "Enter":
                benny = 1
                while benny == 1:
                    print("At the back of the casino stands Benny")
                    action = input("Kill Benny, talk to Benny or leave: ")
                    if action == "kill" or action == "Kill":
                        print("You kill him dead")
                        benny = 0
                        end = 1
                        explore = 1

    def newvegas():
        explore = 0
        while explore == 0:
            action = input("Enter New Vegas or leave back to the wastes: ")
            if action == "leave" or action == "Leave":
                explore = 1
            
            elif action == "enter" or action == "Enter":
                print("You enter the New Vegas strip")
                action = input("Enter the Tops Casino or leave the strip?: ")
                if action == "enter" or action == "Enter":
                    while benny == 1:
                        print("At the back of the casino stands Benny")
                        action = input("Kill Benny, talk to Benny or leave: ")
                        if action == "kill" or action == "Kill":
                            print("You kill him dead")
                            benny = 0
                            explore = 1
                                 
    if end == 1:
        print("Congrats",name, " you did it!")
        print("In the end you killed", enemys_killed,"enemies, fled",flee,"times and got",caps," caps")
        #header = ["Enemies killed", "Caps", "Times fled"]
        record = [enemys_killed,caps,flee]
        file = open("results.csv","a",newline="")
        #table = csv.writer(file)
        #table.writerow(header)
        r = csv.writer(file)
        r.writerow(record)
        file.close()
        print("New Record added to CSV")
        
    
    print("Welcome to Fallout New Vegas, the text based version. In this game your goal is to explore the different areas and get revenge on the man who shot you, Benn! Good luck!")
    enter = input("Press enter to start")
    name = input("What's your name? ")
    print("Nice to meet you! Go on and explore the house if you want or go on and get out there")

    items = 0
    outside = 0
    enemys_killed = 0
    caps = 0
    flee = 0
    
    while outside == 0:
        action = input("What do you wanna do? Search or leave? ")
        if action == "search" or  action == "Search":
            if items == 0:
                print("You search the house for anything you can use. You find a stimpack and a gun")
                items = 1
                inventory = ["Stimpack","Gun"]
            elif items == 1:
                print("You already searched everything")
                
        elif action == "leave" or action == "Leave":
            print("You go to the outside world")
            outside = 1
            
        else:
            print("I didn't understand that")
            
    explore = 0
    print("You stand outside the docs house")
    while explore == 0:
        action = input("To the south stands the Saloon, beside it is the shop or you can leave the town to explore. Go to Saloon, Go to shop or leave the town?: ")
        
        if action == "saloon" or  action == "Saloon":
            print("You go inside the saloon")          
        elif action == "shop" or action == "Shop":
            print("You go to the shop")
        elif action == "leave" or action == "Leave":
            explore = 1
        else:
            print("I didn't understand that")

    def goodsprings():
        explore = 0
        
        while explore == 0:
            action = input("To the south stands the Saloon, beside it is the shop or you can leave the town to explore. Go to Saloon, Go to shop or leave the town?: ")
        
        
            if action == "saloon" or  action == "Saloon":
                print("You go inside the saloon")
                saloon = input("Look around or leave?: ")
                
               
            elif action == "shop" or action == "Shop":
                print("You go to the shop")
                

            
            elif action == "leave" or action == "Leave":
                explore = 1
        
            else:
                print("I didn't understand that")

    print("You stand outside the town of Goodsprings.")


    while explore == 1:
        action = input("Explore the wasteland or go back to Goodsprings?: ")

        if action == "goodsprings" or action == "Goodsprings":
            goodsprings()
        
        def choice():
            print("You encouter an enemy")
            choice = input("What do you wanna do? Attack or flee?: ")
            if choice == "attack" or choice == "Attack":
                print("You attack and kill the enemy!")
                global enemys_killed
                enemys_killed = enemys_killed + 1
                caps_gained = random.randint(1,50)
                print("You got",caps_gained,"caps")
                global caps
                caps = caps + caps_gained
            elif choice == "flee" or choice == "Flee":
                print("You run away from the enemy!")
                global flee
                flee = flee + 1
        
        if action == "explore" or action == "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Primm")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found a good item")
            elif success % 5 == 0:
                print("You found a junk item")
            elif success % 10 == 0:
                print("You found a junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        print("You stand in Primm")
        action = input("Go to the Vikki and Vance Casino? Or leave and explore the wastes?: ")
        if action == "leave" or action == "Leave":
            explore = 1
            
        else:
            print("I didn't understand that")

    def primm():
        explore = 0
        while explore == 0:
            print("You stand in Primm")
            action = input("Go to the Vikki and Vance Casino? Or leave and explore the wastes?: ")
            if action == "leave" or action == "Leave":
                explore = 1
            
            
            else:
                print("I didn't understand that")
                
    while explore == 1:
        action = input("Explore the wasteland, go back to Goodsprings or go back to Primm?: ")

        if action == "goodsprings" or action == "Goodsprings":
                goodsprings()
            
        elif action == "primm" or action == "Primm":
                primm()
        
        elif action == "explore" or "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Novac")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                print("You encouter an enemy")
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        action = input("Go to the funny dinosaur or leave to the wastes?: ")
        if action == "leave" or action == "Leave":
            explore = 1
            
    def novac():
        explore = 0       
        while explore == 0:
            action = input("Go to the funny dinosaur or leave to the wastes?: ")
            if action == "leave" or action == "Leave":
                explore = 1 
            
    while explore == 1:
        action = input("Explore the wasteland, go back to Goodsprings, go back to Primm or go back to Novac?: ")

        if action == "goodsprings" or action == "Goodsprings":
                goodsprings()
            
        elif action == "primm" or action == "Primm":
                primm()
                
        elif action == "novac" or action == "Novac":
                novac()
        
        elif action == "explore" or "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found Boulder City")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")

    while explore == 0:
        action = input("Go to the inside the ruined city or leave to the wastes?: ")
        if action == "leave" or action == "Leave":
            explore = 1
                
    def boulderCity():
        explore = 0       
        while explore == 0:
            action = input("Go to the funny dinosaur or leave to the wastes?: ")
            if action == "leave" or "Leave":
                explore = 1
                    
    while explore == 1:
        action = input("Explore the wasteland, go back to Goodsprings, go back to Primm, back to Novac or Boulder City?: ")

        if action == "goodsprings" or action == "Goodsprings":
                goodsprings()
            
        elif action == "primm" or action == "Primm":
                primm()
                
        elif action == "novac" or action == "Novac":
                novac()
                
        elif action == "boulder city" or action == "Boulder City":
                boulderCity()
        
        elif action == "explore" or "Explore":
            success = random.randint(1,100)
            if success % 3 == 0:
                print("You found New Vegas")
                explore = 0
            elif success % 2 == 0:
                choice()
            elif success % 1 == 0:
                choice()
            elif success % 4 == 0:
                choice()
            elif success % 9 == 0:
                print("You found good item")
            elif success % 5 == 0:
                print("You found junk item")
            elif success % 10 == 0:
                print("You found junk item")
            elif success % 6 == 0:
                choice()
            elif success % 7 == 0:
                choice()
            elif success % 8 == 0:
                print("You found a good item")
                
        else:
            print("I didn't understand that")
            
    while explore == 0:
        action = input("Enter New Vegas or leave back to the wastes: ")
        if action == "leave" or action == "Leave":
            explore = 1
        elif action == "enter" or action == "Enter":
            print("You enter the New Vegas strip")
            action = input("Enter the Tops Casino or leave the strip?: ")
            if action == "enter" or action == "Enter":
                benny = 1
                while benny == 1:
                    print("At the back of the casino stands Benny")
                    action = input("Kill Benny, talk to Benny or leave: ")
                    if action == "kill" or action == "Kill":
                        print("You kill him dead")
                        benny = 0
                        end = 1
                        explore = 1

    def newvegas():
        explore = 0
        while explore == 0:
            action = input("Enter New Vegas or leave back to the wastes: ")
            if action == "leave" or action == "Leave":
                explore = 1
            
            elif action == "enter" or action == "Enter":
                print("You enter the New Vegas strip")
                action = input("Enter the Tops Casino or leave the strip?: ")
                if action == "enter" or action == "Enter":
                    while benny == 1:
                        print("At the back of the casino stands Benny")
                        action = input("Kill Benny, talk to Benny or leave: ")
                        if action == "kill" or action == "Kill":
                            print("You kill him dead")
                            benny = 0
                            explore = 1
                                 
    if end == 1:
        print("Congrats",name," did it!")
        print("In the end you killed", enemys_killed,"enemies, fled",flee,"times and got",caps," caps")
        #header = ["Enemies killed", "Caps", "Times fled"]
        record = [enemys_killed,caps,flee]
        file = open("results.csv","a",newline="")
        #table = csv.writer(file)
        #table.writerow(header)
        r = csv.writer(file)
        r.writerow(record)
        file.close()
        print("New Record added to CSV")
else:
    print("I didn't understand that")
