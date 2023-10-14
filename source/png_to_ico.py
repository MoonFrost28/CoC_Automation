from PIL import Image

def convert_image_to_ico(image_path, output_path):

    # Chargement de l'image source

    image = Image.open(image_path)

 

    # Conversion de l'image en format ICO

    image.save(output_path, format="ICO")

 

# Chemin vers l'image source

image_path = "Images/Diamond_LeagueB.png"  # Remplacez par le chemin réel vers votre image

 

# Chemin de sortie pour l'icône ICO

output_path = "Images/Diamond_LeagueB.ico"  # Spécifiez le chemin et le nom de fichier souhaités pour l'icône ICO


# Conversion de l'image en icône ICO

convert_image_to_ico(image_path, output_path)