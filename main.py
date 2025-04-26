from core.recognizer import recognize_speech
from core.command_handler import handle_command
from core.synthesizer import speak

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        print(f"You said: {command}")
        handle_command(command)
