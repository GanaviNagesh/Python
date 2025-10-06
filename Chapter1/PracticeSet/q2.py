import pyttsx3

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.save_to_file("Hello from Codespaces, saved as audio file", "output.mp3")
engine.runAndWait()
