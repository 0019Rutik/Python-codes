import speech_recognition as sr

Audio_file =("audio.wav")

#use audio file as a source 
r = sr.Recognizer()  # initialize the recognizer 

with sr.AudioFile(Audio_file) as source:
    audio = r.record(source)

    print ("audio fille contain " + r.recognize_google(audio))
