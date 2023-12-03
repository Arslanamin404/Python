import pyttsx3

# The text you want to convert to speech
text = 'Hello World, My Admin is Mr. Mohammad Arsalan Rather'

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Say the specified text
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
