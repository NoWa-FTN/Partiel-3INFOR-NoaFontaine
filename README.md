# Partiel DEVOPS - Exemple avec Python et GitHub Actions

Ce dépôt contient un projet Python simple avec :

- Des fonctions simples
- Des tests unitaires pour valider le comportement de la fonction.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/<votre-organisation>/<votre-repo>.git
   cd <votre-repo>

2. Installez les dépendances :
```pip install -r requirements.txt```

3. Exécutez les tests localement :
```pytest```

4. Ajouter un .gitignore pour ne pas commit __pycache__ et autre dossiers non pertinents à commit 

4. Creez un github workflow pour éxécuter des tests et  un github workflow pour éxécuter le linter 

5. Ajouter des badges de réussite d'execution de vos tests et de votre linter dans le readme (voir ***GITHUB_BADGES_GUIDE.md***)

6. Améliorer le code pour réussir le linter

7. Rendre le lien de votre répository contenant les github actions que vous aurez implémenté. 

***Attention à bien mettre votre repository en PUBLIC !***

# Status WorkFlow

[![Test Status](https://github.com/NoWa-FTN/Partiel-3INFOR-NoaFontaine/actions/workflows/test.yml/badge.svg)](https://github.com/NoWa-FTN/Partiel-3INFOR-NoaFontaine/actions/workflows/test.yml)
[![Run Linter](https://github.com/NoWa-FTN/Partiel-3INFOR-NoaFontaine/actions/workflows/linter.yml/badge.svg?branch=main)](https://github.com/NoWa-FTN/Partiel-3INFOR-NoaFontaine/actions/workflows/linter.yml)
