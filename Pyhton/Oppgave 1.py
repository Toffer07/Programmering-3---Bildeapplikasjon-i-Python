from PIL import Image
import os

def rotate_and_resize_image(image_path, rotation_degrees, new_width):
    try:
        # Åpne bildet
        image = Image.open(image_path)

        # Rotere bildet
        rotated_image = image.rotate(rotation_degrees)

        # Endre størrelse på bildet
        resized_image = rotated_image.resize((new_width, int(new_width * image.height / image.width)))

        # Lagre det endrede bildet
        output_path = f"processed_{os.path.basename(image_path)}"
        resized_image.save(output_path)

        print(f"Behandlet bilde lagret som {output_path}")

    except Exception as e:
        print(f"Feil: {e}")

if __name__ == "__main__":
    image_path = input("Skriv inn filnavn på bildet: ")

    while not os.path.isfile(image_path):
        print("Fil ikke funnet. Prøv igjen.")
        image_path = input("Skriv inn filnavn på bildet: ")

    rotation_degrees = int(input("Skriv inn antall grader å rotere bildet (90, -90, 180): "))
    new_width = int(input("Skriv inn ønsket bredde for bildet: "))

    rotate_and_resize_image(image_path, rotation_degrees, new_width)
    