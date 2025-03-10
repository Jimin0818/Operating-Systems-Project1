# Operating-Systems-Project1
Project 1 for CS 4348: Operating Systems

Vigenère Cipher Encryption System

Project Overview
The Vigenère Cipher Encryption System consists of three main components: the Logger (logger.py) which records system activities with timestamps, the Encryption Program (encrypt.py) which is responsible for encrypting and decrypting messages using the Vigenère cipher, and the Driver (driver.py) which is responsible for managing user interactions, spawns subprocesses, and facilitates communication between these components. As the main entry point, driver.py organizes the encryption system by handling user commands and managing subprocesses. The encrypt.py file ensures secure message transformation through encryption and decryption, while logger.py maintains a detailed log of user actions and system events. These logs are stored in logfile.txt.

To run the program, execute the command:
python driver.py logfile.txt
This initiates the driver program which initializes both the logger and encryption processes. When the program is running, users can enter commands to interact with the system. 
* The password command allows users to set a new encryption password or select one from history. 
* The encrypt command enables users to encrypt a new input or a previously entered string using the stored passkey. 
* The decrypt command allows decryption of previously encrypted messages. 
* The history command displays a log of all entered strings from the session, providing a reference for past interactions. 
* The quit command terminates all processes and exits the program, ensuring a clean shutdown of the system.

The Logger (logger.py) program records system activity in a log file. Each log entry follows the format:
YYYY-MM-DD HH:MM [ACTION] MESSAGE
For example, if the system starts on March 10, 2025, at 4:55 PM, it logs:
2025-03-10 16:55 [START] Logging Started.
The logger accepts a log file name as a command-line argument and writes logs with timestamps. It continuously records system events until it receives the QUIT command, at which point logging stops.

The Encryption Program (encrypt.py) handles encryption and decryption using the Vigenère cipher. 
It receives commands through standard input and provides responses through standard output. Users can interact with it using the following commands: password, encrypt, decrypt, history, and quit (case insensitive). The encryption program provides two types of responses. If a command executes successfully, it returns a RESULT <output> message with the corresponding result. If an error occurs, it returns an ERROR <message> message detailing the issue. For example, this system operates only on letters so any input must be solely of alphabetic characters. Additionally, the system is case insensitive, meaning that "hello" and "HELLO" will encrypt to the same result. Before performing encryption or decryption, a password must be set, or the system will return an error. 

The Driver Program (driver.py) is responsible for managing both the logger and encryption processes while ensuring smooth interaction between them. 
It logs all commands and their results to maintain a record of system activity. The driver program starts both the logger and encryption processes and then prompts the user for input commands. It also maintains a history of strings used for encryption and decryption. The driver ensures input validation, allowing only letters for passwords, encryption, and decryption to prevent invalid input errors. Additionally, all interactions—including system startup and shutdown—are recorded in the log file.


