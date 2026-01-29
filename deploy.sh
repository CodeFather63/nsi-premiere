#!/bin/bash

echo "🔹 Activation de l'environnement virtuel"
source .venv/bin/activate || {
  echo "❌ Impossible d'activer le venv"
  exit 1
}

echo "🔹 Ajout des fichiers"
git add .

echo "🔹 Commit"
git commit -m "Mise à jour du site"

echo "🔹 Push vers GitHub"
git push

echo "🔹 Déploiement MkDocs"
mkdocs gh-deploy

echo "✅ Déploiement terminé"

