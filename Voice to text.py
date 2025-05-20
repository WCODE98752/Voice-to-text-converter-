





import speech_recognition as s

sr=s.Recognizer()
print("listening.....")
with s.Microphone() as m:
    audio=sr.listen(m)
    query=sr.recognize_google(audio,language='eng')
    print(query)

