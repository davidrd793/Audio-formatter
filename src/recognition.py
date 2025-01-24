import speech_recognition as sr 

class Transformer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.keywords = self.extract_keywords()

    @staticmethod
    def extract_keywords():
        return ["titulo"] #Connect to keywords.json later

    def listen(self):
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source, timeout=5)
        return audio

a = Transformer()
print(type(a.listen()))

