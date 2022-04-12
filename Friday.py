import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
     
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour<=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    speak("I am Friday Sir. How may I help you ?")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")    
        return "None"
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('qwertylove719@gmail.com','12345ayush@')
    server.sendmail('qwertylove719@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    if 1:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=5)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            webbrowser.open("https://gaana.com/")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\ayush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open game' in query:
            gamepath="C:\\GOG Games\\Prince of Persia The Two Thrones\\PrinceOfPersia.exe"
            os.startfile(gamepath)
        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content=takecommand()
                to="gauravrai54152@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry!The email has not been sent")


        