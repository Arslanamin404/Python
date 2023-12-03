import gtts
import playsound

text = input("Enter text: ") #we can also read text file

textToSpeach = gtts.gTTS(text, lang="en")
textToSpeach.save("textToSpeach.mp3")
playsound.playsound("textToSpeach.mp3")
