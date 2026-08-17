#!/bin/bash
# ============================================================
# Script de mise à jour automatique du site NSI (GitHub Pages)
# Double-cliquer sur ce fichier pour l'exécuter (macOS)
# ============================================================

set -e  # arrête le script en cas d'erreur

# Se placer dans le dossier où se trouve ce script
cd "$(dirname "$0")"

echo "============================================"
echo " Mise à jour du site NSI"
echo "============================================"

# 1. Vérifier qu'on est bien dans le bon dossier
if [ ! -f "mkdocs.yml" ]; then
    echo "❌ Erreur : mkdocs.yml introuvable dans ce dossier."
    echo "   Place ce script dans le dossier du projet (à côté de mkdocs.yml)."
    read -p "Appuie sur Entrée pour fermer..."
    exit 1
fi

# 2. Activer l'environnement virtuel si présent
if [ -d ".venv" ]; then
    echo "🔹 Activation de l'environnement virtuel..."
    source .venv/bin/activate
fi

# 3. Message de commit (optionnel, avec date par défaut)
DEFAULT_MSG="Mise à jour du site - $(date '+%Y-%m-%d %H:%M')"
read -p "Message de commit [Entrée = message par défaut] : " COMMIT_MSG
COMMIT_MSG=${COMMIT_MSG:-$DEFAULT_MSG}

# 4. Envoyer les modifications sur GitHub
echo "🔹 Ajout des fichiers modifiés..."
git add .

if git diff --cached --quiet; then
    echo "ℹ️  Aucun changement à committer."
else
    echo "🔹 Commit : $COMMIT_MSG"
    git commit -m "$COMMIT_MSG"
    echo "🔹 Envoi vers GitHub (git push)..."
    git push
fi

# 5. Publier le site pour les élèves
echo "🔹 Publication du site (mkdocs gh-deploy)..."
mkdocs gh-deploy

# 6. Fin
echo "============================================"
echo "✅ Site mis à jour et publié avec succès !"
echo "🔗 https://CodeFather63.github.io/nsi-premiere"
echo "============================================"

read -p "Appuie sur Entrée pour fermer..."