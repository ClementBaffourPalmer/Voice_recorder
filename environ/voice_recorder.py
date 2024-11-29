import sounddevice as sd
import numpy as np
import wave

def record_audio(file_name: str, duration: int, sample_rate: int = 44100):
    """
    Records audio and saves it to a .wav file.

    Args:
        file_name (str): Name of the output file.
        duration (int): Duration of the recording in seconds.
        sample_rate (int): Sampling frequency in Hz (default is 44100).
    """
    print(f"Recording for {duration} seconds...")

    # Capture audio with the specified settings
    audio_data = sd.rec(frames=duration * sample_rate, samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()  # Ensure recording is finished
    print("Recording complete.")

    # Save the recorded audio to a file
    with wave.open(file_name, 'wb') as audio_file:
        audio_file.setnchannels(1)  # Mono
        audio_file.setsampwidth(2)  # 16-bit
        audio_file.setframerate(sample_rate)
        audio_file.writeframes(audio_data.tobytes())  # Convert NumPy array to bytes
    print(f"Audio saved as {file_name}.")

if __name__ == "__main__":
    # Customize the recording
    output_file = "recording.wav"  # Change file name as desired
    recording_duration = 10  # Set your recording duration in seconds
    sampling_rate = 44100  # Default high-quality sampling rate

    # Record and save the audio
    record_audio(file_name=output_file, duration=recording_duration, sample_rate=sampling_rate)
