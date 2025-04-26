from core.synthesizer import speak
from datetime import datetime
import webbrowser
import json
import subprocess
import os

with open('data/keywords.json', 'r') as f:
    commands = json.load(f)

def handle_command(command):
    command = command.lower()

    for action_key, data in commands.items():
        for phrase in data["phrases"]:
            if phrase in command:
                action = data["action"]
                action_data = data.get("data")

                if action == "say":
                    speak(action_data)

                elif action == "open_url":
                    speak(f"Opening {action_key}")
                    webbrowser.open(action_data)

                elif action == "search":
                    search_query = command.replace(phrase, "").strip()
                    speak(f"Searching for {search_query}")
                    webbrowser.open(f"https://www.google.com/search?q={search_query}")

                elif action == "time":
                    now = datetime.now().strftime("%H:%M")
                    speak(f"The time is {now}")

                elif action == "exit":
                    speak("Goodbye!")
                    exit()

                elif action == "open_app":
                    speak(f"Launching {action_key}")
                    try:
                        subprocess.Popen(action_data)
                    except Exception as e:
                        speak(f"Failed to open app: {str(e)}")

                elif action == "play_music":
                    speak(f"Playing music from {action_data}")
                    os.startfile(action_data)

                elif action == "open_folder":
                    speak(f"Opening folder {action_data}")
                    os.startfile(action_data)

                elif action == "shutdown":
                    speak("Shutting down the system.")
                    os.system("shutdown /s /t 5")

                elif action == "restart":
                    speak("Restarting the system.")
                    os.system("shutdown /r /t 5")

                else:
                    speak("Action type not supported.")
                return  # Stop after first match

    speak("Sorry, I didn't understand that command.")
