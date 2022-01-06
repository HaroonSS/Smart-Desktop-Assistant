'''
first import necessary modules ,

pip install pyttsx3
pip install speechRecognition
pip install wikipedia
pip install psutil
pip install pyautogui

'''
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import psutil  
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#function to speak given text
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#function to listen and recognize voice
def takeCommand():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")  
        # Recognizing speech using Google Speech Recognition  
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        #print("Please say that again ...") 
        speak("Please say that again ...")  
        return "None"
    return query


def greet_me():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("Your Jarvis Desktop Assistant here . Please tell me how can I help you")       

def about_myself():
    f = open("about_myself.txt", 'r')
    speak(f.read())
    speak("how can i help you sir")


#time function
def time():
    time = datetime.datetime.now().strftime("%H:%M:%S") 
    print(f"The current time is {time}")   
    speak("The current time is")
    speak(time)

#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print(f"The current date is {date} {month} {year}")
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def battery():
    
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))
    battery_left=time.strftime("%H:%M:%S", time.gmtime(battery.secsleft))
    print("Battery left : ", battery_left)

#screenshot function
def screenshot():
    img = pyautogui.screenshot()
    img.save( "C:\\Users\\HP\\OneDrive\\Pictures\\Screenshots\\ss.png" )

#joke function
def joke():
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)
    

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def open_app(query):

    if 'open google' in query  :
        speak("Opening google in chrome ...")
        webbrowser.open("https://www.google.com/")

    elif 'open youtube' in query:
        speak("Opening youtube...")
        webbrowser.open("https://www.youtube.com/")

    elif 'open gmail' in query:
        speak("Opening gmail...")
        webbrowser.open("https://www.gmail.com/")

    elif 'open whatsapp' in query:
        speak("Opening whatsapp...")
        os.startfile("C:\\Users\\HP\\AppData\\Local\\WhatsApp\\whatsapp.exe")

    elif 'open telegram' in query:
        speak("Opening telegram...")
        os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\telegram.exe")

    elif 'open visual studio' in query or 'open v s code' in query:
        speak("Opening visual studio code...")
        os.startfile("C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")

    elif 'open word' in query or 'open m s word' in query :
        speak("Opening word...")
        os.startfile('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"')

    elif 'open notepad' in query or 'open text editor' in query :
        speak("Opening notepad...")
        os.startfile("C:\\WINDOWS\\system32\\notepad.exe")

    elif 'open power point' in query:
        speak("Opening power point...")
        os.startfile('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"')

    elif 'open calculator' in query or 'open calci' in query :
        speak("Opening Calculator...")
        os.startfile('C:\\Windows\\System32\\calc.exe')

    elif 'open command prompt' in query or 'open cmd' in query:
        speak("Opening command prompt...")
        os.system("start cmd")

    elif 'pdf reader' in query or 'adobe' in query or 'acrobat reader' in query :
        speak("Opening adobe reader...")
        os.startfile('C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe')

    else:
        speak('sorry sir ! i dont understand , try again')
        print('sorry sir ! i dont understand , try again...')

def close_app(query):

    if 'close google' in query or 'close chrome' in query:
        speak("closing google in chrome...")
        os.system("taskkill /im chrome.exe /f")

    elif 'close whatsapp' in query:
        speak("closing whatsapp...")
        os.system("taskkill /im whatsapp.exe /f")

    elif 'close telegram' in query:
        speak("closing telegram...")
        os.system("taskkill /im telegram.exe /f")

    elif 'close visual studio' in query or 'close v s code' in query:
        speak("closing visual studio...")
        os.system("taskkill /im code.exe /f")

    elif 'close word' in query:
        speak("closing word...")
        os.system("taskkill /im winword.exe /f")

    elif 'close notepad' in query:
        speak("closing notepad...")
        os.system("taskkill /im notepad.exe /f")

    elif 'close power point' in query:
        speak("closing power point...")
        os.system("taskkill /im POWERPNT.exe /f")

    elif 'close command prompt' in query or 'close cmd' in query:
        speak("closing command prompt...")
        os.system("taskkill /im cmd.exe /f")

    elif 'close pdf reader' in query or 'close adobe' in query or 'close acrobat reader' in query :
        speak("closing adobe reader...")
        os.system("taskkill /im AcroRd32.exe /f")

    else:
        speak('sorry sir ! i don\'t understand , try again...')
        #print('sorry sir ! i don\'t understand , try again...')


if __name__ == "__main__":
    
    greet_me()
    
    while True:
    
        query = takeCommand().lower()

        if ('open' or 'start' or 'run') in query:
            query = query.replace("run", "open")
            query = query.replace("start", "open")
            open_app(query)

        elif 'close' in query:
            close_app(query)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'send email' in query:

            try:
                speak("What is the message for the email")
                content = takeCommand()
                to = 'reciever@xyz.com'
                send_email(to, content)
                speak("Email has been sent successfully")
                print("Email has been sent successfully.")
            except Exception as e:
                #print(e)
                speak("Unable to send email , try again")
                print("Unable to send email , try again")

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
        
        elif 'screenshot' in query:
            screenshot()

        elif 'battery' in query:
            battery()

        elif 'joke' in query:
            joke()

        elif 'sleep' in query or "don't listen" in query or 'stop listening' in query:
            speak("for how much time you want to stop me from listening commands")
            n = int(takeCommand()) or 30
            time.sleep(n)
            print(n)

        elif ('quit' in query or 'exit' in query or 'bye' in query or 'go offline ' in query):
              speak("okay sir , have a good day")
              print("okay sir , have a good day !")
              exit()

        elif ('about yourself' or 'who are you' or 'about you') in query:
            about_myself()

        #speak("next command sir")