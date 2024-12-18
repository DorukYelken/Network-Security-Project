from PIL import Image
import random
import os

__version__ = "0.1"

def load_image(name):
    return Image.open(name)

def prepare_message_image(image, size):
    if size != image.size:
        image = image.resize(size, Image.ANTIALIAS)
    return image.convert("1")

def generate_secret(size, secret_image=None):
    width, height = size
    new_secret_image = Image.new(mode="1", size=(width * 2, height * 2))
    if secret_image:
        old_width, old_height = secret_image.size
    else:
        old_width, old_height = (-1, -1)

    for x in range(0, 2 * width, 2):
        for y in range(0, 2 * height, 2):
            if x < old_width and y < old_height:
                color = secret_image.getpixel((x, y))
            else:
                color = random.getrandbits(1)
            new_secret_image.putpixel((x, y), color)
            new_secret_image.putpixel((x + 1, y), 1 - color)
            new_secret_image.putpixel((x, y + 1), 1 - color)
            new_secret_image.putpixel((x + 1, y + 1), color)
    return new_secret_image

def generate_ciphered_image(secret_image, prepared_image):
    width, height = prepared_image.size
    ciphered_image = Image.new(mode="1", size=(width * 2, height * 2))
    for x in range(0, width * 2, 2):
        for y in range(0, height * 2, 2):
            secret = secret_image.getpixel((x, y))
            message = prepared_image.getpixel((x // 2, y // 2))
            if (message > 0 and secret > 0) or (message == 0 and secret == 0):
                color = 0
            else:
                color = 1
            ciphered_image.putpixel((x, y), 1 - color)
            ciphered_image.putpixel((x + 1, y), color)
            ciphered_image.putpixel((x, y + 1), color)
            ciphered_image.putpixel((x + 1, y + 1), 1 - color)
    return ciphered_image

def main():
    # File paths for images
    message_image_path = 'image.jpg'  # Replace with your message image path
    secret_image_path = 'secret.png'  # Replace with your secret image path
    ciphered_image_path = 'ciphered.png'  # Replace with your output path for ciphered image
    prepared_message_path = 'prepared_message.jpg'  # Replace with your output path for prepared message image

    try:
        # Load the message image
        message_image = load_image(message_image_path)
    except IOError as e:
        print(f"Fatal error: I/O error while loading message image '{message_image_path}' ({str(e)})")
        return

    size = message_image.size  # Use the size of the message image
    
    save_secret = False
    
    if os.path.isfile(secret_image_path):
        try:
            secret_image = load_image(secret_image_path)
            secret_width, secret_height = secret_image.size
            if secret_width < size[0] or secret_height < size[1]:
                print("Enlarging secret image to fit message size")
                secret_image = generate_secret(size, secret_image=secret_image)
                save_secret = True
        except IOError as e:
            print(f"I/O error while loading secret image '{secret_image_path}' ({str(e)})")
            return
    else:
        print(f"Generating secret image '{secret_image_path}'")
        secret_image = generate_secret(size)
        save_secret = True

    prepared_image = prepare_message_image(message_image, size)
    ciphered_image = generate_ciphered_image(secret_image, prepared_image)

    # Save images if necessary
    if save_secret:
        try:
            secret_image.save(secret_image_path)
        except IOError as e:
            print(f"I/O error while saving secret image '{secret_image_path}' ({str(e)})")

    if prepared_message_path:
        try:
            prepared_image.save(prepared_message_path)
        except IOError as e:
            print(f"I/O error while saving prepared message image '{prepared_message_path}' ({str(e)})")

    try:
        ciphered_image.save(ciphered_image_path)
    except IOError as e:
        print(f"I/O error while saving ciphered image '{ciphered_image_path}' ({str(e)})")
        return

    # Display the images
    prepared_image.show()
    secret_image.show()
    ciphered_image.show()

if __name__ == '__main__':
    main()
