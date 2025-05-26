import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    """Speak out the given text."""
    engine.say(text)
    engine.runAndWait()

# Initialize the recognizer for voice input
recognizer = sr.Recognizer()

def listen():
    """Listen to the user's voice and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def process_command(command):
    """Process the recognized command and take action."""
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What do you want to search?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here is what I found for {query}")
    elif command:
        speak("Sorry, I didn't understand that command.")

def main():
    """Main loop of the assistant."""
    speak("Hi! I am your voice assistant.")
    while True:
        command = listen()
        process_command(command)

if __name__ == "__main__":
    main()
