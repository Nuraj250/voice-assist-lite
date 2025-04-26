from core.synthesizer import speak

def handle_command(command):
    if "time" in command:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    else:
        speak("Sorry, I don't understand that command.")
