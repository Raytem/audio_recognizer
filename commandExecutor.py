import webbrowser
from commands import Commands
from volumeController import VolumeController

class CommandExecutor:
    def __init__(self):
        self.volController = VolumeController()

    def execute_command(self, app, command: str):
        if (any(com.value == command for com in list(Commands))):
            match command:
                case Commands.INC_VOLUME.value: self.volController.inc_volume()
                case Commands.DEC_VOLUME.value: self.volController.dec_volume()
                case Commands.OPEN_BROWSER.value: self.open_browser()

    def open_browser(self):
        webbrowser.open('https://www.google.com/')
        pass

    def exit_program(self, app):
        # app.quit()
        pass