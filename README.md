# Network-Security-Project
Secret Sharing and Visual Cryptography

  Okan Selçuk Bayata
  Department of Computer Engineering
  Akdeniz University
  Antalya, Türkiye
  Email: 20230808301@ogr.akdeniz.edu.tr
  
  Doruk Yelken
  Department of Computer Engineering
  Akdeniz University
  Antalya, Türkiye
  Email: 20220808609@ogr.akdeniz.edu.tr


Experiment: Visual Cryptography Image Generator
 In this experiment, a visual cryptography technique is employed to encrypt a message
image into a ciphered image. The process involves using a secret image and the message
image to generate the ciphered output, which can be decrypted visually by overlapping the
ciphered image with the secret image.
 The implemented Python code leverages the PIL (Python Imaging Library) to perform
image manipulations such as resizing, converting to black-and-white, and pixel-wise
modifications necessary for visual cryptography.
Process Overview:
1. Loading the Message Image: The code begins by loading the message image, which
represents the image to be encrypted. The image is opened using PIL's Image.open()
method.
2. Preparing the Message Image: The loaded message image is converted into a binary
(black-and-white) format using the convert("1") method, ensuring that the image is
suitable for the visual cryptography process. If the image size diƯers from the
desired dimensions, it is resized accordingly.
3. Generating the Secret Image: If a secret image exists, it is loaded and resized (if
necessary) to match the dimensions of the message image. If the secret image does
not exist, a new one is generated by randomly assigning binary values to its pixels.
This secret image is created such that when combined with the ciphered image, it
reveals the original message.
4. Ciphering the Message: The core of the visual cryptography process involves the
creation of the ciphered image. This image is generated by combining the prepared
message image with the secret image. The ciphering is done pixel by pixel, ensuring
that the message is hidden in a way that requires both the secret and ciphered
images to decode.
5. Saving the Output: After generating the ciphered image, it is saved to disk along with
the prepared message and secret image (if necessary). The images are displayed for
visual inspection, ensuring that the process was carried out correctly.
Key Features:
 Message Encryption: The message image is encrypted into a binary format, ensuring
that only the intended recipient can view the original message by aligning the secret
image with the ciphered image.
 Secret Image Generation: If no secret image is provided, one is randomly generated
to create a secure encryption method. The generation process ensures
randomness, making decryption without the secret image computationally
infeasible.
 Display and Save Options: The resulting images (prepared message, secret image,
and ciphered image) are displayed for immediate visualization and saved to
specified file paths for future use.
 This method demonstrates how visual cryptography can be applied to image data, where
two or more images (in this case, the secret and ciphered images) are needed to visually
decode the encrypted message. The script operates entirely on image processing
techniques and does not require external cryptographic libraries, making it a lightweight
and accessible implementation.
 The decrypt_image function is designed to reconstruct the original message from the
ciphered and secret images in a visual cryptography scheme. It first ensures that both the
secret and ciphered images have the same dimensions, as this is a prerequisite for the
decryption process. For each pixel in the two images, the function compares the
corresponding pixels: if the pixels in both images are identical (both black or both white),
the pixel in the decrypted image is set to the same value as the secret image pixel,
revealing part of the original message. However, if the pixels diƯer (one is white and the
other is black), the function sets the corresponding pixel in the decrypted image to white,
as this diƯerence indicates that the pixel in the original message was white. After
processing all pixels, the function returns the decrypted image, which represents the
reconstructed message. This process adheres to the principles of visual cryptography,
where the secret and ciphered images are combined to reveal the hidden message.

