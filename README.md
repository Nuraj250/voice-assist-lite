
## 🗣️ **Voice Assist Lite**
A lightweight Python-based voice assistant for Windows that supports voice commands like:
- Opening apps
- Playing music
- Browsing websites
- Searching Google
- System control (shutdown, restart)
- More — fully dynamic via `keywords.json`

---

## 🚀 **Setup Instructions**

### 1️⃣ **Clone the Repository:**
```bash
git clone https://github.com/Nuraj250/voice-assist-lite.git
cd voice-assist-lite
```

### 2️⃣ **Create Virtual Environment (Optional but Recommended):**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3️⃣ **Install Dependencies:**
```bash
pip install -r requirements.txt
```

> **⚠️ PyAudio Note (if installation fails):**  
> For Windows:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```
> For Linux:
> ```bash
> sudo apt-get install portaudio19-dev python3-pyaudio
> pip install pyaudio
> ```

---

## ▶️ **How to Run the Assistant:**
```bash
python main.py
```

The assistant will:
1. List all available microphone devices.
2. Test microphones automatically.
3. Select the first working microphone.
4. Start listening for commands.

---

## 🧩 **How to Add or Update Commands (No Coding Needed!):**

### 📂 Edit this file:
```
data/keywords.json
```

### ✅ Example Command Format:
```json
{
  "open_google": {
    "phrases": ["open google"],
    "action": "open_url",
    "data": "https://www.google.com"
  },
  "play_song": {
    "phrases": ["play music", "start music"],
    "action": "play_music",
    "data": "C:/Users/YourName/Music/song.mp3"
  },
  "shutdown": {
    "phrases": ["shut down", "power off"],
    "action": "shutdown"
  }
}
```

---

### 🎯 **Supported Actions:**
| Action Type     | What It Does                        | Example                        |
|-----------------|-------------------------------------|--------------------------------|
| `say`           | Speaks the given text               | `"data": "Hello there!"`       |
| `open_url`      | Opens a website                     | `"data": "https://google.com"` |
| `search`        | Google search with spoken query     | No extra data needed          |
| `time`          | Tells the current time              | No extra data needed          |
| `exit`          | Stops the assistant                 | No extra data needed          |
| `open_app`      | Opens a program (.exe path)         | `"data": "notepad.exe"`        |
| `play_music`    | Plays a local music file            | `"data": "path_to_song.mp3"`   |
| `open_folder`   | Opens a folder                      | `"data": "C:/Users/YourName/Documents"` |
| `shutdown`      | Shuts down the PC                   | No extra data needed          |
| `restart`       | Restarts the PC                     | No extra data needed          |

---

## ⚡ **Performance Tips & Troubleshooting:**

### ✅ Microphone Not Detected?
- Check **Windows Sound Settings → Input Devices**.
- Ensure the correct mic is enabled.
- If using Bluetooth, make sure **Hands-Free AG Audio** is active.

### ✅ Improve Recognition Accuracy:
- Speak **clearly** and keep the mic close.
- Use **quiet environments** for best results.
- Adjust `adjust_for_ambient_noise(source, duration=1)` if needed.

### ✅ Reduce Listening Delay:
- Change the `timeout=3` or `phrase_time_limit=3` values in `recognizer.py` for faster detection.

---

## 🏆 **Future Improvements (Optional Ideas):**
- Add support for **voice confirmation before shutdown/restart**.
- Support for **multi-language commands**.
- Command history logging in the `logs/assistant.log` file.

---

## 📢 **License:**
MIT License – free to use and modify.