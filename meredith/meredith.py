import pyttsx3
import speech_recognition


class Meredith:
    def __init__(self):
        self.name = self.__class__.__name__.lower()
        self.listener = speech_recognition.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def talk(self, text: str) -> None:
        print('%s: %s' % (self.name, text))
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self) -> list:
        try:
            with speech_recognition.Microphone() as source:
                print('Listening...')
                self.listener.adjust_for_ambient_noise(source)
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice, language='it-IT').lower()
                if self.name in command:
                    command = command.replace(self.name, '')
                    print('command: %s' % command)
                    return command
        except:
            pass

    def run(self):
        command = self.listen()
        if command is None:
            return

        if 'ciao' in command:
            self.talk('Ciao, sono {}. Come posso essere d\'aiuto?'.format(self.name))
        else:
            self.talk('Mi dispiace, non so cosa fare!')
