import webbrowser
from commands import Commands
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class CommandExecutor:
    def __init__(self):
        pass

    def execute_command(self, app, command: str):
        if (any(com.value == command for com in list(Commands))):
            match command:
                case Commands.EXIT.value: self.exit_program(app)
                case Commands.INC_VOLUME.value: pass
                case Commands.DEC_VOLUME.value: pass
                case Commands.OPEN_BROWSER.value: self.open_browser()

    def open_browser(self):
        webbrowser.open('https://www.google.com/')
        pass

    def exit_program(self, app):
        app.quit()

    