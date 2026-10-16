"""Exercise 4: Demonstrate confidentiality with a toy XOR stream cipher.
This is an educational stand-in only, NOT secure encryption and NOT a real VPN.
"""
import base64

def xor_cipher(data: bytes, key: bytes) -> bytes:
    if not key:
        raise ValueError("Key cannot be empty.")
    return bytes(byte ^ key[i % len(key)] for i, byte in enumerate(data))

if __name__ == "__main__":
    message = input("Enter a message to send through the simulated VPN: ")
    key_text = input("Enter a shared key (demo only): ")
    plaintext = message.encode("utf-8")
    key = key_text.encode("utf-8")
    ciphertext = xor_cipher(plaintext, key)
    captured = base64.b64encode(ciphertext).decode("ascii")
    recovered = xor_cipher(ciphertext, key).decode("utf-8", errors="replace")
    print("\\nCaptured transit data (Base64-encoded ciphertext):")
    print(captured)
    print("\\nReadable without the key? No — it is represented as ciphertext.")
    print("Decrypted with the shared key:")
    print(recovered)
    print("\\nNote: XOR demo is not cryptographically secure; real VPNs use established protocols.")
