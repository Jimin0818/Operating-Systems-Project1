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
