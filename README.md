# speech-to-text

Voice Assistant Script

This Python script serves as a basic voice assistant that can recognize spoken commands and perform certain actions, such as opening applications. The script uses the SpeechRecognition and pyttsx3 libraries for speech recognition and text-to-speech functionalities.

Prerequisites

Install the required Python libraries:
```bash
pip install SpeechRecognition pyttsx3
```
Ensure that you have a working microphone connected to your system.

Usage

Save the script with an appropriate name, for example, voice_assistant.py.

Run the script:

```bash
python voice_assistant.py
```
The voice assistant will greet you and listen for your commands.

Speak a command, and the assistant will attempt to recognize it and perform the corresponding action.

Available Commands

To exit the program, say "exit."

To open Notepad, say "open Notepad," "run Notepad," or similar variations.

Note

The script uses the Google Speech Recognition API for speech recognition. Ensure you have a stable internet connection for this feature to work.

Adjust the recognizer.pause_threshold value based on your environment and microphone sensitivity.

This script is a basic example and can be extended to include more commands and functionalities.
