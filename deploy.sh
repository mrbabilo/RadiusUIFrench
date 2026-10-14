#!/bin/sh
# Publish this folder (minus docs and tools) to RimWorld's Mods folder. No build: the mod has no code.
set -eu

HERE=$(cd "$(dirname "$0")" && pwd)
MODS="/Volumes/BABILOGAMES/JEUX EN COURS/RimWorld.app/Mods"
DEST="$MODS/RadiusUIFrench"

[ -d "$MODS" ] || { echo "Dossier Mods du jeu introuvable (volume BABILOGAMES non monté ?) : $MODS" >&2; exit 1; }
python3 "$HERE/tools/check_translations.py"
rsync -a --delete --exclude docs/ --exclude tools/ --exclude deploy.sh --exclude .DS_Store --exclude .git/ --exclude .gitignore "$HERE/" "$DEST/"
echo "Publié : $DEST"
