import ttkbootstrap as ttk
import tkinter as tk
import threading
from recognizer import Recognizer
from commandExecutor import CommandExecutor
from commands import Commands

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.commandExecutor = CommandExecutor()
        self.rec = Recognizer()
        self.isRecognizeCommands = tk.BooleanVar()

        self.textField = ttk.Text(width=60)
        self.toggleRecordBtn = ttk.Button(text='▶️', command=self.toggle_record)
        self.clearTextBtn = ttk.Button(text='Очистить', command=lambda: self.clear_text())
        self.checkbox = ttk.Checkbutton(text="Распознавть команды", variable=self.isRecognizeCommands)
        self.commandsTable = ttk.Treeview(columns=("Команды"), show="headings")

        self.commandsTable.heading("Команды", text="Команды")        
        for command in list(Commands):
            self.commandsTable.insert("", tk.END, values=(command.value, ))

        self.style = ttk.Style('darkly')
        self.geometry('665x460')
        self.title('Распознователь речи')
        self.resizable(0, 0)

        self.textField.grid(row=0, column=0, padx=(10, 0), pady=10)
        self.commandsTable.grid(row=0, column=1, padx=(10, 0), pady=10)
        self.toggleRecordBtn.grid()
        self.clearTextBtn.grid(pady=10)
        self.checkbox.grid()

    def toggle_record(self):
        if (self.rec.is_recording):
            self.stop_record()
        else: 
            self.start_record()

    def start_record(self):
        self.toggleRecordBtn.config(text='⏸️')
        self.rec.start_recording()

        def update_text(text: str):
            if self.isRecognizeCommands.get():
                self.commandExecutor.execute_command(self, text)
            self.textField.insert(ttk.END, f' {text}')

        threading.Thread(target=self.rec.record_and_recognize, args=(update_text,)).start()

    def stop_record(self):
        self.toggleRecordBtn.config(text='▶️')
        self.rec.finish_recording()

    def clear_text(self):
        self.textField.delete(1.0, ttk.END)