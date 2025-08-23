    """
    I commenti vengono fatti con LE VIRGOLETTE
        FILE Main_attiva_comandi.py
        """


import sublime
import sublime_plugin
import os

# ======================================================================
# FUNZIONE DI UTILITÀ
# ----------------------------------------------------------------------
# apri_file(window, percorso, esterno=False)
# - window: finestra corrente di Sublime Text
# - percorso: percorso completo del file da aprire
# - esterno=True → apre con l'applicazione predefinita di Windows
# - esterno=False → apre direttamente in Sublime Text
# ======================================================================
def apri_file(window, percorso, esterno=False):
    if os.path.exists(percorso):
        if esterno:
            os.startfile(percorso)
        else:
            window.open_file(percorso)
        sublime.status_message("Aperto: " + percorso)
    else:
        sublime.error_message("File non trovato: " + percorso)

# ======================================================================
# COMANDI ESISTENTI - TUTORIAL
# ======================================================================
class OpenPdfBatCommand(sublime_plugin.WindowCommand):
    """Apre il file RIASSUNTO_TONY_CHAN.md con l'app predefinita"""
    def run(self):
        apri_file(self.window,
                  r"C:\CASA\LINGUAGGI\RUST\PROGETTI_RUST\TUTORIAL_TONY_CHAN\RIASSUNTO_TONY_CHAN.md",
                  esterno=True)

class OpenReadmeCommand(sublime_plugin.WindowCommand):
    """Apre il file README_COMANDI_VARI.md in Sublime Text"""
    def run(self):
        apri_file(self.window,
                  r"C:\CASA\LINGUAGGI\SUBLIMETEXT\README_COMANDI_VARI.md")

# ======================================================================
# LAVORI PUBBLICI
# ======================================================================
class ApriDelibereLlppCommand(sublime_plugin.WindowCommand):
    def run(self):
        apri_file(self.window, r"C:\LLPP\DELIBERE\elenco.txt")

class UtileLlppDetermine31Command(sublime_plugin.WindowCommand):
    def run(self):
        apri_file(self.window, r"C:\LLPP\DETERMINE\utile31.txt")

class UtileLlppDetermine32Command(sublime_plugin.WindowCommand):
    def run(self):
        apri_file(self.window, r"C:\LLPP\DETERMINE\utile32.txt")

class ApriElencoDipendentiCommand(sublime_plugin.WindowCommand):
    def run(self):
        apri_file(self.window, r"C:\LLPP\DIPENDENTI\elenco.txt")

# ======================================================================
# TUTORIAL → APPROFONDIMENTI
# ======================================================================
class UtileTutorial31Command(sublime_plugin.WindowCommand):
    def run(self):
        apri_file(self.window, r"C:\TUTORIAL\utile31.txt")

class UtileTutorial32Command(sublime_plugin.WindowCommand):
    def run(self):
        apri_file(self.window, r"C:\TUTORIAL\utile32.txt")

# ======================================================================
# PARAMETRI SUBLIMETEXT
# ======================================================================

class ApriParametriSublimeCommand(sublime_plugin.WindowCommand):
    """
    Apre la cartella 'User' di Sublime Text dove si trovano:
    - File di configurazione personali
    - Plugin e menu creati dall'utente
        inserita correzione finale

        Sublime Text non “grigierà” mai il menu per questa voce.
        L’eventuale errore viene gestito solo dentro run() con il messaggio “Cartella non trovata”.

    """
    def run(self):
        cartella = os.path.join(sublime.packages_path(), "User")
        if os.path.exists(cartella):
            os.startfile(cartella)  # Apre in Esplora Risorse
            sublime.status_message("Aperta cartella: " + cartella)
        else:
            sublime.error_message("Cartella non trovata: " + cartella)

      def is_enabled(self):
        return True  # Comando sempre attivo


class VisualizzaCorrenteTxtCommand(sublime_plugin.WindowCommand):
    """Crea una copia del file corrente in formato .txt e la apre"""
    def run(self):
        view = self.window.active_view()
        if view:
            file_path = view.file_name()
            if file_path and os.path.exists(file_path):
                nuovo = os.path.splitext(file_path)[0] + ".txt"
                with open(file_path, "r", encoding="utf-8") as src, open(nuovo, "w", encoding="utf-8") as dst:
                    dst.write(src.read())
                apri_file(self.window, nuovo)
            else:
                sublime.error_message("Nessun file aperto.")

class VisualizzaCorrenteMdCommand(sublime_plugin.WindowCommand):
    """Crea una copia del file corrente in formato .md e la apre"""
    def run(self):
        view = self.window.active_view()
        if view:
            file_path = view.file_name()
            if file_path and os.path.exists(file_path):
                nuovo = os.path.splitext(file_path)[0] + ".md"
                with open(file_path, "r", encoding="utf-8") as src, open(nuovo, "w", encoding="utf-8") as dst:
                    dst.write(src.read())
                apri_file(self.window, nuovo)
            else:
                sublime.error_message("Nessun file aperto.")
