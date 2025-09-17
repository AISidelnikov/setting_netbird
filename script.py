import subprocess
import os
from datetime import datetime

def run_sudo_nopasswd(cmd, password):
    """Выполняет команду с sudo"""
    try:
        full_cmd = f'echo "{password}" | sudo -S {cmd}'
        result = subprocess.run(
            full_cmd,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"{datetime.now()}: Команда выполнена: {cmd}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"{datetime.now()}: Ошибка выполнения: {cmd}")
        print(f"{datetime.now()}: Ошибка: {e.stderr}")
        return None


if __name__ == '__main__':
    passwd = "ХХХХХХХ"

    commands = [
        "netbird service uninstall",
        "netbird service install",
        "netbird service start"
    ]

    for cmd in commands:
        output = run_sudo_nopasswd(cmd, passwd)
        if output:
            print(f"Результат: {output}")
        print("-" * 50)