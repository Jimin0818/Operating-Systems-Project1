
import sys
import datetime


def log_message(log_file):
    """Logs messages received from standard input to the specified log file."""
    with open(log_file, 'a') as file:
        while True:
            try:
                line = sys.stdin.readline().strip()
                if line == "QUIT":
                    break

                if not line:
                    continue

                parts = line.split(" ", 1)
                action = parts[0]
                message = parts[1] if len(parts) > 1 else ""

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                log_entry = f"{timestamp} [{action}] {message}\n"

                file.write(log_entry)
                file.flush()

            except Exception as e:
                sys.stderr.write(f"Logging error: {e}\n")
                sys.stderr.flush()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python logger.py <logfile>\n")
        sys.exit(1)

    log_file = sys.argv[1]
    log_message(log_file)
