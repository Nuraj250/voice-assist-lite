import speech_recognition as sr

def get_device_index(target_name):
    mic_list = sr.Microphone.list_microphone_names()
    for idx, name in enumerate(mic_list):
        if target_name.lower() in name.lower():
            print(f"✅ Selected microphone: {name} at index {idx}")
            return idx
    raise ValueError("❌ Microphone not found!")

def recognize_speech():
    recognizer = sr.Recognizer()
    device_index = get_device_index("联想thinkplus-GM2")  # Using your device name here
    with sr.Microphone(device_index=device_index) as source:
        print("🎤 Listening with 联想thinkplus-GM2...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return "I didn't catch that."
