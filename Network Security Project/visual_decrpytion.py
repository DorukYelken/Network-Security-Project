from PIL import Image

def decrypt_image(secret_image, ciphered_image):
    # Ensure both images are in the same size
    if secret_image.size != ciphered_image.size:
        raise ValueError("The secret image and ciphered image must have the same dimensions.")

    # Get the dimensions of the images
    width, height = secret_image.size
    
    # Create a new image to store the decrypted message
    decrypted_image = Image.new(mode="1", size=(width, height))
    
    # Loop through each pixel in the secret and ciphered images
    for x in range(width):
        for y in range(height):
            secret_pixel = secret_image.getpixel((x, y))
            ciphered_pixel = ciphered_image.getpixel((x, y))
            
            # If the secret and ciphered pixels are the same (both white or both black), reveal the message
            if secret_pixel == ciphered_pixel:
                decrypted_image.putpixel((x, y), secret_pixel)
            else:
                # If they differ, the decrypted pixel is white
                decrypted_image.putpixel((x, y), 1)  # White pixel (binary 1)

    return decrypted_image


# Assuming you have secret_image and ciphered_image as PIL Image objects
secret_image = Image.open("secret.png")
ciphered_image = Image.open("ciphered.png")

decrypted_image = decrypt_image(secret_image, ciphered_image)
decrypted_image.show()  # Display the decrypted image
decrypted_image.save("decrypted_message.png")  # Save the decrypted message
