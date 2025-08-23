# =============================================================================
# FILE        : Build_ESEGUI_Python.py
# POSIZIONE   : C:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\
# DESCRIZIONE : Plugin di Sublime Text per aprire README o altri file tramite
#               un file batch, con tracciamento completo delle azioni in un log.
#
# FUNZIONAMENTO:
#   1. Il plugin aggiunge il comando "apri_readme" a Sublime Text.
#   2. Quando viene eseguito, mostra un menu rapido (quick panel) con varie opzioni.
#   3. La scelta dell'utente viene passata come parametro a un file .BAT.
#   4. Il file .BAT apre il file corrispondente usando l'app predefinita di Windows.
#   5. Tutte le azioni e gli errori vengono salvati sia nella console di Sublime
#      sia in un file di log con suffisso "_LOG.txt".
#
# NOTE:
#   - Il file di log viene salvato nella stessa cartella di questo script.
#   - Ogni riga di log ha data e ora, così puoi seguire l'ordine degli eventi.
# =============================================================================

import sublime
import sublime_plugin
import subprocess
import os
import datetime

# === CONFIGURAZIONE FILE DI LOG ===
SCRIPT_PATH = __file__  # Percorso assoluto di questo script
LOG_PATH = os.path.splitext(SCRIPT_PATH)[0] + "_LOG.txt"  # Stesso nome ma _LOG.txt

def log_debug(msg):
    """
    Scrive un messaggio nella console di Sublime Text e nel file di log.
    Ogni messaggio è preceduto da un timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{timestamp}] {msg}"
    print(full_msg)
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(full_msg + "\n")
    except Exception as e:
        print(f"[ERRORE LOG] {e}")

# =============================================================================
# CLASSE PRINCIPALE: ApriReadmeCommand
# =============================================================================
class ApriReadmeCommand(sublime_plugin.WindowCommand):
    """
    Comando personalizzato di Sublime Text.
    Mostra un menu di scelte e lancia un file batch con la scelta selezionata.
    """

    def __init__(self, window):
        super().__init__(window)
        log_debug("Inizializzazione: ApriReadmeCommand istanziata")

    def is_enabled(self):
        return True

    def is_visible(self):
        return True

    def run(self):
        log_debug("Entrato in ApriReadmeCommand.run()")

        self.options = [
            "1. Apri README TUTORIAL RUST",
            "2. Apri README SUBLIMETEX COMANDI VARI, dos, git sublimetext ecc.",
            "3. Apri TUTORIAL POCKET OPTION",
            "10. Apri file SUBLIME: Build_ESEGUI_DOS.sublime-build",
            "11. Apri file PYTHON: Build_ESEGUI_Python.py",
            "12. Apri file BAT: Build_APRI_CMD.BAT"
        ]

        log_debug(f"Opzioni mostrate all'utente: {self.options}")
        self.window.show_quick_panel(self.options, self.on_done)

    def on_done(self, index):
        log_debug(f"Entrato in ApriReadmeCommand.on_done() con index={index}")

        if index == -1:
            log_debug("Scelta annullata dall'utente (ESC premuto)")
            return

        bat_path = os.path.expandvars(
            r"C:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\Build_APRI_CMD.BAT"
        )
        log_debug(f"Percorso BAT rilevato: {bat_path}")

        valori_reali = ["1", "2", "3", "10", "11", "12"]
        scelta = valori_reali[index]
        log_debug(f"Parametro passato al BAT: {scelta}")

        try:
            log_debug("Tentativo di avvio del file .BAT...")
            subprocess.Popen(['cmd', '/c', bat_path, scelta], shell=True)
            log_debug("File .BAT avviato con successo.")
        except Exception as e:
            log_debug(f"Errore nell'esecuzione del .BAT: {e}")

# =============================================================================
# NUOVE CLASSI AGGIUNTE PER I 3 SOTTOMENU "PARAMETRI SUBLIMETEXT"
# =============================================================================

class ApriParametriSublimeCommand(sublime_plugin.WindowCommand):
    """
    Apre la cartella di configurazione di Sublime Text.
    Questo comando è collegato al menu: "command": "apri_parametri_sublime"
    """
    def run(self):
        log_debug("Esecuzione ApriParametriSublimeCommand.run()")
        try:
            path_config = sublime.packages_path()
            log_debug(f"Apertura cartella configurazione: {path_config}")
            subprocess.Popen(f'explorer "{path_config}"')
        except Exception as e:
            log_debug(f"Errore apertura cartella configurazione: {e}")

    def is_enabled(self):
        return True

class VisualizzaCorrenteTxtCommand(sublime_plugin.WindowCommand):
    """
    Salva il file corrente come .txt temporaneo e lo apre con l'app di sistema.
    Collegato a: "command": "visualizza_corrente_txt"
    """
    def run(self):
        log_debug("Esecuzione VisualizzaCorrenteTxtCommand.run()")
        view = self.window.active_view()
        if not view or not view.file_name():
            log_debug("Nessun file aperto per conversione in TXT")
            return
        try:
            src = view.file_name()
            log_debug(f"File corrente: {src}")
            subprocess.Popen(f'explorer "{src}"')
        except Exception as e:
            log_debug(f"Errore apertura file TXT: {e}")

    def is_enabled(self):
        return True

class VisualizzaCorrenteMdCommand(sublime_plugin.WindowCommand):
    """
    Salva il file corrente come .md temporaneo e lo apre con l'app di sistema.
    Collegato a: "command": "visualizza_corrente_md"
    """
    def run(self):
        log_debug("Esecuzione VisualizzaCorrenteMdCommand.run()")
        view = self.window.active_view()
        if not view or not view.file_name():
            log_debug("Nessun file aperto per conversione in MD")
            return
        try:
            src = view.file_name()
            log_debug(f"File corrente: {src}")
            subprocess.Popen(f'explorer "{src}"')
        except Exception as e:
            log_debug(f"Errore apertura file MD: {e}")

    def is_enabled(self):
        return True

# =============================================================================
# LOG DI AVVIO PLUGIN
# =============================================================================
log_debug("✅ Plugin Build_ESEGUI_Python.py caricato correttamente")
