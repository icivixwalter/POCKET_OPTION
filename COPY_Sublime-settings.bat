@rem COPY_Sublime-settings_and_Mariana.bat

@echo off
setlocal

:: Percorsi sorgente e cartella di destinazione
set "source1=C:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\Preferences.sublime-settings"
set "source2=C:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\Mariana.sublime-color-scheme"
set "dest_folder=C:\CASA\GE_CASA\GE_MARINO\BANCA\POCKET_OPTION\IMPOSTAZIONI_SUBLIMETXT"
set "logfile=%dest_folder%\LOG_COPY_Sublime-settings.txt"

:: Creazione del file log (se non esiste)
if not exist "%logfile%" (
    echo ================================ > "%logfile%"
    echo LOG OPERAZIONI - Sublime Text Backup >> "%logfile%"
    echo ================================ >> "%logfile%"
)

:: Scrive intestazione nel log per ogni esecuzione
echo.
echo === Operazione avviata: %DATE% %TIME% ===
echo === Operazione avviata: %DATE% %TIME% === >> "%logfile%"
echo.

:: Controlla se la cartella di destinazione esiste, altrimenti la crea
if not exist "%dest_folder%" (
    echo [INFO] Creazione cartella di destinazione...
    echo [INFO] Creazione cartella di destinazione... >> "%logfile%"
    mkdir "%dest_folder%" && (
        echo.
        echo [OK] Cartella creata: "%dest_folder%"
        echo [OK] Cartella creata: "%dest_folder%" >> "%logfile%"
    ) || (
        echo.
        echo [ERRORE] Impossibile creare la cartella di destinazione!
        echo [ERRORE] Impossibile creare la cartella di destinazione! >> "%logfile%"
        echo === Operazione FALLITA: %DATE% %TIME% === >> "%logfile%"
        echo --------------------
        echo -------------------- >> "%logfile%"
        pause
        exit /b
    )
) else (
    echo.
    echo [OK] Cartella di destinazione esistente: "%dest_folder%"
    echo [OK] Cartella di destinazione esistente: "%dest_folder%" >> "%logfile%"
)

echo.
echo --- Inizio copia file ---
echo --- Inizio copia file --- >> "%logfile%"
echo.

:: Esegue la copia dei file
call :CopyAndLog "%source1%" "%dest_folder%"
call :CopyAndLog "%source2%" "%dest_folder%"

echo.
echo === Operazione COMPLETATA: %DATE% %TIME% ===
echo === Operazione COMPLETATA: %DATE% %TIME% === >> "%logfile%"
echo --------------------
echo -------------------- >> "%logfile%"
pause
exit /b

:: ------------------- FUNZIONE PER LA COPIA -------------------
:CopyAndLog
set "source=%~1"
set "dest_folder=%~2"
set "filename=%~nx1"
set "destination=%dest_folder%\%filename%"

:: Verifica se il file sorgente esiste
if not exist "%source%" (
    echo.
    echo [ERRORE] File NON trovato: "%source%"
    echo [ERRORE] File NON trovato: "%source%" >> "%logfile%"
    echo === Operazione FALLITA: %DATE% %TIME% === >> "%logfile%"
) else (
    echo.
    echo [OK] File trovato: "%source%"
    echo [OK] File trovato: "%source%" >> "%logfile%"
    
    :: Esegue la copia
    copy /Y "%source%" "%destination%" > nul 2>&1
    if errorlevel 1 (
        echo.
        echo [ERRORE] Problema nella copia: "%source%"
        echo [ERRORE] Problema nella copia: "%source%" >> "%logfile%"
    ) else (
        echo.
        echo [OK] Copia riuscita: "%filename%"
        echo [OK] Copia riuscita: "%filename%" >> "%logfile%"
        echo [INFO] File copiato in: "%destination%"
        echo [INFO] File copiato in: "%destination%" >> "%logfile%"
    )
)
@echo off
exit /b
