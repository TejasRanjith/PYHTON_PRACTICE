import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate",160)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        exit()
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:                           #for playing song
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:                         #for checking time
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif "hello" in command:                        #just a simple simulation
        talk("Hi, how can i help you ?")
    elif "what can you do" in command:              #just a frequent question
        import time
        talk("one moment please")
        time.sleep(3)
        talk("I can play some songs, which you want, ")
    elif "open my app" in command:                  #just to run my app
        import os
        talk("opening your app, open important websites")
        os.startfile("C://Users//home//Desktop//Python Stuff//CORTANA CMDs//Open important websites.py")
    elif 'who is' in command:                       #just a search a thing in wikipedia
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:                         #just a command to make jokes
        talk(pyjokes.get_joke())
    elif 'google' in command:                       #just to search google
        import webbrowser
        google = command.replace('google',"")
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=' + google)
    elif 'what is' in command:                      #just to search google
        import webbrowser
        google = command.replace('what is',"")
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=' + google)
    elif 'thank you' in command:                    #just a question
        talk("Your welcome. See you later !")
        exit()
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
