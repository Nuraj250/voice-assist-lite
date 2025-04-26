import speech_recognition as sr

def list_microphones():
    mic_list = sr.Microphone.list_microphone_names()
    print("🎙️ Available Microphones:")
    for idx, name in enumerate(mic_list):
        print(f"[{idx}] {name}")
    return mic_list

def find_working_microphone():
    mic_list = list_microphones()
    recognizer = sr.Recognizer()

    for idx, name in enumerate(mic_list):
        try:
            with sr.Microphone(device_index=idx) as source:
                print(f"🎧 Testing mic: {name} at index {idx}...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("🔊 Please say something...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                test_text = recognizer.recognize_google(audio)
                print(f"✅ Mic [{idx}] '{name}' works! Heard: {test_text}")
                return idx, name  # First working mic found!
        except Exception as e:
            print(f"❌ Mic [{idx}] '{name}' failed: {e}")

    raise RuntimeError("❌ No working microphone found!")

def recognize_speech():
    recognizer = sr.Recognizer()
    device_index, mic_name = find_working_microphone()
    with sr.Microphone(device_index=device_index) as source:
        print(f"🎤 Listening with selected mic: {mic_name}...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return "I didn't catch that."
