import subprocess
import sys
import os


def check_migrations():
    # Use subprocess to execute the command and capture the output
    proc = subprocess.Popen(
        ["python", "manage.py", "showmigrations"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()

    # Check for the [ ] pattern in the output indicating pending migrations
    return any("[ ]" in line for line in stdout.decode().splitlines())


def apply_migrations():
    # Applying `makemigrations`
    subprocess.check_call([sys.executable, "manage.py", "makemigrations", "lists"])
    subprocess.check_call([sys.executable, "manage.py", "makemigrations", "todos"])
    # Applying `migrate`
    subprocess.check_call([sys.executable, "manage.py", "migrate"])


def run_server():
    # Starting `runserver`
    subprocess.check_call([sys.executable, "manage.py", "runserver"])
    return True


if __name__ == "__main__":
    try:
        if check_migrations():
            apply_migrations()
        run_server()
    except KeyboardInterrupt:
        print("Server stopped by user")
        try:
            sys.exit(0)  # Try to exit gracefully
        except SystemExit:
            os._exit(0)  # Force exit if necessary
