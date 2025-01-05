import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(audio):
    """Speaks the provided text."""
    engine.say(audio)
    engine.runAndWait()

def wish_user():
    """Wishes the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you today?")

def take_command():
    """Listens for a command and returns the text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {query}")
        except Exception as e:
            print("Sorry, I couldn't understand. Can you say that again?")
            return None
    return query.lower()

def main():
    """Main function to handle commands."""
    wish_user()
    
    while True:
        query = take_command()
        if not query:
            continue

        # Functional commands
        if "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The current time is {current_time}")
            speak(f"The current time is {current_time}")
        
        elif "open youtube" in query:
            print("Opening YouTube...")
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")
        
        elif "open google" in query:
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.open("https://www.google.com")
        
        elif "play music" in query:
            music_dir = "C:\\Users\\nelly\\Music"  # Update this path
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                print(f"Playing {song}...")
                speak(f"Playing {song}...")
                os.startfile(os.path.join(music_dir, song))
            else:
                print("No songs found in your music directory.")
                speak("No songs found in your music directory.")
        
        elif "exit" in query or "quit" in query:
            print("Goodbye! Have a great day!")
            speak("Goodbye! Have a great day!")
            break
        
        else:
            print("Sorry, I can't do that yet.")
            speak("Sorry, I can't do that yet.")

# Run the assistant
if __name__ == "__main__":
    main()
