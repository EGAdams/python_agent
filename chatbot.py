import time
import sys
from threading import Thread

class Chatbot:
    # ...

    def spinner(self):
        spinner = "|/-\\"
        while self.spin:
            for char in spinner:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
                sys.stdout.write('\b')

    def listen(self):
        delay = 1
        while True:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source, phrase_time_limit=delay)

            try:
                print("Recognizing...")
                text = self.recognizer.recognize_google(audio)
                print(f"Recognized: {text}")

                if 'shutdown' in text:
                    return

                if 'Giz' in text:
                    print("How can I help you?")
                elif any(substring in text for substring in ['Gi', 'iz']):
                    print("Listening more closely...")
                    self.spin = True
                    spinner_thread = Thread(target=self.spinner)
                    spinner_thread.start()
                    delay = 0.2
                    start_time = time.time()

                    while time.time() - start_time < 3:
                        with self.microphone as source:
                            audio = self.recognizer.listen(source, phrase_time_limit=delay)

                        try:
                            text = self.recognizer.recognize_google(audio)

                            if 'Giz' in text:
                                self.spin = False
                                spinner_thread.join()
                                print("\bHow can I help you?")
                                break
                        except sr.UnknownValueError:
                            pass
                        except sr.RequestError as e:
                            pass

                    self.spin = False
                    spinner_thread.join()
                    print("\b")
                    delay = 1

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error with the API; {0}".format(e))

            time.sleep(delay)
