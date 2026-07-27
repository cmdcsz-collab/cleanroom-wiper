import subprocess, json, os
home = os.path.expanduser("~")
with open(home + "/.ssh/id_ed25519.pub") as f:
    pubkey = f.read().strip()

payload = '{"title":"Codex CLI","key":"' + pubkey + '"}'
cmd = [
    "curl.exe", "-s", "-X", "POST",
    "https://api.github.com/user/keys",
    "-H", "Authorization: Bearer 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",
    "-H", "Accept: application/vnd.github+json",
    "-H", "Content-Type: application/json",
    "-d", payload
]
r = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
try:
    data = json.loads(r.stdout)
    if "id" in data:
        print("SSH key added! ID:", data["id"])
    else:
        print("Error:", data.get("message",""))
except:
    print(r.stdout[:300])
