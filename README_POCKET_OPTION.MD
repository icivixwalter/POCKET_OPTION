@README_POCKET_OPTION.MD
   Gli originali dei comandi si trovano qui:
      START "APRI COMANDI LINGUAGGI" c:\\Casa\\LINGUAGGI\\RUST\\RUST_TUTORIAL\\RUST_TUTORIAL_TONY_CHAN\\README_TUTORIAL_RUST.MD

GITHUB
   @Progetto@web
      si trova in questa posizione su github:
         https://github.com/icivixwalter/RUST_TUTORIAL

   @comando@githu@unico
      copiare il comando ..
         git status & git pull & git add . & git commit -m "agg" & git push

@DOS
     dir /A /b *.*  >> A.TXT           = salvo su a.txt le cartellse senza path
     dir /s /b >> output.txt           = salvo tutte le sotto cartelle ed i file con la path completa
     dir *.* /w >a.txt                 = salvo 
SUBLIMETEXT
   Comandi contenuti in Preferences-->Key Bindings

      ctrl+shift+t                     = terminale basso
      ctrl+shift+y                     = chiudo il terminale basso
      ctrl+shift+r                     = terminale a destra nuovo tab

COMANDI MARKDOWN 
   Preview
      per aprire in visualizzazine diretta scrivere:

         view ---> row2                 = visualizzo in orizzontale pannello 1 sopra e 2 sotto
         ctrl+shift+p+ OPEN PREVIEW     = command palette + OPEN PREVIEW ---> PREVIEW IN MARKDOWN IN 
                                          UNA TAB SEPARATA,   @visualizza@markdown@preview
         alt+shift+1                    = a 1 scheda
         ctrl+shift+p                   = command palette
         cr                             = ritorno a capo con 2 spazi
                                        oppure <br> come forzatura
         grassetto                      = puoi utilizzare doppio asterisco o doppio undescore
                                          es.   **grassetto** oppure __grassetto__
         dimensione carattere           = non esiste in mardown la possibilita di aumentare la   
                                        dimensione del carattere ma si puo utilizzare Html es:  
                                        grassetto + carattere 24 px
                                        **<span style="font-size: 24px;">trait</span>**

         alt+shift+8                   = visualizzo in 2 pannelli orizzontali



TRASFORMARE .MD IN @WORD
         pandoc                        = scarica pandoc come programma esterno +
                                       1) installa pandoc: https://github.com/jgm/pandoc/releases/tag/3.7.0.2   
                                       2) Crea un Build System in Sublime
                                          Vai su:Tools > Build System > New Build System  
                                          Incolla questo codice
                                             {
                                              "cmd": ["pandoc", "$file", "-o", "${file_base_name}.docx"],
                                              "file_regex": "^(...*?):([0-9]*):?([0-9]*)",
                                              "selector": "text.html.markdown"
                                             }

                                       3) per attivare pandoc e trasformare il file aperto corrente  
                                       da .md a docx attivare lo script :  
                                          Tools --> Builds with --> Pandoc
                                          e verra creato il file .docs nella stessa cartella.
                                             @creare@file@doc@docs
                                          




