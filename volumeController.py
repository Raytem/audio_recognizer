import os
import subprocess

class VolumeController:
    def inc_volume(self):
        curVolume = self.get_volume()
        newVolume = min(curVolume + 10, 100)
        os.system(f"osascript -e 'set volume output volume {newVolume}'")

    def dec_volume(self):
        curVolume = self.get_volume()
        newVolume = max(curVolume - 10, 0)
        os.system(f"osascript -e 'set volume output volume {newVolume}'")

    def get_volume(self):
        script = "output volume of (get volume settings)"
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        current_volume = int(result.stdout.strip())
        return current_volume