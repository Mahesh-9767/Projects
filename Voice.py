import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You said: " + query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")

def assistant():
    speak("Hello!")
    
    while True:
        command = listen()

        if "stop" in command:
            speak("Goodbye!")
            break
        elif "hello" in command:
            speak("Hi there! How can I help?")
        elif "time" in command:
            current_time = get_time()
            speak(f"The current time is {current_time}")
        elif "date" in command:
            current_date = get_date()
            speak(f"Today's date is {current_date}")
        elif "search" in command:
            search_query = command.replace("search", "").strip()
            result = wikipedia.summary(search_query, sentences=2)
            speak(f"According to Wikipedia, {result}")
        else:
            speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    assistant()
