import sys
import subprocess


def main():
    if len(sys.argv) != 2:
        print("python driver.py <logfile>")
        sys.exit(1)
    logging_file = sys.argv[1]
    logger = subprocess.Popen(["python", "logger.py", logging_file], stdin=subprocess.PIPE, encoding="utf8")
    encryptor = subprocess.Popen(["python", "encrypt.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf8")
    history = []
    def log(action, message=""):
        logger.stdin.write(f"{action} {message}\n")
        logger.stdin.flush()
    log("START", "Driver started")
 while True:
        print("\nCommands: password, encrypt, decrypt, history, quit")
        command = input("> ").strip().lower()
        match command:
            case "password":
                print("Enter new password: ", end="")
                password = input().strip().upper()
                encryptor.stdin.write(f"PASS {password}\n")
                encryptor.stdin.flush()
                encryptor.stdout.readline()
                log("PASSWORD_SET")
            case "encrypt":
                print("Enter text to encrypt: ", end="")
                text = input().strip().upper()
                encryptor.stdin.write(f"ENCRYPT {text}\n")
                encryptor.stdin.flush()
                result = encryptor.stdout.readline().strip()
                history.append(result.split(" ", 1)[1])
                print(result)
                log("ENCRYPT", text)
                 case "decrypt":
                print("Enter text to decrypt: ", end="")
                text = input().strip().upper()
                encryptor.stdin.write(f"DECRYPT {text}\n")
                encryptor.stdin.flush()
                result = encryptor.stdout.readline().strip()
                history.append(result.split(" ", 1)[1])
                print(result)
                log("DECRYPT", text)
            case "history":
                print("History")
                for i, item in enumerate(history):
                    print(f"{i+1}: {item}")
            case "quit":
                log("EXIT", "driver exit")
                encryptor.stdin.write("QUIT\n")
                encryptor.stdin.flush()
                logger.stdin.write("QUIT\n")
                logger.stdin.flush()
                encryptor.wait()
                logger.wait()
                break
            case _:
                print("invalid command")
if __name__ == "__main__":
    main()


