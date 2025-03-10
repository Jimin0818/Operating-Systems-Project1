
import sys
import itertools

passkey = None

def vigenere_cipher(text, key, decrypt=False):
    """Encrypts or decrypts text using the Vigenère cipher."""
    key = itertools.cycle(key)  # Cycle through the key indefinitely
    result = []

    for char in text:
        if char.isalpha():
            shift = ord(next(key).upper()) - ord('A')
            if decrypt:
                new_char = chr(((ord(char.upper()) - ord('A') - shift) % 26) + ord('A'))
            else:
                new_char = chr(((ord(char.upper()) - ord('A') + shift) % 26) + ord('A'))
            result.append(new_char.lower() if char.islower() else new_char)
        else:
            result.append(char)
    
    return "".join(result)

def process_command():
    """Processes user commands interactively via standard input."""
    global passkey
    
    while True:
        try:
            line = input().strip()
            if not line:
                continue

            parts = line.split(" ", 1)
            command = parts[0].upper()
            argument = parts[1] if len(parts) > 1 else ""

            if command == "PASS":
                passkey = argument
                print("RESULT")
            elif command == "ENCRYPT":
                if passkey is None:
                    print("ERROR Password not set")
                elif any(not char.isalpha() and not char.isspace() for char in argument):
                    print("ERROR Encryption input contains symbols")
                else:
                    print("RESULT", vigenere_cipher(argument, passkey))
            elif command == "DECRYPT":
                if passkey is None:
                    print("ERROR Password not set: UNKNOWN CHARACTER")
                else:
                    print("RESULT", vigenere_cipher(argument, passkey, decrypt=True))
            elif command == "QUIT":
                break
            else:
                print("ERROR Invalid command")
        
            sys.stdout.flush()

        except EOFError:
            break  # Exit cleanly on EOF (useful for piping input)

if __name__ == "__main__":
    process_command()
