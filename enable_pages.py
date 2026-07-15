import subprocess
cmd = [
    "curl.exe", "-s", "-X", "POST",
    "https://api.github.com/repos/cmdcsz-collab/cleanroom-wiper/pages",
    "-H", "Authorization: Bearer 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",
    "-H", "Accept: application/vnd.github+json",
    "-H", "X-GitHub-Api-Version: 2022-11-28",
    "-d", '{"source":{"branch":"main","path":"/"}}'
]
r = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
print("RC:", r.returncode)
print(r.stdout[:2000])
