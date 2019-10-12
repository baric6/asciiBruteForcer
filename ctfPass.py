#ascii password generator
#using python andaconda
#TO EXECUTE -> $pythonw ctfPass.py
#by joe hollon

import random
import time

#open and read a file to lazy to rename
#open_file = open("bsaicWords.txt", "r")
#stri= ""
#sum = 0
#for line in open_file:
#    stri+=line 
#word_stri = stri.split()
#open_file.close()

#first attempt(FAILED)
#method 1 string 
#this takes the list word_stri adds up all letters ascii value if true prints out the word 
#that fits the bill
#i made a list of all english word with "S" as the second number i assumed it was all captial 
#because of the ascii value of 83
#but didnt find a result
#for word in word_stri:
#    if len(word) == 10:
#        wordsum = ord(word[0]) + ord(word[1]) + ord(word[2]) + ord(word[3]) 
#        + ord(word[4])+ ord(word[5]) + ord(word[6]) + ord(word[7]) + ord(word[8]) + ord(word[9])
#        if wordsum ==  1000:
#            print(word)
#            print("true")
            
            
#second try           
#method 2 random number way(ascii) 
#set up a random number generator that took the ascii values 65-122 randomly picked the range
count = 0  
sum = 83  
sumList = []
#this loop automates me running the program a billion times    
while True: 
    
    #reset result
    result = 0 
    #always append 83 to the begening of the list
    sumList.append(83)
    
    #if sum is 1000 or count is less then 9
    #append the random number to the list
    #TODO take out the sum meaningless right now
    while sum <= 1000 and count < 9:
        r = random.randint(65, 122)
        sumList.append(r)
        count +=1
        
    #dont work true never gets executed
    #loop never stops
    #TODO need fix
    if result == 1000:
        print("\n==============================================\n")
        print(sumList)
        print(result)
        print("\n==============================================\n")
        break
    else: 
        #sum up all values in list
        print(sumList)
        for sym in sumList:
            result += sym
        print(result)
        #clear list for next increment
        sumList.clear()
        #set counter to 0 so second loop to execute took me forever to figure out  
        count = 0
     
    #tell me when at the bottom of outerLoop 
    print("outer loop") 
    #need this here to slow down the loop or i will get the same random numbers in list
    time.sleep(1)          