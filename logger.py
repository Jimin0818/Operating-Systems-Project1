import sys
from datetime import datetime

def logging(log_file):
    try:
        with open(log_file, "a") as f, sys.stdin as stdin:
            while True:
                try:
                    #Read input
                    line = stdin.readline().strip()
                    if not line:
                        continue  #Skip empty lines
                    
                    if line.upper() == "QUIT":
                        break  #Exit logger
                    
                    #Split input
                    parts = line.split(" ", 1)
                    action = parts[0].strip()
                    message = parts[1].strip() if len(parts) > 1 else ""

                    if action:
                        #Write timestamp and log entry
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        log_entry = f"{timestamp} [{action}] {message}\n"
                        f.write(log_entry)
                        f.flush()
                
                except Exception as e:
                    #Log errors
                    print(f"Logger Error: {e}", file=sys.stderr)
                    continue

    except Exception as e:
        #Handle file errors
        print(f"Error opening log file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python logger.py <logfile>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    logging(log_file)
