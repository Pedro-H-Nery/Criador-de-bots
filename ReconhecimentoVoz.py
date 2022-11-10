import speech_recognition as sr

def ReconhecerVoz(microfone):
    rec = sr.Recognizer()

    with sr.Microphone(microfone) as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Pode falar que estou ouvindo")
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language='pt-BR')
        print(texto)

if __name__ == '__main__':
    #print(sr.Microphone.list_microphone_names())
    ReconhecerVoz(2)