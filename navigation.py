import webbrowser as wb
import speech_recognition as sr

#wb.open('https://shimla.kvs.ac.in/')

#listener will listen your command and processing will held below


listener= sr.Recognizer()

#This is a function which will used below for taking command from user basically used in def program and inside that a variable store 
#command where this function is used


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
        #command lower is used to take the command from user in lowercase to prevent the error if occur in code that it will
        #not take any command in capital letters
            command = command.lower()
            
                
    except:
        pass
    return command



def program():
    command = take_command()

    print(command)


    #cmd is a variable which takes input from user
    cmd=(command)



   #This Code Will Navigate You To Google And Search What You've Searched For But It Will Not Open A Specific Website It Will Open Webpage
    
    if cmd in command:
        wb.open(command)

    #The Following Code will navigate you to directly website i.e line 35 to 43

    #if " kv shimla " in command:
    #    wb.open(command)   
    #    wb.open("https://shimla.kvs.ac.in/") 

    #elif 'youtube' in command:
    #   wb.open("https://www.youtube.com/")   

    #elif 'ncert' in command:
    #   wb.open("https://ncert.nic.in/")    



while True:
    program()
