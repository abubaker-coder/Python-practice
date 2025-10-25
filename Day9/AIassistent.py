import speech_recognition as sr
import openai
import wikipedia as wp
import os
import pyttsx3
import datetime
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
 

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=1, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak('I did not hear anything, please try again.')
            return "none"
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        speak('Sorry, I did not catch that. Please say again...')
        return "none"
    except sr.RequestError:
        speak('Network error. Please check your internet connection.')
        return "none"
    
    return query


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you")



if __name__ == '__main__':
    wish()
    if 1:
        query = takecommand().lower()


        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("cmd")

        elif "open camera" in query:
            cap = cv2.videocapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()