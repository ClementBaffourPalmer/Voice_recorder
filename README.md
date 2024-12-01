# Voice_recorder with Python

This is a simple Python-based voice recorder application that allows users to record audio and save it as a WAV file. The application uses the sounddevice library for recording and scipy for handling the audio data.


# Features

Record audio for a specified duration.
Save the recording as a WAV file in high-quality format.
Easy-to-use interface (can be extended with a GUI).


# Requirements
Ensure you have the following installed:

Python 3.6 or higher
Required Python packages:
sounddevice
scipy
wavio (optional, for alternative WAV file handling)
You can install the required packages by running:

# bash
pip install sounddevice scipy wavio
How to Use
Clone the repository to your local machine:

# bash
git clone https://github.com/ClementBaffourPalmer/Voice_recorder.git
cd Voice_recorder
Ensure the virtual environment is set up and activated:

# bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
Install dependencies:

# bash
pip install -r requirements.txt
Run the Python script to record audio:


# bash
python voice_recorder.py
The recorded audio will be saved in the same directory as recording.wav.

# How It Works

Recording: The sounddevice library captures audio input from your microphone.
Saving: The recording is saved as a WAV file using the scipy.io.wavfile.write function.
Channels and Sampling Rate:
The application records mono (1 channel) audio at a sample rate of 44100 Hz, which is CD quality.


# Future Improvements

Add a GUI using Tkinter for ease of use.
Allow users to customize recording duration.
Include a playback option.
Add error handling for microphone availability.
Project Structure

# bash

Voice_recorder/
├── environ/          # Virtual environment (optional, not pushed to GitHub)
├── voice_recorder.py # Main script for recording audio
├── README.md         # Project documentation
└── requirements.txt  # Required Python packages

