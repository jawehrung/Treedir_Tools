from pathlib import Path

def generate_treedir_markdown(root_path, indent=""):
    """
    Génère une représentation en Markdown de l'arborescence des répertoires.

    Parameters:
    root_path (str): Le chemin du répertoire racine.
    indent (str): La chaîne de caractères utilisée pour l'indentation (par défaut "").

    Returns:
    str: La représentation en Markdown de l'arborescence des répertoires.
    """
    entries = [entry for entry in Path(root_path).iterdir() if entry.is_dir()]
    # Filtrer les entrées pour exclure celles contenant ".git" etc...
    # entries = [entry for entry in entries if ".git" not in entry.name]
    # entries = [entry for entry in entries if ".idea" not in entry.name]
    # entries = [entry for entry in entries if "\docs" not in entry.name]
    entries.sort()
    markdown = ""
    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "
        markdown += f"{indent}{connector}{entry.name}\n"  # Ajoutez '/' pour indiquer que c'est un répertoire
        markdown += generate_treedir_markdown(entry, indent + ("    " if index == len(entries) - 1 else "│   "))
    return markdown


def generate_tree_markdown(root_path, indent=""):
    """
    Génère une représentation en Markdown de l'arborescence des répertoires et des fichiers.

    Parameters:
    root_path (str): Le chemin du répertoire racine.
    indent (str): La chaîne de caractères utilisée pour l'indentation (par défaut "").

    Returns:
    str: La représentation en Markdown de l'arborescence des répertoires et fichiers.
    """
    entries = list(Path(root_path).iterdir())
    # Filtrer les entrées pour exclure celles contenant ".git" etc...
    # entries = [entry for entry in entries if ".git" not in entry.name]
    # entries = [entry for entry in entries if ".idea" not in entry.name]
    # entries = [entry for entry in entries if "\docs" not in entry.name]
    entries.sort()
    markdown = ""
    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "
        markdown += f"{indent}{connector}{entry.name}\n"
        if entry.is_dir():
            sub_indent = "    " if index == len(entries) - 1 else "│   "
            markdown += generate_tree_markdown(entry, indent + sub_indent)
    return markdown


def main():
    """
    Fonction principale pour générer et afficher les représentations en Markdown de l'arborescence des répertoires et fichiers.

    Parameters:
    None

    Returns:
    None
    """
    root_path = "D:\Python"  # Remplacez par le chemin de votre répertoire

    # Écrire le rendu dans un fichier Markdown
    with open("Treedir.md", 'w', encoding='utf-8') as md_file:
        md_file.write(generate_treedir_markdown(root_path))

    with open("Tree.md", 'w', encoding='utf-8') as md_file:
        md_file.write(generate_tree_markdown(root_path))


if __name__ == "__main__":
    main()