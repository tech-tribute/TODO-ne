import subprocess
import sys
import os
import webbrowser
from threading import Thread
from time import sleep
import requests


default_address = "http://127.0.0.1:8000"


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


def open_tab():
    sleep(1)
    while not is_run():
        sleep(0.5)
    return webbrowser.open_new_tab(default_address)


def is_run():
    req = requests.get(default_address)
    return req.status_code == 200


if __name__ == "__main__":
    if check_migrations():
        apply_migrations()
    Thread(target=open_tab).start()
    try:
        run_server()
    except KeyboardInterrupt:
        print("Server stopped by user")
        try:
            sys.exit(0)  # Try to exit gracefully
        except SystemExit:
            os._exit(0)  # Force exit if necessary
