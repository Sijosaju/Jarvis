import pyttsx3
import speech_recognition as sr

def speak(text):
    if text:  # Only try to speak if there's actual text
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate', 174)
        engine.say(text)
        engine.runAndWait()
    else:
        print("Nothing to speak")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            print("recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            print("No speech detected within timeout")
            return ""
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""

# Main execution
while True:
    text = takecommand()
    if text:
        speak(text)
    if "exit" in text:  # Add a way to exit the loop
        speak("Goodbye")
        break
