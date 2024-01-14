import sys

import speech_recognition as sr
from gtts import gTTS
import playsound
import os
recognizer = sr.Recognizer()
#generate audio from text (google text-to-speach API)
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")

#simple command processing test, will later integrate with OpenAi API
def process_command(text):
    # Process the command here and return a response
    # For example, a simple greeting
    if 'hello' in text.lower():
        return "Hello, how can I help you?"
    elif 'what is your name' in text.lower():
        return "I am your voice assistant big daddy Sav."
    elif 'ok goodbye' in text.lower():
        return 'thank you goodbye'
    else:
        return "Sorry, I didn't understand that."



# Running the voice assistant
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)

            response = process_command(text)
            speak(response)

            if response == 'thank you goodbye':
                print('program exiting...')
                break
        except sr.UnknownValueError:
            print("I could not understand audio")
            speak("I didn't get that, could you please repeat?")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("I'm having trouble connecting to the server.")

sys.exit()