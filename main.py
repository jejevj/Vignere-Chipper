import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char.upper()) + shift - ord('A')) % 26 + ord('A'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char.upper()) - shift - ord('A')) % 26 + ord('A'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

def create_vigenere_qrcode(text, key, filename):
    encrypted_text = vigenere_encrypt(text, key)
    
    # Membuat QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(encrypted_text)
    qr.make(fit=True)

    img = img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())

    filename_with_extension = filename + '.png'
    img.save(filename_with_extension)

    print(f"QR Code dengan teks '{text}' yang dienkripsi dengan Vigenere cipher menggunakan kunci '{key}' telah dibuat sebagai '{filename_with_extension}'.")

# Contoh penggunaan
text_to_encode = "HELLO SEMUANYA PERKENALKAN NAMA SAYA J ANGGA WIJAYA"
encryption_key = "COBALAGI"
qrcode_filename = "encrypted_qrcode"

create_vigenere_qrcode(text_to_encode, encryption_key, qrcode_filename)

# Contoh penggunaan
encrypted_text = "JSMLZ SKUWOOYL PKZMSOAWKGV PONA DAEI L OOGRA CQLOZA"

decryption_key = "COBALAGI"
decrypted_text = vigenere_decrypt(encrypted_text, decryption_key)

print(f"Hasil dekripsi dari teks '{encrypted_text}' dengan kunci '{decryption_key}' adalah '{decrypted_text}'.")

