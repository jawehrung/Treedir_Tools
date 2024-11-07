from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

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


def save_markdown_as_image(markdown, output_path):
    """
    Sauvegarde une chaîne Markdown sous forme d'image.

    Parameters:
    markdown (str): La chaîne de caractères en Markdown à convertir en image.
    output_path (str): Le chemin du fichier de sortie pour l'image.

    Returns:
    None
    """
    # Définir les paramètres de l'image
    font_path = "DejaVuSans.ttf"  # Remplacez par le chemin de votre police TTF
    font_size = 16
    font = ImageFont.truetype(font_path, font_size)
    lines = markdown.split('\n')
    image = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(image)
    max_width = max(draw.textbbox((0, 0), line, font=font)[2] for line in lines) + 10
    max_height = draw.textbbox((0, 0), lines[0], font=font)[3]
    image_height = (max_height * len(lines)) + 10

    # Créer une nouvelle image avec un fond blanc
    image = Image.new('RGB', (max_width, image_height), color='white')
    draw = ImageDraw.Draw(image)

    # Dessiner le texte sur l'image
    y_text = 5
    for line in lines:
        draw.text((5, y_text), line, font=font, fill='black')
        y_text += max_height

    # Sauvegarder l'image
    image.save(output_path)

def main():
    """
    Fonction principale pour générer une représentation en Markdown de l'arborescence des répertoires
    et la sauvegarder sous forme d'image.

    Parameters:
    None

    Returns:
    None
    """
    root_path = "D:\\Python"  # Remplacez par le chemin de votre répertoire
    markdown = generate_treedir_markdown(root_path)
    output_image_path = "directory_tree.png"
    save_markdown_as_image(markdown, output_image_path)
    print(f"L'image de l'arborescence a été générée : {output_image_path}")

if __name__ == "__main__":
    main()