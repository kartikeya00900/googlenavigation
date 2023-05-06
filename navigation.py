import webbrowser as wb
import speech_recognition as sr


listener= sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
                  
    except:
        pass
    return command

def program():
    command = take_command()
    print(command)
    cmd=(command)

    if cmd in command:
        prefix=("http:/")
        suffix=('.com')
        wb.open(prefix+cmd+suffix)
    else:
        program=='quit'

while True:
    program()
