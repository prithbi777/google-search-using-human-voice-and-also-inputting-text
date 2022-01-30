import speech_recognition as sr
import pywhatkit
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source :
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate",140)
    print("\n\nGoogle Search :-\n")
    decide = "repeat"
    while (decide == "repeat"):
        print("1. Text Search!\n2. Voice Seach!")
        engine.say("for text search say enter and for voice search say listen...")
        engine.runAndWait()            
        print("listening...")
        engine.say("now say..")
        engine.runAndWait()
        audio = r.listen(source)
        choice = r.recognize_google(audio)
        if choice == "enter" :
            print("Text Search : \n")
            command = input("What are you looking for : ")
            pywhatkit.search(command)    
            print("If you want to continue to search then enter 'repeat' otherwise enter 'stop' :")
            decide = input("Now enter : ")
        elif choice == "listen" :
            engine.say("Just say what are you looking for...")
            engine.runAndWait()            
            print("listening...")
            engine.say("now say..")
            engine.runAndWait()
            audio = r.listen(source)
            choice = r.recognize_google(audio)
            pywhatkit.search(choice)            
            engine.say("If you want to continue to search then say repeat otherwise say stop...")
            engine.runAndWait()
            print("listening...")
            engine.say("now say..")
            engine.runAndWait()
            audio = r.listen(source)
            decide = r.recognize_google(audio)
        else :
            engine.say("couldn't understand what you say or type if you want to continue then say repeat otherwise say stop...")
            engine.runAndWait()            
            print("listening...")
            engine.say("now say..")
            engine.runAndWait()
            audio = r.listen(source)
            decide = r.recognize_google(audio)


    
engine.say("All right my friend see you again...")
engine.runAndWait()