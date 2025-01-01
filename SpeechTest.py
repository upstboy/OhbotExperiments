from ohbot import ohbot
import speech_recognition as sr

# Initialize Ohbot first
ohbot.init()


def speak_with_expression(text):
    ohbot.say(text, True, True)

# Add speech recognition to get the name
def get_name():
    # Initialize recognizer
    r = sr.Recognizer()
    
    ohbot.say("What is your name?", True, True)
    
    # Listen for input using microphone
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source, timeout=10)
            name = r.recognize_google(audio)
            print(f"Recognized name: {name}")
        except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
            name = "friend"
    return name

# Main interaction
name = get_name()
speak_with_expression(f"Hello, {name}. Nice to meet you!")