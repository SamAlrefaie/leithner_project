import pickle
from datetime import datetime
from datetime import  timedelta
from tkinter import END  
#listofcards = []
file = open('totoalcards2', 'rb')
listofcards = pickle.load(file)
file.close()
CurrentDate = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f")

class card(object):
    def __init__(self, word, meaning , boxnumber , timeofreview):
        self.word = word
        self.meaning = meaning
        self.boxnumber = boxnumber
        self.timeofreview = timeofreview 

# Defining a function for making a list of flashcards
    def flashcard( flash , word, meaning , boxnumber , timeofreview):        
        flash.append([word, meaning , boxnumber, timeofreview])
        return flash

def new_word():
    global listofcards
#    y = input("for adding a flashcard, press Y/y : ")
 #   while  y == 'y' or y == 'Y':
    word = input("Word you want to add to your Flashcards: ")
    meaning = input("Meaning of the word in flashcard: ")
    boxnumber = 0
    timeofreview = datetime.strptime( str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f")
    listofcards =  card.flashcard(listofcards, word, meaning , boxnumber , timeofreview)
#            y = input("for adding another flashcard, press Y/y :")
    file = open('totoalcards1', 'wb')
    pickle.dump(listofcards, file)
    file.close()
    
def practice():
    file = open('totoalcards1', 'rb')
    listofcards = pickle.load(file)
    file.close()
    for ele in listofcards :
        if CurrentDate  > ele[3] and ele[2] != 6 :
           print(ele[0])
           x = input("enter the meaning : ")
           if x == ele[1] :
                if int(ele[2]) == 0 :
                    ele[2] = 1
                    ele[3] = CurrentDate + timedelta(seconds= 10)
                    print("Correct!! Now the Flashcard will be moved to next box (box number 1)")
                elif int(ele[2]) == 1 :
                    ele[2] = 2
                    ele[3] = CurrentDate + timedelta(seconds= 20)
                    print("Correct!! Now the Flashcard will be moved to next box (box number 2)")
                elif int(ele[2]) == 2 :
                    ele[2] = 3
                    ele[3] = CurrentDate + timedelta(seconds= 40)
                    print("Correct!! Now the Flashcard will be moved to next box (box number 3)")
                elif int(ele[2]) == 3 :
                    ele[2] = 4
                    ele[3] = CurrentDate + timedelta(seconds= 60)
                    print("Correct!! Now the Flashcard will be moved to next box (box number 4)")
                elif int(ele[2]) == 4 :
                    ele[2] = 5
                    ele[3] = CurrentDate + timedelta(seconds= 80)
                    print("Correct!! Now the Flashcard will be moved to next box (box number 5)")
                elif int(ele[2]) == 5 :
                    ele[2] = 6
                    ele[3] = CurrentDate + timedelta(seconds= 10)
                    print("congratulations!!! you have memorised this Word!!!! ")
           else:
             ele[2] = 0
             ele[3] = CurrentDate
             print("wrong!! Now the Flashcard will be moved to first box ")
    else :
        print("No more Words to review or now! come back later ;) ")      
    listofcards2 = []
    def modify():
        for item in listofcards:
            #print(item)
            listofcards2.append(item)
            file = open('totoalcards2', 'wb')
            pickle.dump(listofcards2, file)    
            file.close()
    modify()  
    file = open('totoalcards1', 'wb')
    pickle.dump(listofcards, file)
    file.close()
    
def start():
    z= input("Hi ,to add a new word type:' new ' to practice , type ' p '  and to quit type: 'q': ")
    if z == 'new' :
        new_word()
    elif z == 'p' :
        practice()
    elif z=='q' :
        END
    else:
        start()

#start()
#new_word()
practice()
