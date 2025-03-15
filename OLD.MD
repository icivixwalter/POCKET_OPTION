OLD.MD

/* KEY_BINDING_TERMINUS
    sono le impostazioni per aprire il 
        @terminale@interno_(@terminus che viene aperto dentso sublimetext)
        FILE:
            C:\Users\icivi\AppData\Roaming\Sublime Text\Packages\User\Default (Windows).sublime-keymap
    

    */
            [
               //apro il terminale esterno
                //--------------------------------------------------------------//
                 // { "keys": ["ctrl+shift+t"], "command": "open_terminal"},

                    { "keys": ["ctrl+shift+t"],
                    "command": "terminus_open",
                    "args": {
                        "cwd": "${file_path:${folder}}",
                        "panel_name": "Terminus"
                    }},

                   
                   //per aprire il pannello denominato toggle_pane occore questo camdo
                   //??

                   { "keys": ["ctrl+shift+m"], "command": "toggle_menus"},

                //--------------------------------------------------------------//

               // Open a terminal tab at current file directory all'interno di sublimeText
                //--------------------------------------------------------------//
                    {
                        "keys": ["ctrl+alt+t"], "command": "terminus_open", "args": {
                            "cwd": "${file_path:${folder}}",
                            "title": "Command Prompt",
                            "panel_name": "Terminus"
                        }
                    },

                //--------------------------------------------------------------//
                
                //@APRIRE@TERMINALE_(per aprire il terminale nel progetto)
                //APRI IL MENU Preferences-->keybinding
                //per visualizzare il trminale nel progetto di sublimetext
                //utilizzare il comando alt+1 per attivare il terminus con ALT+1
                //E PER CHIUDERE IL TERMINALE  ALT+2 
                //- VEDI LINK https://pythonprogramming.altervista.org/how-to-keybind-sublime-repl-and-terminus-for-sublime-text-on-the-mac/
                //--------------------------------------------------------------//
                    {
                        "keys": ["alt+1"],
                        "command": "terminus_open",
                        "args" : {
                            "cmd": "cmd.exe",               //shell di comando
                            "cwd": "${file_path:${folder}}",//stessa path della cartella attiva
                            // Tell terminus to put it in the panel at the bottom of the screen
                            "panel_name": "Terminus"        //NOME PANNELLO!!
                        }
                    },
                    // PER CHIUDERE il TOOGLE PANE utilizzare esc gia di default oppure alt+2
                    { "keys": ["alt+2"], "command": "terminus_close"},
                    

                //--------------------------------------------------------------//



            ]
