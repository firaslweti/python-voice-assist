import speech_recognition as sr
import openai

class VoiceAssistant:
    def __init__(self):
        openai.api_key = "your open ai api here 🙏"

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            self.process_query(query)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Sorry, there was an issue with the request.")

    def process_query(self, query):
        try:
            completion = openai.Completion.create(
                engine="text-davinci-003",  # if not working just change the latest engine 
                prompt=query,
                max_tokens=50
            )
            response = completion.choices[0].text.strip()
            print(f"Assistant: {response}")
        except openai.OpenAIError as e:
            print(f"An error occurred while communicating with OpenAI: {e}")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    while True:
        assistant.listen()
