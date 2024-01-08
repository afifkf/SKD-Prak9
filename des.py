from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key():
    # Menghasilkan kunci acak 8 byte
    return get_random_bytes(8)

def encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    # Melakukan padding jika panjang teks tidak kelipatan 8
    padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text)
    # Menghapus padding setelah dekripsi
    unpadded_text = unpad(decrypted_text, DES.block_size)
    return unpadded_text.decode('utf-8')

if __name__ == "__main__":
    # Contoh penggunaan
    plaintext = "Afif Khalid Fadhillah Dari Kelas TI-D"
    
    # Menghasilkan kunci
    key = generate_key()

    # Enkripsi teks
    ciphertext = encrypt(plaintext, key)
    print(f"Encrypted Text: {ciphertext}")

    # Dekripsi teks
    decrypted_text = decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")
