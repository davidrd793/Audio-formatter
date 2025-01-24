import speech_recognition as sr 

class Transformer:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.keywords = self.extract_keywords()
        self.text = None

    @staticmethod
    def extract_keywords() -> list:
        """
        Extracts json keywords for searching them on the audio record
        JSON file is configurable, so feel free to put any keywords you want instead of mines
        """
        return ["titulo"] #Connect to keywords.json later

    def listen(self) -> None:
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source, timeout=5)
        traslated_audio = self.audio_to_text(audio)
        print(traslated_audio)

    def audio_to_text(self, audio):
        try:
            text = self.recognizer.recognize_google(audio, language="es-ES")
            return text
        except UnknownValueError:
            return "Cannot understand audio"
        except RequestError:
            return "Something went wrong on connecting to Google API, code {e}"







if __name__=="__main__":
    transformer = Transformer()
    transformer.listen()

