::FILE                         : Build_APRI_CMD.BAT
::SI TROVA IN QUESTA PATH      : c:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\

:: FLUSSO LOGICO COMPLETO:
::
:: 1) Il file Build_ESEGUI_DOS.sublime-build è un Build System di Sublime Text
::    che avvia il comando Python definito in Build_ESEGUI_Python.py
::    tramite il comando "apri_readme".
::
:: 2) Build_ESEGUI_Python.py definisce la classe ApriReadmeCommand che
::    mostra un menu di opzioni all'utente e, in base alla scelta,
::    esegue il file batch Build_APRI_CMD.BAT passando il numero
::    della scelta come parametro.
::
:: 3) Build_APRI_CMD.BAT riceve il parametro numerico (1, 2 o 3)
::    e apre il file README corrispondente con l'applicazione associata di Windows.
::
:: In questo modo si realizza un sistema modulare e centralizzato per
:: aprire rapidamente file README da qualsiasi progetto in Sublime Text,
:: mantenendo pulito e semplice il Build System.
@echo off
echo ATTIVA IL COMANDO MULTI APERTURA FILE VALIDO PER TUTTI I PROGETTI SUBLIMETEXT CON I PARAMETRI
echo.

if "%1"=="" (
	
	echo "Errore: nessuna scelta specificata. Usa 1, 2, 3, 10, 11 o 12."
	
    exit /b 1
)

if "%1"=="1" (
  start "" "c:\CASA\LINGUAGGI\RUST\PROGETTI_RUST\TUTORIAL_TONY_CHAN\README_TUTORIAL_RUST.MD"
  goto :EOF
)
if "%1"=="2" (
  start "" "c:\Casa\LINGUAGGI\SUBLIMETEXT\README_COMANDI_VARI.MD"
  goto :EOF
)
if "%1"=="3" (
  start "" "c:\Casa\GE_CASA\GE_MARINO\BANCA\POCKET_OPTION\TUTORIAL_POCKET_OPTION.MD"
  goto :EOF
)


if "%1"=="10" (
  start "" "C:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\Build_ESEGUI_DOS.sublime-build"
  goto :EOF
)

if "%1"=="11" (
  start "" "C:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\Build_ESEGUI_Python.py"
  goto :EOF
)


if "%1"=="12" (
 start "" "C:\Program Files\Sublime Text\sublime_text.exe" "C:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\Build_APRI_CMD.BAT"
  goto :EOF
)


echo Scelta non valida: %1. Usa 1, 2, 3, 10, 11 o 12.
exit /b 1
