import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import threading

# Initialize the speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice assistant's voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Use the second voice in the list

# Define a function to speak a message
def speak(message):
    engine.say(message)
    engine.runAndWait()

# Define a function to listen for a command
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # Calibrate the microphone for ambient noise levels
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio) # Use Google Speech Recognition to transcribe the audio
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return None

# Define a function to set a reminder
def set_reminder():
    speak("What would you like me to remind you about?")
    reminder = listen()
    if reminder is not None:
        speak("When would you like me to remind you?")
        time = listen()
        if time is not None:
            try:
                time_obj = datetime.datetime.strptime(time, "%H:%M")
                now = datetime.datetime.now()
                if now.time() < time_obj.time():
                    delay = (time_obj - now).seconds
                    speak("Okay, I will remind you about " + reminder + " in " + str(delay) + " seconds.")
                    reminder_timer = threading.Timer(delay, lambda: speak("Reminder: " + reminder))
                    reminder_timer.start()
                else:
                    speak("Sorry, that time has already passed.")
            except ValueError:
                speak("Sorry, I didn't understand the time. Please try again.")

# Define a function to create a to-do list
def create_todo_list():
    speak("What would you like to add to your to-do list?")
    item = listen()
    if item is not None:
        with open("todo.txt", "a") as f:
            f.write("- " + item + "\n")
        speak("Okay, I added " + item + " to your to-do list.")

# Define a function to search the web
def search_web():
    speak("What would you like to search for?")
    query = listen()
    if query is not None:
        url = "https://www.google.com/search?q=" + query
        webbrowser.open(url)
        speak("Here are the search results for " + query + ".")

# Define a main function to handle user commands
def main():
    speak("Hello, how can I help you?")
    while True:
        command = listen()
        if command is not None:
            if "remind me" in command:
                set_reminder()
            elif "to-do list" in command:
                create_todo_list()
            elif "search" in command:
                search_web()
            elif "exit" in command:
                speak("Goodbye.")
                break

if __name__ == "__main__":
    main()
