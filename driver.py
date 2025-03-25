import sys
import subprocess


def main():
    if len(sys.argv) != 2:
        print("python driver.py <logfile>")
        sys.exit(1)
    logging_file = sys.argv[1]
    #Start subprocesses: logger.py and encryptor.poy
    logger = subprocess.Popen(["python3", "logger.py", logging_file], stdin=subprocess.PIPE, encoding="utf8")
    encryptor = subprocess.Popen(["python3", "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf8")
     #Stores encryption and decryption results
    history = []
    def log(action, message=""):
        logger.stdin.write(f"{action} {message}\n")
        logger.stdin.flush()
    log("START", "Driver started")

    while True:
        #Prints available commands
        print("\nCommands: Password, Encrypt, Decrypt, History, Quit (Case Insensitive)")
        command = input("> ").strip().lower()

        match command:
            case "password":
                #Set a new password for encryption/decryption
                print("Enter new password: ", end="")
                password = input().strip().upper()
                encryptor.stdin.write(f"PASS {password}\n")
                encryptor.stdin.flush()
                encryptor.stdout.readline()
                log("PASSWORD_SET")

            case "encrypt":
                #Encrypt user input and store result in history
                text = input("Enter text to encrypt: ").strip().upper()
                encryptor.stdin.write(f"ENCRYPT {text}\n")
                encryptor.stdin.flush()
                #Get encryption output
                result = encryptor.stdout.readline().strip()  
                encrypted_text = result.split(" ", 1)[1] 
                history.append(encrypted_text)
                #Prints encrypted text
                print(result) 
                log("ENCRYPT", text)

            case "decrypt":
                # ecrypt user input and store result in history
                print("Enter text to decrypt: ", end="")
                text = input().strip().upper()
                encryptor.stdin.write(f"DECRYPT {text}\n")
                encryptor.stdin.flush()
                #Get decryption output
                result = encryptor.stdout.readline().strip()
                history.append(result.split(" ", 1)[1])
                history.append(decrypted_text)
                #Prints decrypted text
                print(result) 
                log("DECRYPT", text)

            case "history":
                #Prints encryption/decryption history
                print("History")
                for i, item in enumerate(history, 1):
                    print(f"{i}: {item}")

            case "quit":
                #Shutdown subprocesses
                log("EXIT", "driver exit")

                #Send QUIT command to encryptor and logger processes
                encryptor.stdin.write("QUIT\n")
                encryptor.stdin.flush()
                logger.stdin.write("QUIT\n")
                logger.stdin.flush()

                #Wait for processes to exit 
                encryptor.wait()
                logger.wait()
                #Exits
                break 

if __name__ == "__main__":
    main()
