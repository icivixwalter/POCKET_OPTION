import sublime
import sublime_plugin
import os

# 1° comando: apri PDF
class OpenPdfBatCommand(sublime_plugin.WindowCommand):
    def run(self):
        file_path = r"C:\CASA\LINGUAGGI\RUST\PROGETTI_RUST\TUTORIAL_TONY_CHAN\RIASSUNTO_TONY_CHAN.md"
        if os.path.exists(file_path):
            os.startfile(file_path)
            sublime.status_message("Aperto PDF: " + file_path)
        else:
            sublime.error_message("File non trovato: " + file_path)


# 2° comando: apri README in Sublime
class OpenReadmeCommand(sublime_plugin.WindowCommand):
    def run(self):
        file_path = r"C:\CASA\LINGUAGGI\SUBLIMETEXT\README_COMANDI_VARI.md"
        if os.path.exists(file_path):
            self.window.open_file(file_path)
            sublime.status_message("Aperto README: " + file_path)
        else:
            sublime.error_message("File non trovato: " + file_path)
