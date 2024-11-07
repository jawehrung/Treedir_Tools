# Simple Treedir Tools For Python

![Language Python](https://img.shields.io/badge/%20Language-python-blue.svg)
![License MIT](https://img.shields.io/badge/%20License-MIT-blue.svg)

## Description

Ce projet contient deux scripts Python pour générer des représentations en Markdown de l'arborescence des répertoires et des fichiers, et pour sauvegarder cette représentation sous forme d'image.

## Scripts

### `treedir_to_md.py`

Ce script génère une représentation en Markdown de l'arborescence des répertoires et des fichiers.

#### Utilisation

1. Modifiez la variable `root_path` dans la fonction `main` pour indiquer le chemin de votre répertoire racine.
2. Exécutez le script :

```sh
python treedir_to_md.py
```

#### Fonctions

`generate_treedir_markdown(root_path, indent="")` : Génère une représentation en Markdown de l'arborescence des répertoires.   
`generate_tree_markdown(root_path, indent="")` : Génère une représentation en Markdown de l'arborescence des répertoires et des fichiers.   

### `treedir_to_png.py`

Ce script génère une représentation en Markdown de l'arborescence des répertoires et la sauvegarde sous forme d'image.

#### Utilisation

1. Modifiez la variable root_path dans la fonction main pour indiquer le chemin de votre répertoire racine.
2. Exécutez le script :

```sh
python treedir_to_png.py
```

#### Fonctions

`generate_treedir_markdown(root_path, indent="")` : Génère une représentation en Markdown de l'arborescence des répertoires.   
`save_markdown_as_image(markdown, output_path)` : Sauvegarde une chaîne Markdown sous forme d'image.   


## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.