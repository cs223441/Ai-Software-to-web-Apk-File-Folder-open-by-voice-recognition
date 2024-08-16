import tkinter as tk
import threading
import webbrowser
import speech_recognition as sr
import pyautogui

def listen_and_open():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command: {command}")
        if "open" in command:
            site = command.replace("open ", "")
            webbrowser.open(f"https://{site}.com")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Could not request results")

def start_listening():
    while True:
        listen_and_open()

def on_start():
    threading.Thread(target=start_listening).start()

root = tk.Tk()
root.title("Voice Command App")
root.geometry("300x200")

start_button = tk.Button(root, text="Start Listening", command=on_start)
start_button.pack(pady=20)

root.mainloop()
