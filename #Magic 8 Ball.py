#Magic 8 Ball
#Michael Hein
#1/22/24 

#Functions 
import random
responseslist= ["Of Course",
            "Yes",
            "No",
            "Not Gonna Happen",
            "Ask Again Later",
            "Maybe",
            "Don't count on it",
            "I'd put my rent on that",
            "Sure",
            "Definatly Not"]

def eightball(): 
    response = random.choice(responseslist)
    question = input("Ask a yes or no question ending in a ?") 
    if question.endswith("?"):
        print(response) 
        
    else: 
        print("Please ask a question ending in a ?")
        eightball() 
    repeat=str(input("Do you want to ask another question(y)or quit(q)"))
    if repeat=="y": 
        eightball() 
    if repeat=="q": 
        print("Thank you for playing Magic 8 Ball") 

eightball()

    


    
