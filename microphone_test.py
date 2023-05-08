import pyaudio
import wave

def record_audio(filename, seconds=3):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wave_file = wave.open(filename, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

def play_audio(filename):
    CHUNK = 1024

    wave_file = wave.open(filename, 'rb')
    audio = pyaudio.PyAudio()

    stream = audio.open(format=audio.get_format_from_width(wave_file.getsampwidth()),
                        channels=wave_file.getnchannels(),
                        rate=wave_file.getframerate(),
                        output=True)

    print("Playing...")

    data = wave_file.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wave_file.readframes(CHUNK)

    print("Finished playing")

    stream.stop_stream()
    stream.close()
    audio.terminate()

if __name__ == '__main__':
    audio_filename = "test_mic.wav"
    record_duration = 5  # Record for 5 seconds

    record_audio(audio_filename, record_duration)
    play_audio(audio_filename)
