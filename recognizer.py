import json, pyaudio
from vosk import Model, KaldiRecognizer
import threading

class Recognizer:
    def __init__(self) -> None:
        self.model = Model('vosk-model-small-ru-0.22')
        self.rec = KaldiRecognizer(self.model, 16000)
        self.p = None
        self.stream = None
        self.is_recording = False

    def start_recording(self):
        if (not self.is_recording):
            self.p = pyaudio.PyAudio()
            self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
            self.stream.start_stream()
            self.is_recording = True

    def finish_recording(self):
        if (self.is_recording):
            self.stream.close()
            self.p.terminate()
            self.is_recording = False

    def record_and_recognize(self, text_printer_fn):
        if not self.stream:
            raise EOFError('Recording was not started!')

        while self.is_recording: 
            data = self.stream.read(4000, exception_on_overflow=False)
            if (self.rec.AcceptWaveform(data) and (len(data) > 0)) :
                answer = json.loads(self.rec.Result())
                if answer['text']: 
                  text_printer_fn(answer['text'])

            # if (self.rec.AcceptWaveform(data)) :
            #     answer = json.loads(self.rec.Result())
            #     text_printer_fn(answer)