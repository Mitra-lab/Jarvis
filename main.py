import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser as wb
import os
import smtplib
import psutil#pip install pysutil
import pyjokes#pip install pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")
        
    speak("I am Jarvis Mam Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hardcoregirl693@gmail.com', 'mitra4596')
    server.sendmail('hardcoregirl693@gmail.com', to, content)
    server.close()

def cpu():
    usgae=str(psutil.cpu_percent())
    speak("cpu is at "+usage)

    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open quora' in query:
            webbrowser.open("quora.com")   


        elif 'play music' in query:
            webbrowser.open("spotify.com") 

        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'open notepad' in query:
            codePath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(codePath)

        elif 'go offline' in query:
            quit()

        
        elif 'send email' in query:
            try:
                speak("Tell the receiver email correctly")
                to=(input("Enter the email here: "))
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Mam.I am not able to send this email")

        elif 'search in chrome' in query:
            speak('What sould I search?')
            chromepath="C:\\Users\\M & V\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            search =takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'cpu' in query:
            cpu()

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif "remember that" in query:
            speak("What should I Remember?")
            data=takeCommand()
            speak("you said me to remember"+date)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember=open("data.txt","r")
            speak("you said me to remember that"+remember.read())

        elif 'jokes' in query:
            jokes()
        
