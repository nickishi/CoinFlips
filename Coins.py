'''
Created on Sep 27, 2019

@author: Nick
'''
import sys            #import sys used for exiting program. Random used for generating
import random         #0 or 1 to represent tails or heads, respectively.

gate1 = "yes"         #Initialization of variables used throughout the program.
gate2 = False
gate3 = False   
coin = int(0)
HeadsCheck = 1
CoinCounter = []

print("Welcome to the coin flip simulator.")
while gate1.lower() == "yes":                  #While loop to keep user in program.
    while gate2 == False:                      #While loop used to generate numbers
        coin = random.randint(0,1)             #until a condition is met.
        if coin == 0:                          #if elif used to check for tails or heads.
            print("Tails")
            CoinCounter.append(coin)
        elif coin == 1:
            print("Heads")
            CoinCounter.append(coin)
            while gate3 == False:                              
                if CoinCounter.count(1) == 8 or CoinCounter.count(0) == 9:
                    break                                      #while loop used to generate 3 possible heads.
                coin = random.randint(0,2)                     #Coin is flipped again. If it is tails, program
                if coin == 0:                                  #breaks from while loop. If it is heads, HeadsCheck
                    print("Tails")                             #counts the consecutive heads (1's). If HeadsCheck == 3,
                    CoinCounter.append(coin)                   #gate3 is set to True to break from loop and satisfying 
                    HeadsCheck = 1
                    break                                      #the 3 heads condition below. If 5 heads were rolled prior
                elif coin == 1:                                #and/or during gate3 while loop, 8 heads condition is
                    print("Heads")                             #also met, thus printing both sentences.
                    CoinCounter.append(coin)
                    HeadsCheck += 1
                    if HeadsCheck == 3:
                        gate3 = True
                        break
        if HeadsCheck == 3 or CoinCounter.count(1) == 8 or CoinCounter.count(0) == 9:
            print("Simulation Complete!")
            if HeadsCheck == 3:
                print("3 consecutive heads were flipped.")           #Prints proper sentence depending
            if CoinCounter.count(1) == 8:                            #on which condition is met.
                print("8 heads were flipped.")                       #only runs if at least one condition
            elif CoinCounter.count(0) == 9:                          #is met.
                print("9 tails were flipped.")
            gate2 = True
        
        gate3 = False
        coin = None
    print(CoinCounter)          #Prints list to show that the condition is actually met.
    gate1 = input("Would you like to run another simulation? (yes/no): ")
    if gate1.lower() == "yes": 
        coin = 0                                #Checks to see if user wants to continue. Yes continues
        HeadsCheck = 1                          #program and resets variables + list.
        gate2 = False                           #No or incorrect entry exits the program.
        gate3 = False
        CoinCounter.clear()
    elif gate1.lower() == "no":
        print("Goodbye!")
        sys.exit()
    else:
        print("Incorrect entry. System shutting down. Goodbye!")
        sys.exit()