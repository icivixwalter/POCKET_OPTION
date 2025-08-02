# FILE                         : Build_ESEGUI_Python.py
# SI TROVA IN QUESTA PATH      : c:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\
#
# FLUSSO LOGICO COMPLETO:
#
# 1) Il file Build_ESEGUI_DOS.sublime-build è un Build System di Sublime Text
#    che avvia il comando Python definito in questo file tramite il comando "apri_readme".
#
# 2) Questo file definisce la classe ApriReadmeCommand che mostra un menu di opzioni all'utente.
#    In base alla scelta fatta, esegue il file batch Build_APRI_CMD.BAT, passando il numero della scelta come parametro.
#
# 3) Il file Build_APRI_CMD.BAT riceve il parametro numerico (1, 2, 3, 10 o 11) e apre il file README corrispondente
#    con l'applicazione associata di Windows.
#
# Così si realizza un sistema modulare e centralizzato per aprire rapidamente file README da qualsiasi progetto in Sublime Text,
# mantenendo pulito e semplice il Build System.

import sublime
import sublime_plugin
import subprocess
import os

# Definisce un nuovo comando di finestra per Sublime chiamato "apri_readme"
class ApriReadmeCommand(sublime_plugin.WindowCommand):

    # Questo metodo viene eseguito quando il comando viene attivato
    def run(self):
        
        print("ApriReadmeCommand eseguito")  # Per debugging
        
        # Definisce le opzioni che l'utente vedrà nel menu a scelta rapida che saranno
        # aperte con il file .bat in quanto passa i parametri al file.bat, puoi aggiunge
        # altre voci che corrispondono a di file.bat
        self.options = [
            "1. Apri README TUTORIAL RUST",
            "2. Apri README COMANDI VARI",
            "3. Apri TUTORIAL POCKET OPTION",
            "10. Apri file SUBLIME: Build_ESEGUI_DOS.sublime-build",
            "11. Apri file PYTHON: Build_ESEGUI_Python.py",
            "12. Apri file BAT: Build_APRI_CMD.BAT"
        ]

        # Mostra il menu a scelta (quick panel) con le opzioni
        # Al termine della scelta, chiama il metodo self.on_done
        self.window.show_quick_panel(self.options, self.on_done)

    # Questo metodo viene chiamato quando l'utente fa una scelta
    def on_done(self, index):
        # Se l'utente preme ESC o annulla, esci senza fare nulla
        if index == -1:
            return  # Annullato

        # Specifica il percorso assoluto del file .BAT
        # Usa os.path.expandvars per essere sicuri che eventuali variabili d'ambiente vengano risolte
        bat_path = os.path.expandvars(
            r"C:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\Build_APRI_CMD.BAT"
        )

        # Mappa esplicita tra l'indice (0-based) e il parametro numerico da passare
        # In questo modo evitiamo ambiguità con scelte come 10 o 11
        valori_reali = ["1", "2", "3", "10", "11", "12"]
        scelta = valori_reali[index]

        # Debug: stampa la scelta effettiva
        print(f"Scelta effettuata: {scelta}")

        # Esegue il .BAT passando come argomento la scelta (1, 2, 3, 10 o 11)
        # 'cmd /c' esegue il comando e chiude il prompt subito dopo
        # shell=True permette a 'cmd' di interpretare correttamente la stringa
        subprocess.Popen(['cmd', '/c', bat_path, scelta], shell=True)
