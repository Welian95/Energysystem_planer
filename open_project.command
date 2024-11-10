#!/bin/bash

# Setzt den Pfad zum aktuellen Projektverzeichnis (Verzeichnis des Skripts)
PROJECT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Wechsle zum Projektordner
cd "$PROJECT_PATH"

# VSCode öffnen
code "$PROJECT_PATH"

# Warte ein paar Sekunden, bis VSCode gestartet ist (optional)
sleep 3

# Virtuelle Umgebung aktivieren
source "$PROJECT_PATH/venv/bin/activate"

# Hinweis für den Nutzer
echo "Virtuelle Umgebung wurde aktiviert. Das Projekt ist nun in VSCode geöffnet."
