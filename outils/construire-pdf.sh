#!/usr/bin/env bash
# ==================================================
#   Construit tous les PDF du cours dans le dossier pdf/
#   Prérequis : Node.js (pour npx). Rien d'autre à installer :
#   npx télécharge Marp (diaporamas) et md-to-pdf (fiches) au premier lancement.
#
#   Utilisation :  bash outils/construire-pdf.sh
# ==================================================
set -e
cd "$(dirname "$0")/.."
mkdir -p pdf

for dossier in seance-*/; do
  s="${dossier%/}"
  echo "→ $s"
  npx -y @marp-team/marp-cli@latest "$s/slides.md" --pdf --allow-local-files -o "pdf/$s-slides.pdf"
  npx -y md-to-pdf "$s/fiche-eleve.md"
  mv "$s/fiche-eleve.pdf" "pdf/$s-fiche-eleve.pdf"
done

for doc in plan-du-cours guide-animateur aide-memoire detective-des-bugs saison-2 installation/guide-installation seance-10/diplome; do
  echo "→ $doc"
  npx -y md-to-pdf "$doc.md"
  mv "$doc.pdf" "pdf/$(basename "$doc").pdf"
done

echo "Terminé : les PDF sont dans le dossier pdf/"
