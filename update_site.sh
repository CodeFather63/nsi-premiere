#!/bin/bash

# ============================================================
#  Mise à jour du site NSI (GitHub Pages)
#  Usage : ./update_site.sh ["message de commit"]
# ============================================================

# Message de commit par défaut ou personnalisé
COMMIT_MSG="${1:-Mise à jour du site}"

echo "======================================"
echo "  Mise à jour du site NSI"
echo "======================================"

# 1. Activer l'environnement virtuel Python (si présent)
if [ -f ".venv/bin/activate" ]; then
    echo ""
    echo ">>> Activation de l'environnement Python..."
    source .venv/bin/activate
fi

# 2. Envoi des sources sur GitHub
echo ""
echo ">>> Envoi des fichiers sur GitHub..."
git add .
git commit -m "$COMMIT_MSG"
git push

# 3. Publication sur GitHub Pages
echo ""
echo ">>> Publication sur GitHub Pages..."
mkdocs gh-deploy

echo ""
echo "======================================"
echo "  Terminé !"
echo "  Site visible sur :"
echo "  https://CodeFather63.github.io/nsi-premiere"
echo "======================================"
